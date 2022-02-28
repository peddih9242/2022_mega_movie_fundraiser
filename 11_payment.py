def string_checker(choice, options):
    
    # check for valid input in each list
    for var_list in options:

        # look for valid input in each list
        if choice in var_list:
            chosen = var_list[0].title()
            valid = "yes"
            break
        else:
            valid = "no"
    if valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"

# main routine

ticket_costs = [7.5, 10.5, 10.5, 10.5, 6.5]
ticket_price = 0

payment_options = [
    ["cash", "coins"],
    ["credit", "card", "debit card", "credit card"]
]

payment = "invalid choice"
while payment == "invalid choice":
    payment = input("What payment method would you like to use? ")
    check_payment = string_checker(payment, payment_options)

print(check_payment)
for price in ticket_costs:
    if check_payment == "Credit":
        ticket_price = price * 1.05
    else:
        ticket_price = price
    print("Price: ${:.2f}".format(ticket_price))
    print()
