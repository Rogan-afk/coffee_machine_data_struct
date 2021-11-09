from resourcess import MENU
#print(MENU)


def counter():
    """Checks user_choice and counts the cash received,refunds if not enough cash"""
    global user_choice
    global MENU
    global resource
    global cost
    global sufficient
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("how many pennies?"))
    cost = [quarters * 0.25,dimes * 0.10,nickles * 0.05,pennies * 0.01]
    total_cost = round(sum(cost),2)
    print(f"your total inserted cash for this is order: ${total_cost}")
    if total_cost < MENU[user_choice]["cost"]:
        print("That's not enough money! sorry, refunded")
        sufficient = False  #some flag variable to come here
    else:
        if user_choice == "latte":
            resource[3] += 2.5
        if user_choice == "cappuccino":
            resource[3] += 3.0
        if user_choice == "espresso":
            resource[3] += 1.5
        print(f"Here's your change $:{round(total_cost - MENU[user_choice]['cost'],2)}")

def res_check():
    """Checks if there is sufficient resource in the inventory to make the customer's choice"""
    global sufficient
    while sufficient:
        if user_choice == "espresso":
            if resource[0] < MENU[user_choice]["ingredients"]["water"]:
                sufficient = False #some flag_variable becomes false
            elif resource[1] < MENU[user_choice]["ingredients"]["coffee"]:
                sufficient = False  #some flag_variable becomes false
            else:
                resource[0] = resource[0] - MENU[user_choice]["ingredients"]["water"]
                resource[1] = resource[1] - MENU[user_choice]["ingredients"]["coffee"]
        elif user_choice == "latte" or user_choice == "cappuccino":
            if resource[0] < MENU[user_choice]["ingredients"]["water"]:
                sufficient = False
                  # some flag_variable becomes false
            elif resource[1] < MENU[user_choice]["ingredients"]["coffee"]:
                sufficient = False
                  # some flag_variable becomes false
            elif resource[2] < MENU[user_choice]["ingredients"]["milk"]:
                sufficient = False
                  # some flag_variable becomes false
            else:
                resource[0] = resource[0] - MENU[user_choice]["ingredients"]["water"]
                resource[1] = resource[1] - MENU[user_choice]["ingredients"]["coffee"]
                resource[2] = resource[2] - MENU[user_choice]["ingredients"]["coffee"]



resource = [300,100,250,0]
while True:
    sufficient = True
    user_choice = input("What would you like? espresso/latte/cappuccino?\n")
    if user_choice == "report":
        print(f""" water:{resource[0]}ml\n,milk:{resource[2]}ml\n,coffee:{resource[1]} gms\n,cash :${resource[3]}""")
        continue
    if user_choice == "off":
        break
    cost = list()
    counter()
    if sufficient == False:
        continue
    res_check()
    if sufficient == False:
        print("Sorry, your order cannot be processed, your cash has been refunded\n")
        resource[3] = resource[3] - MENU[user_choice]['cost']
        continue

