# 메뉴보여주고, 메뉴상의 숫자가 아닌 다른 숫자를 입력하면 다시 menu_number이 출력되도록 하기
menu_number = """1. coffee__300won
2. juice__500won

choose your beverage : """
insert = "insert coin: "
coffee = 5
juice = 3

number = 0
while (number != 1) and (number != 2):
    print(menu_number)
    number = int(input())

# # 돈을 넣어달라고 한 후에, 금액을 확인하고 커피와 거스름돈을 주기, 그리고 소진되면 표현


while True :
    if number == 1:
        money = int(input(insert))    
        if money==300:
            print("you can Get coffee")
            coffee=coffee-1
            break
        
        elif money>300:
            print("you can Take charge %dwon and Get coffee" %(money-300))
            coffee=coffee-1
            break
        elif money<300:
            print("you can Take your %dwon and lack of coin" %(money))
            break
        
        if coffee==0:
            print("coffee is soldout")

            
    else:
        money = int(input(insert))    
        if money==500:
            print("you can Get juice")
            juice=juice-1
        
        elif money>500:
            print("you can Take charge %dwon and Get juice" %(money-500))
            juice=juice-1
        
        else:
            print("you can Take your %dwon and lack of coin" %(money))
        if juice==0:
            print("you can juice is soldout")
        break










