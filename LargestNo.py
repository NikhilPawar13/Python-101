listOfNo = []
while(True):
    choice = input("Do you want to add No in List press (y) or No (N)")
    if(choice == 'N' or choice == 'n'):
        break;
    if(choice == 'Y' or choice == 'y'):
        listOfNo.append(int(input("Please Enter No:-")))
print("Your List is:-", listOfNo)
if(len(listOfNo) > 0):
    print("Largest No is:-", max(listOfNo))