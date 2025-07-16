import datetime

def write_invoice(name,numb, kitta_number, address, direction, anna, duration,total_cost,total_cumulative_cost,rented_date):
    
    # Write invoice to the console
    print("\t")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\tInvoice:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Time of the rent: Rs.", rented_date)
    print("Name of the borrower:", name)
    print("Number of the borrower:", numb)
    print("Taken Kitta Number:", kitta_number)
    print("Adress:", address)
    print("Direction of land:", direction)
    print("Number of Anna taken:", anna)
    print("Duration (in months):", duration)
    print("Total Cost: Rs.", total_cost)
    print("Final cost: Rs.", total_cumulative_cost)
    print("Invoice has been generated.Thanks for choosing us")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    invoice_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Write invoice to a text file
    with open("invoice.txt", "a") as file:
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        file.write("\tInvoice is generated here:\n")
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        file.write("Rented invoice date:" + rented_date + "\n") 
        file.write("Name of the borrower: " + name + "\n")
        file.write("Number of the borrower:"+ str(numb) + "\n")
        file.write("Taken Kitta Number: " + kitta_number + "\n")
        file.write("Address: " + address + "\n")
        file.write("Direction of land: " + direction + "\n")
        file.write("Anna taken: " + str(anna) + "\n")
        file.write("Duration (in months): " + str(duration) + "\n")
        file.write("Total Cost: Rs. " + str(total_cost) + "\n")
        file.write("Final cost: Rs."+str( total_cumulative_cost)+"\n")
        file.write("~~~~~~~~~~~Thanks for choosing us~~~~~~~~~~~~~~\n")
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        

def write_return_invoice(name, numb, kitta_number, address, direction, months_taken, months_returning, total_fine, total_amount,returned_date):
    # Write return invoice to the console
    print("\t")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\tReturn Invoice:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Time of the rent returned: Rs.", returned_date)
    print("Name:", name)
    print("Number of the borrower:", numb)
    print("Kitta Number:", kitta_number)
    print("Adress:", address)
    print("Direction of land:", direction)
    print("Months Taken:", months_taken)
    print("Months Returning For:", months_returning)
    print("Total Fine: Rs.", total_fine)
    print("Total Amount: Rs.", total_amount)
    print("Extra Months: ", months_returning - months_taken)
    print("Return invoice has been generated successfully!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Write return invoice to a text file
    with open("return_invoice.txt", "a") as file:
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        file.write("Return Invoice is generated here:\n")
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        file.write("Rented invoice date:" + returned_date + "\n")
        file.write("Name: " + name + "\n")
        file.write("Number of the borrower:"+ str(numb) + "\n")
        file.write("Kitta Number: " + kitta_number + "\n")
        file.write("Address: " + address + "\n")
        file.write("Direction of land: " + direction + "\n")
        file.write("Months Taken: " + str(months_taken) + "\n")
        file.write("Months Returning For: " + str(months_returning) + "\n")
        file.write("Total Fine: Rs. " + str(total_fine) + "\n")
        file.write("Total Amount: Rs. " + str(total_amount) + "\n")
        file.write("Extra Months: " + str(months_returning - months_taken) + "\n")
        file.write("~~~~~~~~~~~Thanks for choosing us~~~~~~~~~~~~~~\n")
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
