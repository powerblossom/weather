import json
import requests

#res = requests.get('http://api.weatherapi.com/v1/current.json?key=35372b0b50c9464a87a01147210810&q=seoul&api=yes')
#print(res.text)
#jsonObj = json.loads(res.text)

#print(json.dumps(jsonObj, indent=4))
#print(jsonObj['current']['temp_c'])

info = '''
1.seoul
2.pusan
3.inchon
4.jeju
5.New York
6.Beijing
'''
print(info)
inputVal = input('번호를 입력하세요(선택이 잘못된경우 서울이 기본 값): ')
cityname = 'Seoul'
if int(inputVal) == 2:
    cityname = 'pusan'
    korname = '부산'
elif int(inputVal) == 3:
    cityname = 'inchon'
    korname = '인천'
elif int(inputVal) == 4:
    cityname = 'jeju'
    korname = '제주'
elif int(inputVal) == 5:
    cityname = 'nyc'
    korname = '뉴욕'
elif int(inputVal) == 6:
    cityname = 'Beijing'
    korname = '베이징'
else:
    cityname = 'seoul'
    korname = '서울'

res = requests.get('http://api.weatherapi.com/v1/current.json?key=35372b0b50c9464a87a01147210810&q='+ cityname + '&api=yes')
jsonObj = json.loads(res.text)
rain = jsonObj['current']['condition']['text']

if rain == "Light rain":
    rain = "가벼운비"    
elif rain == 'Partly cloudy':
    rain = '부분적으로 흐림'
elif rain =='Overcast':
    rain = '전체적으로 흐림'
elif rain == 'Clear':
    rain = '맑음'


print(korname, jsonObj['current']['temp_c'],'도',rain)