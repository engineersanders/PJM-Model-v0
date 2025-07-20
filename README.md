# PJM Hourly Load Forecasting Package (No-Python-Install Needed)

This repo contains two ways to use the trained PJM hourly load model without installing Python locally:

## 1. Excel 365 with Python in Excel
Open `pjm_load_forecast_template.xlsx` in Microsoft 365 (Fast/Insider build with Python in Excel).

1. Paste or link your feature rows in the **Inputs** sheet.
2. In any empty cell, enter something like:

    ```excel
    =PY("
    import pandas as pd, joblib
    model = joblib.load('pjm_load_gbr_model.joblib')
    df = Inputs
    df['load_pred'] = model.predict(df)
    df
    ")
    ```

   That Python cell will return a new DataFrame with the `load_pred` column.
3. Copy/paste the output where you need it.

**Tip:** Keep `pjm_load_gbr_model.joblib` in the same folder as the workbook so Python in Excel can find it.

## 2. Web Dashboard (Streamlit)

Files:
- `app.py` — Streamlit app
- `requirements.txt` — dependencies
- `pjm_load_gbr_model.joblib` — trained model
- `example_features.csv` — sample input

### Run locally (if you have Python)

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Deploy to Streamlit Cloud

1. Push these files to a new GitHub repo.
2. Go to **https://streamlit.io/cloud** and link the repo.
3. Set **Main file** to `app.py`.
4. Click **Deploy** (free tier works fine).

Then share the generated URL with anyone who needs forecasts.

---

Enjoy!