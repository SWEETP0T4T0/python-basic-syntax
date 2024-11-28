# #형변환
# stra = "Hello"
# inta = 5
# print(stra + str(inta))
# #int >> str 로 갈땐 str()
# #str >> int 로 갈땐 int()


# 출력
# # 콤마를 넣으면 자동으로 공백 삽입 그러나 +를 하면 공백삽입X
# # 콤마(,)는 모든 자료형의 값을 연결할 수 있는 반면, 덧셈(+)은 문자열들만을 연결
# print("출력값 숫자", 4)
# print("출력값 숫자 여러개", 4, 5, 6)
# su =5
# dan = 800   
# print("su 주소 : " + str(id(su)))
# print("dan 주소 : " + str(id(dan)))
# print("금액 : " + str(su*dan))
# print("금액 :", su*dan)

# #입력
# num = input()
# print(num)
# num = input("숫자를 입력하세요")
# print(num)
# print(type(num))
# #파이썬에서는 항상 문자열로 입력을 받는다.
# fat = input("지방의 그램을 입력하세요 ")
# tan = input("탄수화물의 그램을 입력하세요 ")
# dan = input("단백질의 그램을 입력하세요 ")
# total = int(fat)*9 + int(dan)*4 + int(tan)*4
# print("총칼로리 :", total)


#연습문제 4.
word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")
print("===================")
abbr = word1[0] + word2[0] + word3[0]
print("약자 :", abbr)