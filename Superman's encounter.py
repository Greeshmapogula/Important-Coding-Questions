l = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'kryptonday', 'coluday', 'daxamday']
for i in range(int(input())):
    n=int(input())
    c = n // 296
    n = n - c* 296
    index= n % 10
    print(l[index])
