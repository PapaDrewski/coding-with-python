first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #this is an f-string that combines the values of first_name and last_name and stuff it into one variable
                                        # f-strings are a way to format strings by using the f character and {} to represent the variables
print(full_name)                        #this will print out ada lovelace


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!") #this will print out Hello, Ada Lovelace! i's adds a title method to the full_name variable and the world hello



first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message) #this will print out Hello, Ada Lovelace! it combines the message variable with the full_name variable and prints it out