T = int(input())
for case in range(T):
    n , p = list(map(int,input().split()))

    prisoners = p

    cells = [0]*n


    for i in range(len(cells)):
        for j in range(0, len(cells)):
            if p==0:
                break
            if ((i+j) >= len(cells)):
                continue
            cells[i+j]+= 1
            p-= 1
    
    cells[0]+= p

    for ans in cells:
        print(ans, end = ' ')
    print()
