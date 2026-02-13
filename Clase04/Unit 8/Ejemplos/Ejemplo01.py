breads = ["Rye bread", "Wheat", "White"]
meats = ["Meatball", "Sausage", "Chicken breast"]
vegis = ["Lettuce", "Tomato", "Cucumber"]
sauces = ["Mayonnaise", "Honey Mustard", "Chili"]

print("Possible combinations of David's sandwich shop")
for b in breads:
    for m in meats:
        for v in vegis:
            for s in sauces:
                print(f"{b} + {m} + {v} + {s}")