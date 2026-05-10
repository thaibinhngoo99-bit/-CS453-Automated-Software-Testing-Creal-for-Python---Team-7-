"""
Problem:

    
The function 'doubler' takes a word as input.  
It should create and print
    
a string, where each character in the string is doubled, for example:

    
"test" -> "tteesstt"


Tests:

    
>>> doubler("test")
tteesstt
    
>>> doubler("original")
oorriiggiinnaall
    
>>> doubler("hihihi")
hhiihhiihhii
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def doubler(word):
    print(''.join([char + char for char in word]))

if __name__ == "__main__":
    run_tests()