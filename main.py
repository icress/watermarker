import PIL.Image
from PIL import ImageDraw, ImageFont
from tkinter import *
from tkinter.filedialog import askopenfilename

filename: str = ''

window = Tk()
window.geometry("700x350")
window.config(padx=130, pady=50)
window.title('Watermarker')

title = Label(text='Welcome to the Image Watermarker!', justify='left', font=('Arial', 20))
title.config(pady=30)
title.grid(columnspan=2, column=0, row=0)
label = Label(text="What would you like your watermark to say?")
label.grid(column=0, row=1)
label.config(padx=5, pady=10)
watermark = Entry()
watermark.grid(column=1, row=1)


def open_img():
    global filename
    filename = askopenfilename()
    show_filename = filename.split('/')[-1]
    file_label = Label(text=show_filename)
    file_label.grid(column=1, row=3)
    return filename


def open_file():
    try:
        global filename
        watermark_text = watermark.get()
        if watermark_text == '':
            water_error = Label(text='Please provide a watermark', fg='red')
            water_error.grid(columnspan=2, column=0, row=6)
        else:
            with PIL.Image.open(filename).convert("RGBA") as img:
                txt = PIL.Image.new(mode='RGBA', size=img.size)
                fnt = ImageFont.truetype("arial.ttf", 100)
                draw = PIL.ImageDraw.Draw(txt)
                draw.text((img.size[0]/12, img.size[1]/1.15), watermark_text, font=fnt, fill=(255, 255, 255, 128))
                output = PIL.Image.alpha_composite(img, txt)
                output.show()
    except AttributeError:
        error_label = Label(text='Please select a file', fg='red')
        error_label.grid(columnspan=2, column=0, row=5)


label_b = Label(text='What picture do you want to mark?')
label_b.grid(column=0, row=2)
browse = Button(text='Browse', command=open_img)
browse.grid(column=1, row=2)

label_f = Label(text='File name: ', justify='left')
label_f.grid(column=0, row=3)
label_f.config(pady=10)
submit = Button(text='Submit', command=open_file)
submit.config(width=30)
submit.grid(columnspan=2, row=4)

window.mainloop()
