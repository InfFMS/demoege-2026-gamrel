def conv(n):
    alph = '0123456789A'
    ans = ''
    while n:
        ans = alph[n % 11] + ans
        n//= 11
    return ans
x=3000

while x>0:
    n = 9 * 11**210 + 8 * 11**150 - x
    if conv(n).count('0') == 60:
        print(x)
        break
    x-=1
x=0

from string import *
for x in printable[:29]:
    a = int(f'923{x}874',29) + int(f'524{x}6152',29)
    if a % 28 == 0:
        print(x, a // 28)
print(x)