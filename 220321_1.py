import random

#무작위 난수 생성
ranNum = random.sample(range(1,100),2)
print("난수 : ",ranNum)

num1 = ranNum[0]
num2 = ranNum[1]

print('num1 : ',num1)
print('num2 : ',num2)

print('num1 + num2 = ', (num1 + num2))
print('num1 - num2 = ', (num1 - num2))
print('num1 * num2 = ', (num1 * num2))
print('num1 / num2 = ', (num1 / num2))