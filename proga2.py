import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os
import pytesseract
import re
import pyautogui as pg

def finding2(x2,y2):
 filename = 'image.png'
 x=1
 last_time = time.time()
 while(True):
     screen=np.array(ImageGrab.grab(bbox=(x2-200,y2+50,x2-15,y2+65)))
# Делаем скриншот (левой) области с текстом "ПК: Намайнено"
# x1 y1 - координаты курсора "+" - прибавление координат(можно настроить самому
# СНАЧАЛА ЛЕВЫЕ ВЕРХНИЕ, ПОТОМ НИЖНИЕ ПРАВЫЕ) для образования прмоугольника
     cv2.imwrite(filename,screen)
     x=x+1
     if x==2:
         cv2.destroyAllWindows()
         break
 img = cv2.imread('image.png')
 text = pytesseract.image_to_string(img) #получаем текст со скрина
 print(text)
 return text

def finding(x1,y1):
 filename = 'image.png'
 x=1
 last_time = time.time()
 while(True):
     screen=np.array(ImageGrab.grab(bbox=(x1+40,y1+48,x1+230,y1+66)))
# Делаем скриншот области с текстом "ПК: Намайнено"
# x1 y1 - координаты курсора "+" - прибавление координат(можно настроить самому)
# для образования прмоугольника
     cv2.imwrite(filename,screen)
     x=x+1
     if x==2:
         cv2.destroyAllWindows()
         break
 img = cv2.imread('image.png')
 text = pytesseract.image_to_string(img) #получаем текст со скрина
 return text
def c_find():
 i=0
 a=0
 b=0
 string = str(pg.position())
 while string[i]!='x':
     i+=1
 i+=2
 while string[i]!=',':
         a=a*10+int(string[i])
         i+=1
 i+=2
 if string[i]=='y':
         i+=2
         while string[i]!=')':
              b=b*10+int(string[i])
              i+=1
 s_f=str(finding(a,b)) 
 print(s_f)
 c=''
 i=s_f.find(':')
 print(i)
 if i==':':
  while s_f[i]!='0' or s_f[i]!='1' or s_f[i]!='2' or s_f[i]!='3' or s_f[i]!='4' or s_f[i]!='5' or s_f[i]!='6' or s_f[i]!='7' or s_f[i]!='8' or s_f[i]!='9':
      i+=1
  count_d=0
  while s_f[i]=='.' or s_f[i]=='0' or s_f[i]=='1' or s_f[i]=='2' or s_f[i]=='3' or s_f[i]=='4' or s_f[i]=='5' or s_f[i]=='6' or s_f[i]=='7' or s_f[i]=='8' or s_f[i]=='9':
      if s_f[i]=='.':
          count_d+=1
      if count_d==2:
          break
      c+=s_f[i]
      i+=1
  print(c)
  c=float(c)
  return c
 else:
     w='corrupted screenshot'
     s_f=str(finding2(a,b)) 
     c=''
     i=s_f.find(':')
     #print(s_f)
     if s_f[i]==':':
         i+=2
         count_d=0
         while s_f[i]=='.' or s_f[i]=='0' or s_f[i]=='1' or s_f[i]=='2' or s_f[i]=='3' or s_f[i]=='4' or s_f[i]=='5' or s_f[i]=='6' or s_f[i]=='7' or s_f[i]=='8' or s_f[i]=='9':
             if s_f[i]=='.':
                 count_d+=1
             if count_d==2:
                 break
             c+=s_f[i]
             i+=1
         c=float(c)
         return c
print('5seconds') 
time.sleep(5)
s=float(0)
c_m=float(0)
while(True):
    c_n=float(c_find())
    print(c_n,c_m, c_n != c_m)
    if c_n != c_m:
        s+=c_n
    c_m=c_n
    print('c_m',c_m)
    print('Сатоши = ',s)
    print()
    print()
    print()
    pg.move(1, 0)

