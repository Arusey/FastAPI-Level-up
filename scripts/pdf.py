import urllib.request

url = "https://www.irs.gov/pub/lrs-pdf/p1.pdf"

urllib.request.urlretrieve(url, "p1.pdf")