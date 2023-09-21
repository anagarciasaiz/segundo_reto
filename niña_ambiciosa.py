n = int(input())
a = list(map(int,input().split()))
m=abs(a[0])


for i in a[1:]:
    if abs(i)<m:
        m=abs(i)

print(m)



