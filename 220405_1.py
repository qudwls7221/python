# 0x 는 16진수라는것을 알려주는것이다.
a = 0xFA
print ("a =", a)
a = 0o123
print ("a = ",a)

# 파이썬의경우 큰수는 , 가아닌 _ 을사용하여 구분한다 출력값은 동일하지만 작성시 구분이용이하기위해서
print (100_000_000)
# 숫자를 입력할때 0을 앞에 작성하면 오류가뜬다.

#12.5123 같이 소수점이있는 방식들은 정수가아닌 실수이다. float 이라고한다.
a = 12.5123
print (type(a))

#컴퓨터식 지수표형 방식
# 3.23E8 은 3.23* 10의 8승을 의미한다.
b = 3.23E8
print (b)
# 23e-10 은 23*10의 -10 승을 의미한다.
c = 23e-10
print (c)

# 문자열데이터 방식으로 String 또는 str 로 표기한다
a = "Hello"
b = 'World'
print (type(a))
print (type(b))


# 부울형으로 Boolean 또는 bool 으로 표기하면 출력값은 True 화 False 두가지로출력한다 조건문에서 많이사용한다
a = True
b = False
print (type(a))
print (type(b))

# 100이 100 보다 크다 False 출력 300 은 300과 같다 True 출력
a = (100 < 100)
print (a)
b = (300 == 300)
print (b)

a = None
print (a)
print (type(a))

x = 10
y = 20
print ( x + y )
x = "Hello"
y = "World"
print (x + y)


radius = 5.0
# radius 를 2번 곱했지만 아래처럼 2번곱할경우와 값은같다
area = 3.141592 * radius * radius
print ("원의 면적은", area)

# **2 는 앞에 값을 2번 곱한다는 의미이다
area = 3.141592 * radius ** 2
print ("원의 면적은",area)

# 키
h = float(input("키"))
# 무게
w = float(input("몸무게"))
# bmi 지수 계산법
bmi = w / h ** 2
print ('BMI는',bmi)

if bmi < 18 :
    print ("당신은 저체중 입니다")
elif bmi < 25 :
    print ("당신은 정상체중 입니다")
elif bmi < 30 :
    print ("당신은 과체중 입니다")
else :
    print ("당신은 고도비만 입니다")


# 부울형 한번더 설명
b1 = True
b2 = False
# 위같이 참거짓리하고 입력해도되지만

print (b1)
print (b2)
# 출력할때 참인것과 거짓인것을 물어도 정상적으로 출력된다
print (3<4)
print (3>4)