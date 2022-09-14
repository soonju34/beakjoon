# price의 배수가 count만큼잇고 그 수를 다 더해서 money를 뺴면 됨
# 3+6+9 = 3(1+2+3)
def solution(price, money, count):
    for i in range(1,count+1):
        money -= price * i
    if money < 0:
        money = abs(money)
    else:
        money = 0 

    return money