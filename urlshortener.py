# doc about this https://cutt.ly/api-documentation/cuttly-links-api
# The requests module allows you to send HTTP requests using Python
import requests
api_key = "3c20d1d7d5a11f27aac76508c71d528b0db35"
url = "https://www.cnbc.com/2022/09/01/thursdays-losses-bring-the-sp-500-to-a-critical-juncture-that-could-signal-whats-next-for-stocks.html"
# A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces {}
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
# we can also have an alias instead of random HEX
# alias = "SongHu516"
# api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name={alias}"
response = requests.get(api_url)
# parse as json format
temp_data = response.json()
# the response from the web has a url for some reason
data = temp_data["url"]
if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
    print("Title:", data["title"])
else:
    print("[!] Error Shortening URL:", data)
