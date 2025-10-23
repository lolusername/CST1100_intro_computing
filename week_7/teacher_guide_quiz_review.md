Title: Instructor Guide – CST1100 Midterm Review (Weeks 1–7)

## Quick Answer Key

| Q | Answer | Concept |
| --- | --- | --- |
| 1 | Electronic circuits have two stable states (on/off) | Binary rationale |
| 2 | 11 | Binary → decimal |
| 3 | 8 bits | Data units |
| 4 | `int('1010', 2)` | Python base conversion |
| 5 | `A` | ASCII |
| 6 | `ord('A')` | Unicode/ASCII |
| 7 | 256 | Color depth |
| 8 | The opposite of the input | NOT gate |
| 9 | 0 | AND gate |
| 10 | Fetch → Decode → Execute | CPU cycle |
| 11 | 2 | Floor division |
| 12 | 8 | String length |
| 13 | `#` | Comments |
| 14 | True | Boolean logic |
| 15 | `for line in f:` pattern | File I/O |
| 16 | Human-readable logic steps | Pseudocode |
| 17 | `for` loop | Repeat N times |
| 18 | `0 1 2` | `range()` behavior |
| 19 | `SELECT` | SQL retrieval |
| 20 | Both B and C | PostgreSQL concatenation |

## Facilitation Insights

### Binary & Encoding (Q1–Q7)
- **Hook**: Use a light switch metaphor for binary states; invite everyday examples.
- **Debunk**: Address the misconception that binary is “faster”; emphasize hardware compatibility (Q1).
- **Conversion Strategy**: For Q2, have students verbalize positional weights (8, 4, 2, 1). Encourage showing work.
- **ASCII Reminders**: Project a small ASCII chart; demonstrate `ord()` live for Q6.
- **Color Depth**: Show the 2ⁿ pattern; extend to 16-bit/24-bit to challenge advanced students (Q7).

### Logic & Architecture (Q8–Q11)
- Build truth tables collaboratively; assign student scribes on the board.
- Contrast AND vs OR before focusing on AND for Q9 to clarify confusion.
- Narrate the CPU cycle with a story (e.g., following a recipe) to make Fetch → Decode → Execute tangible.
- Demo `5 // 2` vs `5 / 2` in Python; explain floor division behavior for negative numbers as a curiosity.

### Python Fundamentals (Q12–Q18)
- **Strings & Comments**: Count characters together, noting uppercase letters count the same (Q12) and `#` introduces comments (Q13).
- **Boolean Walkthrough**: Substitute step by step for Q14 (`not False` → `True`; `True and True` → `True`).
- **File Loop**: Recommend using a `with open(...) as f:` block even though the question highlights `for line in f` (Q15).
- **Pseudocode**: Stress clarity over syntax correctness; show a “bad” pseudocode example and revise it (Q16).
- **Loop Structure**: Q17 sets up the range discussion; Q18 addresses off-by-one errors—run the snippet to prove the output.

### SQL Review (Q19–Q20)
- Position `SELECT` as “choose the columns you want” vs `INSERT`/`UPDATE`.
- Demo concatenation in PostgreSQL. Ask what alternative syntax looks like in SQL Server or MySQL.
- Encourage students to verbalize why `+` fails in PostgreSQL to reinforce data-type sensitivity.

## Discussion Prompts
- “Why does hardware design make binary the default?”
- “How can you verify a Python loop before running it?”
- “What parallels exist between Python string concatenation and SQL concatenation?”

## Python Demonstration Snippets

### Binary & Encoding (Q1–Q7)
```python
binary = "1011"
decimal = int(binary, 2)
print(f"{binary}_2 -> {decimal}_10")  # Q2

byte_bits = 8
print(f"One byte contains {byte_bits} bits")  # Q3

print(ord("A"))  # Q6
print(chr(65))   # Q5

colors = 2 ** 8
print(f"8-bit color depth supports {colors} colors")  # Q7
```

### Logic & Architecture (Q8–Q11)
```python
def not_gate(x):
    return 1 - x

def and_gate(a, b):
    return 1 if (a == 1 and b == 1) else 0

for a in (0, 1):
    print(f"NOT {a} -> {not_gate(a)}")  # Q8

a, b = 1, 0
print(f"A AND B (1, 0) -> {and_gate(a, b)}")  # Q9

cpu_cycle = ["Fetch", "Decode", "Execute"]
print("CPU cycle:", " -> ".join(cpu_cycle))  # Q10

x, y = 5, 2
print(x // y)  # Q11
```

### Python Fundamentals (Q12–Q18)
```python
print(len("CityTech"))  # Q12

comment_example = "# This is a Python comment"  # Q13
print("True and not False ->", True and not False)  # Q14

with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\n")

with open("sample.txt") as f:
    for line in f:
        print(line.rstrip())  # Q15

pseudocode_steps = [
    "START",
    "SET total = 0",
    "FOR each number in list",
    "    ADD number to total",
    "PRINT total",
    "END"
]
print("\n".join(pseudocode_steps))  # Q16

for i in range(3):
    print(i, end=" ")  # Q18
print()
```

