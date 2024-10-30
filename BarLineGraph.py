import matplotlib.pyplot as ok

sNames = ["Sanjay", "Rahul", "Karan","Ramesh", "Ajay", "Piyush", "Priya"]
sMarks = [35, 48, 28, 25, 45, 50, 46 ]

Perc = []

for x in sMarks:
    res = (x/50)*100
    Perc.append(res)

print(Perc)

def lineChart():
    ok.plot(sNames, sMarks)
    ok.title("Students Marks Graph")
    ok.xlabel("Student's Names")
    ok.ylabel("Student's Marks")
    ok.show()




def percBar():
    ok.bar(sNames, Perc)
    ok.title("Student's Percentage Graphs")
    ok.xlabel("Student's Names")
    ok.ylabel("Student's Percentge")
    ok.show()

percBar()