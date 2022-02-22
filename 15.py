## even odd list
def even_odd_list(list1, list2):
    even_list = [] 
    odd_list = [] 
    new_list = []
    for i in list1: 
        if (i % 2 != 0): 
            odd_list.append(i)
            new_list.append(i)
            
    for i in list2: 
        if (i % 2 == 0): 
            even_list.append(i)
            new_list.append(i)
        
    print(f'Odd list from first list: {odd_list}')
    print(f'Even list from second list: {even_list}')
    print(f'\nThe new List: {new_list}')
    
list1 = []
length = int(input("Enter list length: "))
for i in range(0,length): 
    a = int(input(f'Enter value {i+1}: '))
    list1.append(a)
print(f'First List: {list1}')
print("\n")

list2 = []
length = int(input("Enter list length: "))
for i in range(0,length): 
    a = int(input(f'Enter value {i+1}: '))
    list2.append(a)
print(f'Second List: {list2}')
print("\n")

even_odd_list(list1, list2)
