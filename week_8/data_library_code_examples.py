"""
Comprehensive NumPy, pandas, and seaborn example snippets.

Each section below can be executed independently. Running the module will
demonstrate every API listed in the reference brief by printing outputs
and saving plots/files in the local directory.
"""

from pathlib import Path
import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


DATA_DIR = Path(__file__).parent
DATA_DIR.mkdir(parents=True, exist_ok=True)


def numpy_essentials():
    print("=== NumPy Essentials ===")

    # Array creation
    base_list = [1, 2, 3]
    arr = np.array(base_list)
    zeros = np.zeros((2, 3))
    ones = np.ones((3, 2))
    full = np.full((2, 2), 7)
    arange = np.arange(0, 10, 2)
    linspace = np.linspace(0, 1, num=5)

    print("array:", arr)
    print("zeros:\n", zeros)
    print("ones:\n", ones)
    print("full:\n", full)
    print("arange:", arange)
    print("linspace:", linspace)

    # Reshape & combine
    reshaped = arr.reshape(3, 1)
    stacked = np.stack([arr, arr * 2])
    concatenated = np.concatenate([arr, arr])
    vstacked = np.vstack([arr, arr + 5])
    hstacked = np.hstack([reshaped, reshaped + 10])

    print("reshaped:\n", reshaped)
    print("stacked:\n", stacked)
    print("concatenated:", concatenated)
    print("vstacked:\n", vstacked)
    print("hstacked:\n", hstacked)

    # Math operations & broadcasting
    other = np.array([10, 20, 30])
    print("Broadcasting add (arr + 5):", arr + 5)
    print("np.add:", np.add(arr, other))
    print("np.subtract:", np.subtract(other, arr))
    print("np.multiply:", np.multiply(arr, 2))
    print("np.divide:", np.divide(other, arr))
    print("np.power:", np.power(arr, 2))
    print("np.dot:", np.dot(arr, other))
    print("np.matmul (matrix multiply):\n", np.matmul(vstacked, reshaped))

    # Aggregations
    matrix = np.arange(1, 10).reshape(3, 3)
    print("matrix:\n", matrix)
    print("sum axis=0:", matrix.sum(axis=0))
    print("mean:", matrix.mean())
    print("std:", matrix.std())
    print("var:", matrix.var())
    print("min:", matrix.min())
    print("max:", matrix.max())
    print("percentile 90:", np.percentile(matrix, 90))

    # Indexing tricks
    mask = matrix > 5
    print("boolean mask:\n", mask)
    print("matrix[mask]:", matrix[mask])
    print("fancy indexing matrix[[0,2], [1,2]]:", matrix[[0, 2], [1, 2]])
    print("slicing matrix[:, 1:]:\n", matrix[:, 1:])

    # Random sampling
    np.random.seed(42)
    print("np.random.rand:", np.random.rand(2, 3))
    print("np.random.randn:", np.random.randn(3))
    print("np.random.randint:", np.random.randint(0, 10, size=5))
    print("np.random.choice:", np.random.choice(arr, size=4, replace=True))

    # Linear algebra
    lin_alg_matrix = np.array([[4, 7], [2, 6]])
    print("np.linalg.inv:\n", np.linalg.inv(lin_alg_matrix))
    print("np.linalg.det:", np.linalg.det(lin_alg_matrix))
    eig_vals, eig_vecs = np.linalg.eig(lin_alg_matrix)
    print("eigenvalues:", eig_vals)
    print("eigenvectors:\n", eig_vecs)
    b = np.array([1, 0])
    print("np.linalg.solve:", np.linalg.solve(lin_alg_matrix, b))
    print("np.linalg.norm:", np.linalg.norm(lin_alg_matrix))

    # Saving/loading
    npy_path = DATA_DIR / "sample_array.npy"
    np_txt_path = DATA_DIR / "sample_array.txt"
    np.save(npy_path, matrix)
    np.savetxt(np_txt_path, matrix, fmt="%d")
    print("np.load:", np.load(npy_path))
    print("np.loadtxt:\n", np.loadtxt(np_txt_path))


