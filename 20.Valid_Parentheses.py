# Given a string 's' containing just the characters '(',')', '{','}', '[' and ']', determine if the input string is valid.
# An input string is valid if :
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open breacket of the same type.

# Example:1
#   Input: s = "()"
#   Output: true

# Example:2
#   Input: s = "() [] {}"
#   Output: true

# Example:3
#   Input: s = "(]"
#   Output: false

# Solution
# hashmap = {')':'(','{':'}','[':']'}
# stk = []
# for c in s:
#   if c not in hashmap:
#       stk.append(c)
#   else:
#       if not stk:
#           return False
#       else:
#           popped = stk.pop()
#           if popped != hashmap[c]:
#               return False
#   return not stk