#lambda arguments : expression

x=lambda a: a+10
print(x(5))

Y=lambda a,b,c: (a+b)/c
print(Y(5,10,3))


def myfun(n):
    return lambda a:a * n

ans1= myfun(5) 
ans2= myfun(10)

print(ans1(11))
print(ans2(11))