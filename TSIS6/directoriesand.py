#1
import os

path = input()   #C:\Users\User\OneDrive\Рабочий стол\TSIS6
os.chdir(path)   

dirctry = os.listdir(os.getcwd())  
for i in dirctry:
    if os.path.isdir(i):       
        print(i)
    elif os.path.isfile(i):        
        print(i)


#2
import os

print('existence: ', os.access('C:\\Users\\User\\OneDrive\\Рабочий стол\\TSIS6', os.F_OK))
print('readability: ', os.access('C:\\Users\\User\\OneDrive\\Рабочий стол\\TSIS6', os.R_OK))
print('writability: ', os.access('C:\\Users\\User\\OneDrive\\Рабочий стол\\TSIS6', os.W_OK))
print('executability: ', os.access('C:\\Users\\User\\OneDrive\\Рабочий стол\\TSIS6', os.X_OK))


#3
import os

path = r'C:\Users\User\OneDrive\Рабочий стол\TSIS6'

os.chdir(path)
    
print(os.getcwd())  

dirctr = os.listdir(os.getcwd()) 
for i in dirctr:
    if os.path.isdir(i):
        print(i)
    elif os.path.isfile(i):
        print(i)


#4
import os

path = r'C:\Users\User\OneDrive\Рабочий стол\TSIS6'
os.chdir(path)
txt = input()

result = open(txt, 'r')
cnt = 0

for str in result:
    if str != "\n":
        cnt += 1
        print(cnt)


#5
import os

path = r'C:\Users\User\OneDrive\Рабочий стол\TSIS6'

os.chdir(path)
txt = input()

output = open(txt, 'w') 
output.write(str(list(map(int, input().split()))))  
output.close()


#6
import os

path = r'C:\Users\User\OneDrive\Рабочий стол\TSIS6'
os.chdir(path)

for i in range(65, 91):
    res = open(chr(i)+'.txt', 'w')   

#7
import os

path = r'C:\Users\User\OneDrive\Рабочий стол\TSIS6'
os.chdir(path)

txt = input()
path2 = input()
txt2 = input()

with open(txt,'r') as input, open(path2 + txt2,'a') as output:
    for line in input:
        output.write(line)


#8
import os

path = r'C:\Users\User\OneDrive\Рабочий стол\TSIS6'

os.chdir(path)
dirctr = os.listdir(os.getcwd())   

for i in dirctr:        
    if os.path.isdir(i):
        print(f'dir: {i}')
    elif os.path.isfile(i):
        print(f'file: {i}')

name = input() 
os.remove(name)
