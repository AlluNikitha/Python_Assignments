"""
Mini Project (W3): Billing System (OOP-based)
- Product class -> attributes: name, price, quantity
- Bill class -> total calculation + tax
- Display final bill in tabular format

Skill Gain: Real-world class design, object interaction.
"""

TAX_RATE = 0.05  # 5% tax


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def subtotal(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        subtotal = sum(p.subtotal() for p in self.products)
        tax = subtotal * TAX_RATE
        total = subtotal + tax
        return subtotal, tax, total

    def display_bill(self):
        if not self.products:
            print("No products added to the bill.")
            return

        print("\n" + "=" * 50)
        print(f"{'Product':<15}{'Price':>10}{'Qty':>8}{'Subtotal':>15}")
        print("=" * 50)

        for p in self.products:
            print(f"{p.name:<15}{p.price:>10.2f}{p.quantity:>8}{p.subtotal():>15.2f}")

        subtotal, tax, total = self.calculate_total()
        print("=" * 50)
        print(f"{'Subtotal:':<41}{subtotal:>9.2f}")
        print(f"{'Tax (5%):':<41}{tax:>9.2f}")
        print(f"{'Total:':<41}{total:>9.2f}")
        print("=" * 50)


def main():
    bill = Bill()

    while True:
        print("\n----- Billing System -----")
        print("1. Add Product")
        print("2. Display Bill")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            try:
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            bill.add_product(Product(name, price, quantity))
            print(f"'{name}' added to bill.")
        elif choice == "2":
            bill.display_bill()
        elif choice == "3":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()