# Exercise 7:Sum of the First n Positive Integers


def n_positive_num():

    # Reading the number from user

    n = int(input("Enter Positive Integer number :"))

    # Calculating sum from 1 to n

    n_sum = n*(n+1)/2

    # displaying sum of all integer from 1 to n i.e: 1+2+....+n

    print("Sum of all integer from 1 to", n, "is:", n_sum)


n_positive_num()

