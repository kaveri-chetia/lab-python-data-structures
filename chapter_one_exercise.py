# Solution: 1
products = ["t-shirt", "mug", "hat", "book", "keychain"]

# Solution: 2
inventory = {}

# Solution: 3
for product in products:
    quantity = int(input("Enter quantity for {}".format(product)))
    inventory[product] = quantity

# Solution: 4
customer_orders = set()

# Solution: 5
print("Enter the name of three products that a customer wants to order:")
for _ in range(3):
    product_order = input("Product name: ").strip()
    if product_order in products:
        customer_orders.add(product_order)
    else:
        print(f"{product_order} is not available. Please choose from {products}.")


# Solution: 6
print(customer_orders)

# Solution: 7
total_products_ordered = len(customer_orders)
total_available_products = sum(inventory.values())
percentage_ordered = (total_products_ordered / total_available_products) * 100
order_status = (total_products_ordered, percentage_ordered)

# Solution: 8
print("\nOrder Statistics:")
print(f"Total Products Ordered: {order_status[0]}")
print(f"Percentage of Products Ordered: {order_status[1]:.2f}%")

# Solution: 9
for customer_order in customer_orders:
    inventory[customer_order] = inventory[customer_order] - 1

# Solution: 10
print("Updated Inventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")
