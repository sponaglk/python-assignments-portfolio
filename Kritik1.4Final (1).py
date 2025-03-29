x = float(input("Input: "))
def kritik(x):
    if input != x>=0 and x<=1:
        def err(a,b):
            y= (a**((2*b)+1)/((2*b)+1))
            return y
        n=0
        while err(x,n)>=0.0001:
            n+=1
        i=0
        c=0
        f=0
        while i<=(n-1):
            c=(((-1)**i)*(x**((2*i)+1)))/((2*i)+1)
            f=f+c
            i+=1
        answer= (f,n,err(x,n))
        print(answer)
    else:
        print('Error!')
print(kritik(x))