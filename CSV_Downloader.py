from urllib import request
btc_url = 'http://chart.finance.yahoo.com/table.csv?s=GBTC&a=1&b=5&c=2017&d=2&e=5&f=2017&g=d&ignore=.csv'

# csv_url = input("Enter CSV URL: ")


def download_stock_data(csv_url):
    requested_url = request.urlopen(csv_url)
    csv = requested_url.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    destination = r"btc.csv"
    file = open(destination, 'w')
    for line in lines:
        file.write(line + '\n')
    file.close()

download_stock_data(btc_url)

