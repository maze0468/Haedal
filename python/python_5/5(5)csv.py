import csv

with open("pokemon.csv", 'w') as c:
    wr = csv.writer(c)
    wr.writerow(['Name', 'skill 1', 'skill 2', 'skill 3'])

for j in range(3):
    name = input("Name: ")
    skills = ['','','']
    for i in range(3):
        print(f"skill {i+1}: ", end ='')
        skills[i] = input("")
    with open("pokemon.csv", 'a',newline='') as c:
        wr = csv.writer(c)
        wr.writerow([name, skills[0], skills[1], skills[2]])
