# Exercise 6:Tax and Tip


def tax_of_tip():
    local_tax = 0.32
    tip = 0.18

    # Reading cost of the meal

    meal_cost = float(input("Enter cost of teh meal:"))
    tax_amount = meal_cost * local_tax
    tip_amount = meal_cost * tip
    grand_total = meal_cost + tax_amount + tip_amount

    # Displaying amounts calculated

    print("Tax Amount is:", round(tax_amount, 2), "$")
    print("Tip Amount is :", round(tip_amount, 2), "$")
    print("Grant Total for meal is :", round(grand_total, 2), "$")


tax_of_tip()
