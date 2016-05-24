z=7
a=6
b=1
c=25
z=a*z+b
print (z)
for i in range(0, 50):
    z1=a*z+b
    z=z1%c
    print (z)
