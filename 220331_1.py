#나
money = int(input("투입한돈"))
b = int(input("믈건값"))
print ("투입한돈 : ",money)
print ("물건값 : ",b)
print ("거스름돈 : ",money-b)
print ("500원 동전의 개수 : ",(money-b)/500)
print ("100원 동전의 개수 : ",(money-b)%500/100)

#손세준님
input_money = int(input())
price = int(input())
value = 0
if input_money > price:
    value = input_money - price
print("500원 동전의 개수 : ", int(value / 500))
value %= 500
print("100원 동전의 개수 : ", int(value / 100))

#동아리회장님
money = int(input("두입한 돈: "))
price = int(input("물건값: "))
change = money - price
print("거스름돈을: ", change)
coin500s = change // 500
change = change % 500
coin100s = change // 100
print("500원 동전의 개수: ", coin500s)
print("100원 동전의 개수: ", coin100s)