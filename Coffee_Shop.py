print("Welcome to the Python Coffee Shop!")
 
customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")
 
price_coffee = 3.50
price_latte = 4.00
price_matcha = 4.50

while True:
 
    print("Coffee: $" + str(price_coffee))
    print("Latte: $" + str(price_latte))
    print("Matcha: $" + str(price_matcha))
     
    choice = input("What would you like to order? (coffee/latte/matcha): ")
     
    if choice == "coffee":
         cost = price_coffee
    elif choice == "latte":
         cost = price_latte
    elif choice == "matcha":
         cost = price_matcha
    else:
        print("Sorry, we do not have that.")
        cost = 0

    quantity = int(input("How many cups would you like? "))

    student = input("Are you a student? (yes/no):")
     
    total_cost = cost * quantity
     
    if quantity > 1:
        print("You get a discount of $1.00!")
        total_cost -= 1.00

    if student == "yes":
       print("you get a 10% discount!")
       total_cost *= 0.9
       
    print("Your total is: $" + str(total_cost))

    second_order = input("would you like anything else?: (yes/no)")

    if second_order == "no":
        print("Thank you, " + customer_name + "! Please come again.")
        break
        

 
