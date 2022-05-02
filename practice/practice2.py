import requests
import json
# jsondata pprint 출력 코드
# from pprint import pprint
cityname= "Incheon"
APIkey = "9e449d60b1076be971ff2ef3650eb148"
lang="kr"
api=f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={APIkey}&lang={lang}&units=metric"
result=requests.get(api)
data=json.loads(result.text)


print(data['name'],"의 날씨입니다.")
print("날씨는",data['weather'][0]['description'],"입니다.")
print("현재 온도는",data["main"]["temp"],"입니다.")
print("체감 온도는",data["main"]["feels_like"],"입니다.")
print("최저 기온은",data["main"]["temp_min"],"입니다.")
print("최고 기온은",data["main"]["temp_max"],"입니다.")
print("습도는",data["main"]["humidity"],"입니다.")
print("기압은",data["main"]["pressure"],"입니다.")
print("풍향은",data["wind"]["deg"],"입니다.")
print("풍속은",data["wind"]["speed"],"입니다.")
