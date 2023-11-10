#File Handling
#การจัดการไฟล์
#คือการทำงานกับไฟล์
#การเปิดไฟล์ write (w)/ extend (x)/ read (r) apppend (a)

try:
    f_uwu = open('uwu3.txt','r',encoding='utf-8')

    f_uwu.write('HeHe..')
    f_uwu.write('HooHoo..\n')
    f_uwu.write('crispyPorkrice\n')

    f_uwu.close()
except FileExistsError :
    print('เปลี่ยนชื่อใหม่ชื่อนี้มีแล้ว')