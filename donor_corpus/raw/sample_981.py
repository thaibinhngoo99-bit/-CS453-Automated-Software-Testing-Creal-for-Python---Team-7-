# url="http://www.baidu.com/?page=/wd=xiaopangzi"
'''
url1="www.baidu.com/?page="
url2="wd=xiaopangzi"
while(1):
    for i in range(1,100):
        print(url1,i,url2)
       i=i+1 
    break
         
for i in range(100):
    part1=www.baidu.com/?page=
    res = part1 + 
'''
'''
A1=[1,1,1,1,1,2,2,2,2,2,3]
a1=[]
for i in A1:
    if i not in a1:
        a1.append(i)
print a1

#A2=[1,2,3]
#A2.append(10)
#print A2
'''
'''
a4 = [['liuyanyun',22,['360',100]],['jingjing',12,['baidu',1]],['taotao',-1,['Google',0]]]
a4.sort(key=lambda x:x[2][1])
print(a4)
'''
'''
t=(1,2,3,7,9,0,5)
print(t[ : -1])
'''
'''
a=0
b=0
while a < 10 :
    a=a+1
    print("a= {}".format(a))
    if a%10==0:
        print("")
print(a)
'''
'''
i=0
sum=0
while i<100:
    i=i+1
#    if i%2==0:
    sum=i+sum
    print("i={},sum={}".format(i,sum))
'''
'''
#shu chu 1-100 zhi jian de ou shu he
i=0
sum=0
while i<=100:
    i+=2
    sum=sum+i 
print(sum)
'''
'''
#1-100(while xun hua ) ji shu he he ou shu he shu chu
i=0
sum=0
a=0
while i<100:
    i=i+1
    if i%2==0:
        sum=sum+i
    else:
        a=a+i
print(sum,a)
'''
'''
# 1-100(for xun huan) ji shu he he ou shu he shu chu
sum=0
a=0
for i in range(1,101):
    if i%2==0:
        sum=sum+i
    else:
        a=a+i
print(sum,a)
'''
#for i in range(1,100,2):
#    print(i,end="\t")


# shu chu 10 hang 10 lie de *
#for i in range(1,11):
#    for j in range(1,j):
#         print(i,j)
#for i in range(1,11):
#    for j in range(1,11):
#        print("*")
#    print()

# shu chu 10 hang 10 lie de dong xi 
#for i in range(1,11):
#    for j in range(1,11):

# shu chu shi hang nei rong mei hang xian shi *
'''
for i in range(1,11):
    for j in range(1,11):
        print("*")
        if i%10==0:
            print("")
'''

'''
# shu chu shi hang neirong  mei hang xian shi *
for i in range(1,11):
    print("*"*10)
'''


'''
#输出十行内容，每行输入不同，第一行输入×，第二行输出××，以此类推
for i in range(1,11):
    print("a"*i)
'''

'''
#输出九行，第1行输出1,第二行输出12,第九行输出12345789.
for i in range(1,10):
    for j in range(1,i+1):
         print(j,end=" ")
    print("")

#print("")
'''
"""

            ***
for i in range(1,10):
    for j in range(1,i+1):
        for z in range(1,j+1):
            print(z,end=" ")
        print("")
    print("")
"""
'''
#输入九九乘法表
for i in range (1,10):
    for j in range(1,i+1):
        s=i*j
        print(j,"x",i,"=",s," ",end="")
    print("")    
'''

'''
#  计算10个99相加后的值并输出
sum=0
for i in range(10):
    sum+=99*10
    print(sum)
'''

'''
#计算从1加到100的值并输出
sum = 0
for i in range(101):
    sum+=i
print(sum)
'''


#计算10的阶乘（1x2x3x4x5x6x7x8x9）



'''
#python爆破密码
import crypt
def testPass(cryptPass):
    salt = cryptPass[0:2]
    dictFile = open("/root/Desktop/dictionary.txt","r")
    for word in dictFile.readlines():
        word = word.strip("\n")
        cryptWord=crypt.crypt(word,salt)
        if cryptWord == cryptPass:
            print ("[+]Found Password: " +word)
        else:
            print("[-]Password {} Not found.".format(word))

def main():
    passFile = open('/root/Desktop/2.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print ("[*] Cracking Password For:" + user)
            testPass(cryptPass)


if __name__ == "__main__":
    main()
'''

import crypt
import itertools

def main():
    flag=0
    salt='AB'
    cryptPass='5I64J9ZNvp2'
    test=(''.join(x) for x in in itertools.productduct("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM", repeat=7))
    while flag==0:
        word=next(test)
        cryptWord =  = crypt.crypt(wor(word,salt)
        if cryptWord == cryptPass:
            print('[+] Found Password:'+word)
            flag=1

if __name__ == '__main__':
    main()






