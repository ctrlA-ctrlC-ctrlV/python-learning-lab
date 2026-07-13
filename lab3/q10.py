# Q10 — star ratings (nested loops)
ratings = [3, 5, 2] 

for i in range(len(ratings)):
    for j in range(ratings[i]):
        print('*', end='')

    print()
    