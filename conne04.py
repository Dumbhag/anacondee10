#File Handling
#การจัดการไฟล์
#คือการทำงานกับไฟล์
#การเปิดไฟล์ write (w)/ extend (x)/ read (r) apppend (a)

f_uwu = open('uwu4.txt','a',encoding='utf-8')

f_uwu.write('HeHe..')
f_uwu.write('HooHoo..\n')
f_uwu.write('crispyPorkrice\n')

f_uwu.close()