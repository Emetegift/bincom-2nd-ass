with open("full_name.txt", "r") as file:
    full_name = file.read().strip()


names =full_name.split(" ")
first_name = names[0]
last_name = names[-1]
middle_name = " ".join(names[1:-1])
# middle_name = names[1]


print("First Name:", first_name)
print("Last Name:", last_name)
print("Middle Name:", middle_name)