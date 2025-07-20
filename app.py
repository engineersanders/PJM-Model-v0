
import streamlit as st
import pandas as pd
import joblib
import io

st.set_page_config(page_title="PJM Hourly Load Forecaster", layout="wide")

st.title("PJM Hourly Load Forecaster")

@st.cache_resource
def load_model():
    return joblib.load("pjm_load_gbr_model.joblib")

model = load_model()

st.markdown(
    """Upload a CSV containing the feature columns listed below,
    and download the resulting predictions as a new CSV.

    **Required columns**

    - `temp_72406`
    - `temp_72408`
    - `temp_72530`
    - `temp_72428`
    - `hour`
    - `dow`
    - `month`
    - `lag1`

    The order doesn't matter as long as the column names match exactly.
    """)

uploaded_file = st.file_uploader("Upload feature CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    with st.spinner("Scoring..."):
        preds = model.predict(df)
        df["load_pred"] = preds
    st.success(f"Forecast complete! {len(df)} rows scored.")
    st.dataframe(df.head())

    csv_buf = io.StringIO()
    df.to_csv(csv_buf, index=False)
    st.download_button(
        "Download predictions CSV",
        data=csv_buf.getvalue(),
        file_name="pjm_load_forecast.csv",
        mime="text/csv"
    )
