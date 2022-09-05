import random
from tkinter import * 
from tkinter import messagebox

#main function
def generator():
    up =  ["A", "B", "C", "D", "E", "F", "G",
            "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S",
            "T", "U", "V", "W", "X", "Y",
            "Z"]

    low = [char.lower() for char in up]

    num = ["0", "1", "2", "3", "4",
            "5", "6", "7", "8", "9"
            ]

    spec = ["~", "@", "#", "$", "%",
            "^", "&", "*", "(", ")"
            ]
    #takes the lists of all char and adds together
    total_list = up + low + num + spec

    #saves a random choice of each list in a var string
    ran_up = random.choice(up)
    ran_low = random.choice(low)
    ran_num = random.choice(num)
    ran_spec = random.choice(spec)

    #saves the random choices in a var string
    temp_pass = ran_up + ran_low + ran_num + ran_spec
    #loops through temp_pass and adds it with random choice of total_list to make password less predictable
    for i in range(8):
        temp_pass = temp_pass + random.choice(total_list)
        temp_pass_list = [char for char in temp_pass]
        random.shuffle(temp_pass_list)
        final_pass = " "
        for char in temp_pass_list:
        	final_pass = final_pass + char

    #changes the label text to display the password string
    final_pass_lbl["text"] = f"This is your randomly generated password: {final_pass}"
    final_pass_lbl.pack(pady=20, padx=20)
    


app = Tk()
app.title("Password Generator ")
app.geometry("850x500")

generator_btn = Button(app, text="Generate your password", width=25, command=generator)
generator_btn.pack(pady=20)


final_pass_lbl = Label(app, text= " ", font=("bold", 20))

app.mainloop()
