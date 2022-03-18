import random

# 무작위 난수 생성
# 랜덤Num은 랜덤으로 정한다, 샘플 (1~100까지)1개 추출
ranNum = random.sample(range(1,100),1)
# "난수:" 랜덤Num을 출력시킨다
print("난수 : ", ranNum)

# 난수 testNum 변수에 저장
#테스트 숫자는?? 이해못함
testNum = ranNum[0]

# 기억력 테스트 게임 시작
# 게임 기본 인터페이스 Text
print("당신의 기억력을 테스트합니다.")
print("준비되셧습니까? ")
print("1. yes / 2. no")

inputNum = int(input())
type(inputNum)

# 만약 입력값이 1이라면
if inputNum == 1:
    #난수를 가리기 위해 공백 문자는 20번 출력
    for i in range(20):
        print()
        #출력값을 물어본다
        print("난수는?")
        #출력값에 대한 정답 사용자가 입력
        myNum = int(input())

        #사용자 입력 수와 난수 비교
        #입력값이 맞다면 출력
        if myNum == testNum:
            print("빙고~ 훌륭합니다.")
            #그렇지않다면 실패
        else:
            print("아쉽습니다.")

#1번 이아닌 수를입력했을시 출력
#위 설명처럼 2번을누르면 no가출력되진않는다.

else:
    print("게임을 종료합니다.")
