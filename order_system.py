def place_order(menu):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices, using the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    # Set up order list. Order list will store a list of dictionaries for
    # menu item name, item price, and quantity ordered
    order = []

    # Get the menu items mapped to the menu numbers
    menu_items = get_menu_items_dict(menu)

    # Launch the store and present a greeting to the customer
    print("Welcome to the Generic Take Out Restaurant.")

    place_order = True
    # TODO: Create a continuous while loop so customers can order multiple items
    while place_order: 
        print ("What is your order?")
        i=1
    
        # TODO: Loop through the menu dictionary, extracting the food category and
        # the options for each category
        for food_category, options in menu.items():

            # TODO: Loop through the options for each food category, extracting the
            # meal and the price
            for meal,price in options.items():

                # TODO: Print the menu item number, food category, meal, and price
                print_menu_line(i, food_category, meal, price)


                # TODO: Update the menu selection number
                i += 1
                

        # Ask customer to input menu item number
        menu_selection = input("Type menu number: ")

        # Update the order list using the update_order function
        # Send the order list, menu selection, and menu items as arguments
        order = update_order(order, menu_selection, menu_items)

        # Ask the customer if they would like to order anything else
        # Let the customer know if they should type 'n' or 'N' to quit
        keep_ordering = input("Would you like to keep ordering? (N) to quit: ")

        # TODO: Write a conditional statement that checks if the customer types
        # 'n' or 'N'
        if keep_ordering == 'n' or keep_ordering == 'N':
    # Code to execute if the user wants to quit ordering
       

            # Since the customer decided to stop ordering, thank them for
            # their order
            print("Thank you for your order.")

            # TODO: Use a list comprehension to create a list called prices_list,
            # which contains the total prices for each item in the order list:
            # The total price for each item should multiply the price by quantity

            prices_list = [item['price'] * item['quantity'] for item in order]


            #item['price'] retrieves the price of each item.
            #item['quantity'] retrieves the quantity of each item.


            # TODO: Create an order_total from the prices list using sum()
            # and round the prices to 2 decimal places.
            order_total = round(sum(prices_list),2)

            # Write a break statement or set the condition to False to exit
            # the ordering loop

            place_order = False

    # TODO: Return the order list and the order total
    return order, order_total
    


def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    # TODO: Check if the customer's input string can be converted 
    # to an integer and prints an error message if it does not
     
    # Try to convert the input to an integer
    customer_input = input("Please enter the menu item number: ")

    # Check if the customer's input string can be converted to an integer
    try:
        menu_selection = int(customer_input)  # Convert the menu selection to an integer
    except ValueError:
        print("Error: Please enter a valid number.")
        return  # Exit the function if the input is not a valid integer

    # Continue with the rest of the function logic
    # For example, check if the menu_selection is valid
    if menu_selection not in range(1, (menu_items) + 1):
        print("Error: Please select a valid menu item.")
    else:
        # Proceed with the order update logic
        print(f"You selected menu item number {menu_selection}.")


    
        # TODO: Convert the menu selection to an integer
       # Prompt the user to select a menu option
menu_selection = input("Please select a menu option (enter a number): ")

try:
    # Convert the input to an integer
    menu_selection_int = int(menu_selection)
    print(f"You selected option: {menu_selection_int}")
except ValueError:
    # Print an error message if the conversion fails
    print("Error: Invalid selection! Please enter a valid number.")


        # TODO: Write a conditional statement that checks if the customer's input is 
        # an item on the menu and prints an error message if it is not
        
            # Store the item name as a variable
       # Prompt the user to enter an item name
item_name = input("Please enter the item you want to order: ")
# Example of getting user input for selection
menu_selection = input(
    "Select an item  number (0 is Pizza, 1 is Burger, 2 is Salad, 3 is Pasta):"
)

# Check if the item is on the menu
menu_items = ("Pizza", "Burger", "Salad", "Pasta")

#
if item_name in menu_items:
    print(f"You have selected: {item_name}")
else:
    print("Error: Item not on the menu! Please select a valid menu item.")
           


# Check if the item is on the menu
if item_name in menu_items:
    # Prompt for quantity
    quantity = input(
        
        f"You have selected: {item_name}. How many would you like to order? "
    )
    print(f"You have ordered {quantity} of {item_name}.")
else:
    print("Error: Item not on the menu! Please select a valid menu item.")

item_name = input("Please enter the item you want to order: ")

# Check if the item is on the menu
if item_name in menu_items:
    # Prompt for quantity and store it in a variable
    quantity = input(f"You have selected: {item_name}. How many would you like to order? ")
    
    # Optionally, you can convert the quantity to an integer
    try:
        quantity = int(quantity)  # Convert to integer
        print(f"You have ordered {quantity} of {item_name}.")
    except ValueError:
        print("Error: Please enter a valid number for the quantity.")
else:
    print("Error: Item not on the menu! Please select a valid menu item.")

            #In this code:

            #he program prompts the user to enter the name of the item they want to order.
            #It checks if the entered item_name is in the menu_items list.
            #If the item is found, it prompts the user for the quantity and stores the input in the quantity variable.
            #It attempts to convert the quantity to an integer. If the conversion is successful, it confirms the order. If not, it prints an error message indicating that the input was invalid.
            #If the item is not on the menu, it prints an error message.



            

            # TODO: Write a conditional statement that checks if the input quantity 
            # can be converted to an integer, then converts it to an integer. 
            # Have it default to 1 if it does not.
            # Try to convert the input to an integer
            # If conversion fails, default to 1
            # Prompt the user to enter an item name

