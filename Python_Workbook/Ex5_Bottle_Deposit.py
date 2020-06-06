# Exercise 5: Bottle Deposits


def bottle_deposit():
    # Reading container count for each size from user

    one_ltr_cost = 0.01
    one_ltr_more_cst = 0.25
    one_ltr_less = int(input("enter number of container which are less than or euqal to 1 liter:"))
    one_ltr_more = int(input("enter number of containers which ar more than 1 liter size:"))

    # Computing refund for the container

    refund = one_ltr_less * one_ltr_cost + one_ltr_more * one_ltr_more_cst

    print("Your total refund is :", round(refund, 2), "$")


bottle_deposit()
