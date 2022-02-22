## Calc large & small number

def largest_number_024(numb):
    large = numb[0]
    large_position = 0
    if len(numb) == 0:
        print("Empty List")
    else:
        for i in range(0, len(numb)):
             if(large < numb[i]):
                    large = numb[i]
                    large_position += 1
    print(f'{large} is the Largest Element in this List.\n')
    print(f'{large_position+1} is the position of Largest Element in this List.\n')


def smallest_number_024(numb):
    small = numb[0]
    small_position = 0
    if len(numb) == 0:
        print("Empty List")
    else:
        for i in range(0, len(numb)):
             if(small > numb[i]):
                    small = numb[i]
                    small_position += 1
    print(f'{small} is the Smallest Element in this List.\n')
    print(f'{small_position+1} is the position of Smallest Element in this List.\n')
                
lst = []
length = int(input("Enter list length: "))
for i in range(0,length): 
    a = int(input(f'Enter value {i+1}: '))
    lst.append(a)
print(lst)
print("\n")

largest_number_024(lst)
smallest_number_024(lst)
