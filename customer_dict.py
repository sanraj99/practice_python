# Create an list

customers = []

# Create a loop

while True:

    # Get input and make it work for y or n
    createEntry = raw_input('Enter Customer (Yes/No) : ')
    createEntry = createEntry[0].lower()

    # Check to leave a loop
    if createEntry == 'n':
        break
    # Get Customer data
    else:
        fname , lname = raw_input('Enter the Customer Name : ').split()
    # Add customer data to list
        customers.append({'fname': fname, 'lname': lname})

# Print customer data

for cust in customers:

    print(cust['fname'], cust['lname'])



