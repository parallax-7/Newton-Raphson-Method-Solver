 #given a poly function finding its root by newton method.
#x^3-x-2
#f'(x)=3x^2-1
#x^{5}-x^{3}-x-2
def f(i):
    return i**5-i**3-i-2
def Diff(i):
    return 5*(i**4)+3*(i**2)-1

def newtonMethod():
    x=1
    count=1
    while(f(x)>0.0001 or f(x)< -1*0.0001):
        h= -1* (f(x)/Diff(x))
        x+=h
        count+=1
        print(x,count,sep=" ")
    return x
print(newtonMethod())

    
