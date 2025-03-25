price = int(input("Enter the price of the item: "))
discount = int(input("Enter the discount percentage: "))

def calculate_discount(price, discount):
    if discount >= 20:
        discount_amount = price * discount / 100
        discounted_price = price - discount_amount
        return discounted_price
    else:
        return price
# Call the function and print the result 
final_price = calculate_discount(price, discount)
print(f"The final price of the item is: {final_price}" )