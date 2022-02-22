## Calc large & small number
def second_largest_number(numb):
    second_large = numb[0]
    large = numb[0]
    large_position = 0
    for i in range(len(numb)):
        if(large < numb[i]):
            large = numb[i]
            
    for i in range(len(numb)):
        if numb[i] > second_large and numb[i] != large:
            second_large = numb[i]
            large_position = i+1
            
    print(f'{second_large} is the Second Largest Element in this List.\n')
    print(f'{large_position} is the position of Second Largest Element in this List.\n')

lst = []
length = int(input("Enter list length: "))
for i in range(0,length): 
    a = int(input(f'Enter value {i+1}: '))
    lst.append(a)
print(lst)
print("\n")

second_largest_number(lst)
