data = [ ['장려상', 60, 1, 0, 0],
         ['동상', 70, 1, 1, 5],
         ['은상', 80, 1, 1, 10],
         ['금상', 90, 1, 1, 20]]

# def prize(List, score):
#     if score >= List[1]:
#         return True

# print(data[::-1])
# score = int(input("점수를 입력하세요: "))
# for idx, List in enumerate(data[::-1]):
#     if prize(List, score):
#         print(data[::-1][idx])
#         break

# 님, ====={rank}=======상품: 문화상품권 {qty}매
score = int(input("점수를 입력하세요: "))
for [rank, min_score, trophy, bonus, qty] in data[::-1]:
    if score >= min_score:
        print(f" 님, ====={rank}=======", end='')
        if qty:
            print(f"상품: 문화상품권 {qty}매")
        print()

        for txt in [rank, qty]:
            if txt:
                print(f"{txt}", end="")
        print()
        break

