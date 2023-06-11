def sort(names):
    # n = len(names)
    for i in range(len(names)):
        for j in range(len(names)-1):
            if names[j] > names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]



def binary_search(names, target):
    low = 0
    high = len(names)-1

    while low<=high:
        mid = (low + high)//2
        if names[mid]==target:
            return mid
        elif names[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

names = ["John", "Sunday,", "Kelvin", "Val", "Gift", "Sarah", "Mathida", "Daniel" ]
target_name = "Gift"
# This will sort the names alphabetically
sort(names)
print("Sorted Names:", names)

index = binary_search(names, target_name)
if index != -1:
    print("Found at index:", index)

else:
    print("Not found in the list!")