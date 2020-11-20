import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Set firestore credentials and make a db object
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Opening clean_menu for parsing
with open("clean_menu.json", "r") as json_file:
    file = json.load(json_file)

# Create a dictionary object for insertion
for (k,v) in file.items():
    # Creating the data object. Contains a menu title (pastas, salads, etc.) and an accompanying description (some have no description)
    data = {
        u'title': str(v['title']),
        u'description': str(v['description']),
        u'items' : [{} for value in v['background']] # Generates n number of array of dictionaries
    }

    print(f"Title: {data['title']}:")
    print(f"Description: {data['description']}:")
    for i in range(len(v['background'])):
        # i gives us the number of elements in each category, e.g.: 3 pasta dishes on the menu, thus i ranges from 0 to 2
        data['items'][i].update({"caption" : v['background'][i]['caption']})
        data['items'][i].update({"image" : v['background'][i]['image']})
        data['items'][i].update({"linkUrl": v['background'][i]['linkUrl']})
        print(f"Added {i}: {data['items'][i]}")
    print("\n")

    # This line does the inserting to the database.
    menu_ref = db.collection(u'db').document(u'menu').collection(u'items').document(f"{v['title']}").set(data)