listOfNo = []
while(True):
    choice = input("Do you want to add No in List press (y) or No (N)")
    if(choice == 'N' or choice == 'n'):
        break;
    if(choice == 'Y' or choice == 'y'):
        listOfNo.append(int(input("Please Enter No:-")))
print("Your List is:-", listOfNo)
if(len(listOfNo) > 1):
    listOfNo.sort()
    print(listOfNo)
    print("Second Largest No is:-",listOfNo[-2] )
else:
    print("Please enter atleast 2 no.s")
