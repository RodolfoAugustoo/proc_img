import cv2
from PIL import Image, ImageDraw, ImageFont
from glob import os, glob

src = ('images/')

pic = ( src + '/1.jpeg')
pic_list = glob(src + '/*.jpeg')
pic_list = pic_list + glob(src + '/*jpeg')

font = cv2.FONT_HERSHEY_COMPLEX

while (cv2.waitKeyEx(5000) != ord('q') and cv2.waitKeyEx(5000) != ord('Q')):
     for i in pic_list :                
          if(cv2.waitKeyEx(5000) == ord('q') or cv2.waitKeyEx(5000) == ord('Q')): 
               break               
          pic = Image.open(i)
          height , width = 512, 512
          pic = pic.resize(
               (round(height),
               round(width)),
               Image.ANTIALIAS)

          pic.save(i, format = 'jpeg')                                
          show_pic = cv2.imread(i)
          text = '{}'.format(i)
          cv2.putText(show_pic,text,(int(512/5), int(50)),font,1,(255,0,255),3)                        
          margin = cv2.copyMakeBorder(show_pic,40,10,10,10,cv2.BORDER_CONSTANT,value=[255,255,255])
          cv2.imshow('Margin',margin)
          cv2.waitKey(5000)