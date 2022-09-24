person = {
        "f_name": "Didier",
        "l_name": "Zublena",
        "age": 50,
        "hometown": "Baune",
        "current_city": "Lyon",
        "username": "colonelz"
        }

print("Exercise 1")
# Q1
print(person)

print(person["f_name"])
print(person["l_name"])
print(person["age"])
print(person["hometown"])
print(person["current_city"])
print(person["username"])

print("\nExercise 2")
# Q2
print(f"This person's first name is {person['f_name']}, last name is {person['l_name']}, is {person['age']} years old, lives in {person['current_city']}, and their username is {person['username']}.")
print(f"For security reasons, we might asks them for their hometown, which is {person['hometown']}")

print("Exercise 3")
# Q3
definitions = {
        "python": "programming language",
        "variable": "keep a value in memory for later use",
        "list": "list of values",
        "method": "function in an class",
        "if_statement": "logical statement used to determine if a condition is true or not",
        "dictionary": "variable containing multiple key-value pairs",
        "function": "block of code which ony runs when it is called"
        }


print(f"\n- python:\n{definitions['python']}")
print(f"\n- variable:\n{definitions['variable']}")
print(f"\n- list:\n{definitions['list']}")
print(f"\n- method:\n{definitions['method']}")
print(f"\n- if_statement:\n{definitions['if_statement']}")
print(f"\n- dictionary:\n{definitions['dictionary']}")
print(f"\n- function:\n{definitions['function']}")

print("\nExercise 4")
# Q4
for word, definition in definitions.items():
    print(f"\n- {word}:\n{definition}")


print("Exercise 5")
# Q5
sc_counties = {
        "abbeville": "abbeville",
        "aiken": "aiken",
        "allendale": "allendale",
        "anderson": "anderson",
        "bamberg": "bamberg",
        "barnwell": "barnwell",
        "beaufort": "beaufort",
        "berkley": "moncks corner",
        "calhoun": "st. matthews",
        "charleston": "charleston",
        "cherokee": "gaffney",
        "chesterfield": "chesterfield",
        "clarendon": "manning",
        "colleton": "walterboro",
        "darlington": "darlington",
        "dillon": "dillon",
        "dorchester": "st. george",
        "edgefield": "edgefield",
        "fairfield": "winnsboro",
        "florence": "florence",
        "georgetown": "georgetown",
        "greenville": "greenville",
        "greenwood": "greenwood",
        "hampton": "hampton",
        "horry": "conway",
        "jasper": "ridgeland",
        "kershaw": "camden",
        "lancaster": "lancaster",
        "laurens": "laurens",
        "lee": "bishopville",
        "lexington": "lexington",
        "marion": "marion",
        "malboro": "bennettsville",
        "mccormick": "mccormick",
        "newberry": "newberry",
        "oconee": "walhalla",
        "orangeburg": "orangeburg",
        "pickens": "pickens",
        "richland": "columbia",
        "saluda": "saluda",
        "spartanburg": "spartanburg",
        "sumter": "sumter",
        "union": "union",
        "williamsburg": "kingstree",
        "york": "york"
        }

print("\nExercise 6")
# Q6
counties = ["union", "yorkshire", "malboro", "greenville", "spartanburg", "saludo", "anderson", "newberry", "hampton", "charleston"]
for county in counties:
    if county in sc_counties:
        print(f"{county.title()} is in our dictionary, and the capital is {sc_counties[county].title()}")
    else:
        print(f"{county.title()} is not in our dictionary. We will add this county shortly. Thanks!")

print("\nExercise 8")
# Q8
anderson = {
        "anderson": 28106,
        "iva": 1218,
        "belton": 4134,
        "clemson": 13905,
        "easley": 22921
        }
greenville = {
        "greenville": 70720,
        "greer": 35308,
        "mauldin": 24724,
        "simpsonville": 22234,
        "travelers rest": 5253
        }
spartanburg = {
        "chesnee": 868,
        "greer": 35308,
        "spartanburg": 38732,
        "landrum": 2376,
        "wellford": 2378
        }
laurens = {
        "clinton": 8490,
        "fountain inn": 7799,
        "laurens": 9139,
        "cross hill": 507,
        "gray court": 795
        }
newberry = {
        "newberry": 10277,
        "little mountain": 291,
        "peak": 64,
        "pomaria": 179,
        "prosperity": 1180
        }

counties = [["anderson", anderson], ["greenville", greenville], ["spartanburg", spartanburg], ["laurens", laurens], ["newberry", newberry]]
for county in counties:
    for city, population in county[-1].items():
        print(f"In {city.title()}, {county[0].title()}, the current population is {population}")

print("\nExercise 9")
# Q9
sc_counties = {
        "anderson": ["anderson", "easley", "clemson"],
        "greenville": ["greenville", "greer", "mauldin"],
        "spartanburg": ["spartanburg", "greer", "wellford"],
        "laurens": ["laurens", "clinton", "fountain inn"],
        "newberry": ["newberry", "prosperity", "little mountain"]
        }

for county, cities in sc_counties.items():
    print(f"In {county.title()}, the largest cities are {cities[0].title()}, {cities[1].title()}, and {cities[2].title()}")

