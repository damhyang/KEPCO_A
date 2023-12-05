

### 선택구조_상, 시상기준, 시상내역
#1차
score = int(input("점수를 입력해 주세요: "))
if score >= 90 :
    category = "금상"
    present = "상장, 도서상품권 20개"
elif 80 <= score < 90 :
    category = "은상"
    present = "상장, 도서상품권 10개"
elif 70 <= score < 80 :
    category = "동상"
    present = "상장, 도서상품권 5개"
elif 60 <= score < 70 :
    category = "장려상"
    present = "상장"
print([score, category, present])

#2차 
category_paper = {'금상': True, '은상': True, '동상' : True, '장려상' : True}
category_coupon = {'금상' : True, '은상' : True, '동상' : True, '장려상' : True}
category_coupon_number = {'금상': 20, '은상': 10, '동상': 5, '장려상' : 0}

def Score():
    score = int(input("점수를 입력해 주세요: "))
    return score

def Judge(score):
    if score >= 90 : category = "금상"
    elif 80 <= score < 90 : category = "은상"
    elif 70 <= score < 80 : category = "동상"
    elif 60 <= score < 70 : category = "장려상"
    return category

def Result(category) :
    result = [score, category, category_paper[category], category_coupon[category], category_coupon_number[category]]
    return(result)
    

# main 함수
score = Score()
category = Judge(score)
result.append(Result(category))
print(result)

