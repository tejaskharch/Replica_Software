import tkinter as tk
from PIL import Image , ImageTk

root = tk.Tk()
root.title("Financial Management")
root.geometry("1950x1080")

title_bar = tk.Frame(root, bg="white", height=30)
title_bar.pack(fill=tk.X)

back_button = tk.Button(title_bar, text="◁", bg="white", relief=tk.FLAT, command=root.destroy)
back_button.pack(side=tk.LEFT, padx=5)

title_label = tk.Label(title_bar, text="Financial Management", bg="white", font=("Helvetica", 12))
title_label.pack(side=tk.LEFT, padx=5)

specs_button = tk.Button(title_bar, text="🛈", bg="white", relief=tk.FLAT, command=lambda: print("Specs clicked"))
specs_button.pack(side=tk.LEFT, padx=5)

menu_button = tk.Button(title_bar, text="...", bg="white", relief=tk.FLAT, command=lambda: print("Menu clicked"))
menu_button.pack(side=tk.RIGHT, padx=5)

content_frame = tk.Frame(root)
content_frame.pack(fill=tk.BOTH, expand=True)

p1=Image.open("C:\Users\tejas\Desktop\task\p1.png")
rp1=p1.resize((35,7),Image.ANTIALIAS)
rrp1=ImageTk.PhotoImage(rp1)
p2=Image.open("C:\Users\tejas\Desktop\task\p2.png")
rp2=p2.resize((35,7),Image.ANTIALIAS)
rrp2=ImageTk.PhotoImage(rp2)
p3=Image.open("C:\Users\tejas\Desktop\task\p3.png")
rp3=p3.resize((35,7),Image.ANTIALIAS)
rrp3=ImageTk.PhotoImage(rp3)
p4=Image.open("C:\Users\tejas\Desktop\task\p4.png")
rp4=p4.resize((35,7),Image.ANTIALIAS)
rrp4=ImageTk.PhotoImage(rp4)
p5=Image.open("C:\Users\tejas\Desktop\task\p5.png")
rp5=p5.resize((35,15),Image.ANTIALIAS)
rrp5=ImageTk.PhotoImage(rp5)
p6=Image.open("C:\Users\tejas\Desktop\task\p6.png")
rp6=p6.resize((35,15),Image.ANTIALIAS)
rrp6=ImageTk.PhotoImage(rp6)
p7=Image.open("C:\Users\tejas\Desktop\task\p7.png")
rp7=p7.resize((35,15),Image.ANTIALIAS)
rrp7=ImageTk.PhotoImage(rp7)
p8=Image.open("C:\Users\tejas\Desktop\task\p8.png")
rp8=p8.resize((35,15),Image.ANTIALIAS)
rrp8=ImageTk.PhotoImage(rp8)
p9=Image.open("C:\Users\tejas\Desktop\task\p9.png")
rp9=p9.resize((60,24),Image.ANTIALIAS)
rrp9=ImageTk.PhotoImage(rp9)
p10=Image.open("C:\Users\tejas\Desktop\task\p10.png")
rp10=p10.resize((100,24),Image.ANTIALIAS)
rrp10=ImageTk.PhotoImage(rp10)
p11=Image.open("C:\Users\tejas\Desktop\task\p11.png")
rp11=p11.resize((10,24),Image.ANTIALIAS)
rrp11=ImageTk.PhotoImage(rp11)

box1 = tk.Label(content_frame, text="Total Accounts Receivable" , width=35, height=7, relief=tk.FLAT, bg="white")
box2 = tk.Label(content_frame, text="Total Account Payable", width=35, height=7, relief=tk.FLAT, bg="white")
box3 = tk.Label(content_frame, text="Equity Ratio", width=35, height=7, relief=tk.FLAT, bg="white")
box4 = tk.Label(content_frame, text="Debt Equity", width=35, height=7, relief=tk.FLAT, bg="white")

box1.grid(row=0, column=0, padx=10, pady=10)
box2.grid(row=0, column=1, padx=10, pady=10)
box3.grid(row=0, column=2, padx=10, pady=10)
box4.grid(row=0, column=3, padx=10, pady=10)

box5 = tk.Label(content_frame,image=rrp1, text="Square Box 1", width=35, height=15, relief=tk.FLAT, bg="white")
box6 = tk.Label(content_frame, text="Square Box 2", width=35, height=15, relief=tk.FLAT, bg="white")
box7 = tk.Label(content_frame, text="Square Box 3", width=35, height=15, relief=tk.FLAT, bg="white")
box8 = tk.Label(content_frame, text="Square Box 4", width=35, height=15, relief=tk.FLAT, bg="white")

box5.grid(row=1, column=0, padx=10, pady=10)
box6.grid(row=1, column=1, padx=10, pady=10)
box7.grid(row=1, column=2, padx=10, pady=10)
box8.grid(row=1, column=3, padx=10, pady=10)

box9 = tk.Label(content_frame, text="Square Box 9", width=60, height=24, relief=tk.FLAT, bg="white")
box9.grid(row=0, column=4, rowspan=2, padx=10, pady=10)
box10 = tk.Label(content_frame, text="Square Box 9", width=100, height=24, relief=tk.FLAT, bg="white")
box10.grid(row=2,column=0,columnspan=3, rowspan=2, padx=5, pady=5)

box11 = tk.Label(content_frame, text="Square Box 9", width=100, height=24, relief=tk.FLAT, bg="white")
box11.grid(row=2,column=2,columnspan=3, rowspan=2, padx=5, pady=5)

root.mainloop()


