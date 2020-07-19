for _ in range(int(input())):
    no_of_villains = int(input())
    l = []
    for i in range(no_of_villains):
        l.append(list(map(int, input().split())))
    already_defeated = [0]
    new_list = []
    total_time = 0
    while l:
        start = end = len(new_list)
        i = 0
        s = 1
        al_defeated = []
        while i < len(l):
            if set(l[i][2:]).issubset(set(already_defeated)):
                al_defeated.append(l[i][0])
                new_list.append(l.pop(i))
                if s:
                    s = 0
                    start = end
                else:
                    end += 1
            else:
                i += 1
        mx = 0
        for k in range(start, end + 1):
            if new_list[k][1] > mx:
                mx = new_list[k][1]
        total_time += mx
        already_defeated.extend(al_defeated)
    print(total_time)
        