def pandas_essentials():
    print("\n=== pandas Essentials ===")

    # Core objects
    series = pd.Series([10, 20, 30], name="scores")
    df = pd.DataFrame(
        {
            "name": ["Ada", "Grace", "Linus", "Anita"],
            "major": ["CS", "Math", "CS", "Physics"],
            "score": [95, 88, 82, 91],
            "credits": [12, 15, 12, 18],
        }
    )
    print("Series:\n", series)
    print("DataFrame:\n", df)
    print("Index:", df.index)
    print("Columns:", df.columns)
    print("df.info():")
    print(df.info())
    print("df.describe():\n", df.describe())

    # Reading/writing data
    csv_path = DATA_DIR / "students.csv"
    excel_path = DATA_DIR / "students.xlsx"
    json_path = DATA_DIR / "students.json"
    df.to_csv(csv_path, index=False)
    df.to_json(json_path, orient="records", indent=2)
    try:
        df.to_excel(excel_path, index=False)
    except ImportError:
        print("Install openpyxl to enable Excel export.")

    csv_loaded = pd.read_csv(csv_path)
    json_loaded = pd.read_json(json_path)
    print("pd.read_csv:\n", csv_loaded)
    print("pd.read_json:\n", json_loaded)

    # SQLite example for pd.read_sql
    with sqlite3.connect(":memory:") as conn:
        df.to_sql("students", conn, index=False)
        sql_loaded = pd.read_sql("SELECT name, score FROM students", conn)
        print("pd.read_sql:\n", sql_loaded)

    # Selection
    print("loc name column:", df.loc[:, "name"])
    print("iloc first row:", df.iloc[0])
    print(
        'Boolean filter df[df["score"] > 90]:\n',
        df[df["score"] > 90],
    )

    # Cleaning
    dirty_df = pd.DataFrame(
        {
            "name": ["Ada", None, "Linus", "Anita"],
            "major": ["CS", "Math", "CS", "Physics"],
            "score": [95, None, 82, 91],
            "alias": ["Ada", "Grace", "Linus", "Anita B."],
        }
    )
    print("dropna:\n", dirty_df.dropna())
    print("fillna:\n", dirty_df.fillna({"name": "Unknown", "score": dirty_df["score"].mean()}))
    print("replace:\n", df.replace({"CS": "Computer Science"}))
    print("astype credits to float:\n", df.assign(credits=df["credits"].astype(float)))
    print("rename columns:\n", df.rename(columns={"score": "final_score"}))
    print("drop_duplicates:\n", df.drop_duplicates(subset=["major"]))

    # Transformations
    transformed = (
        df.assign(
            grade=lambda d: pd.cut(d["score"], bins=[0, 85, 90, 100], labels=["C", "B", "A"]),
            score_scaled=lambda d: d["score"] / 100,
        )
        .assign(letters=lambda d: d["name"].str.len().map({3: "short", 5: "medium"}).fillna("long"))
    )
    print("assign/map/apply:\n", transformed)
    print("apply column-wise:\n", df.apply(lambda col: col if col.name == "score" else col))
    print("applymap example:\n", df[["name", "major"]].applymap(str.upper))

    # Grouping & aggregation
    grouped = df.groupby("major").agg({"score": ["mean", "count"], "credits": "sum"})
    print("groupby agg:\n", grouped)
    print(
        "pivot_table:\n",
        pd.pivot_table(df, values="score", index="major", columns="credits", aggfunc="mean"),
    )
    print(
        "crosstab:\n",
        pd.crosstab(df["major"], df["credits"], margins=True),
    )

    # Merging & reshaping
    dept_info = pd.DataFrame(
        {"major": ["CS", "Math", "Physics"], "chair": ["Dr. Hopper", "Dr. Noether", "Dr. Feynman"]}
    )
    merged = pd.merge(df, dept_info, on="major", how="left")
    print("pd.merge:\n", merged)
    joined = merged.set_index("name").join(dept_info.set_index("major"), rsuffix="_dept")
    print("join:\n", joined)
    concatenated = pd.concat([df.head(2), df.tail(2)], axis=0)
    print("concat:\n", concatenated)
    melted = df.melt(id_vars="name", value_vars=["score", "credits"], var_name="metric")
    print("melt:\n", melted)
    stacked = df.set_index("name").stack()
    print("stack:\n", stacked)
    print("unstack:\n", stacked.unstack())
    print("set_index:\n", df.set_index("name"))
    print("reset_index:\n", df.set_index("name").reset_index())

    # Time series
    time_df = pd.DataFrame(
        {
            "timestamp": pd.date_range("2023-01-01", periods=6, freq="D"),
            "value": [10, 12, 15, 14, 13, 16],
        }
    )
    time_df["timestamp"] = pd.to_datetime(time_df["timestamp"])
    time_df = time_df.set_index("timestamp")
    print("dt accessor day of week:\n", time_df.index.day_name())
    print("resample weekly sum:\n", time_df.resample("W").sum())
    print("rolling mean (window=3):\n", time_df.rolling(window=3).mean())
    print("expanding mean:\n", time_df.expanding().mean())

    # Export & reporting
    print("DataFrame.style highlight max (first 5 rows):")
    print(df.style.highlight_max(subset=["score"]).to_html())
    print("to_markdown:\n", df.to_markdown(index=False))
    print("to_latex:\n", df.to_latex(index=False))
    print("Copy to clipboard skipped in non-interactive script (uncomment to run).")
    # df.to_clipboard(index=False)  # Uncomment to copy table to clipboard


