#count / len

a="happy"
a.count("p")
print(a.count("p"))
print(a)

len(a)
print(len(a))
print(a)
#########################
#find / index
a="python is the best choice"
a.find("t")
print(a.find("t"))
print(a)

a.find("z")
print(a.find("z"))
print(a)
#문자열 내장함수 find는 없을 경우 -1이 나온다.


a.index("t")
print(a.index("t"))
print(a)

#error# a.index("z")
#error# print(a.index("z"))
#문자열 내장함수 index는 없을 경우 error가 발생한다.
################################
#join(문자열(리스트, 튜플)->문자열로 합침) / split(문자열->리스트로 나눔.)

print("abcd")
print((" ").join("abcd"))
print(("").join("abcd"))
print((",").join("abcd"))
print(",".join("abcd"))
print((", ").join("abcd"))
#error# print(().join("abcd"))

a="abcd"
print(",".join(a))
print(a)

print((",").join(["apple", "boom", "card"]))

a=["apple", "boom", "card"]
print(",".join(a))
print(a)

a="python is the best choice"
print(a.split())
print(a.split(" "))
print(("python is the best choice").split())
print(a)

b="a:b:c:d"
b.split(":")
print(b)

