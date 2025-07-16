from operation import rent_land, return_land
from read_file import opening


def design():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("\t\t~~~~~~~~~Welcome to Techno Property, Nepal~~~~~~~~\n")
    print("\t\t\t\tTillottama-4, Butwal")
    print("\t\t\t\tMobile:9800711771")
    print("\t\t\tEmail add:companytechno11@gmail.com")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")


def table():
    data = opening()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Kitta""\t"" Address""\t"" Direction""\t""Anna""\t""Price""\t""Availability")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    for i in data:
        if len(i) >= 6: # Added a check to ensure the row has enough elements
            print("%-8s %-15s %-15s %-7s %-8s %-8s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
        
design()
table()

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    while True:
        print("\nEnter 1 to rent the land.")
        print("Enter 2 to return the land.")
        print("Enter 3 to exit the process.\n")
        option = int(input("Please enter your option: "))

        if option <= 0:
            print("Invalid option. Please enter a positive option.")
            continue

        if option == 1:
            rent_land()
        elif option == 2:
            table()
            return_land()
        elif option == 3:
            print("The process is exited.Thank you")
            break
        else:
            print("Invalid option. Please enter a valid option.")
            
main()
