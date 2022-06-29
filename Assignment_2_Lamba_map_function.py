cube = lambda x: x**3

def fibonacci(n):
    a=0
    b=1
    list=[]
    if n==a:
        list=[]
    elif b==n:
        list=[0]
    else:        
        list.append(a)
        list.append(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            list.append(c)
    return list
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))