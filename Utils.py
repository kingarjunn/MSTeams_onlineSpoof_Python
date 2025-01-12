import tkinter as tk
def app1(str1):
    r = tk.Tk()
    r.title('Message Window')
    r.geometry("500x250")  # Window size
    r.resizable(False, False)
    text_box = tk.Text(r, wrap="word", height=5, width=50, font=("Arial", 12))
    text_box.pack(padx=10, pady=10)
    button = tk.Button(r, text='ok', width=25, command=r.destroy)
    text_box.insert(tk.END,str(str1))
    button.pack()
    r.mainloop()
