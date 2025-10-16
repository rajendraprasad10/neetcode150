

"""
write approach using two pointers

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man a plan a canal: Panama" is a palindrome.

approch for this 
"race a car" is not a palindrome.

 
"""
class Solution:
    """sumary_line
    
    Keyword arguments:
    argument -- str
    Return: bool
    """
    
    def isPalindrome(self, s):
        # two pointer approach
        # time complexity O(n)
        # space complexity O(1)
        # edge case 
        # if len(s) == 0:
        #    return True
        # if len(s) == 1:
        #   return True
        l, r = 0, len(s) - 1

        while l < r:
            # skip non alphanumeric characters # example ".,"
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # skip non alphanumeric characters example ".,"
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            # compare characters ignoring case example "A" and "c"
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
            
        return True
    # helper function to check if a character is alphanumeric example "A" or "1" or "a" or "z" or "Z" or "0" or "9" 
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')
                or ord('a') <= ord(c) <= ord('z')
                or ord('0') <= ord(c) <= ord('9'))