### SQL Concepts (Q19–Q20)
```python
select_statement = "SELECT firstname, surname FROM members;"
concat_b = "SELECT firstname || ' ' || surname AS full_name FROM members;"
concat_c = "SELECT concat(firstname, ' ', surname) AS full_name FROM members;"
print(select_statement)  # Q19
print(concat_b)          # Q20 option B
print(concat_c)          # Q20 option C
```

## Differentiation Tips
- Provide conversion cheat-sheets and ASCII references for learners needing pacing support.
- Offer challenge tasks (e.g., implement a `while` loop equivalent of Q18’s `for` loop) for advanced students.
- Rotate student “explainers”: assign each pair one question to teach back to the class.

## After-Class Follow-Up
- Email the slide deck and annotated solutions.
- Summarize exit ticket results and address muddy points in LMS or a follow-up video.
- Schedule optional help sessions focused on the toughest areas identified.

## Data Science Cheatsheet

### NumPy Essentials
- **Array creation**: `np.array()`, `np.zeros()`, `np.ones()`, `np.full()`, `np.arange()`, `np.linspace()`
- **Reshape & combine**: `arr.reshape()`, `np.stack()`, `np.concatenate()`, `np.vstack()`, `np.hstack()`
- **Math operations**: broadcasting rules, `np.add`, `np.subtract`, `np.multiply`, `np.divide`, `np.power`, `np.dot`, `np.matmul`
- **Aggregations**: `arr.sum(axis=...)`, `arr.mean()`, `arr.std()`, `arr.var()`, `arr.min()`, `arr.max()`, `np.percentile()`
- **Indexing tricks**: boolean masks (`arr[arr > 0]`), fancy indexing (`arr[[0, 2, 4]]`), slicing (`arr[:, 1:]`)
- **Random sampling**: `np.random.seed()`, `np.random.rand()`, `np.random.randn()`, `np.random.randint()`, `np.random.choice()`
- **Linear algebra**: `np.linalg.inv()`, `np.linalg.det()`, `np.linalg.eig()`, `np.linalg.solve()`, `np.linalg.norm()`
- **Saving/loading**: `np.save()`, `np.load()`, `np.savetxt()`, `np.loadtxt()`

### pandas Essentials
- **Core objects**: `pd.Series`, `pd.DataFrame`, `.index`, `.columns`, `.info()`, `.describe()`
- **Reading data**: `pd.read_csv()`, `pd.read_excel()`, `pd.read_sql()`, `pd.read_json()`, `.to_csv()`, `.to_excel()`
- **Selection**: `.loc[row_label, col_label]`, `.iloc[row_index, col_index]`, boolean filtering (`df[df["col"] > 0]`)
- **Cleaning**: `.dropna()`, `.fillna()`, `.replace()`, `.astype()`, `.rename()`, `.drop_duplicates()`
- **Transformations**: `.assign()`, column arithmetic, `.apply()`, `.map()`, `.applymap()`
- **Grouping & aggregation**: `.groupby("col").agg({"other_col": ["mean", "count"]})`, `.pivot_table()`, `.crosstab()`
- **Merging & reshaping**: `pd.merge()`, `.join()`, `.concat()`, `.melt()`, `.stack()`, `.unstack()`, `.set_index()`, `.reset_index()`
- **Time series**: `pd.to_datetime()`, `.dt` accessor, `.resample()`, `.rolling()`, `.expanding()`
- **Export & reporting**: `.style`, `.to_markdown()`, `.to_latex()`, `.to_clipboard()`

### seaborn Essentials
- **High-level plots**: `sns.relplot()`, `sns.scatterplot()`, `sns.lineplot()`, `sns.barplot()`, `sns.countplot()`, `sns.histplot()`, `sns.kdeplot()`, `sns.boxplot()`, `sns.violinplot()`
- **Categorical relationships**: `sns.catplot()`, `sns.pointplot()`, `sns.stripplot()`, `sns.swarmplot()`
- **Matrix plots**: `sns.heatmap()`, `sns.clustermap()`, `sns.pairplot()`, `sns.jointplot()`
- **Styling**: `sns.set_theme()`, `sns.set_style()`, `sns.set_palette()`, `sns.color_palette()`
- **Faceting**: `sns.FacetGrid`, `sns.relplot(..., col="group")`
- **Statistical overlays**: `sns.regplot()`, `sns.lmplot()`, `sns.residplot()`
- **Export**: `plt.savefig("plot.png", dpi=300, bbox_inches="tight")`

### Additional Helpful Tools
- **Matplotlib essentials**: `plt.figure()`, `plt.subplots()`, `ax.plot()`, `ax.bar()`, `ax.set_title()`, `ax.set_xlabel()`, `ax.legend()`
- **Data helpers**: `itertools.product`, `collections.Counter`, `statistics.mean`, `datetime`, `pathlib`
- **Notebook productivity**: `%matplotlib inline`, `%timeit`, `%who`, `%%time`, `%%bash`
- **Packaging & environments**: `pip install`, `pip list`, `pip freeze > requirements.txt`, `python -m venv venv`, `source venv/bin/activate`

> Tip: Keep a scratch notebook that imports `numpy as np`, `pandas as pd`, `matplotlib.pyplot as plt`, and `seaborn as sns` with `sns.set_theme()` so you can demo any cheatsheet command live.

