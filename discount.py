def calculate_discount(price, discount_percent):
    """Calculates and returns discounted price if discount >= 20%, else original price"""
    # Only apply discount if it is 20% or more
    if discount_percent < 20:
        return price
    return price * (1 - discount_percent / 100)

# Promts user to put input
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Call function
final_price = calculate_discount(original_price, discount)

# results
if discount >= 20:
    print("Discount applied!")
    print(f"Final price after {discount}% discount: {final_price:}")
else:
    print("No discount applied.")
    print(f"Final price remains: {final_price:.2f}")
