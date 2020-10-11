firstList = list(map(int,input("Enter First List:-").split()))
print("List before Swap:-")
print(firstList)
temp = firstList[0];
firstList[0] = firstList[-1]
firstList[-1] = temp
print("List after Swap")
print(firstList)