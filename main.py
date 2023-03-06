from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

window = Tk()
window.title("Password manager")
window.config(padx=80, pady=50)


def generator():
    pass_e.delete(0, END)
    let = []
    for i in range(7):
        let.append(string.ascii_letters[random.randint(0, 46)])
    num = []
    for i in range(3):
        num.append(str(random.randint(0, 9)))
    password = let + num
    random.shuffle(password)
    password = "".join(password)
    pass_e.insert(0, password)
    pyperclip.copy(password)


def find_password():
    flag = 0
    user_search = web_e.get()
    try:
        with open("data.json", "r") as file:
            json_data = json.load(file)
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(message="No data in file")
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found")
    else:
        for key in json_data:
            if user_search.lower() == key.lower():
                flag = 1
                pas = json_data[key]["password"]
                email = json_data[key]["email"]
                messagebox.showinfo(title=user_search,message=f"email : {email}\nPassword : {pas}")
        if flag == 0:
            messagebox.showinfo(message=f"No file {web_e.get()} found")


def write_file():
    web_l = len(web_e.get())
    pass_l = len(pass_e.get())

    if web_l == 0 or pass_l == 0:
        messagebox.showinfo(message="Please dont leave any fields empty")
    else:
        ans = messagebox.askyesno(title=f"{web_e.get()}",
                                  message=f"These are the details \n email : {email_e.get()} \n password : {pass_e.get()} \n do you want to save")
        if ans:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as file:
                    json.dump({web_e.get().lower(): {"email": email_e.get(), "password": pass_e.get()}}, file, indent=4)
            else:
                data.update({web_e.get().lower(): {"email": email_e.get(), "password": pass_e.get()}})
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_e.delete(0, END)
                pass_e.delete(0, END)


canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_t = Label(text="website")
website_t.grid(row=1, column=0)
email_t = Label(text="email/username")
email_t.grid(row=2, column=0)
password_t = Label(text="password")
password_t.grid(row=3, column=0)

web_e = Entry(width=35)
web_e.grid(row=1, column=1, columnspan=2, sticky="EW")
web_e.focus()

email_e = Entry(width=35)
email_e.grid(row=2, column=1, sticky="EW")
email_e.insert(0, "krishnvaibhav.12c1@gmail.com")
#
pass_e = Entry(width=21)
pass_e.grid(row=3, column=1, sticky="EW")

pass_b = Button(text="Generate password", command=generator)
pass_b.grid(row=3, column=2, sticky="EW")

search_b = Button(text="Search", command=find_password)
search_b.grid(row=1, column=2, sticky="EW")

add_b = Button(text="Add", width=36, command=write_file)
add_b.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
