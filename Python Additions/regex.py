import re

regex = r"\b(\d)(\d)\b"
regex2 = r"(\d{2}).(\d{2}).(\d{4})"
regex3 = r"(\d{4})-(\d{2})-(\d{2})"
regex4 = r"(\w)\1\1"

test_str = "12 34 56 78"
test_str2 = "31.1 2.2025"
test_str3 = "2025-12-31"
test_str4 = "aaa bbb ccc xyz"

new_str = re.sub(regex, r'\2\1', test_str)
new_str2 = re.sub(regex2, r'\3.\2.\1', test_str2)
match_list = re.search(regex3, test_str3)
match_list2 = re.search(regex4, test_str4)

print(new_str)
print(new_str2)
print(match_list[1])
print(match_list[2])
print(match_list[3])
print(match_list2[0])

# first word in a string
print(re.findall(f'^\w+', 'AV is largest Analytics community of India'))
# last word in a string
print(re.findall(f'\w+$', 'AV is largest Analytics community of India'))
s = 'По всем вопросам пишите на vasiliy-pupkin@gmail.com, или на secondemail@yandex.ru, отвечу сразу. Или пишите моему ассистенту secretary@gmail.com!'
# emails = re.findall(r'', s)
# print(emails)

print(re.findall(r'\s*(\w*(\w)\2\w*)\s*', 'a aa aaa abab bbbb')[2][0])
print(re.findall(r'(\d{2})', '12:59:59'))

date_list1 = re.findall(r'(\d{2})(\:\d{2}\:)(\d{2})', '12:59:59 12:50:12 09:45:09')
list2 = [''.join(i) for i in date_list1 if i[0] == i[2]]
print(list2)

print(re.findall(r'(\w+)[$@]{1,}(\w+)', 'aaa$@bbb aaa$@$@bbb aaa$@$@$@bbb'))
print(re.search(r'(?P<karman1>\w+)[$@]{1,}(\w+)', 'aaa$@bbb aaa$@$@bbb aaa$@$@$@bbb'))
match = re.search(r'(?P<karman1>\w+)[$@]{1,}(\w+)', 'aaa$@bbb aaa$@$@bbb aaa$@$@$@bbb')
print(match.group('karman1'))
