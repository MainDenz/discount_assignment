
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

    # Prompting the user for inputs
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

    # Calculating the final price
final_price = calculate_discount(price, discount_percent)

    # Displaying the result
if final_price == price:
    print("No discount applied. Final price:", price)
else:
    print("Final price after applying the discount:", final_price)

