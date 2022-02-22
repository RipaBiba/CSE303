import math
def compound_interest(principle, rate, time):

    Amount = principle * (pow((1 + rate / 100), time))
    Compound_Interest = Amount - principle
    print("Compound interest is", Compound_Interest)

principle = float(input("Enter Principle Value: "))
rate = float(input("Enter Rate: "))
time = float (input("Enter Time: "))

compound_interest(principle, rate, time)
