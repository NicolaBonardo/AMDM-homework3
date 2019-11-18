from itertools import combinations 

def findCombinations(str, i): 
    l = len(str) 
    return set([''.join(comb) for comb in combinations(str, l - i)])

def isPalindrome(word):
    return(word == reverse(word))    

def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str

inputString = input("Please, insert the input string: ")
n = len(inputString)

for i in range(n):
    
    combs = findCombinations(inputString, i)
    
    for word in combs:
        if isPalindrome(word):
            print("Length of longest palindrome: ", str(n-i))
            print("Palindrome: ", word)
            break
    else:
        continue
    break




      
