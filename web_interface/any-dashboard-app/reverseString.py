def reverseString(s):
    s[:] = s[::-1]
    return s
print(reverseString(["H","a","n","n","a","h"]))