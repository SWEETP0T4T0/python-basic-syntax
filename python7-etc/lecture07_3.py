
# #웹크롤링 예제
# # 파이썬을 설치하면 자동으로 pip가 설치
# # pip를 통해 requests와 beautifulsoup4 설치
# import requests
# from bs4 import BeautifulSoup

# url = 'https://ko.wikipedia.org/wiki/%EC%95%84%EB%B0%94%ED%83%80:_%EB%AC%BC%EC%9D%98_%EA%B8%B8'

# # User-Agent 정보 추가
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(url, headers=headers)

# # HTML 파싱
# soup = BeautifulSoup(response.text, 'html.parser')

# # 감독 정보 추출
# director = soup.select_one('table.infobox > tbody > tr:nth-of-type(3) > td').get_text().strip()

# # 제작비 정보 추출
# budget = soup.select_one('table.infobox > tbody > tr:nth-of-type(10) > td').get_text().strip()

# # 결과 출력
# print(f"감독: {director}")
# print(f"제작비: {budget}")


# import requests
# import json

# # 코인 시세 정보 API URL
# url = "https://api.binance.com/api/v3/ticker/24hr"

# # 코인 시세 정보 가져오기
# response = requests.get(url)
# data = json.loads(response.text)

# # 코인 시세 정보 출력
# for coin in data:
#     if coin["symbol"] == "BTCUSDT":
#         print("BTC price:", coin["lastPrice"])
#     elif coin["symbol"] == "ETHUSDT":
#         print("ETH price:", coin["lastPrice"])




# #많이 쓰이는 외장함수
# #time
# import time
# print(time.localtime())
# print("현재 시각은 %d:%d:%d 입니다." %(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec))
# print("타입슬립")
# time.sleep(5)
# print("타입슬립끝")

# #random
# import random
# print(random.randint(1, 10))
# lista = random.sample(range(1,46), 6)
# lista.sort()
# print(lista)
# print(sorted(random.sample(range(1,46), 6)))

#webbrowser
# import webbrowser
# webbrowser.open("https://www.naver.com/")



# import seaborn as sns
# import matplotlib.pyplot as plt

# # 맛집 추천 웹사이트에서 수집한 리뷰 데이터
# reviews = sns.load_dataset('tips')

# # 요일별 팁의 평균과 표준편차를 계산
# tip_by_day = reviews.groupby('day')['tip'].agg(['mean', 'std']).reset_index()

# # 막대 그래프(bar plot)로 시각화
# sns.barplot(x='day', y='mean', data=tip_by_day, yerr=tip_by_day['std'], capsize=0.1)
# sns.despine()  # 축과 테두리를 없애주는 함수
# plt.title('Average Tip per Day of Week')
# plt.xlabel('Day of Week')
# plt.ylabel('Average Tip ($)')
# plt.show()

