import tkinter
from tkinter import *
from PIL import Image
import struct
import math

root = Tk()
im = Image.open('../img/map.png', 'r')
#
w_image, h_image = im.size
cv = Canvas(root, height=h_image, width=w_image)
cv.pack()
root.update_idletasks()
cv.update()
value_list = list(im.getdata())

test = True
i = 0
nb_px_box = 0
while test and i < 300:

    if value_list[i] == value_list[i-1] or i == 0:
        nb_px_box += 1
    else:
        test = False
    i += 1
print(nb_px_box)
mid = math.floor(nb_px_box/2)
print(mid)



px = im.load()

for i in range(mid, w_image, nb_px_box+1):
    for j in range(mid, h_image, nb_px_box+1):
        x = px[i, j]
        col = '#{:02x}{:02x}{:02x}'.format(*x)
        cv.create_rectangle(i-mid, j-mid, i+25, j+25, fill=col, width=1)

cv.mainloop()


















def va_te_faire_foutre():
    root = Tk()
    im = Image.open('../img/map.png', 'r')
    w_image, h_image = im.size
    cv = Canvas(root, height=h_image, width=w_image)
    cv.pack()
    root.update_idletasks()
    cv.update()
    px = im.load()

    for i in range(w_image):
        for j in range(h_image):
            x = px[i, j]
            col = '#%02x%02x%02x' % x
            cv.create_rectangle(i, j, i + 2, j + 2, fill=col, width=0)

    cv.mainloop()

va_te_faire_foutre()





