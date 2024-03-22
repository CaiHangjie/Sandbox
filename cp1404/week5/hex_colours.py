"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

# CODE_COLOR_NAME dictionary
CODE_COLOR_NAME = {
    "Aquamarine1": "#7fffd4",
    "Aquamarine2": "#76eec6",
    "Asparagus": "#87a96b",
    "Baby Blue": "#89cff0",
    "Baker-Miller Pink": "#ff91af",
    "Beaver": "#9f8170",
    "Bisque3": "#cdb79e",
    "Bittersweet Shimmer": "#bf4f51",
    "Black Shadows": "#bfafb2",
    "CadetBlue3": "#7ac5cd"
}

for color_name, color_code in CODE_COLOR_NAME.items():
    print(f"{color_name:<20} is {color_code}")

color_name = input("Enter a color name: ").upper()
while color_name != "":
    if color_name in CODE_COLOR_NAME:
        print(f"The hexadecimal code for {color_name} is {CODE_COLOR_NAME[color_name]}")
    else:
        print("Invalid name")
    color_name = input("Enter a color name: ").upper()
