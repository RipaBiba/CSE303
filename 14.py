## check palindrome 
def palindrome_checker_024(string):
    count = 0
    for i in range(0, int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
            count += 1
    if count == 0:
        print(f'{string} string is Palindrome')
    else:
        print (f'{string} string is not Palindrome')
    
string = input("Enter a String: ")
palindrome_checker_024(string)
