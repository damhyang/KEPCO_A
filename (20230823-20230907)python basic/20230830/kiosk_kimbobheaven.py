menu_list = [['김밥', 1, '원조김밥', 2500], ['김밥', 2, '김치김밥', 3000], ['김밥', 3, '참치김밥', 3000],
            ['돈까스', 4, '돈까스', 7000], ['돈까스',5, '더블돈까스', 9000], ['돈까스', 6, '치킨까스', 7500],
            ['분식', 7, '유부우동', 5000], ['분식', 8,'쫄면', 6000],['분식', 9, '라볶이', 5000],
            ['식사', 10,'갈비탕', 7000], ['식사', 11, '순대국', 7000], ['식사', 12, '부대찌개', 7000],
            ['국밥', 13, '갈비탕', 7000], ['국밥', 14,'순대국', 7000], ['국밥', 15,'부대찌개', 7000], 
            ['사이드메뉴', 16, '콜라(250ml)',1000], ['사이드메뉴', 17,'공기밥', 1000], ['사이드메뉴', 18, '계란찜', 5000]]



#menu_list_print: 
for i in range(18): 
    if i%3==0 : 
        print("%5s" %(menu_list[i][0]))    
    for j in range(1,4): 
        print("%8s" %(menu_list[i][j]), end=" ") #ary[0]=[1,2,3,4,5] / ary[1] = [6,7,8,9,10]
    print()


class Kiosk():
    def __init__(self) -> None:     # admin, user, guest   사용자 / 필요요소를 담은 틀(O)
        self.total = 0
        self.money = 0
        self.history = [ ]
        self.qty = 0        
#     #order 받기
    def Choice(self):
        while True:
            food = int(input("주문할 메뉴의 번호를 입력해 주세요: "))
            if 0 < food <= 18 :
                while True:
                    quantity = int(input("선택한 메뉴의 수량를 입력해 주세요(주문 진행 취소를 원하시면 0을 입력해주세요.): "))
                    if quantity>0 :
                        break
                    elif quantity <= 0:
                        print("주문진행이 취소되었습니다.")
                        break
            break
        return food, quantity
# #장바구니
#     def Cart(self,food, quantity):
        