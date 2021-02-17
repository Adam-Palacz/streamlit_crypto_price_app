from datetime import date
import pandas as pd
import ccxt


def today_date():
    today = date.today().strftime("%Y-%m-%d")
    return today


# App import cryptocurrencies data from crypto exchanges thanks ccxt (https://github.com/ccxt)
def get_crypto_data(symbol, limit=today_date(), time_resolution="1d", exchange="binance"):
    get_exchange = getattr(ccxt, exchange)({"verbose": False})
    ohlcv_build = get_exchange.fetch_ohlcv(symbol, time_resolution, since=None, limit=None)
    ohlcv_df = pd.DataFrame(ohlcv_build, columns=["timestamp", "open", "high", "low", "close", "volume"])
    ohlcv_df["timestamp"] = pd.to_datetime(ohlcv_df["timestamp"], unit="ms")
    ohlcv_df = ohlcv_df[ohlcv_df.timestamp <= limit]
    ohlcv_df.end_date = limit
    ohlcv_df.symbol = symbol
    final_df = ohlcv_df.set_index("timestamp")
    return final_df[::-1]
