import tkinter
from tkinter import *
from PIL import Image
import struct
import math

root = Tk()
im = Image.open('../img/srcMAP.png', 'r').convert('RGB')
#
w_image, h_image = im.size
cv = Canvas(root, height=960, width=960)
cv.pack()
root.update_idletasks()
cv.update()
value_list = list(im.getdata())
px = im.load()


palette = ['#5741b0', '#6da6b7', '#ec1c1a', '#ee8438', '#a0be0e', '#1e736e', '#5bc944']
print('route: ', '#{:02x}{:02x}{:02x}'.format(*px[36,8]), ' / vide : ', '#{:02x}{:02x}{:02x}'.format(*px[0,0]))

print('#{:02x}{:02x}{:02x}'.format(*px[5,24]), ' / vide : ', '#{:02x}{:02x}{:02x}'.format(*px[5,25]))
pal = ['#efe4c6', '#b17578']
i = 0
j = 0
ix = 0
iy = 0
while i < h_image:
    j = 0
    ix = 0
    while j < w_image:
        x = px[i, j]
        col = '#{:02x}{:02x}{:02x}'.format(*x)
        if col in palette:
            cv.create_rectangle(iy, ix, iy+20, ix+20, fill=col, width=1, outline='#0b181c')
        else:
            cv.create_rectangle(iy, ix, iy+20, ix+20, fill=col, width=1, outline='#967979')

        j += 1
        ix += 20
    i += 1
    iy += 20



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

#va_te_faire_foutre()





