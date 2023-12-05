####시간

time = int(input("초 단위로 입력해 주세요."))

#몇 시간인지 구하기.
unit_hour = time//3600

#시간을 뺀 나머지 초 구하기.
#time_hour = time - (3600*time_hour)
time_hour = time%3600

#몇 분인지 구하기.
unit_min = time_hour//60

#분을 뺀 나머지 초 구하기.
# time_sec = total_hour - (60*time_min)
unit_sec = time_hour%60

print(f'{time_hour}시간 {unit_min}분 {unit_sec}초')