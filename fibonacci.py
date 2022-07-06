def fibonacci(n):
    if n==1:
        return 1
    elif n<0 or n==0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=4
for i in range(n):
    print(fibonacci(i))


# efficient way by dynamic programming
# arr=[-1]*n
def fibo(n,arr):
    if arr[n]>=0:
        return arr[n]

    if n==0 or n==1:
        q=n
    else:
        q=fibo(n-1,arr)+fibo(n-2,arr)

    arr[n]= q
    print(arr)
    return q

n=3
arr=[-1]*(n+1)
print(fibo(n,arr))