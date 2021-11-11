'''
There are five workers : James,John,Robert,Michael and William.
They work one by one and on weekends they rest.
Order is same as in the description
(James works on mondays,John works on tuesdays and so on).
You have to create a function 'task' that will take 3 arguments(w, n, c):

1. Weekday

2. Number of trees that must be sprayed on that day

3. Cost of 1 litre liquid that is needed to spray tree,
let's say one tree needs 1 litre liquid.
Let cost of all liquid be x

Your function should return string like this :
'It is (weekday) today, (name), you have to work,
you must spray (number) trees and you need (x) dollars to buy liquid'

For example:
task('Monday', 15, 2) -> 'It is Monday today, James, you have to work,
you must spray 15 trees and you need 30 dollars to buy liquid'
'''

def task(w,n,c):
    workers = ["James", "John", "Robert", "Michael", "William"]
    worker = ""
    if w == "Monday":
        worker = workers[0]
    elif w == "Tuesday":
        worker = workers[1]
    elif w == "Wednesday":
        worker = workers[2]
    elif w == "Thursday":
        worker = workers[3]
    elif w == "Friday":
        worker = workers[4]
    sum = c * n
    print("It is " + w + " today, " + worker + ", you have to work, you must spray " + str(n) + " trees and you need " + str(sum) + " dollars to buy liquid")

task("Monday",10,2)


#def task(w,n,c):
#    workers = {"Monday" : "James", "Tuesday" : "John", "Wednesday" : "Robert", "Thursday" : "Michael", "Friday" : "William"}
#    return f"It is {w} today, {workers[w]}, you have to work, you must spray {n} trees and you need {n * c} dollars to buy liquid"
