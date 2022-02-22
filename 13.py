## Count substrings
def count_substrings(string, sub_string):
    count = 0
    start = 0
    
    for i in range(len(string)):
        position = string.find(sub_string, start)
        if position != -1:
            start = position + 1
            count += 1
        
    if count == 0:
        print("There has no Substring found.")
    else:
        print(f'There are total {count} substrings found.')

string = input("Enter a String: ")
sub_string = input("Enter a Sub String: ")
count_substrings(string, sub_string)
