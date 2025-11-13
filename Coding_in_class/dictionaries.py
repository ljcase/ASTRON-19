exaple_dict = {
    "class": "ASTR 19",
    "prof": "Brant",
    "awsomeness": 10
}

print(exaple_dict)
print(type(exaple_dict))

course = exaple_dict["class"]
print(course)

exaple_dict["awsomeness"] += 1
print(exaple_dict)

print(exaple_dict.keys())       

for x in exaple_dict.keys():
    print(x, exaple_dict[x])