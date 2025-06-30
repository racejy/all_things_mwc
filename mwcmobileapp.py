import streamlit as st
import requests
import datetime

def get_price():
    try:
        response = requests.get("https://pacificpool.ws/price-index")
        response.raise_for_status()
        return response.json()
    except:
        return {"price": "N/A", "timestamp": 0}

data = get_price()
timestamp = datetime.datetime.fromtimestamp(data['timestamp'])

st.set_page_config(page_title="MWC Price", layout="centered")
st.title("MWC Price")
st.metric(label="Current Price (USD)", value=f"${data['price']}")
st.caption(f"Last Updated: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
