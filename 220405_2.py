from re import S



# 문자열을 사용할때 따옴표 사용법
s = "그가 '좋아'라고 답했다"
print (s)
s = "그가 \'좋아\'라고 답했다"
print (s)
s = '''그가 '좋아'라고 답했다'''
print (s)

#이스케이프 시퀀스
# \n 줄바꿈  \t 탭기능  \\ 역슬래시를 입력할때

print ("Hello \nWolrd")
print ("Hello \tWolrd")
print ("Hello \\Wolrd")
print ("Hello \bWolrd")
print ("Hello \vWolrd")
print ("\u0061") #유니코드 0061값에 해당되는 문자

# 문자열 포멧팅
name = "홍길동"
print ("제 이름은 %s 입니다." % name)
age = 22
print ("나이는 %d 살입니다." % age)
height = 176.5
print ("키는 %fcm 입니다." % height)
print ("키는 %.1fcm 입니다." % height) # %f 자리수를 정하기

# 포멧팅 응용하여 사용법
msg = "현재 시간은 %s 입니다."
time = "12:00pm"
print (msg % time)

#응용 2
msg = "오늘은 %s월 %s일입니다."
print(msg % (5, 15))

# 문자열 을 더할경우 각문자열 끼리 붙어서 합쳐진다
first = "컴퓨터"
print (first + "공학관")

# 문자열을 곱할경우에는 해당 문자열이 반복된다.
s1 = "컴퓨터"
s2 ="공학과"
s3 =(s1 + s2 + "!!") *3
print (s3)

#인덱스 추출 0부터 시작!!! 인덱스수는 []에 감싸서 계산한다
#인덱스는 추출만가능하기때문에 인덱스를 이용한 문자열수정은 불가능하다
s ="Hello"
print (s[1])
print (s[0])
print (s[-1])
#인덱스 응용
print (s[0]+s[1]+s[2]+s[3]+s[4])
print (s[4]+s[3]+s[2]+s[1]+s[0])

#슬라이싱
# 인덱스 추출에서 일정문자열을 추출하는방식으로 [1:3] 은 1~2 까지 꺼낸다는 의미이다 마지막의 1개는 뺀다고 생각하면 편하다
print (s[0:2])
print (s[0:5])

s = "Hello Wolrd"
# 아래는 0~4반까지출력
print (s [:5])
# 아래 6번부터 끝까지
print (s [6:])
# 아래 처음부터 끝까지
print (s[:])

s = ('20210514Friday')
year = s[:4]
month = s[4:6]
day = s[6:8]
week = s[8:]
date = year + '년' + month + "월" + day + "일" + week + "요일"
print (date)
print (s[:4]+"년"+s[4:6]+"월"+s[6:8]+"일"+s[8:]+'요일')

# 해당하는 문자의 갯수를 출력한다
s = "Hello World"
print (s.count('l'))
print (s.count('w'))

# find 함수는 인덱스주소로 찾는다 없을경우 -1 을출력
print (s.find("H"))

# index() 함수는 해당함수의 인덱스 주소를알려준다 find와 달리 없을경우 오류를 발생시킨다.
print (s.index("H"))

# strip() 함수의 경우 문자열의 왼쪽과 오른쪽에 공백을제거
# lstrip() 문자열의 왼쪽에 포함된 공백을 삭제
# rstrip() 문자열의 오른쪽에 포함된 공백 삭제

s = "    Hello    "
print (s.strip())
print (s.lstrip())
print (s.rstrip())

# upper() 문자열의 모든알파벳을 대문자로
# lower() 문자열의 모든 영어를 소문자로
s = "Hello World"
print (s.upper())
print (s.lower())

#join() 구분자를 사용하여 문자열의 각각 문자 사이에 삽입
s = "Hello"
# s 변수안에 문자 마다 / 를입력한다는 의미
print ("/".join(s))

sep = " - "
print (sep.join("ABCDE"))

# replace(인수1, 인수2) 문자열에서 1을 2로 치환하는 함수
s = 'Hello World'
print (s.replace("o", "a"))

#split(공백 또는 구분자) 리스트업 시키는것이다
s = "Hello World"
print (s.split())

s = "www.nrf.re.kr"
print (s.split("."))

# format()
s = 'Hello {}'
print (s.format("World"))

#format 응용1
s = "Hello {0} {1}"
print (s.format("World","Python"))
s = "Hello {1} {0}"
print (s.format("World","Python"))

#format 응용2
s= "Hello {s1} {s2}"
print (s.format(s2="World", s1="Python"))

#len() 문자열의 길이를 반환
s = "Hello"
print (len(s))

col = [1, 2, 3]
print (len(col))

#chr()함수 , ord() 함수
print (chr(97)) # 유니코드 값을 문자로 바꾸기
print (ord('a')) # 문자를 입력받고 유니코드로 바꾸기

#hex() 16진수  oct() 8진수 입력받은 수를 16혹은 8진수로 변환한다
print (hex(12593))
print (hex(97))

print (oct(9))
print (oct(16))

#자료형 변환 input 함수사용시 많이사용한다 input 의 경우 기본적으로 str방식으로 입력을받기 때문에 연산을위해서는 변환필수
print (10+int('10'))
print (str(10)+'10')

#정수변환
print (int(3.14159))
print (int(7 / 3))
print (int("2000"))

#실수변환
print (float(3))
print (float(6/3))
print (float("2000"))
print (float('3.14159'))

#문자열 변환 str()
print ("score = 100 점입니다")