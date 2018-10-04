import json
import urllib.request

sp = {"elmiram" : "https://github.com/elmiram", "maryszmary" : "https://github.com/maryszmary", "lizaku" : "https://github.com/lizaku", "nevmenandr" : "https://github.com/nevmenandr", "ancatmara" : "https://github.com/ancatmara", "roctbb" : "https://github.com/roctbb", "akutuzov" : "https://github.com/akutuzov", "agricolamz" : "https://github.com/agricolamz", "lehkost" : "https://github.com/lehkost", "kylepjohnson" : "https://github.com/kylepjohnson", "mikekestemont" : "https://github.com/mikekestemont", "demidovakatya" : "https://github.com/demidovakatya", "shwars" : "https://github.com/shwars", "JelteF" : "https://github.com/JelteF", "timgraham" : "https://github.com/timgraham", "arogozhnikov" : "https://github.com/arogozhnikov", "jasny" : "https://github.com/jasny", "bcongdon" : "https://github.com/bcongdon", "whyisjake" : "https://github.com/whyisjake", "gvanrossum" : "https://github.com/gvanrossum"}

x = input ()

if x in sp:
    print("вы выбрали пользователя" , x)
else:
    print("выбранный пользователь отсутствует в базе, повторите попытку ввода" )
user = x  # пользователь, про которого мы хотим что-то узнать
url = sp[x]   # по этой ссылке мы будем доставать джейсон, попробуйте вставить ссылку в браузер и посмотреть, что там
response = urllib.request.urlopen(url)  # посылаем серверу запрос и достаем ответ
text = response.read().decode('utf-8')  # читаем ответ в строку
data = json.loads(text) # превращаем джейсон-строку в объекты питона
maxi = len(data)  # сколько у пользователя репозиториев
print("Список репозиториев с описаниями")
for i in data:
    print(i["name", "description"])

for c in data:
    a = [c["language"]]    #список всех упоминаний всех языков
    words = count(a.split()) #делим на слова и считаем
print (words)

