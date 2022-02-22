numb01 = int(input("Enter 1st number: "))
numb02 = int(input("Enter 2nd number: "))

product = numb01*numb02
sum = numb01+numb02

if product > 1000:
     res = sum
else:
    res = product
    
print("Result: ", res)
