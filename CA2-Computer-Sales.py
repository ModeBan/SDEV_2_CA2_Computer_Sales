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
    def display_low_stock(products_in): # lists low stock
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

    @staticmethod
    def reorder_low_stock(products_in):
        products = products_in
        products_raised = 0
        print("{:10}{:20}{:^15}{:^15}{:^15}".format("ID", "Name", "Quantity", "Re Order Level","Ordered"))
        for row in range(len(products)):
            if products[row][4] < products[row][5]:
                ordered = products[row][5] - products[row][4]
                products[row][4] += ordered
                print("{:10}{:20}{:^15}{:^15}{:^15}".format(products[row][0], products[row][1], products[row][4], products[row][5], ordered))
                products_raised += 1
        if products_raised == 0:
            print("No products were raised to order", end="\n\n")
        else:
            print("Number or products raised to order:",products_raised, end="\n\n")

    @staticmethod
    def make_sale(products_in, id_in, required_qty_in): # Make sale
        products = products_in
        prod_id = id_in
        required_qty = required_qty_in
        product_index = -1 # check whether a product exists: -2 initial , -1 not found, index in list
        number = len(products)
        if len(products) > 0:
            for index, product in enumerate(products):
                if prod_id == product[0]:
                    product_index = index

            if product_index == -1:
                print("Product not found!")
            elif product_index > -1:
                quantity_available = products[product_index][4]
                if quantity_available > required_qty:
                    products[product_index][4] -= required_qty
                    sale_price = (products[product_index][3] + (products[product_index][3] * (ProductUtility.VAT / 100))) * required_qty
                    print("Cost of the sale €" + str(round(sale_price,2)))
                else:
                    print("Product not enough stock!")
                    print("Cost of the sale €" + str(0.00))

        else:
            print("No products added!")
        print()

    @staticmethod
    def add_product(products_list_in ,id_in, name_in, cost_in, selling_in, qty_on_hand_in, re_order_in):
        new_product = []
        new_product.append(id_in)
        new_product.append(name_in)
        new_product.append(cost_in)
        new_product.append(selling_in)
        new_product.append(qty_on_hand_in)
        new_product.append(re_order_in)
        products_list_in.append(new_product)

    @staticmethod
    def create_dictionary(products_in):
        product_dict = {}
        for product in products_in:
            if product[0] not in product_dict:
                product_dict[product[0]] = product[4]
        print("{:<15}{:<15}".format("Accessory ID", "Quantity on Hand"))
        print("_"*31)
        for key in product_dict:
            print("{:<15}{:<15}".format(key, product_dict.get(key)))
        print()


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
# menu_option = int(input("Please enter option:"))
menu_option = 6
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
        print("\n*", ("{:^" + str(CELL_LENGTH) + "}").format("Re-Order Low Stock"), "*")
        ProductUtility.reorder_low_stock(products)

    elif menu_option == 4: # Make a Sale
        print("\n*", ("{:^" + str(CELL_LENGTH) + "}").format("Make a Sale"), "*")
        product_to_sell = input("Enter ID of accessory to sell: ")
        product_qty_to_sell = int(input("Enter the quantity required: "))

        while  product_qty_to_sell < 1: # input validation
            print("Invalid quantity, must be above 0!")
            product_qty_to_sell = int(input("Enter the quantity required: "))
        ProductUtility.make_sale(products,product_to_sell,product_qty_to_sell)

    elif menu_option == 5: # Add a New Product
        print("\n*", ("{:^" + str(CELL_LENGTH) + "}").format("Add New Product"), "*")

        id = input("ID: ")
        name = input("Name: ")
        name = name.lower()
        cost_price = float(input("Cost price: "))
        selling_price = float(input("Selling price: "))
        qty_on_hand = int(input("Quantity on hand: "))
        re_order_level = int(input("Re order Level: "))
        ProductUtility.add_product(products, id, name, cost_price, selling_price, qty_on_hand, re_order_level)
        print(name,"added!")

    elif menu_option == 6: # Product and Stock on Hand
        print("\n*", ("{:^" + str(CELL_LENGTH) + "}").format("Product and Stock on Hand"), "*")
        ProductUtility.create_dictionary(products)
    ProductUtility.menu()
    menu_option = int(input("Please enter option:"))
    while menu_option > 7 or menu_option < 1:
        print("Invalid input! Enter option from menu")
        menu_option = int(input("Please enter option:"))

if menu_option == 7: # Exit & write to file
    print("Please wait program writting to file!")
    with open("stock.csv", "w", newline="") as file:
        write = csv.writer(file)
        write.writerows(products)
    print("Program finished! - stock.csv now available.")