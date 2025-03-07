COLOR_TO_CODE = {"Absolute Zero": "#0048ba", "Apricot": "#fbceb1", "Amethyst": "#9966cc", "Barn Red": "#7c0a02",
                "Beige": "#f5f5dc", "Carnelian": "#b31b1b", "Dark Brown": "#654321", "Egyptian Blue" : "#1034a6"}
print(COLOR_TO_CODE)

for color,code in COLOR_TO_CODE.items():
    print(f"{color:<13} is {code}")
color_name= input("Enter Color Name: ").title()

while color_name != "":
    try:
        print(color_name, "is", COLOR_TO_CODE[color_name])
    except KeyError:
        print("Invalid Color Name!")
    color_name = input("Enter Color Name: ").title()