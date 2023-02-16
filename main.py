import requests

API_key = "1ecd2b254398465fb92ac340347869f1"

url="https://newsapi.org/v2/everything?q=apple&from=2023-02-15& \
    to=2023-02-15&sortBy=popularity&apiKey=" \
    "1ecd2b254398465fb92ac340347869f1"

req = requests.get(url)
content = req.json()
for article in content["articles"]:
    print(article["title"])

