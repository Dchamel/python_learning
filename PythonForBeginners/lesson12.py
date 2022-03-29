def rocket_launch_time(type,distantion):
    if (type=='Циркон'):
        launch_time = 5
        lay_on_course = 20
        speed = 2600

    elif (type=='Гранит'):
        launch_time = 15
        lay_on_course = 35
        speed = 850
    else:
        print ('Неверный тип ракеты.')

    distantion = distantion * 1000
    fly_time = distantion / speed
    fly_time = (fly_time + launch_time + lay_on_course) / 60
    return fly_time

print(str(rocket_launch_time('Циркон', 450)) + ' минут полета до цели')
print(str(rocket_launch_time('Гранит', 450)) + ' минут полета до цели')

text = ' В романе прослеживается также ряд параллелей или даже заимствований из творчества предшественников Оруэлла — прежде всего, романа-антиутопии Евгения Замятина «Мы» (Благодетель — Старший Брат; Единое Государство — Океания; операция по удалению из мозга центра фантазии — промывка мозгов). Английский критик Исаак Дойчер ещё в 1955 году обратил внимание, что Оруэлл «заимствовал идею, сюжет, главных героев, символику и всю атмосферу» замятинского «Мы». В письме Глебу Струве от 17 февраля 1944 года Оруэлл писал: «Вы меня заинтересовали романом „Мы“, о котором я раньше не слышал. Такого рода книги меня очень интересуют, и я даже делаю наброски для подобной книги, которую раньше или позже напишу».'
textUtf = text.strip()
textPrepared = textUtf.split(' ')
print(len(textPrepared))
print(textPrepared)

textPrepared = set(textPrepared)
print(len(textPrepared))
print(textPrepared)
# Now we need to use Regular Expressions to delete all symbols

# let it be Top of the file
import re

s = 'LOLololOLOL/Lol/LOoL/LO/OL/lo'
res1 = re.match('LO', s)
res2 = re.search('ol', s)
res3 = re.findall('ol', s)
res4 = re.split('/', s, maxsplit=2)
res5 = re.sub('olo', 'pish', s)
res6 = re.fullmatch('LO', s)
print(res1,'\n',
      res2,'\n',
      res3,'\n',
      res4,'\n',
      res5,'\n',
      res6,'\n')

s = 'askldhлырв_ ап"№;№(*№+80947508970свыаывапdfIO&^F*(#$HDFJ - --wdfw-e-ethg--egholjlk fg089W42604qqw.'
s1 = 'Уинстон Смит (англ. Winston Smith) — главный герой, 39-летний мужчина. Родился в Лондоне в 1944 или 1945 году — точную дату установить невозможно. С молодых лет работает в Министерстве Правды, в отделе документации: в его обязанности входит внесение уточнений в документы, которые содержат факты, противоречащие партийной пропаганде.'

res1 = re.search(r'с.ы', s)
res2 = re.search(r'\d', s)
res3 = re.search(r'\D', s)
res4 = re.search(r'\d*', s)
res5 = re.search(r'\d{11}', s)
res6 = re.search(r'[4-8]', s)
res7 = re.search(r'[^4-8]', s)
res8 = re.search(r'\d{3}', s)
res9 = re.search(r'\d{3,11}', s)
res10 = re.findall(r'[аеиоуыАЕИОУЫ]\w+', s1)
print(res1,'\n',
      res2,'\n',
      res3,'\n',
      res4,'\n',
      res5,'\n',
      res6,'\n',
      res7,'\n',
      res8,'\n',
      res9,'\n',
      res10,'\n')