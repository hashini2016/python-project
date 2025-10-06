from tkinter import *
import random

#fuctions
def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " - turn"))
        elif check_winner() is True:
            label.config(text=(player + " - You are Wins"))
        elif check_winner() == "Try Again":
            label.config(text="Try Again")

def check_winner():
    # Check rows
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            disable_buttons()
            return True

    # Check columns
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            disable_buttons()
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        disable_buttons()
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        disable_buttons()
        return True

    # Check for try
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="pink")
        disable_buttons()
        return "Try Again"

    else:
        return False

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def disable_buttons():
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(state=DISABLED)

def new_game():
    global player

    # Randomly new game ekak start karanna
    player = random.choice(players)
    label.config(text=player + " - turn")

    # Reset the game board setting eka
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0", state=NORMAL)

# box eke size aka, name aka , color aka
window = Tk()
window.title("Tic-Tac-Toe")
window.config(bg='light gray')
window.geometry('520x680+0+0')  # Size
window.resizable(False, False)

# x and 0 i choise this game simbles
players = ["X", "O"]
player = random.choice(players)

#array
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " - turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 15), command=new_game)
reset_button.config(bg="red")
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
        command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()