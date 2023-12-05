# a = int(input("첫번째 성적을 입력해 주세요:" ))
# b = int(input("두번째 성적을 입력해 주세요:" ))
# c = int(input("세번째 성적을 입력해 주세요:" ))

# sum = (a + b + c)
# average = (sum)/3

# print(f"합계 : {sum}")
# print(f"합계 : {average}")
####################################################################################

# number = input("3개의 성적을 ,로 구분하여 입력해 주세요(예 : 100,100,100): " )
# number_split = number.split(",")
# [a,b,c] = [int(number_split[0]), int(number_split[1]), int(number_split[2])]


# sum = (a + b + c)
# average = (sum)/3

# print(f"합계 : {sum}점")
# print(f"합계 : {average}점")
####################################################################################

number = int(input("미터 단위로 변환하고 싶은 cm의 값은?: "))
unit_portion = number//100
unit_rest = number%100
meter = f'{unit_portion}.{unit_rest} m'
print(meter)