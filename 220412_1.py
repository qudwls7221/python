#대입 연산자 
x = 10 
print (x)

x = y = 100
print (x,y)

x , y = 100 , 200
print (x,y)

#산술 연산자
print ("덧셈 1+2 =",1+2)
print ("뺄셈 2-1 =",2-1)
print ("곱셈 4*2 =",4*2)
print ("나눗셈 4/2 =",4/2)
print ("버림 10//5 =",10//5)
print ("나머지 2%10 =",2%10)
print ("제곱 5**5 =",5**5)

#정수와 실수 계산일 경우     오차가있다!!!
print ("-2 + 3.0 =",-2 + 3.0)
print ("4.3 - 2.7 =",4.3 - 2.7) #대표적인오차 1.6 이정상이지만 1.59999999996 으로출력된다
print ("0.1 + 0.1 + 0.1 =",0.1 + 0.1 + 0.1) # 2번째 오류 0.3 이아닌 0.300000000000004 로 출력
# 실수의 경우 2진수방식으로 저장될때 정확한 수가아닌 근사치 로 저장되기 때문에 이러한 오류가 생긴다.

#정수 입력 연습
x = int(input())
p = x+10
m = x-10
s = x*10
e = x/10
print (p,m,s,e)

#정수 입력 연습
i = int(input())
y = (i//5, i%5)
print (y)

#정수 연습
in1 = int(input("정수1"))
in2 = int(input("정수2"))
sm = in1 + in2
sq = in1 * in2
print ("이들의 합은 ",sm," 이고 이들의 곱은 ",sq,"입니다")

# cm 입력을 인치로 바꿔주는것
cm = float(input())
inc = (cm / 2.54)
print ("인치로 변환하면", inc,"inch 입니다")

#합계, 평균 구하기
in1 = int(input())
in2 = int(input())
in3 = int(input())
su = in1+in2+in3
avg = su/3
print ("합계는",su,"이고 평균은",avg,"입니다.")

#생년월일 출력
inp = input()
year = (inp[:4])
mon = (inp[4:6])
day = (inp[6:])
print ("출생일자:",year,"년",mon,"월",day,"일")
#또는
inp = input()
year = (inp[:4])
mon = (inp[4:6])
day = (inp[6:])
print ("출생일자:%s년%s월%s일" %(year, mon, day))
# 나누기, 나머지로 구하기  계산을 이용한 방식
inp = int(input())
year = inp // 10000
mon = inp % 10000 // 100
day = inp % 100
print ("출생일자:%s년%s월%s일" %(year, mon, day))

#복합 연산자 
a = 200
print ("a는",a)
a -= 100 
print ("a -= 100 =",a)
a *= 20
print ("a *= 20 =",a)
a /= 2
print ("a /= 2 =",a)

#관계 연산자 
a , b = 10, 20
print ("a == b", a==b)
print ("a != b", a!=b)
print ("a > b", a>b)
print ("a < b", a<b)
print ("a >= b", a>=b)
print ("a <= b", a<=b)

#논리 연산자   and , or , not (&& , || , !)
a= 10 == 10 and 5 == 6
print (a)
b = 10 == 10 and 5 != 6
print (b)
a, b = 10, 0
ou1 = a == b or a > b
print (ou1)
print (not a) #숫자 0은 false 로 출력하고 그외의숫자는 true 로출력된다
print (not b)

#윤년 계산기
year = int(input("년도를 입력하세요"))
yuu = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print ("입력년도 :",year,"\n","윤년여부 :", yuu)
