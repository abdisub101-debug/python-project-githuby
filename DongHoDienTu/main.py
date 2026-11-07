import tkinter
import time

window = tkinter.Tk()
print(dir(window))
label = tkinter.Label (window, bg='white', fg='black', font=('DJB Get Digital', 150))
label.pack()
window.title("Đồng Hồ Điện Tử")
window.geometry("600x200")
while True:
    tgain = time.strftime("%H:%M:%S")
    label.config(text=tgain)
    window.update()
