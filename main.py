from pybit import inverse_perpetual


session = inverse_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key="lAQbwnADHXBtVszS2Z",
    api_secret="R174Q1JVjpd5mlHcVqbG1JdnH9cBfVG27pLT"
)
requests = (session.get_wallet_balance(coin="USDT"))
print(requests)


#print(session.get_wallet_balance(coin="BTC"))

