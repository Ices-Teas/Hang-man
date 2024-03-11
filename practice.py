list_location = ["Kamuting", "Kuala Kangsar", "Gopeng", "Slim River"]
list_KM = [199, 241.9, 296.1, 372.6]

def camViewer():
    print("List of speed camera location")
    print("------------------------------")
    for i in range(4):
        print(i+1, " . ", " KM ", list_KM[i], " , ", list_location[i], "junction")

def OffenderRecord():
    infile = open("C:\\users\\mhazi\\documents\\Offender_record_NAUFALHAZIM.txt", "a")
    infile.write("Name: "+input("Enter offender name: "))
    infile.write("\n"+"Identification number: "+input("Enter identification number: "))
    infile.write("\n"+"Phone number: "+input("Enter phone number: "))
    infile.write("\n"+"Type of offence: "+input("Enter type of offence: "))
    infile.write("\n"+"Fine: RM "+input("Enter fine: "))
    infile.close()




def function_menu():
    print("-----RMP OPS Summon-----")
    option = input(" A: View Speed Camera Location \n B: Create New Offence Record \n Enter your option: ").upper()
    while option != "Q":
        if option == "A":
            camViewer()
        elif option == "B":
            OffenderRecord()
        else:
            print("Invalid input!")
        option = input("Do you wish to continue? Enter Option or press Q to quit: ").upper()

function_menu()
































