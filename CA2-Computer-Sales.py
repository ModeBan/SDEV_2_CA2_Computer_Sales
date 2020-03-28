"""
Software Development 2 - CA2
Modestas Banys - X00160730
"""
# Imports
import csv


# Classes
class ProductUtility:
    VAT = 23

    @staticmethod
    def menu(): # Displays menu and returns user selected option

        menu_options = ["List All Stock", "List Low-stock Products", "Reorder Low Stock", "Make a Sale",
                        "Add a New Product", "Product and Stock on Hand", "Exit"]


        line_length = 30
        line_format = "{:<" +str(line_length)+"}"

        print("*" * (line_length + 4))
        print("*", ("{:^" + str(line_length) + "}").format("Computer Accessory System"), "*")
        print("*" * (line_length + 4))

        for i in range(len(menu_options)):
            print("*", line_format.format("" + str(i + 1) + ") " + str(menu_options[i])), "*")
        print("*" * (line_length + 4))

    @staticmethod
    def display_stock(products_in): # shows list of all stock
        headings = ["ID", "Name", "Cost Price €", "Selling Price €", "Quantity on Hand", "Re Order Level"]
        cols = len(headings)
        cell_length = 25
        table_format = "{:<" +str(cell_length)+"}"

        print("*" * (cell_length * cols))
        print((table_format * cols).format(*headings))
        print("*" * (cell_length * cols))
        for row in products_in:
            print((table_format * cols).format(*row))

    @staticmethod
    def display_low_stock(products_in):
        headings = ["ID", "Name", "Quantity", "Re Order Level"]
        cols = len(headings)
        cell_length = 25
        table_format = "{:<" +str(cell_length)+"}"

        print("*" * (cell_length * cols))
        print((table_format * cols).format(*headings))
        print("*" * (cell_length * cols))
        for row in products_in:
            if row[4] <= row[5]:
                print((table_format).format(row[0]),end="")
                print((table_format).format(row[1]),end="")
                print((table_format).format(row[4]),end="")
                print((table_format).format(row[5]),end="\n")



# Main body of program
CELL_LENGTH = 30

# Products.csv read in & Process
with open("products.csv", "r") as product_file:
    products = list(csv.reader(product_file))

for i in range(len(products)): # conversion of numerical values stored as strings
    products[i][2] = float(products[i][2])
    products[i][3] = float(products[i][3])
    products[i][4] = int(products[i][4])
    products[i][5] = int(products[i][5])

# Menu
ProductUtility.menu()
menu_option = int(input("Please enter option:"))
while menu_option > 7 or menu_option < 1:
    print("Invalid input! Enter option from menu")
    menu_option = int(input("Please enter option:"))

while menu_option != 7:
    if menu_option == 1: # List all stock
        print("\n*", ("{:^" + str(CELL_LENGTH) + "}").format("All Stock"), "*")
        ProductUtility.display_stock(products)

    elif menu_option == 2: # List Low-stock Products
        print("\n*", ("{:^" + str(CELL_LENGTH) + "}").format("Low Stock"), "*")
        ProductUtility.display_low_stock(products)

    elif menu_option == 3: # Reorder Low Stock
        print("Menu Action 3")
    elif menu_option == 4: # Make a Sale
        print("Menu Action 4")
    elif menu_option == 5: # Add a New Product
        print("Menu Action 5")
    elif menu_option == 6: # Product and Stock on Hand
        print("Menu Action 6")

    ProductUtility.menu()
    menu_option = int(input("Please enter option:"))
    while menu_option > 7 or menu_option < 1:
        print("Invalid input! Enter option from menu")
        menu_option = int(input("Please enter option:"))

if menu_option == 7: # Exit
    print("Menu action 7")