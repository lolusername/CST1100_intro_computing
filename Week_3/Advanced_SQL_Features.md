# Advanced SQL Features
## Week 3: CST1100 Introduction to Computing

---

## Table of Contents

1. **Introduction to Advanced SQL**
2. **Database Views**
3. **Triggers**
4. **Stored Procedures**
5. **Indexes**
6. **Transactions and ACID Properties**
7. **Best Practices and Performance**
8. **Hands-on Examples**

---

## 1. Introduction to Advanced SQL

### What We'll Cover Today
- **Views**: Virtual tables that simplify complex queries
- **Triggers**: Automated responses to database events
- **Stored Procedures**: Reusable database functions
- **Indexes**: Performance optimization tools
- **Transactions**: Data integrity and consistency

### Why Learn Advanced SQL?
- **Performance**: Faster query execution
- **Security**: Controlled data access
- **Maintainability**: Reusable code
- **Data Integrity**: Automated validation
- **Scalability**: Handle large datasets efficiently

---

## 2. Database Views

### What is a View?
A **view** is a virtual table based on the result of a SQL statement. It contains rows and columns just like a real table, but the data comes from one or more base tables.

### Key Characteristics
- **Virtual**: No physical storage of data
- **Dynamic**: Always reflects current data from base tables
- **Customizable**: Can show only specific columns or rows
- **Secure**: Can hide sensitive data from users

### Syntax
```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

---

## 2.1 Types of Views

### Simple Views
- Based on a single table
- Can perform basic operations (SELECT, WHERE, ORDER BY)

```sql
CREATE VIEW active_customers AS
SELECT customer_id, first_name, last_name, email
FROM customers
WHERE status = 'active';
```

### Complex Views
- Based on multiple tables (JOINs)
- Can include calculations and aggregations

```sql
CREATE VIEW order_summary AS
SELECT 
    o.order_id,
    c.first_name,
    c.last_name,
    o.order_date,
    SUM(oi.quantity * oi.price) as total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, c.first_name, c.last_name, o.order_date;
```

---

## 2.2 View Operations

### Creating Views
```sql
-- Create a view for product inventory
CREATE VIEW product_inventory AS
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    i.quantity_in_stock,
    i.reorder_level
FROM products p
JOIN inventory i ON p.product_id = i.product_id
WHERE i.quantity_in_stock > 0;
```

### Using Views
```sql
-- Query the view like a regular table
SELECT * FROM product_inventory 
WHERE category = 'Electronics';

-- Join views with other tables
SELECT pi.product_name, s.supplier_name
FROM product_inventory pi
JOIN suppliers s ON pi.product_id = s.product_id;
```

### Modifying Views
```sql
-- Update view definition
CREATE OR REPLACE VIEW product_inventory AS
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    i.quantity_in_stock,
    i.reorder_level,
    p.price
FROM products p
JOIN inventory i ON p.product_id = i.product_id
WHERE i.quantity_in_stock > 0;
```

### Dropping Views
```sql
DROP VIEW product_inventory;
```

---

## 2.3 View Benefits and Limitations

### Benefits
- **Simplified Queries**: Complex joins hidden from users
- **Security**: Restrict access to sensitive columns
- **Consistency**: Standardized data presentation
- **Maintainability**: Changes in one place affect all users

### Limitations
- **Performance**: May be slower than direct table queries
- **Update Restrictions**: Not all views are updatable
- **Dependencies**: Changes to base tables can break views

### Updatable Views (Conditions)
- Based on single table
- No GROUP BY, HAVING, or aggregate functions
- No DISTINCT
- No subqueries in SELECT

---

## 3. Triggers

### What is a Trigger?
A **trigger** is a stored procedure that automatically executes in response to specific database events (INSERT, UPDATE, DELETE).

### Trigger Events
- **BEFORE**: Executes before the event
- **AFTER**: Executes after the event
- **INSTEAD OF**: Replaces the event (for views)

### Trigger Types
- **Row-level**: Executes once for each affected row
- **Statement-level**: Executes once per statement

---

## 3.1 Trigger Syntax

### Basic Syntax
```sql
CREATE TRIGGER trigger_name
    {BEFORE | AFTER | INSTEAD OF} event_type
    ON table_name
    [FOR EACH ROW]
    [WHEN condition]
    BEGIN
        -- trigger body
    END;
```

### Example: Audit Log Trigger
```sql
CREATE TRIGGER audit_customer_changes
    AFTER UPDATE ON customers
    FOR EACH ROW
    BEGIN
        INSERT INTO audit_log (
            table_name, 
            operation, 
            old_values, 
            new_values, 
            changed_by, 
            change_date
        ) VALUES (
            'customers',
            'UPDATE',
            OLD.customer_id || ',' || OLD.email,
            NEW.customer_id || ',' || NEW.email,
            USER(),
            NOW()
        );
    END;
