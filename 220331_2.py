#나
sec = int(input("초를 입력하세요: "))
s = sec % 60
m = sec / 60 % 60
h = sec // 3600
print ("입력한 시간은",h,"시간",int(m),"분",s,"초입니다.")

#동아리 회장님
i = int(input("초를 입력하세요: "))
hour = i // 3600
i = i%3600
min = i//60
sec = i - min*60
print("입력한 시간은",hour,"시간",min,"분",sec,"초입니다.")