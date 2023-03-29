count = {"spencer":0, "pog":0, "dro":0, "mater": 0}

pog = ["spencer", "mater", "dro", "spencer", "spencer", "mater"]


for i in count.keys():
    for j in pog:
        if i == j:
            count[i] += 1
print(count)