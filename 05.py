# Check Prime
def prime_find_024(numb):
    if numb > 1:
        for i in range(2, int(numb/2)+1):
            if numb % i == 0:
                print(f'{numb} is not a prime number')
                break
            else:
                print(f'{numb} is a prime number')
                break
    else:
        print(f'{numb} is not a prime number')
        
numb = int(input("Enter a Number: "))
prime_find_024(numb)
