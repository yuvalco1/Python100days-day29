import random
from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.append([random.choice(letters) for x in range(nr_letters)])
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list.append([random.choice(symbols) for x in range(nr_symbols)])
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list.append([random.choice(numbers) for x in range(nr_numbers)])
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = [item for sublist in password_list for item in sublist]
    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char

    #print(f"Your password is: {password}")
    password_entry.delete(0, "end")
    password_entry.insert(0, password)

    # add password to clipboard
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    is_ok = messagebox.askokcancel(title=website_entry.get(),
                                   message=f"These are the details entered: \nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\nIs it ok to save?")
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
        else:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# Add image file using canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website:", bg="white", fg="black", font=("Arial", 14, "normal"))
website_label.grid(column=0, row=1, padx=(20, 0))

# email/username label
email_label = Label(text="Email/Username:", bg="white", fg="black", font=("Arial", 14, "normal"))
email_label.grid(column=0, row=2, padx=(20, 0))

# password label
password_label = Label(text="Password:", bg="white", fg="black", font=("Arial", 14, "normal"))
password_label.grid(column=0, row=3, padx=(20, 0))

# website entry
website_entry = Entry(width=35, bg="white", fg="black", font=("Arial", 14, "normal"))
website_entry.grid(column=1, row=1, columnspan=2, padx=(0, 20))
website_entry.focus()

# email/username entry
email_entry = Entry(width=35, bg="white", fg="black", font=("Arial", 14, "normal"))
email_entry.grid(column=1, row=2, columnspan=2, padx=(0, 20))
email_entry.insert(0, "yuvalco1@gmail.com")

# password entry
password_entry = Entry(width=21, bg="white", fg="black", font=("Arial", 14, "normal"))
password_entry.grid(column=1, row=3, padx=(20, 20))

# generate password button
generate_password_btn = Button(text="Generate Password", command=generate_password, bg="white", fg="black",
                               font=("Arial", 14, "normal"))
generate_password_btn.grid(column=2, row=3, padx=(20, 20))

# add button
add_btn = Button(width=36, text="Add", command=save, bg="white", fg="black", font=("Arial", 14, "normal"))
add_btn.grid(column=1, row=4, columnspan=2, padx=(0, 20))

window.mainloop()
