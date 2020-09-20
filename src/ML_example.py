# ###### this is simple ML program with use of Classification Tree method
# ###### this program learn sex of people from ghad, vazn, kafsh, and predict base on them

import csv
from sklearn import tree

x = []
y = []

with open('somefile_withdataforlearning.csv', 'r') as fin:
    data = csv.reader(fin)
    for line in data:
        x.append(line[1:4])     # ghad, vazn, kafsh!
        y.append(line[4])       # sex

clf = tree.DecisionTreeClassifier()
machine_xy = clf.fit(x, y)

newdata = [[185, 79, 43], [165, 57, 38]]
answer = machine_xy.predict(newdata)
print(answer[0], answer[1])
