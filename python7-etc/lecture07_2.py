
# #파일최초생성하기
# #open을 하였으나, 해당 파일이 없으면 자동 생성
# #f는 변수이자 파일객체로서, 해당 파일에 대한 정보와 mode(w, r, a)를 갖고 있다.
# #이 변수를 통해 해당 파일을 컨트롤 하는것.
# f = open("test.txt", 'w')
# f.close()
#
# #파일 쓰기모드로 열어 내용삽입.
# f = open("test.txt", "w", encoding="UTF-8")
# for i in range(1,10):
# 	data = "%d번째 줄입니다. \n" %i
# 	f.write(data)
# f.close()

# # #아스키코드 출력
# # print(chr(97))

#파일 읽기모드.
# readline으로 파일을 읽을경우
# f = open("test.txt", "r", encoding="utf-8")
# line = f.readline()
# print(line)
# f.close()
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()

# #readlines를 통해 리스트 형태로 담는경우
# f = open("test.txt", "r", encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# #기본적으로 readline을 통해 읽어오는 line에 개행이 추가되므로, strip을 통해 \n 제거
# f = open("test.txt", "r", encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line.strip('\n'))
# f.close()

# #통째로 읽어 오기
# f = open("test.txt", "r", encoding="utf-8")
# data = f.read()
# print(data)
# f.close()


# # #추가 모드로 읽어오기
# f = open("test.txt", "a", encoding="utf-8")
# for i in range(10,21):
# 	data = "%d번째 줄입니다. \n" %i
# 	f.write(data)
# f.close()

# # 파일을 오픈하면 해당 파일은 파일 디스크립터(file descriptor)라는 것으로 추상화되어 컴퓨터의 메모리상에서 파일 입출력을 관리합니다. 
# # 파일 디스크립터는 운영체제 내에서 파일과 연관된 정보를 담고 있으며, 파일의 상태, 파일 위치 등을 추적하고 유지한다.
# # 그러므로, 해당 자원을 close(해제) 하지 않으면 메모리 누수(leak)이 발생합니다.
# #close 없이 파일 open 방법
# with open("test.txt", "w", encoding="UTF-8") as f:
#     for i in range(1,10):
#         data = "%d번째 줄입니다. \n" %i
#         f.write(data)




#os 라이브러리를 활용한 디렉터리내 .py 파일검색
import os
#
# serchdir = 'D:\개발자료\PycharmProjects\pythonProject'
# dirlist = os.listdir(serchdir)
# print(dirlist)
# for dir in dirlist:
#     dirtuple = os.path.splitext(dir)
#     if(dirtuple[1] == '.py'):
#         print(os.path.join(serchdir, dir))

#디렉토리내 디렉토리 속의 모든 파일을 search하려면?
# serchdir = 'D:\개발자료\PycharmProjects\pythonProject'
# dirlist = os.listdir(serchdir)
# print(dirlist)
# for dir in dirlist:
#     filename = os.path.join(serchdir, dir)
#     if os.path.isdir(filename):
#         for dir2 in filename:
#             filename = os.path.join(serchdir, dir2)
#             dirtuple2 = os.path.splitext(dir2)
#             if (dirtuple2[1] == '.py'):
#                 print(filename)
#
#     dirtuple = os.path.splitext(dir)
#     if(dirtuple[1] == '.py'):
#         print(filename)

#재귀함수 필요
# def search(serchdir):
#     dirlist = os.listdir(serchdir)
#     for dir in dirlist:
#         filename = os.path.join(serchdir, dir)
#         if os.path.isdir(filename):
#             search(filename)
#         else:
#             dirtuple = os.path.splitext(dir)
#             if(dirtuple[1] == '.py'):
#                 print(filename)
# search('D:\개발자료\PycharmProjects\pythonProject')

#예외처리까지 해주면 더욱 좋다.
# def search(serchdir):
#     try:
#         dirlist = os.listdir(serchdir)
#         for dir in dirlist:
#             filename = os.path.join(serchdir, dir)
#             if os.path.isdir(filename):
#                 search(filename)
#             else:
#                 dirtuple = os.path.splitext(dir)
#                 if(dirtuple[1] == '.py'):
#                     print(filename)
#     except Exception as e:
#         print(e)
#         pass
# search('D:\개발자료\PycharmProjects\pythonProject')




