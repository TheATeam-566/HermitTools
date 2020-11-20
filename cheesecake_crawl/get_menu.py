from bs4 import BeautifulSoup
import requests
import json

r = requests.get("https://www.thecheesecakefactory.com/menu/")
soup = BeautifulSoup(r.content, "html.parser")

# get the script with a type of application/json on the cheesecake factory
script = soup.find("script", {"type": "application/json"})

# turn it into a string, removing the first 48 characters and last 10 characters (the script tags)
data = json.loads(str(script)[48:-10])

# dump to a file called "menu.json"
with open("dirty_menu.json", "w") as outfile:
    json.dump(data, outfile, indent=2)
