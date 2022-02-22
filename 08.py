## Calc even index Sum
def Sum(numb):
    total = 0
    if len(numb) == 0:
        print("Empty List")
    else:
        for i in range(0, len(numb)):
            if i % 2 == 0:
                total += numb[i]
            
    print("Sum of all even index elements in given list: ", total)
    
lst = []
length = int(input("Enter list length: "))
for i in range(0,length): 
    a = int(input(f'Enter value {i+1}: '))
    lst.append(a)
print(lst)

Sum(lst)
