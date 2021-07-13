import requests
res = requests.get("http://google.com")
# res = requests.get("http://dsf.tistory.com")
res.raise_for_status()
# print("응답코드 : ", res.status_code) # 200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

# res.raise_for_status() # 올바른 코드를 가져오지 않았을 때 에러를 냄
# print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoogle.html", 'w', encoding='utf-8') as f:
    f.write(res.text)