# Challenge 1: Name the variable types of the following variables. Print them out into console in the format "Variable: Variable Type" (might have to google "how to print variables in python")

var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4
print(var1, ": Integer")
print(var2, ": String")
print(var3, ": Character")
print(var4, ": Double")

# Challenge 2: Pass list1 into list2. However, list2 must contain the elements of list1 in order. Print list2. +0.3 if you can create a function to order a list and can display it on your website

list1 = [5, 3, 4, 1, 2]
list2 = list1
# def orderList (list):
# ?
# I WOULD USE list2.sort() BUT I'M APPARENTLY NOT ALLOWED TO AAAAAAAAA
# I WOULD ALSO SORT IT MANUALLY bUt THatS CHeaTiNg!!11!!!!1!
print(list2)

# Challenge 3: Find a way to add 3 to each element in the array. Then, take the average of the array and put it into the variable avg. +0.2 if you can turn this into a function and display it on your website.

averageList = [23, 41, 90, 55, 71, 83]
# def averageList (list):
# ?
averageList[0] += 3
averageList[1] += 3
averageList[2] += 3
averageList[3] += 3
averageList[4] += 3
averageList[5] += 3
avg = (averageList[0] + averageList[1] + averageList[2] + averageList[3] + averageList[4] + averageList[5]) / 6
print(avg)