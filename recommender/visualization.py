import plotly.express as px

def plot_similarity(item_sim_df, item):
    sims = item_sim_df[item].sort_values(ascending=False).iloc[1:6]
    fig = px.bar(sims, x=sims.index, y=sims.values, 
                 labels={'x':'Item','y':'Similarity'},
                 title=f"Top Similar Items to '{item}'")
    return fig