def seaborn_essentials():
    print("\n=== seaborn Essentials ===")
    tips = sns.load_dataset("tips")

    # High-level plots
    sns.relplot(data=tips, x="total_bill", y="tip", hue="time")
    plt.savefig(DATA_DIR / "relplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day")
    plt.savefig(DATA_DIR / "scatterplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.lineplot(data=tips, x="size", y="tip", estimator="mean")
    plt.savefig(DATA_DIR / "lineplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.barplot(data=tips, x="day", y="tip", estimator=np.mean, errorbar="sd")
    plt.savefig(DATA_DIR / "barplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.countplot(data=tips, x="size")
    plt.savefig(DATA_DIR / "countplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.histplot(data=tips, x="total_bill", bins=20, kde=True)
    plt.savefig(DATA_DIR / "histplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.kdeplot(data=tips, x="tip", hue="sex", fill=True)
    plt.savefig(DATA_DIR / "kdeplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.boxplot(data=tips, x="day", y="total_bill")
    plt.savefig(DATA_DIR / "boxplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.violinplot(data=tips, x="day", y="tip")
    plt.savefig(DATA_DIR / "violinplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Categorical relationships
    sns.catplot(data=tips, x="day", y="tip", kind="point", hue="sex")
    plt.savefig(DATA_DIR / "catplot_point.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.pointplot(data=tips, x="day", y="tip", hue="sex")
    plt.savefig(DATA_DIR / "pointplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.stripplot(data=tips, x="day", y="tip", jitter=True)
    plt.savefig(DATA_DIR / "stripplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.swarmplot(data=tips, x="day", y="total_bill")
    plt.savefig(DATA_DIR / "swarmplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Matrix plots
    corr = tips.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.savefig(DATA_DIR / "heatmap.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.clustermap(corr, cmap="viridis")
    plt.savefig(DATA_DIR / "clustermap.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.pairplot(tips[["total_bill", "tip", "size", "time"]], hue="time")
    plt.savefig(DATA_DIR / "pairplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.jointplot(data=tips, x="total_bill", y="tip", kind="hex")
    plt.savefig(DATA_DIR / "jointplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Styling
    sns.set_theme(style="whitegrid", palette="muted")
    sns.scatterplot(data=tips, x="total_bill", y="tip")
    plt.savefig(DATA_DIR / "styled_scatter.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.set_style("dark")
    sns.set_palette("Set2")
    sns.lineplot(data=tips, x="size", y="tip")
    plt.savefig(DATA_DIR / "styled_line.png", dpi=300, bbox_inches="tight")
    plt.close()

    palette = sns.color_palette("coolwarm", as_cmap=False)
    print("Custom palette:", palette)

    # Faceting
    g = sns.FacetGrid(tips, col="day", hue="sex")
    g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
    g.add_legend()
    g.savefig(DATA_DIR / "facetgrid.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="time", kind="scatter")
    plt.savefig(DATA_DIR / "relplot_col.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Statistical overlays
    sns.regplot(data=tips, x="total_bill", y="tip")
    plt.savefig(DATA_DIR / "regplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.lmplot(data=tips, x="total_bill", y="tip", hue="sex")
    plt.savefig(DATA_DIR / "lmplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    sns.residplot(data=tips, x="total_bill", y="tip")
    plt.savefig(DATA_DIR / "residplot.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Export
    sns.barplot(data=tips, x="day", y="tip", hue="sex")
    export_path = DATA_DIR / "plot_export.png"
    plt.savefig(export_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved seaborn export to {export_path}")


def main():
    numpy_essentials()
    pandas_essentials()
    seaborn_essentials()


if __name__ == "__main__":
    main()
