import http.client
def finnhub():
    conn = http.client.HTTPSConnection("finnhub-realtime-stock-price.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "finnhub-realtime-stock-price.p.rapidapi.com",
        'x-rapidapi-key': "4477ed2d7fmsh5ebfe59dfc5b92fp18bd72jsn6618d344a800"
        }

    conn.request("GET", "/stock/profile?symbol=AAPL", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")