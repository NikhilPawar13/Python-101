firstList = list(map(int,input("Enter First List:-").split()))
secondList = list(map(int,input("Enter First List:-").split()))
print("Both list Before Merger and sort")
print(firstList)
print(secondList)
listMerge = firstList + secondList
print("Merged both List and sorted...")
listMerge.sort()
print(listMerge)