a = [1,2,3]
b = [4,5,6]

print (a+b)

#리스트 더하기 가능
#[1, 2, 3, 4, 5, 6]

print (a*3)

#곱하기 
##[1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트에서 삭제 , 변경도가능 

a = ["문제성","유병진","신이야"]
a[0:2]  = ["아이우","이이아"]
print (a)
# 리스트 변경
#['아이우', '이이아', '신이야']

a = ["문제성","유병진","신이야"]
a[0:2]  = []
print (a)

#리스트에서 내용삭제
#['신이야']

a = ["문제성","유병진","신이야"]
del a[0]
print (a)

# 삭제_2 특정인덱스 삭제
#['유병진', '신이야']

#리스트 함수 append 뒤에 추가한다
a = [1,2,3]
a.append(4)
print (a)

#리스트 sort() 정렬 숫자 크기순 문자 가나다 순으로 정렬
a = [5,2,3]
a.sort()
print (a)

#리스트 reverse()
a = [1,2,3]
a.reverse()
print (a)

#리스트 index() 내부에 있는 수를찾으며 찾은수의 인덱스 주소를 출력해준다
print (a.index(3))

#리스트 추가 insert()
a = [1,2,3]
a.insert(0,4) # 0번째 인덱스에 , 4를 추가해라는의미
print (a)

#리스트 인덱스 제거 remove()
a = [1,2,3]
a.remove(2) # 2라는 값이 있다면 인덱스 수에서 가까운것을 1개 제거해라 전부제거하려면 for문 사용
print (a)

#리스트 인덱스 pop
a = [1,2,3]
print (a.pop(2)) #인덱스 주소 2번의 수를 [] 에서 빼고 출력 시킨다
print (a)

#리스트 count()
a = [1,2,3,2,1]
print (a.count(1))  # 1이라는 수가 몇개있는지 출력한다
