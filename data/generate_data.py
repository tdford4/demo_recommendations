import pandas as pd
import numpy as np
import sqlite3
import os

def generate_data(n_users=50, n_items=25, sparsity=0.3, seed=42):
    np.random.seed(seed)
    users = [f"user_{i}" for i in range(1, n_users+1)]
    items = [f"item_{j}" for j in range(1, n_items+1)]

    rows = []
    for user in users:
        for item in items:
            if np.random.rand() < sparsity:
                rows.append((user, item, np.random.randint(1,6)))

    df = pd.DataFrame(rows, columns=["user_id","item_id","interaction"])
    return df

def save_to_csv_and_sql(df, csv_path="data/sample_data.csv", db_path="data/recommendations.db"):
    os.makedirs("data", exist_ok=True)
    df.to_csv(csv_path, index=False)
    conn = sqlite3.connect(db_path)
    df.to_sql("interactions", conn, if_exists="replace", index=False)
    conn.close()
    print(f"✅ Data saved to {csv_path} and {db_path}")

if __name__ == "__main__":
    df = generate_data()
    print(f"Generated {len(df)} rows, {df['user_id'].nunique()} users, {df['item_id'].nunique()} items.")
    save_to_csv_and_sql(df)
