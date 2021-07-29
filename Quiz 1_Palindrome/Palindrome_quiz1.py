input = list(input("Enter Word "))

def isPalindrome( input ):
    if input[::+1]== input[::-1] :
        print("true")
    else :
        print("false")

isPalindrome(input)


