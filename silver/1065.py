def hansu(n):
    count = 0
    for i in range(1,n+1):
        num_list = list(map(int, str(i)))
        if i < 100:
            count += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            count += 1
    return count

n = int(input())
print(hansu(n))