from tkinter import *

import pandas
import pandas as pd
import random


random_word = {}
swedish_to_english = {}
try:
    new_data_file = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("to_learn.csv")
    swedish_to_english = original_data.to_dict('records')
else:
    swedish_to_english = new_data_file.to_dict('records')

# ---------------------------------------------------

def known_word():
    swedish_to_english.remove(random_word)
    next_swedish_word()
    data = pandas.DataFrame(swedish_to_english)
    data.to_csv("data/words_to_learn.csv", index=0)




def next_swedish_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    # the range was changed from len(swedish_to_english)-1 to 1000 to fit the beginner level
    random_rank = random.randint(0, 1000)
    random_word = swedish_to_english[random_rank]
    random_swedish_word = random_word['Swedish']
    canvas.itemconfig(word_text, text=random_swedish_word, fill='black')
    canvas.itemconfig(canvas_image, image=pic)
    canvas.itemconfig(swedish_text, text='Swedish', fill='black')
    if len(random_swedish_word) < 20:
        flip_timer = window.after(5000, func=flip_card)
    else:
        flip_timer = window.after(9000, func=flip_card)


# --------------------------------------
def flip_card():
    canvas.itemconfig(word_text, text=random_word['English'], fill='white')
    canvas.itemconfig(swedish_text, text='English', fill='white')
    canvas.itemconfig(canvas_image, image=flip_pic)


# ---------------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash card project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(5000, func=flip_card)




canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
pic = PhotoImage(file="images/card_front.png")
flip_pic = PhotoImage(file="images/card_back.png")
wrong_pic = PhotoImage(file="images/wrong.png")
right_pic = PhotoImage(file="images/right.png")

canvas_image = canvas.create_image(400, 268, image=pic)
swedish_text = canvas.create_text(400, 150, text="Swedish", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 15, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

known_word_button = Button(image=right_pic, highlightthickness=0, command=known_word)
known_word_button.grid(column=1, row=1)
unknown_word_button = Button(image=wrong_pic, highlightthickness=0, command=next_swedish_word)
unknown_word_button.grid(column=0, row=1)


next_swedish_word()
print(len(swedish_to_english))

window.mainloop()