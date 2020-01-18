import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 270,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Find Percent of Melting Point')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Melting Point (C):')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 75, window=label2)

entryT = tk.Entry (root)
canvas1.create_window(200, 100, window=entryT)
entryT.focus_set()

label3 = tk.Label(root, text='% of temperature:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200,125, window=label3)

v = tk.StringVar(root, value='40')
entryPercent = tk.Entry (root, textvariable=v)
canvas1.create_window(200,150, window=entryPercent)

label4 = tk.Label(root, text = '', font=('helvetica', 14, 'bold'))
canvas1.create_window(200, 275, window=label4)


# Label(master, textvariable=output_T).pack()


lbl = tk.StringVar()
lbl.set('')
tk.Label(root, textvariable=lbl,font=('helvetica', 20) ).pack()
# tk.Button(root, text="Get Time", command=callback).pack()



def convert ():
    input_T = entryT.get()
    percent = entryPercent.get()
    input_T_K = float(input_T) +273.15
    output_T_K = float(percent)*float(input_T_K)*.01
    output_T = float(output_T_K) - 273.15

    label3 = tk.Label(root, text= percent + '% of ' + input_T + ' is (in C):', font=('helvetica', 10))
    canvas1.create_window(200, 250, window=label3)


    # label4.set(str(output_T))
    lbl.set(str(output_T))

button1 = tk.Button(text='Calculate', command=convert, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 205, window=button1)

def oneclick(event):
    convert()

root.bind('<Return>', oneclick)

root.mainloop()