# Check if the item is on the menu
if item_name in menu_items:
    # Prompt for quantity and store it in a variable
    quantity = input(f"You have selected: {item_name}. How many would you like to order? ")
    
    # Attempt to convert the quantity to an integer
    try:
        quantity = int(quantity)  # Convert to integer
    except ValueError:
        print("Invalid input! Defaulting quantity to 1.")
        quantity = 1  # Default to 1 if conversion fails

    print(f"You have ordered {quantity} of {item_name}.")
else:
    print("Error: Item not on the menu! Please select a valid menu item.")
    
            


            # TODO: Add a dictionary with the item name, price, and quantity to the 
            # order list. Use the following names for the dictionary keys:
            # "Item name", "Price", "Quantity"

            # Initialize the order list
order_list = []

# Example values for item name, price, and quantity
item_name = "Sample Item"
price = 10.99
quantity = 2

# Create a dictionary with the specified keys
order_item = {
    "Item name": item_name,
    "Price": price,
    "Quantity": quantity
}

# Add the dictionary to the order list
order_list.append(order_item)

# Print the order list to verify
print(order_list)
            #In this code:

            #An empty order_list is initialized.
            #An example item name, price, and quantity are defined.
            #A dictionary named order_item is created with the keys "Item name", "Price", and "Quantity".
            #The dictionary is appended to the order_list.
            #Finally, the order list is printed to verify that the item has been added correctly.



            

    # TODO: Return the updated order
    
order_list = []
order_list = update_order(item_name, price, quantity)
print(order_list)
   
    

    
    
    


def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    # Uncomment the following line if you need to check the structure of the receipt
    print(receipt)

     #TODO: Loop through the items in the customer's receipt

def print_itemized_receipt(order):
    for item in order:
        item_name = item['name']
        item_price = item['price']
        item_quantity = item['quantity']
        print(f"{item_quantity} x {item_name} @ ${item_price:.2f}")

    
        # TODO: Store the dictionary items ("Item name", "Price", "Quantity") as variables
        # Example order list
order = [
    {'name': 'Burger', 'price': 5.99, 'quantity': 2},
    {'name': 'Fries', 'price': 2.49, 'quantity': 1},
    {'name': 'Soda', 'price': 1.99, 'quantity': 3}
]
        

        # TODO: Print the receipt line using the print_receipt_line function
        # send the item name, price, and quantity as separate arguments
        # Sample menu items with prices
menu_items = {
    "Pizza": 8.99,
    "Burger": 5.49,
    "Salad": 4.99,
    "Pasta": 7.99
}

def print_receipt_line(item_name, price, quantity):
    """Prints a formatted line for the receipt."""
    total_price = price * quantity
    print(f"{quantity} x {item_name} @ ${price:.2f} each = ${total_price:.2f}")

def place_order():
    # Prompt the user to enter an item name
    item_name = input("Please enter the item you want to order: ")

    # Check if the item is on the menu
    if item_name in menu_items:
        # Prompt for quantity and store it in a variable
        quantity = input(f"You have selected: {item_name} How many would you like to order? ")
        
        # Attempt to convert the quantity to an integer
        try:
            quantity = int(quantity)  # Convert to integer
        except ValueError:
            print("Invalid input! Defaulting quantity to 1.")
            quantity = 1  # Default to 1 if conversion fails

        # Get the price of the item
        price = menu_items[item_name]

        # Print the receipt line
        print_receipt_line(item_name, price, quantity)
        
    else:
        print("Error: Item not on the menu! Please select a valid menu item.")

# Example usage
place_order()
        
        

##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################


def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    # Calculate the number of spaces for formatted printing
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")


def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")


def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")


def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")


def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    # Print the menu item number, food category, meal, and price
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")


def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    # Create an empty dictionary to store the menu items
    menu_items = {}

    # Create a variable for the menu item number
    i = 1

    # Loop through the menu dictionary
    for food_category, options in menu.items():
        # Loop through the options for each food category
        for meal, price in options.items():
            # Store the menu item number, item name and price in the menu_items
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items


def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    # Create a meal menu dictionary
    #"""
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    """
    # This menu is just for testing purposes
    meals = {
        "Cake": {
            "Kuih Lapis": 3.49,
            "Strawberry Cheesecake": 6.49,
            "Chocolate Crepe Cake": 6.99
        },
        "Pie": {
            "Apple": 4.99,
            "Lemon Meringue": 5.49
        },
        "Ice-cream": {
            "2-Scoop Vanilla Cone": 3.49,
            "Banana Split": 8.49,
            "Chocolate Sundae": 6.99
        }
    }
    """
    return meals


# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    receipt, total_price = place_order(meals)

    # Print out the customer's order
    print("This is what we are preparing for you.\n")

    # Print the receipt heading
    print_receipt_heading()

    # Print the customer's itemized receipt
    print_itemized_receipt(receipt)

    # Print the receipt footer with the total price
    print_receipt_footer(total_price)

