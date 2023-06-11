import re

with open("full_name.txt", "r") as file:
    full_text = file.read()

pattern = r"Baby Name: (\w+)"
match = re.search(pattern, full_text)

if match:
    baby_name = match.group(1)
    print("baby name:", baby_name)
else:
    print("No baby name found!")