```

---

## 3.2 Common Trigger Use Cases

### 1. Data Validation
```sql
CREATE TRIGGER validate_email
    BEFORE INSERT ON customers
    FOR EACH ROW
    BEGIN
        IF NEW.email NOT LIKE '%@%.%' THEN
            SIGNAL SQLSTATE '45000' 
            SET MESSAGE_TEXT = 'Invalid email format';
        END IF;
    END;
```

### 2. Automatic Timestamps
```sql
CREATE TRIGGER update_timestamp
    BEFORE UPDATE ON orders
    FOR EACH ROW
    BEGIN
        SET NEW.updated_at = NOW();
    END;
```

### 3. Inventory Management
```sql
CREATE TRIGGER update_inventory
    AFTER INSERT ON order_items
    FOR EACH ROW
    BEGIN
        UPDATE inventory 
        SET quantity_in_stock = quantity_in_stock - NEW.quantity
        WHERE product_id = NEW.product_id;
    END;
```

---

## 3.3 Advanced Trigger Examples

### Cascading Updates
```sql
CREATE TRIGGER cascade_customer_update
    AFTER UPDATE ON customers
    FOR EACH ROW
    BEGIN
        -- Update related orders
        UPDATE orders 
        SET customer_name = NEW.first_name || ' ' || NEW.last_name
        WHERE customer_id = NEW.customer_id;
        
        -- Update related addresses
        UPDATE addresses 
        SET customer_name = NEW.first_name || ' ' || NEW.last_name
        WHERE customer_id = NEW.customer_id;
    END;
```

### Complex Business Logic
```sql
CREATE TRIGGER calculate_order_total
    AFTER INSERT ON order_items
    FOR EACH ROW
    BEGIN
        DECLARE order_total DECIMAL(10,2);
        
        -- Calculate new total
        SELECT SUM(quantity * price) 
        INTO order_total
        FROM order_items 
        WHERE order_id = NEW.order_id;
        
        -- Update order total
        UPDATE orders 
        SET total_amount = order_total
        WHERE order_id = NEW.order_id;
    END;
```

---

## 4. Stored Procedures

### What is a Stored Procedure?
A **stored procedure** is a precompiled collection of SQL statements stored in the database that can be executed as a single unit.

### Benefits
- **Performance**: Precompiled and optimized
- **Reusability**: Can be called from multiple applications
- **Security**: Controlled access to database operations
- **Maintainability**: Centralized business logic

### Basic Syntax
```sql
DELIMITER //
CREATE PROCEDURE procedure_name(parameters)
BEGIN
    -- SQL statements
END //
DELIMITER ;
```

---

## 4.1 Stored Procedure Examples

### Simple Procedure
```sql
DELIMITER //
CREATE PROCEDURE GetCustomerOrders(IN customer_id INT)
BEGIN
    SELECT 
        o.order_id,
        o.order_date,
        o.total_amount,
        o.status
    FROM orders o
    WHERE o.customer_id = customer_id
    ORDER BY o.order_date DESC;
END //
DELIMITER ;

-- Call the procedure
CALL GetCustomerOrders(123);
```

### Procedure with Parameters
```sql
DELIMITER //
CREATE PROCEDURE CreateOrder(
    IN p_customer_id INT,
    IN p_product_id INT,
    IN p_quantity INT,
    OUT p_order_id INT
)
BEGIN
    DECLARE product_price DECIMAL(10,2);
    DECLARE order_total DECIMAL(10,2);
    
    -- Get product price
    SELECT price INTO product_price
    FROM products
    WHERE product_id = p_product_id;
    
    -- Calculate total
    SET order_total = p_quantity * product_price;
    
    -- Insert order
    INSERT INTO orders (customer_id, total_amount, order_date)
    VALUES (p_customer_id, order_total, NOW());
    
    -- Get the new order ID
    SET p_order_id = LAST_INSERT_ID();
    
    -- Insert order item
    INSERT INTO order_items (order_id, product_id, quantity, price)
    VALUES (p_order_id, p_product_id, p_quantity, product_price);
