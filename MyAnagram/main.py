# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram():
    # [assignment] Add your code here
    Sd = "Enter the words to be checked"
    print(Sd)
    firstword = input("first word: ")
    secondword = input("second word: ")

    print(sorted(firstword),sorted(secondword))
    
    if (sorted(firstword)==sorted(secondword)):
        return True
    else:
        return False




find_anagram()
    
