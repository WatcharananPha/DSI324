import pandas as pd
import streamlit as st

golden_df = pd.read_csv('golden_record.csv')

st.set_page_config(page_title="EGAT Realtime Power Dashboard (lakeFS)", layout="wide")

st.title("MDM Golden Record Data Model")

st.write("## Golden Records Table")
st.dataframe(golden_df)

st.write("## Confidence Ratio Distribution")
st.bar_chart(golden_df['confidence_ratio'].value_counts().sort_index())

min_conf = st.slider("Minimum Confidence Ratio", 0.0, 1.0, 0.8, 0.01)
filtered = golden_df[golden_df['confidence_ratio'] >= min_conf]
st.write(f"### Records with confidence ≥ {min_conf}")
st.dataframe(filtered)