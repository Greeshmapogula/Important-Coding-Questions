T = int(input())

for case in range(T):
    time = input()

    hours, mins = list(map(int,time.split(':')))
    i=0
    a = hours

    total = 0

    while i<= mins:
        total = total + a
        a = 2*a - 1
        i = i + 1
    alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # defining all alphabets
    
    password_gen = str(total)
    password = ''

    for i in password_gen:
        password = password + alphas[int(i)]
    
    print(password)
