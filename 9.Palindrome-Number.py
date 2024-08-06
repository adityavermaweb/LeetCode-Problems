# Given an integer 'x', return true if 'x' is a palindrome, and false otherwise.

# Ex:1 Input: x = 121
#      Output: true
#      Explanation: 121 reads as 121 from left to right and from right to left.

# Ex:2 Input: x = -121
#      Output: false
#      Explanation: From left to right, it reads -121. From right to left, it become 121-. Therefore it is not a palindrome.

# Ex:3 Input: x = 10
#      Output: false
#      Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Follow up: Could you solve it without converting the integer to a string?

# if (x < 0):
#     return False
#     i = x
#     s = 0
#     while(i > 0):
#         d = i % 10
#         s = s * 10 + d
#         i = i/10
#         if(x == s):
#         return True 
#     return False       