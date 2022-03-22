from calendar import day_abbr


print ("3 * 1 = 3")
print ("3 * 2 = 6")
print ("3 * 3 = 9")

print ("3 * 1 =", 3*1)
print ("3 * 2 =", 3*2)
print ("3 * 3 =", 3*3)

print ("2 + 5 = 7")
print ("2 + 5 =",2+5)

print ("9 * 1 =", 9*1)
print ("9 * 2 =", 9*2)
print ("9 * 3 =", 9*3)
print ("9 * 4 =", 9*4)
print ("9 * 5 =", 9*5)
print ("9 * 6 =", 9*6)
print ('''9 * 7 =''', 9*7)
print ("""9 * 8 =""", 9*8)
print ('9 * 9 =', 9*9)

print (1,2,3)
print ("Hello",'Python')

print (1,2,3, sep=", ")
print (4,5,6, sep=",")
print ("Hello",'Python',sep="")
print ("010","1234","5678", sep="-")

#정상출력시 줄바꿈있다
print("Hello")
print ("World")
print ("Good")
print ("Job")

#줄바꿈 없에기
print ("Hello", end='')
print ("World", end="")
print ("Good", end="")
print ("Job")

#줄바꿈
print ('1\n\n2\n3')

#반복 넓게쓰기
print (1,2,3,sep="\t")

#;의 엔터기능 대체
print ("Hello"); print("1234")

#실습
print ("15 + 37 =",15+37)
print ("15에서 37을 뺀 값은",15-37,"입니다.")
#완

#변수
no = 75
print ("no의 값은",no,"입니다.")


#년, 월, 일, 시간 변수 선언
year = 2022
month = 10
day = 31
hour = 11
minute = 29
second = 42

print (year,month,day,sep='/',end=" ")
print (hour,minute,second, sep=":")