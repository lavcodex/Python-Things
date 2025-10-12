# Process real-time stock data with various precision requirements and status flags.
symbol = "AAPL"
current = "157.230"
previous = "156.230"
volume = "45678900"
status = "true"
shares = "25.5"

conv_current = float(current)
conv_volume = int(volume)
conv_status = bool(status)
conv_shares = float(shares)
conv_previous = float(previous)

price_change = conv_current - conv_previous
persentage = price_change % 100
portfolio_value = conv_shares * conv_current
if_gaining = price_change >0
print(f"Financial Data\nstock symbol: {symbol}\ncurrent price: {conv_current}\nprevious_close: {conv_previous}\nvolume: {conv_volume}\nmarket open: {conv_status}\nuser shares: {shares}\nportfolio value: {portfolio_value}")