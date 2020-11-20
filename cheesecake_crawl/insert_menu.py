import json

with open("dirty_menu.json", "r") as json_file:
    data = json.load(json_file)
    base_url = "https://www.thecheesecakefactory.com"

    # Menu
    del data["40239"]["path"]
    del data["40239"]["panel"]
    del data["40239"]["customcontent"]
    del data["40239"]["floodlightcat"]
    for item in data["40239"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Beverages
    del data["27952"]["descexpand"]
    del data["27952"]["path"]
    del data["27952"]["panel"]
    del data["27952"]["customcontent"]
    del data["27952"]["floodlightcat"]
    for item in data["27952"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    # print("\n")
    # Beer & Wine - IGNORE FOR NOW, ONLY A SINGLE ENTRY EXISTS.
    del data["27715"]
    # del data['27715']['descexpand']
    # del data['27715']['path']
    # del data['27715']['panel']
    # del data['27715']['customcontent']
    # del data['27715']['floodlightcat']
    # for item in data['27715']['background']:
    #     if 'linkId' in item:
    #         item.pop('linkId')
    #     item['image'] = base_url + item['image']
    #     item['linkUrl'] = base_url + item['linkUrl']
    #     # print(item)

    #print("\n")
    # Cocktails
    del data["36392"]["descexpand"]
    del data["36392"]["path"]
    del data["36392"]["panel"]
    del data["36392"]["customcontent"]
    del data["36392"]["floodlightcat"]
    for item in data["36392"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Margaritas & Mojitos
    del data["39968"]["descexpand"]
    del data["39968"]["path"]
    del data["39968"]["panel"]
    del data["39968"]["customcontent"]
    del data["39968"]["floodlightcat"]
    for item in data["39968"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    # print("\n")
    # Martinis & Daiquiris - IGNORE FOR NOW, ONLY A SINGLE ENTRY EXISTS.
    del data["39965"]
    # del data['39965']['descexpand']
    # del data['39965']['path']
    # del data['39965']['panel']
    # del data['39965']['customcontent']
    # del data['39965']['floodlightcat']
    # for item in data['39965']['background']:
    #     if 'linkId' in item:
    #         item.pop('linkId')
    #     item['image'] = base_url + item['image']
    #     item['linkUrl'] = base_url + item['linkUrl']
    #     # print(item)

    # print("\n")
    # Non-Alcoholic Specialties - IGNORE FOR NOW, ONLY A SINGLE ENTRY EXISTS.
    del data["38001"]
    # del data['38001']['descexpand']
    # del data['38001']['path']
    # del data['38001']['panel']
    # del data['38001']['customcontent']
    # del data['38001']['floodlightcat']
    # for item in data['38001']['background']:
    #     if 'linkId' in item:
    #         item.pop('linkId')
    #     item['image'] = base_url + item['image']
    #     item['linkUrl'] = base_url + item['linkUrl']
    #     # print(item)

    #print("\n")
    # Specialty Drinks
    del data["39963"]["descexpand"]
    del data["39963"]["path"]
    del data["39963"]["panel"]
    del data["39963"]["customcontent"]
    del data["39963"]["floodlightcat"]
    for item in data["39963"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Creamy Milkshakes
    del data["27717"]["descexpand"]
    del data["27717"]["path"]
    del data["27717"]["panel"]
    del data["27717"]["customcontent"]
    del data["27717"]["floodlightcat"]
    for item in data["27717"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Hot Drinks & Espresso
    del data["27718"]["descexpand"]
    del data["27718"]["path"]
    del data["27718"]["panel"]
    del data["27718"]["customcontent"]
    del data["27718"]["floodlightcat"]
    for item in data["27718"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    # print("\n")
    # Iced & Frozen Drinks - IGNORE FOR NOW, ONLY A SINGLE ENTRY EXISTS.
    del data["36526"]
    # del data['36526']['descexpand']
    # del data['36526']['path']
    # del data['36526']['panel']
    # del data['36526']['customcontent']
    # del data['36526']['floodlightcat']
    # for item in data['36526']['background']:
    #     if 'linkId' in item:
    #         item.pop('linkId')
    #     item['image'] = base_url + item['image']
    #     item['linkUrl'] = base_url + item['linkUrl']
    #     # print(item)

    # print("\n")
    # Other Drinks - IGNORE FOR NOW, ONLY A SINGLE ENTRY EXISTS.
    del data["28028"]
    # del data['28028']['descexpand']
    # del data['28028']['path']
    # del data['28028']['panel']
    # del data['28028']['customcontent']
    # del data['28028']['floodlightcat']
    # for item in data['28028']['background']:
    #     if 'linkId' in item:
    #         item.pop('linkId')
    #     item['image'] = base_url + item['image']
    #     item['linkUrl'] = base_url + item['linkUrl']
    #     # print(item)

    #print("\n")
    # Desserts
    del data["27803"]["descexpand"]
    del data["27803"]["path"]
    del data["27803"]["panel"]
    del data["27803"]["customcontent"]
    del data["27803"]["floodlightcat"]
    for item in data["27803"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Cheesecakes
    del data["39960"]["descexpand"]
    del data["39960"]["path"]
    del data["39960"]["panel"]
    del data["39960"]["customcontent"]
    del data["39960"]["floodlightcat"]
    for item in data["39960"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Ice Cream Delights
    del data["27723"]["descexpand"]
    del data["27723"]["path"]
    del data["27723"]["panel"]
    del data["27723"]["customcontent"]
    del data["27723"]["floodlightcat"]
    for item in data["27723"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Specialty Desserts
    del data["27724"]["descexpand"]
    del data["27724"]["path"]
    del data["27724"]["panel"]
    del data["27724"]["customcontent"]
    del data["27724"]["floodlightcat"]
    for item in data["27724"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Eggs & Omelettes & Saturday & Sunday Brunch
    del data["35415"]["descexpand"]
    del data["35415"]["path"]
    del data["35415"]["panel"]
    del data["35415"]["customcontent"]
    del data["35415"]["floodlightcat"]
    for item in data["35415"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Eggs & Omelettes
    del data["33050"]["descexpand"]
    del data["33050"]["path"]
    del data["33050"]["panel"]
    del data["33050"]["customcontent"]
    del data["33050"]["floodlightcat"]
    for item in data["33050"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Saturday & Sunday Brunch
    del data["37993"]["descexpand"]
    del data["37993"]["path"]
    del data["37993"]["panel"]
    del data["37993"]["customcontent"]
    del data["37993"]["floodlightcat"]
    for item in data["37993"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Flatbread Pizzas
    del data["37962"]["descexpand"]
    del data["37962"]["path"]
    del data["37962"]["panel"]
    del data["37962"]["customcontent"]
    del data["37962"]["floodlightcat"]
    for item in data["37962"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Glamburgers\u00ae & Sandwiches
    del data["37306"]["descexpand"]
    del data["37306"]["path"]
    del data["37306"]["panel"]
    del data["37306"]["customcontent"]
    del data["37306"]["floodlightcat"]
    for item in data["37306"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Kids
    del data["35598"]["descexpand"]
    del data["35598"]["path"]
    del data["35598"]["panel"]
    del data["35598"]["customcontent"]
    del data["35598"]["floodlightcat"]
    for item in data["35598"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Lunch Specials
    del data["35602"]["descexpand"]
    del data["35602"]["path"]
    del data["35602"]["panel"]
    del data["35602"]["customcontent"]
    del data["35602"]["floodlightcat"]
    for item in data["35602"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # New Items
    del data["40605"]["descexpand"]
    del data["40605"]["path"]
    del data["40605"]["panel"]
    del data["40605"]["customcontent"]
    del data["40605"]["floodlightcat"]
    for item in data["40605"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Pastas
    del data["37996"]["descexpand"]
    del data["37996"]["path"]
    del data["37996"]["panel"]
    del data["37996"]["customcontent"]
    del data["37996"]["floodlightcat"]
    for item in data["37996"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Salads
    del data["27767"]["descexpand"]
    del data["27767"]["path"]
    del data["27767"]["panel"]
    del data["27767"]["customcontent"]
    del data["27767"]["floodlightcat"]
    for item in data["27767"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Appertizer Salads
    del data["37960"]["descexpand"]
    del data["37960"]["path"]
    del data["37960"]["panel"]
    del data["37960"]["customcontent"]
    del data["37960"]["floodlightcat"]
    for item in data["37960"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Salads... part 2? wtf?
    del data["39971"]["descexpand"]
    del data["39971"]["path"]
    del data["39971"]["panel"]
    del data["39971"]["customcontent"]
    del data["39971"]["floodlightcat"]
    for item in data["39971"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # SkinnyLicious
    del data["27766"]["descexpand"]
    del data["27766"]["path"]
    del data["27766"]["panel"]
    del data["27766"]["customcontent"]
    del data["27766"]["floodlightcat"]
    for item in data["27766"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    # print("\n")
    # Cocktails - IGNORE FOR NOW, ONLY A SINGLE ENTRY EXISTS.
    del data["27732"]
    # del data['28028']['descexpand']
    # del data['28028']['path']
    # del data['28028']['panel']
    # del data['28028']['customcontent']
    # del data['28028']['floodlightcat']
    # for item in data['28028']['background']:
    #     if 'linkId' in item:
    #         item.pop('linkId')
    #     item['image'] = base_url + item['image']
    #     item['linkUrl'] = base_url + item['linkUrl']
    #     # print(item)

    #print("\n")
    # Salads... part 3!!!
    del data["39975"]["descexpand"]
    del data["39975"]["path"]
    del data["39975"]["panel"]
    del data["39975"]["customcontent"]
    del data["39975"]["floodlightcat"]
    for item in data["39975"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Small Plates & Appetizers
    del data["37309"]["descexpand"]
    del data["37309"]["path"]
    del data["37309"]["panel"]
    del data["37309"]["customcontent"]
    del data["37309"]["floodlightcat"]
    for item in data["37309"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Specialties
    del data["37311"]["descexpand"]
    del data["37311"]["path"]
    del data["37311"]["panel"]
    del data["37311"]["customcontent"]
    del data["37311"]["floodlightcat"]
    for item in data["37311"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Small Plates & Snacks & Appetizers
    del data["35413"]["descexpand"]
    del data["35413"]["path"]
    del data["35413"]["panel"]
    del data["35413"]["customcontent"]
    del data["35413"]["floodlightcat"]
    for item in data["35413"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Appetizers
    del data["39969"]["descexpand"]
    del data["39969"]["path"]
    del data["39969"]["panel"]
    del data["39969"]["customcontent"]
    del data["39969"]["floodlightcat"]
    for item in data["39969"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Small Plates & Snacks
    del data["37299"]["descexpand"]
    del data["37299"]["path"]
    del data["37299"]["panel"]
    del data["37299"]["customcontent"]
    del data["37299"]["floodlightcat"]
    for item in data["37299"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Specialties
    del data["39970"]["descexpand"]
    del data["39970"]["path"]
    del data["39970"]["panel"]
    del data["39970"]["customcontent"]
    del data["39970"]["floodlightcat"]
    for item in data["39970"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Steaks, Chops, Fish & Seafood
    del data["37304"]["descexpand"]
    del data["37304"]["path"]
    del data["37304"]["panel"]
    del data["37304"]["customcontent"]
    del data["37304"]["floodlightcat"]
    for item in data["37304"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # "Super" Foods
    del data["39978"]["descexpand"]
    del data["39978"]["path"]
    del data["39978"]["panel"]
    del data["39978"]["customcontent"]
    del data["39978"]["floodlightcat"]
    for item in data["39978"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    #print("\n")
    # Timeless Classics
    del data["40603"]["descexpand"]
    del data["40603"]["path"]
    del data["40603"]["panel"]
    del data["40603"]["customcontent"]
    del data["40603"]["floodlightcat"]
    for item in data["40603"]["background"]:
        if "linkId" in item:
            item.pop("linkId")
        item["image"] = base_url + item["image"]
        item["linkUrl"] = base_url + item["linkUrl"]
        # print(item)

    with open("clean_menu.json", "w") as outfile:
        json.dump(data, outfile, indent=2)