print('Create txt - "w"')
txt_file = open('readme0.txt', 'w', encoding='utf-8')

txt_file.write('Lorem Impsum\n')
txt_file.write('String two\nString three')
txt_file.close()

#again this file but another method
txt_file = open('readme0.txt', 'w', encoding='utf-8')
lines = ['String one\n','String two\n','String three']
txt_file.writelines(lines)
txt_file.close()

txt_file = open('readme1.txt', 'w', encoding='utf-8')
lines = ('String one\n','String two\n','String three')
txt_file.writelines(lines)
txt_file.close()

txt_file = open('readme2.txt', 'w', encoding='utf-8')
lines = {'String one\n','String two\n','String three'}
txt_file.writelines(lines)
txt_file.close()

txt_file = open('readme3.txt', 'w', encoding='utf-8')
lines = {'String one':'String 1\n','String two':'String 2\n','String three':'String 3\n'}
txt_file.writelines(lines)
txt_file.close()

#TypeError: write() argument must be str, not list
# txt_file = open('readme5.txt', 'w', encoding='utf-8')
# lines = ['String one\n','String two\n','String three',['Str4','Str5']]
# txt_file.writelines(lines)
# txt_file.close()
txt_file_all = []
for i in range(4):
    txt_file = open(f'readme{i}.txt', 'r', encoding='utf-8')
    info = txt_file.read()
    txt_file_all.append(info)
    txt_file.close()

print(txt_file_all)