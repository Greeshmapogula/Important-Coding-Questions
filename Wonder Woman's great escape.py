t=int(input())

for i in range(t):

  x1,y1=map(int,input().strip().split(" "))

  x2,y2=map(int,input().strip().split(" "))

  dir=input()

  if((dir[0]=='N' and y1>y2) or (dir[0]=='S' and y2>y1) or (dir[1]=='E' and x1>x2) or (dir[1]=='W' and x2>x1)):

    print("impossible")

  else:

    def nCr(n, r): 

      return (fact(n) // (fact(r)  

            * fact(n - r))) 

    def fact(n): 

      res = 1

      for i in range(2, n+1): 

        res = res * i 

      return res 

    n=abs(x1-x2)+abs(y1-y2)

    r=abs(x1-x2)

    res=nCr(n,r)

    print("Total Ways:",res)
