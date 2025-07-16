from write_file import write_invoice, write_return_invoice
from read_file import opening
import datetime

def rent_land():
    print("\t")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The process of rental land:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    name = input("Enter your name: ")
    
    #Try except for number
    while True:
        numb = input("Enter a 10-digit number: ")
        try:
            if not numb.isdigit() or len(numb)!= 10:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a 10-digit number.")
            continue

    # Retrieve the 2D list of land data
    listt = []
    total_cumulative_cost=0
    land_data = opening()

    while True:
        valid = False
        kitta_number = input("Enter the kitta number you want to rent: ")
        for i in land_data:
            if kitta_number == i[0] and i[-1] == "Available":
                address = i[1]
                direction = i[2]
                available_anna = int(i[3])
                while True:
                    anna = int(input("Enter the anna you want: "))
                    if anna == available_anna:
                        duration = int(input("Enter the duration in months: "))
                        rented_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        info = [kitta_number, duration, rented_date]
                        listt.append(info)
                        price_per_anna = int(i[4])
                        total_cost = price_per_anna * anna * duration
                        total_cumulative_cost += total_cost
                        i[-1] = "Not Available"
                        write_invoice(name, numb, kitta_number, address, direction, anna, duration, total_cost,total_cumulative_cost, rented_date)
                        print("The land has been rented successfully.\n")
                        valid = True
                        break
                    else:
                        print("The customer must rent all the available anna.")

        if not valid:
            print("Kitta number is not found or not available.")

        count = input("Do you want to continue? (yes/no): ")
        if count.lower() != "yes":
            break    

   
    # Write the updated land data back to the file
    file = open("Coursework.txt", "w")
    for i in land_data:
        file.write(",".join(i) + "\n")
    return listt

def return_land():
    print("~~~~~~~~~~~~~~~~~~~~")
    print("Land return process:")
    print("~~~~~~~~~~~~~~~~~~~~")
    name = input("Enter your name: ")
    
    #Try except for number
    while True:
        numb = input("Enter a 10-digit number: ")
        try:
            if not numb.isdigit() or len(numb)!= 10:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a 10-digit number.")
            continue
        
    rented_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    
    # Retrieve the 2D list of land data
    land_data = opening()
    
    while True:
        kitta_number = input("Enter the kitta number you want to return: ")

        # Find the land in the land data
        valid_land = None
        for i in land_data:
            if kitta_number == i[0] and i[-1] == "Not Available":
                valid_land = i
                break

        if not valid_land:
            print("Invalid kitta number or the land is not rented.")
            count = input("Do you want to continue returning land? (yes/no): ")
            if count.lower() != "yes":
                return  # Exit the function if user chooses not to continue
            else:
                continue
        
        address=i[1]
        direction=i[2]
        
    
        # Calculate fine, total amount, and extra months
        months_taken = int(input("Enter the number of months you have taken the land for: "))
        months_returning = int(input("Enter the number of months you are returning for: "))

        if months_returning >= months_taken:
            #fine if the land is returned after the rented months
            extra_months = months_returning - months_taken
            price_per_month = int(valid_land[4])
            total_price = months_returning * price_per_month
            fine_percentage = 0.10  # 10% fine per month
            total_fine = round(extra_months * price_per_month * fine_percentage)  # 10% fine for each extra month
            total_amount = total_price + total_fine
        else:
            #fine if returned before the rented months
            total_price = months_returning * int(valid_land[4])  # Price per anna * months taken
            total_fine = 0  # No fine if returned before rented months
            total_amount = total_price

        # Calling the function to write return invoice
        write_return_invoice(name, numb, kitta_number, address, direction, months_taken, months_returning, total_fine, total_amount, rented_date)
        
            
        # to update land availability in Coursework.txt file
        for i in land_data:
            if i[0] == kitta_number:
                i[-1] = "Available"
                break

        file = open("Coursework.txt", "w")
        for i in land_data:
            file.write(",".join(i) + "\n")        
        
        # Print a success message
        print("Land is now updated accordingly!")

        # Update the unavability status to available
        print("\nUpdated Land Availability:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Kitta""\t"" Address""\t"" Direction""\tAnna""\tPrice""\t""Availability")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        for i in land_data:
            if len(i) >= 6:
                print("%-8s %-15s %-15s %-7s %-8s %-8s" % (i[0], i[1], i[2], i[3], i[4], i[5]))
                
        
        count = input("Do you want to continue returning land? (yes/no): ")
        if count.lower() != "yes":
            break
