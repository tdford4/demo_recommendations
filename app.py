import streamlit as st
import pandas as pd
from recommender.database import init_db, load_data
from recommender.model import build_item_similarity, recommend_items
from recommender.visualization import plot_similarity

# Load data
conn = init_db()
df = load_data(conn)

# Build model
item_sim_df = build_item_similarity(df)

# Streamlit UI
st.set_page_config(page_title="Item-to-Item Recommender", layout="wide")
st.title("🎯 Item-to-Item Recommendation Engine Demo")
st.markdown("Select an item to see recommendations and a similarity chart.")

# Item selection
all_items = sorted(df['item_id'].unique())
selected_item = st.selectbox("Choose an item:", all_items)

# Top N recommendations
top_n = st.slider("Number of recommendations:", 1, 10, 5)
recs = recommend_items(item_sim_df, selected_item, top_n)

st.subheader(f"Top {top_n} Recommendations for '{selected_item}'")
st.table(pd.DataFrame(recs, columns=["Item", "Similarity"]))

# Similarity chart
st.subheader(f"Similarity Chart for '{selected_item}'")
fig = plot_similarity(item_sim_df, selected_item)
st.plotly_chart(fig, use_container_width=True)

# Optional raw data view
if st.checkbox("Show raw interaction data"):
    st.dataframe(df)
