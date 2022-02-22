## Remove n characters
def remove_n_characters(string, n):
    new_string = ""
    for i in range(n,  len(string)):
        new_string = new_string + string[i]
        
    print(f'The New String: {new_string}\nThe old string was: {string}')
    
string = input("Enter a String: ")
n = int(input("Enter how many char want to remove: "))
remove_n_characters(string, n)
