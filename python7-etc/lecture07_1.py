# 사각형 객체1

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area_calc(self):
#         return self.width * self.height
#     def circum_calc(self):
#         return (self.width+self.height)*2
# #
# print("사각형의 넓이와 둘레를 계산합니다.")
# w = int(input('사각형 가로 입력 :'))
# h = int(input('사각형 세로 입력 :'))
# cal1 = Rectangle(w, h)
# print("사각형의 넓이는:", cal1.area_calc())
# print("사각형의 둘레는:", cal1.circum_calc())

# 또다른 사각형 객체2

# # 사람 객체 만들기
# class Person:
#     def __init__(self, name, gender, age):
#         self.name = name
#         self.gender = gender
#         self.age = age

#     def display(self):
#         print("이름 : %s, 성별 : %s \n나이: %s"%(self.name, self.gender, self.age))

# name = input("이름 입력")
# age = input("나이 입력")
# gender = input("성별 입력")

# p1 = Person(name, gender, age)
# p1.display()


# # 계산기 패키지 모듈 추가
# # 아래와 같이 커스마이징한 모듈을 추가하려면 mtCalcPackage 디렉토리가 파이썬 모듈 경로에 등록해야 한다
# import sys
# sys.path.append('/Users/seongukkim/Downloads/빅데이터/pythonLecture-main/pythonLecture-main/')

# from mtCalcPackage import calcModule
# print(calcModule.Add(10, 5))

# #각종 내장함수
# # 절대값 구하기
# print(abs(-3))

# #주요 내장함수1. 아스키코드
# print(chr(97))

# # 최대값
# lista = [1,10,5,2]
# print(max(lista))

# # pow 제곱함수
# print(pow(2,3))

# #id 함수
# a = 3
# print(id(a))


# #map 함수 : 특정함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받아, 특정함수가 수행한 결과를 리턴.
# #  함수의 반환 값은 map object이고 출력시 메모리 주소가 출력된다. list로 변환하려면 list(lista)
# def two_times(x):
#     return x*2
# lista = map(two_times, [1, 2, 3, 4])
# print(lista)

# #함수를 통과하여 참인 value만 돌려주는 filter : 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형
# def trueorfalse(x):
#     if x > 0:
#         return True
#     else:
#         return False
# lista = list(filter(trueorfalse, [1,2,3, -1, -2]))
# print(lista)

# factorial 재귀함수 

# def StarCount(height):
#     starnum = 0
#     for a in range(1, height+1):
#         print("*"*a)
#         starnum += a
#
#     print("star개수:", starnum)
#
# StarCount(int(input("star 층수 입력")))

# result = 1
# def Factorial(n):
#     global result
#     if n == 1:
#         return 1
#     else:
#         result = result*n
#         if n == 2:
#             pass
#         else:
#             Factorial(n-1)
#         return result
# result_fact = Factorial(5)
# print('팩토리얼 결과:', result_fact)




