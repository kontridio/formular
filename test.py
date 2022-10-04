pole = []
pole = ["jan", "horak"]
print(pole)
pole.append("clain")
print(pole)
pole.remove("jan")
print(pole)
print(pole.__len__())

for prvek in pole:
    print(prvek)
pole = [["jmeno", "prijmeni"],["jmeno1", "prijmeni1"]]
print(pole)
print(" ")
for radek in pole:
    print(radek)
    for prvek in radek:
        print(prvek)

jsondata = {"prvek":"1", "object": {'1':"xxx",'2':"yyy"}}
print(jsondata["object"])

