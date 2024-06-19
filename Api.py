import tkinter as tk
from tkinter import Message, Text
import cv2
import random
import numpy as np
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.font as font


IMG_WIDTH = 1200
IMG_HEIGHT = 800
WATERMARK_WIDTH = 256
WATERMARK_HEIGHT = 256

IMG_SIZE = IMG_HEIGHT * IMG_WIDTH
WATERMARK_SIZE = WATERMARK_HEIGHT * WATERMARK_WIDTH

KEY = 1001
THRESH = 75


window = tk.Tk() 
window.title("Invisible Digital Water Marking")
window.configure(background ='Turquoise')
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)
message = tk.Label(
    window, text ="<<***Invisible Digital Water Marking***>>", 
    bg ="pink", fg = "black", width = 50, 
    height = 3, font = ('times', 30, 'bold')) 
      
message.place(x = 200, y = 20)
  

  
def owner_gen():
    def xor(x ,y): 
        if x == 0 and y == 0:
            return 0
        elif x == 0 and y != 0:
            return 255
        elif x != 0 and y == 0:
            return 255
        elif x !=0 and y != 0:
            return 0
    

    def mean_neighbour(img, x, y):
        val = 0
        num = 0
        i = x
        j = y
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x + 1
        j = y + 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x - 1
        j = y - 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x + 1
        j = y
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x
        j = y + 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x + 1
        j = y - 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x - 1
        j = y + 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x - 1
        j = y
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x
        j = y - 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
    
        return val/float(num)
    
    og_img = cv2.imread('images\original_image.jpg',0)
    watermark_img = cv2.imread('images\watermark.jpg', 0)
    ret,watermark_img = cv2.threshold(watermark_img,127,255,cv2.THRESH_BINARY)

    master_img = np.zeros((WATERMARK_WIDTH, WATERMARK_HEIGHT, 1), np.uint8)
    owner_img = np.zeros((WATERMARK_WIDTH, WATERMARK_HEIGHT, 1), np.uint8)

    random.seed(a=KEY)
    random_points = random.sample(range(IMG_SIZE), WATERMARK_SIZE)

    i = 0
    j = 0

    for k in random_points:
        x = int(k / IMG_WIDTH)
        y = int(k % IMG_WIDTH)
        if mean_neighbour(og_img, x, y) > THRESH:
            master_img[i,j] = 255
        j += 1
        if j == 256:
            j = 0
            i += 1

    for i in range(0, WATERMARK_HEIGHT):
        for j in range(0, WATERMARK_WIDTH):
            owner_img[i, j] = xor(master_img[i, j], watermark_img[i, j])

    cv2.imshow('M', master_img)
    cv2.imshow('O', owner_img)
    cv2.imwrite('images\master_img.jpg', master_img)
    cv2.imwrite('images\owner_img.jpg', owner_img)
    cv2.waitKey(0)


    
def mastere():
    def mean_neighbour(img, x, y):
        val = 0
        num = 0
        i = x
        j = y
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x + 1
        j = y + 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x - 1
        j = y - 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x + 1
        j = y
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x
        j = y + 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x + 1
        j = y - 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x - 1
        j = y + 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x - 1
        j = y
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
        i = x
        j = y - 1
        if i >= 0 and i < IMG_HEIGHT and j >= 0 and j < IMG_WIDTH:
            val += img[i, j]
            num += 1
    
        return val/float(num)

    random.seed(a=KEY)
    random_points = random.sample(range(IMG_SIZE), WATERMARK_SIZE)

    for cnt in range(0, 7):
        og_img = cv2.imread('images\stolen_images\stolen_image_'+str(cnt)+'.jpg',0)

        master_img = np.zeros((WATERMARK_WIDTH, WATERMARK_HEIGHT, 1), np.uint8)


        i = 0
        j = 0

        for k in random_points:
            x = int(k / IMG_WIDTH)
            y = int(k % IMG_WIDTH)
            if mean_neighbour(og_img, x, y) > THRESH:
                master_img[i,j] = 255
            j += 1
            if j == 256:
                j = 0
                i += 1

        cv2.imwrite('images\master_images\master_img_'+str(cnt)+'.jpg', master_img)
        #print(cnt)

    print("Visit Master images folder")
    


def ex():
    def xor(x ,y):
        if x == 0 and y == 0:
            return 0
        elif x == 0 and y != 0:
            return 255
        elif x != 0 and y == 0:
            return 255
        elif x !=0 and y != 0:
            return 0

    random.seed(a=KEY)
    random_points = random.sample(range(IMG_SIZE), WATERMARK_SIZE)

    owner_img = cv2.imread('images\owner_img.jpg', 0)

    for k in range(0, 7):
        master_img = cv2.imread('images\master_images\master_img_'+str(k)+'.jpg', 0)
        watermark_img = np.zeros((WATERMARK_WIDTH, WATERMARK_HEIGHT, 1), np.uint8)

        i = 0
        j = 0

        for i in range(0, WATERMARK_HEIGHT):
            for j in range(0, WATERMARK_WIDTH):
                watermark_img[i, j] = xor(master_img[i, j], owner_img[i, j])

        watermark_img = (255-watermark_img)
        kernel = np.ones((4,4),np.uint8)
        watermark_img = cv2.medianBlur(watermark_img, 3)
        watermark_img = cv2.morphologyEx(watermark_img, cv2.MORPH_OPEN, kernel)
        watermark_img = cv2.morphologyEx(watermark_img, cv2.MORPH_CLOSE, kernel)
        watermark_img = (255-watermark_img)

        cv2.imwrite('images\\regenerated_watermarks\\watermark_img_'+str(k)+'.jpg', watermark_img)
        #print(k)
    print("Visit Regenerated Watermark folder")

        
def mat():
    template = cv2.imread('images\watermark.jpg', 0)
    print("Accuracy Match")
    for k in range(0, 7):
        img_gray = cv2.imread('images\\regenerated_watermarks\\watermark_img_'+str(k)+'.jpg', 0)
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        print(res)
	
   
        
a = tk.Button(window, text ="Input", 
command = owner_gen, fg ="white", bg ="blue", 
width = 20, height = 3, activebackground = "red", 
font =('times', 15, ' bold '))
a.place(x = 400, y = 200)

b = tk.Button(window, text ="Master", 
command = mastere, fg ="white", bg ="blue", 
width = 20, height = 3, activebackground = "red", 
font =('times', 15, ' bold '))
b.place(x = 500, y = 300)


c = tk.Button(window, text ="Extract", 
command = ex, fg ="white", bg ="blue", 
width = 20, height = 3, activebackground = "red", 
font =('times', 15, ' bold '))
c.place(x = 600, y = 400)

d = tk.Button(window, text ="MatchTemplate", 
command = mat, fg ="white", bg ="blue", 
width = 20, height = 3, activebackground = "red", 
font =('times', 15, ' bold '))
d.place(x = 700, y = 500)


quitWindow = tk.Button(window, text ="Quit", 
command = window.destroy, fg ="white", bg ="blue", 
width = 20, height = 3, activebackground = "Red", 
font =('times', 15, ' bold '))
quitWindow.place(x = 800, y = 600)


  
   
window.mainloop()
