#1
nums = input().replace(' ', '*')
print(eval(nums))


#2
str = input()

lower = 0
upper = 0

for i in str:
    if ord(i) >= 65 and 90 >= ord(i):
        lower += 1
    elif ord(i) >= 97 and 122 >= ord(i):
        upper += 1

print(lower, upper)


#3
str = input()
rts = str[::-1]

if hash(str) == hash(rts):
    print("Palindrome")
else:
    print("nah")


#4
print('Sample Input:')
inp = int(input())
ms = int(input())
abs(ms/1000)
print('Sample Output:')
print(f'Square root of {inp} after {ms} miliseconds is {inp**0.5}')


#5
tuple = (True, True, True)
tuple2 = (True, False, False)
print(all(tuple))
print(all(tuple2))