# cd ../../pySBAPI/
import streamlit as st
import requests
import pandas as pd

API_URL = "http://211.109.122.32:8000/bdh"

st.title("블벅 데이터 조회")

ticker = st.text_input("티커", "SPX Index")
field = st.text_input("필드", "PX_LAST")
start = st.text_input("시작일 (YYYY-MM-DD)", "2024-01-01")
end = st.text_input("종료일 (YYYY-MM-DD)", "2024-02-01")

if st.button("가지고 오기"):
    params = {
        "ticker": ticker,
        "field": field,
        "start": start,
        "end": end,
    }
    res = requests.get(API_URL, params=params)
    df = pd.DataFrame(res.json())
    st.dataframe(df)

