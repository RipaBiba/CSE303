# check Fibonacci number
def Fibonacci(numb):
    if numb <= 0:
        print("Incorrect input")
    elif numb == 1:
        return 0
    elif numb == 2:
        return 1
    else:
        return Fibonacci(numb-1)+Fibonacci(numb-2)

numb = int(input("Enter a number: "))
result = Fibonacci(numb)
print(f'{numb} th Fibonacci number is {result}')
