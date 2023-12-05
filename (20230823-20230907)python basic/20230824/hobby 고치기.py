print("a">"b")
# 문자열 자료형을 변수에 저장
words = "hobhy"

# words = "hobby"
# "hob"+"b"+"y"
# words[:3]+"b"+words[4:]
# words[:2]+"b"+words[-1]
# words[0]+words[1]+words[2]+'b'+words[4]
print(words)

# words.split("") 에러나옴


words_list=list(words)
print(words_list)

words_list[3]="b"
print(words_list)

print("".join(words_list))

print(f'{"python":!^12}')

# Q1='1 2 3 4 5 6'의 문자열의 합을 구해라.
Q1='1 2 3 4 5 6'
Q1_split=Q1.split(" ")
Print(Q1_split)