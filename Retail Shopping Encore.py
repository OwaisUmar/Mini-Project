import datetime
print("Mini Project: Retail Shopping Encore")
print("-" * 37)

stock = {}
basket = {}

print("\n\nWelcome to Admin Module\n"
          "1)Admin Module  -  Stock (ProductName, UnitPrice)\n"
          "  1-Add Product in Stock\n"
          "  2-Update Product price in Stock\n"
          "  3-Remove Product from Stock\n"
          "  4-View All Products in Stock\n"
          "  5-Logout Admin")

def admin_module():
    ch = input("\nEnter your choice (1-5) :  ")
    if ch == '1':
        item = input("\nEnter product to be added :  ")
        up = int(input("Enter its unit price :  "))
        stock[item] = up
        admin_module()
    elif ch == '2':
        item = input("Enter product to be updated :  ")
        up = int(input("Enter updated unit price :  "))
        if item in stock:
            stock[item] = up
        else:
            print("Item not found.")
        admin_module()
    elif ch == '3':
        item = input("Enter item to be removed :  ")
        if item in stock:
            del stock[item]
        else:
            print("Item not found.")
        admin_module()
    elif ch == '4':
        for item in stock:
            print(item, " : ", stock[item])
        admin_module()
    elif ch == '5':
        print("Admin logged out successfully.")
        consumer_module()
    else:
        print("Invalid input.")
        admin_module()

def consumer_module():
    print("\n\n\nWelcome to Consumer Module\n"
          "2) Consumer Module - Basket (Product Name, Quantity)\n"
          "  1-View All Products in Stock\n"
          "  2-Add to shopping basket\n"
          "  3-View all product of basket\n"
          "  4-Search product in Stock\n"
          "  5-Remove product from basket\n"
          "  6-Print invoice\n"
          "  7-Sign out")
    ch = int(input("\nEnter your choice (1-7) :  "))
    if ch == 1:
        for item in stock:
            print(item, " : ", stock[item])
        consumer_module()
    elif ch == 2:
        item = input("Enter product to be added :  ")
        pq = int(input("Enter product's quantity :  "))
        basket[item] = pq
        consumer_module()
    elif ch == 3:
        for item in basket:
            print(item, " : ", basket[item])
        consumer_module()
    elif ch == 4:
        item = input("Enter product to be searched :  ")
        if item in stock:
            print("Product is in stock with unit price = ", stock[item])
        else:
            print("Product is out of stock.")
        consumer_module()
    elif ch == 5:
        item = input("Enter item to be removed :  ")
        if item in basket:
            del basket[item]
        else:
            print("Item not found.")
        consumer_module()
    elif ch == 6:
        Grand_total = 0
        print("\t\tBilling Invoice\n"
              "\t\t", "-" * 15,
              "\nInvoice Date: ", datetime.date.today(),
              "\nProduct Name\tQuantity\tUnit Price\t\tTotal")
        for item in basket and stock:
            if item in basket and stock:
                print(item,"\t\t\t",basket[item],"\t\t\t",stock[item],"\t\t\t",basket[item] * stock[item])
                Grand_total += basket[item] * stock[item]
        print('-' * 50,
              "\n\t\tGrand Total =\tRupees ", Grand_total, "/-")
        print('-' * 50, '\n...')
    elif ch == 7:
        print("You are signed out successfully.")


admin_module()
