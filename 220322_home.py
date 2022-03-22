# 문자열 자료형

'''
\n 문자열에 줄을바꿀떄사용
\t 문자열 사이에 탭간격을 줄때 사용
\\ 문자 \ 를 그대로 출력하기위해 사용
\' 작은 따옴표(') 를 출력하기 위해사용
\" 큰 따옴표(") 를 출력하기위해 사용
"""""" 또는 '''''' 의장점은 출력시 줄바꿈 자료형을 사용하지않아도 입력한것 그대로 출력된다.
'''

"""
#파이썬의 경우 문자열을 곱하기로 반복출력시킬수있다 
a = "Python"
b = " is fun"
print (a * 100)
"""
#문자열 자료형 2-2 인덱싱 (indexing)
a = "1234567890"
'''
아래 print의 출력값은 1이다 [1]일경우에는 2 [2]일경우 3 이출력된다
print(a[0])
아래의경우 인덱싱의 규칙들이다 :8일경우 처음부터 8까지 8: 8부터끝까지이다
::2 일경우 1 3 5 7 이런식으로 2칸간격으로 출력된다 이것이 슬라이싱이다 -로 작성시 뒤에서부터 시작한다
print (a[이상:미만:간격])
'''

#문자열 포멧팅
'''
number = 10
day = "three"
지금 보는 것과같이 %s 와 %d 를이용하여 큰따옴표를 추가사용하지않고 바로 변수들을 집어넣을수있었다

사용가능한 것들 아래
%s 문자열 (가장많이사용하며 문자열로는 무엇이든출력가능하기에 평범하게 많이쓴다)
%10s 으로 출력시 띄어쓰기 10번사용후 출력 -도 가능
%c 문자 1개
%d 정수
%f 부종 소수
%0.3f 정렬기능 0.3으로 입력시 소수점 3자리까지만 출력
%o 8진수
%x 16진수
%% Literal % (문자 '%' 자체)

a = "I ate %d apples. so I was sick for %s days." % (number, day)

print(a)
출력 I ate 10 apples. so I was sick for three days.
'''
#문자열 포멧팅 2
'''
a = "asdaagfgs asdafg {age} gsdfgsfg {name} fgfgsgh".format(name="유병진",age="24")
이같은 경우 전과는다르게 ()에 첫번째두번쨰 순서상관없이 변수명으로 지정가능하다 물론 이전 1번과같이 사용하려면 변수명없이
{}공란으로 만들어 사용시 1번과같이사용할수있다 %~ 를사용하지않는 다는장점이있다
print (a)
출력 asdaagfgs asdafg 24 gsdfgsfg 유병진 fgfgsgh
'''
#문자열 포멧팅 3 (3.6 버전부터가능)
'''
이것의 좋은점은 훨씬 간소화하였다는것이다
현재 가장짧은 것
name = "int"
a = f"나의 이름은 {name}입니다"
print (a)
출력 나의 이름은 int 입니다
'''

"""
a = "hobby"
#인덱스 찾기 01234 순서이기때문에 b는 2에있다 가장처음나온것을 출력
#없는 것을 찾을시 있으면 인덱스숫자가 나오고 없으면 -1 이출력된다
print (a.find('b'))
#count는 b가몇게있는지 출력한다
print (a.count('b'))
"""
#문자열 추가
'''
#문자열 join 을사용하면 abc사이에 ,가들어간다
a = ",".join('abc')
print (a)
출력 a,b,c
#이런식으로 변수선언시 사용할수도있고 출력시 붙여서 사용할수도있다 
.lower : 소문자
.strip : 공백 없애기
a = "hi"
print (a.upper())
출력 HI

.replace : 문자열 바꾸기
a = "Life is too short"
print (a.replace("Life","Your leg"))
출력 Your leg is too short

.split : 띄어쓰기 별로 나눠서 리스트로 만든다
a = "Life is too short"
split ()사이에 특정문자를 넣을시 그문자가있을떄마다 나누어 리스트로 만든다
print (a.split())
출력 ['Life','is','too','short']
'''



