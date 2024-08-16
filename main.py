from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

french_words = pd.read_csv("data/french_words.csv")
french_words_dict = french_words.to_dict(orient="records")
to_learn = french_words.to_dict(orient="records")


def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(french_words_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_word)
    next_word()


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_pic = PhotoImage(file="images/right.png")
wrong_pic = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

unknown_button = Button(image=wrong_pic, bg=BACKGROUND_COLOR, command=next_word)
unknown_button.grid(row=1, column=1)
known_button = Button(image=right_pic, bg=BACKGROUND_COLOR, command=next_word)
known_button.grid(row=1, column=0)

next_word()

window.mainloop()
