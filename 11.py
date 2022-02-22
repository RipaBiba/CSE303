## Find even index characters from string
def even_index_character(string):
    even_char = []
    for i in range(len(string)):
        if i % 2 == 0:
            even_char.append(string[i])
            
    print(f'Even Characters: {even_char}')
    
string = input("Enter a String: ")
even_index_character(string)
