# 04장. 함수
#지금까지 공부한 내용을 바탕으로 (02,03장. : 프로그래밍의 기초)
#구조
"""
def 함수명(매개변수):
....수행할 문장1
....수행할 문장2
....[return]

      머리(header)          /           몸통(body)
         함수명                   동작과정(절차, 알고리즘)
    매개변수(파라미터)       /    반환값(return (value) )"""


#함수의 종류 4가지로 책에 나와 있지만, 단지 매개변수와 반환값을 생략이 가능하기 때문에 4가지로 보인것 뿐이다.

#print 함수를 실행하면 한줄띄기(줄바뀜)이 실행된다.
#print함수는 반환값이 없는 것 처럼 보인다.(실제로는 있긴하나 지금 수준에서는 없는것으로 취급)
a=print()
print(a)

#input함수 반환값이 있는 함수이다.
input()


#리스트 자료형의 쓰임 : 여러개의 변수를 쓸 떄.

#변수에 리스트가 들어가 여러개를 넣을 수 있다.
#이를 대신하는게 *인데 이해하기에는 C언어의 포인터를 이해가 필요하다.
    

"""
return은 튜플로 묶어 하나로 준다.
그리고 함수를 종료시킨다."""

"""
()의 형태로 따로 인수를 설정하지 않아도 함수 자체에 초기값(갱문자?(띄어쓰기, 한줄띄기))이 있어 수행된다."""