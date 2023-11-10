#Exception Handling
#ข้อผิดพลาด การจัดการ

try :                         #คำสั่งใใช้ในการดักจับ

    nub1 = int(input('ป้อนตัวเลขตัวที่1 :'))
    nub2 = int(input('ป้อนตัวเลขตัวที่2 :'))

    sum = nub1+nub2
    hum = nub1/nub2

    print(f'ผลบวกของ {nub1} + {nub2} คือ {sum}')
    print(f'ผลรวมของ {nub1} / {nub2} คือ {hum}')
except ValueError :
    print('ป้อนด้วยตัวเลขเท่านั้นห้ามตัวอักษร....สงสัยถามตัวเอง')
except ZeroDivisionError :
    print('ป้อนตัวเลขตัวที่2 ห้ามเป็น 0 สงสัยถามตัวเอง')
except Exception : 
    print('มีข้อผิดพลาดเกิดขึ้น ต้องขอโทษนะจ๊ะ ต้องการอะไรถามคอลเซ็นเตอร์ได้เลยนะครับ')

finally :
    print('ฮี้ฮี﹏')
    print('อะปั๊ดชะว๊อกกิ้ง...')