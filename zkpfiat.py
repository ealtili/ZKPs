import sys
import random
import hashlib
import libnum

n=997

password="Hello"

g= 3


def pickg(p):
	for x in range (1,p):
		rand = x
		exp=1
		next = rand % p

		while (next != 1 ):
			next = (next*rand) % p
			exp = exp+1
		
		if (exp==p-1):
			return rand

v = random.randint(1,n)
c = random.randint(1,n)


if (len(sys.argv)>1):
	text=str(sys.argv[1])

if (len(sys.argv)>2):
	v=int(sys.argv[2])

if (len(sys.argv)>3):
	c=int(sys.argv[3])

if (len(sys.argv)>4):
	n=int(sys.argv[4])



print("Password:\t",password)
x = int(hashlib.md5(password.encode()).hexdigest()[:8], 16) % n

g=pickg(n)

y= pow(g,x,n)

t = pow(g,v,n)

r = (v - c * x) 

if (r<0):
	Result = ( libnum.invmod(pow(g,-r,n),n) * pow(y,c,n))  % n
else:
	Result = ( pow(g,r,n) * pow(y,c,n))  % n

print('\n======Agreed parameters============')
print('P=',n,'\t(Prime number)')
print('G=',g,'\t(Generator)')


print('\n======The secret==================')
print('x=',x,'\t(Alice\'s secret)')

print('\n======Random values===============')
print('c=',c,'\t(Bob\'s random value)')
print('v=',v,'\t(Alice\'s random value)')

print('\n======Shared value===============')
print('g^x mod P=\t',y)
print('r=\t\t',r)

print('\n=========Results===================')
print('t=g**v % n =\t\t',t)
print('( (g**r) * (y**c) )=\t',Result)
if (t==Result):
	print('Alice has proven she knows password')
else:
	print('Alice has not proven she knows x')