END //
DELIMITER ;
```

---

## 4.2 Advanced Stored Procedures

### Error Handling
```sql
DELIMITER //
CREATE PROCEDURE ProcessPayment(
    IN p_order_id INT,
    IN p_amount DECIMAL(10,2),
    OUT p_status VARCHAR(50)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET p_status = 'ERROR: Payment processing failed';
    END;
    
    START TRANSACTION;
    
    -- Check if order exists and amount is correct
    IF NOT EXISTS (SELECT 1 FROM orders WHERE order_id = p_order_id) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Order not found';
    END IF;
    
    -- Process payment
    INSERT INTO payments (order_id, amount, payment_date, status)
    VALUES (p_order_id, p_amount, NOW(), 'COMPLETED');
    
    -- Update order status
    UPDATE orders 
    SET status = 'PAID', payment_date = NOW()
    WHERE order_id = p_order_id;
    
    COMMIT;
    SET p_status = 'SUCCESS: Payment processed';
END //
DELIMITER ;
```

### Complex Business Logic
```sql
DELIMITER //
CREATE PROCEDURE GenerateMonthlyReport(IN report_month INT, IN report_year INT)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_customer_id INT;
    DECLARE v_total_orders INT;
    DECLARE v_total_amount DECIMAL(10,2);
    
    -- Cursor for customers
    DECLARE customer_cursor CURSOR FOR
        SELECT DISTINCT customer_id FROM orders
        WHERE MONTH(order_date) = report_month 
        AND YEAR(order_date) = report_year;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    -- Create temporary table for report
    CREATE TEMPORARY TABLE monthly_report (
        customer_id INT,
        customer_name VARCHAR(100),
        total_orders INT,
        total_amount DECIMAL(10,2)
    );
    
    OPEN customer_cursor;
    
    read_loop: LOOP
        FETCH customer_cursor INTO v_customer_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        -- Calculate totals for this customer
        SELECT COUNT(*), COALESCE(SUM(total_amount), 0)
        INTO v_total_orders, v_total_amount
        FROM orders
        WHERE customer_id = v_customer_id
        AND MONTH(order_date) = report_month
        AND YEAR(order_date) = report_year;
        
        -- Insert into report
        INSERT INTO monthly_report (customer_id, customer_name, total_orders, total_amount)
        SELECT v_customer_id, first_name || ' ' || last_name, v_total_orders, v_total_amount
        FROM customers
        WHERE customer_id = v_customer_id;
        
    END LOOP;
    
    CLOSE customer_cursor;
    
    -- Return the report
    SELECT * FROM monthly_report ORDER BY total_amount DESC;
    
    DROP TEMPORARY TABLE monthly_report;
END //
DELIMITER ;
```

---

## 5. Indexes

### What is an Index?
An **index** is a database object that improves the speed of data retrieval operations by providing quick access to rows in a table.

### How Indexes Work
- **B-tree Structure**: Most common index type
- **Sorted Data**: Allows binary search
- **Pointer System**: Points to actual data rows
- **Memory Efficient**: Stores only key values and pointers

### Types of Indexes
- **Primary Index**: Automatically created for PRIMARY KEY
- **Unique Index**: Ensures uniqueness of values
- **Composite Index**: Multiple columns
- **Partial Index**: Only part of the table

---

## 5.1 Index Syntax and Examples

### Creating Indexes
```sql
-- Single column index
CREATE INDEX idx_customer_email ON customers(email);

-- Composite index
CREATE INDEX idx_order_customer_date ON orders(customer_id, order_date);

-- Unique index
CREATE UNIQUE INDEX idx_product_sku ON products(sku);

-- Partial index (PostgreSQL)
CREATE INDEX idx_active_customers ON customers(customer_id) 
WHERE status = 'active';
```

### Index on Views
```sql
-- Create materialized view (PostgreSQL)
CREATE MATERIALIZED VIEW order_summary AS
SELECT 
    customer_id,
    COUNT(*) as order_count,
    SUM(total_amount) as total_spent
FROM orders
GROUP BY customer_id;

-- Create index on materialized view
CREATE INDEX idx_order_summary_customer ON order_summary(customer_id);
```

---

## 5.2 Index Performance and Best Practices

### When to Use Indexes
- **Frequent WHERE clauses**: Columns used in WHERE conditions
- **JOIN columns**: Foreign key columns
- **ORDER BY columns**: Columns used for sorting
- **GROUP BY columns**: Columns used for grouping

### When NOT to Use Indexes
- **Small tables**: Overhead may exceed benefits
- **Frequently updated columns**: Index maintenance cost
- **Low selectivity columns**: Columns with few unique values
- **Large text columns**: Full-text indexes are better

### Index Maintenance
```sql
-- Analyze table statistics (PostgreSQL)
ANALYZE customers;

-- Rebuild index (MySQL)
ALTER TABLE customers DROP INDEX idx_customer_email;
CREATE INDEX idx_customer_email ON customers(email);

-- Check index usage (MySQL)
SHOW INDEX FROM customers;
```

---

## 6. Transactions and ACID Properties

### What is a Transaction?
A **transaction** is a sequence of database operations that are treated as a single unit of work. Either all operations succeed, or all are rolled back.

### ACID Properties
- **Atomicity**: All or nothing
- **Consistency**: Database remains in valid state
- **Isolation**: Concurrent transactions don't interfere
- **Durability**: Committed changes are permanent

### Transaction Syntax
```sql
-- Start transaction
START TRANSACTION;

-- SQL statements
INSERT INTO orders (customer_id, total_amount) VALUES (1, 100.00);
UPDATE inventory SET quantity = quantity - 1 WHERE product_id = 1;

-- Commit or rollback
COMMIT;  -- or ROLLBACK;
```

---

## 6.1 Transaction Examples

### E-commerce Order Processing
```sql
DELIMITER //
CREATE PROCEDURE ProcessOrder(
    IN p_customer_id INT,
    IN p_product_id INT,
    IN p_quantity INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        RESIGNAL;
    END;
    
    START TRANSACTION;
    
    -- Check inventory
    IF (SELECT quantity_in_stock FROM inventory WHERE product_id = p_product_id) < p_quantity THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient inventory';
    END IF;
    
    -- Create order
    INSERT INTO orders (customer_id, order_date, status)
    VALUES (p_customer_id, NOW(), 'PENDING');
    
    SET @order_id = LAST_INSERT_ID();
    
    -- Add order items
    INSERT INTO order_items (order_id, product_id, quantity, price)
    SELECT @order_id, p_product_id, p_quantity, price
    FROM products WHERE product_id = p_product_id;
    
    -- Update inventory
    UPDATE inventory 
    SET quantity_in_stock = quantity_in_stock - p_quantity
    WHERE product_id = p_product_id;
    
    -- Update order total
    UPDATE orders 
    SET total_amount = (SELECT SUM(quantity * price) FROM order_items WHERE order_id = @order_id)
    WHERE order_id = @order_id;
    
    COMMIT;
END //
DELIMITER ;
```

---

## 7. Best Practices and Performance

### Query Optimization
1. **Use appropriate indexes**
2. **Avoid SELECT ***
3. **Use LIMIT for large result sets**
4. **Optimize JOIN conditions**
5. **Use EXPLAIN to analyze queries**

### Security Best Practices
1. **Use parameterized queries** (prepared statements)
2. **Implement proper access controls**
3. **Validate input data**
4. **Use views to restrict data access**
5. **Regular security audits**

### Maintenance Best Practices
1. **Regular index maintenance**
2. **Monitor query performance**
3. **Update table statistics**
4. **Archive old data**
5. **Backup strategies**

---

## 8. Hands-on Examples

### Example 1: Complete E-commerce System
```sql
-- Create tables
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE inventory (
    product_id INT PRIMARY KEY,
    quantity_in_stock INT NOT NULL DEFAULT 0,
    reorder_level INT DEFAULT 10,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(20) DEFAULT 'PENDING',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

---

### Example 2: Views and Triggers
```sql
-- Create a view for order details
CREATE VIEW order_details AS
SELECT 
    o.order_id,
    c.first_name,
    c.last_name,
    c.email,
    o.order_date,
    o.total_amount,
    o.status,
    COUNT(oi.order_item_id) as item_count
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, c.first_name, c.last_name, c.email, o.order_date, o.total_amount, o.status;

-- Create trigger for inventory management
DELIMITER //
CREATE TRIGGER update_inventory_after_order
    AFTER INSERT ON order_items
    FOR EACH ROW
    BEGIN
        UPDATE inventory 
        SET quantity_in_stock = quantity_in_stock - NEW.quantity
        WHERE product_id = NEW.product_id;
        
        -- Check if reorder is needed
        IF (SELECT quantity_in_stock FROM inventory WHERE product_id = NEW.product_id) <= 
           (SELECT reorder_level FROM inventory WHERE product_id = NEW.product_id) THEN
            INSERT INTO reorder_alerts (product_id, current_quantity, reorder_level, alert_date)
            SELECT NEW.product_id, quantity_in_stock, reorder_level, NOW()
            FROM inventory WHERE product_id = NEW.product_id;
        END IF;
    END //
DELIMITER ;
```

---

## Summary

### Key Takeaways
1. **Views** simplify complex queries and provide security
2. **Triggers** automate business logic and maintain data integrity
3. **Stored Procedures** improve performance and code reusability
4. **Indexes** optimize query performance
5. **Transactions** ensure data consistency and reliability

### Next Steps
- Practice with sample databases
- Experiment with different scenarios
- Monitor performance and optimize
- Learn about database-specific features
- Explore advanced topics like partitioning and replication

### Resources
- Database documentation for your specific DBMS
- Online SQL practice platforms
- Performance tuning guides
- Security best practices documentation

---

## Questions and Discussion

### Common Questions
1. When should I use a view vs. a stored procedure?
2. How do I choose the right indexes for my queries?
3. What are the performance implications of triggers?
4. How do I handle errors in stored procedures?
5. What's the difference between row-level and statement-level triggers?

### Practice Exercises
1. Create a view that shows customer order history
2. Write a trigger that logs all price changes
3. Create a stored procedure for processing returns
4. Design indexes for a reporting system
5. Implement a transaction for transferring inventory between warehouses

---

*End of Presentation*
