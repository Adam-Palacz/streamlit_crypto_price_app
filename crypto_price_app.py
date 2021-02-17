import streamlit as st
from get_crypto import get_crypto_data
from PIL import Image

st.set_page_config(layout='wide')

image = Image.open('logo.png')

st.image(image, width=500)

st.title('Streamlit Crypto Price App')

st.markdown("""
This app retrieves chosen cryptocurrency prices from **Binance** !
""")

expander_bar = st.beta_expander("About")
expander_bar.markdown("""
* **Python libraries:** pandas, streamlit,
* **Inspired by:** [Data Professor](https://www.youtube.com/channel/UCV8e2g4IWQqK71bbzGDEI4Q).
* **Credit:** App is importing cryptocurrencies data from crypto exchanges thanks [ccxt](https://github.com/ccxt).
""")

col1 = st.sidebar
col2, col3 = st.beta_columns((4, 1))

col1.header('Options')

units = ['BTC', 'ETH', 'LSK', 'LTC']

price_unit = col1.selectbox('Select price unit', ('USDT', 'BUSD', 'EUR', 'BTC'))
currency_unit = col1.selectbox('Select currency', (units))
time = col1.selectbox('Select time resolution',
                      ('1d', '3d', '1w', '1M'))
col2.subheader("Crypto Data")
# '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h'
if price_unit == 'BTC' and currency_unit == 'BTC':
    col2 = None
else:
    get_data = f"{currency_unit}/{price_unit}"
    crypto_data = get_crypto_data(get_data, time_resolution=time)
    col2.dataframe(crypto_data)
    col2.subheader(get_data)
    col2.line_chart(data=crypto_data[["high", "low"]])
