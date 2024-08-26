str1 = input()
str2 = input()

if str1 + str2 != str2 + str1:
    print("")

from math import gcd
print(str1[:gcd(len(str1), len(str2))])