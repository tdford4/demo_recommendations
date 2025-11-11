import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_item_similarity(df):
    pivot = df.pivot_table(index='user_id', columns='item_id', values='interaction').fillna(0)
    similarity = cosine_similarity(pivot.T)
    return pd.DataFrame(similarity, index=pivot.columns, columns=pivot.columns)

def recommend_items(item_sim_df, item, top_n=5):
    if item not in item_sim_df.columns:
        return []
    recs = item_sim_df[item].sort_values(ascending=False).iloc[1:top_n+1]
    return list(zip(recs.index, recs.values))
