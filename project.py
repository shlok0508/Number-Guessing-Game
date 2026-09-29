import tkinter as tk
import random


# =========================
# GAME VARIABLES
# =========================

secret_number = 0
attempts = 0
guess_history = []
current_min = 1
current_max = 50
game_over = False


# =========================
# COLORS
# =========================

BG = "#07152F"
CARD = "#0D2145"
CARD_2 = "#102B57"
BLUE = "#4DA3FF"
PURPLE = "#8B5CF6"
PINK = "#D946EF"
GREEN = "#22C55E"
YELLOW = "#FACC15"
WHITE = "#F8FAFC"
LIGHT_BLUE = "#B9D7FF"
GRAY = "#7890B5"
RED = "#EF4444"


# =========================
# CREATE WINDOW
# =========================

window = tk.Tk()

window.title("Number Guessing Game")
window.geometry("1000x700")
window.configure(bg=BG)
window.resizable(False, False)


# =========================
# GAME FUNCTIONS
# =========================

def start_game(minimum, maximum):
    global secret_number, attempts, guess_history
    global current_min, current_max, game_over

    current_min = minimum
    current_max = maximum

    secret_number = random.randint(minimum, maximum)

    attempts = 0
    guess_history = []
    game_over = False

    attempts_label.config(text="0")

    result_label.config(
        text="Make your guess!",
        fg=WHITE
    )

    hint_label.config(
        text=f"💡 Hint: The number is between {minimum} and {maximum}."
    )

    guess_entry.delete(0, tk.END)
    guess_entry.config(state="normal")
    guess_button.config(state="normal")

    history_label.config(text="Your guesses:  —")


def check_guess(event=None):

    global attempts, game_over

    if game_over:
        return

    try:
        guess = int(guess_entry.get())
    except ValueError:

        result_label.config(
            text="⚠️ Please enter a number!",
            fg=YELLOW
        )

        guess_entry.delete(0, tk.END)
        return

    # Check range
    if guess < current_min or guess > current_max:

        result_label.config(
            text=f"Enter a number from {current_min} to {current_max}!",
            fg=YELLOW
        )

        guess_entry.delete(0, tk.END)
        return

    # Count attempt
    attempts += 1

    attempts_label.config(text=str(attempts))

    # Add guess to history
    guess_history.append(guess)

    history_text = "Your guesses:  " + "  •  ".join(
        str(number) for number in guess_history
    )

    history_label.config(text=history_text)

    # Compare guess
    if guess < secret_number:

        result_label.config(
            text="Too Low! ⬆️",
            fg=BLUE
        )

        hint_label.config(
            text="💡 Try a bigger number!"
        )

    elif guess > secret_number:

        result_label.config(
            text="Too High! ⬇️",
            fg=PINK
        )

        hint_label.config(
            text="💡 Try a smaller number!"
        )

    else:

        game_over = True

        result_label.config(
            text=f"🎉 You got it! The number was {secret_number}",
            fg=GREEN
        )

        hint_label.config(
            text=f"🏆 You found it in {attempts} attempts!"
        )

        guess_entry.config(state="disabled")
        guess_button.config(state="disabled")

    guess_entry.delete(0, tk.END)


def restart_game():
    start_game(current_min, current_max)


def choose_easy():
    start_game(1, 50)
    easy_button.config(bg=GREEN)
    medium_button.config(bg=CARD_2)
    hard_button.config(bg=CARD_2)


def choose_medium():
    start_game(1, 100)
    easy_button.config(bg=CARD_2)
    medium_button.config(bg=GREEN)
    hard_button.config(bg=CARD_2)


def choose_hard():
    start_game(1, 500)
    easy_button.config(bg=CARD_2)
    medium_button.config(bg=CARD_2)
    hard_button.config(bg=GREEN)


# =========================
# TOP TITLE
# =========================

title_frame = tk.Frame(
    window,
    bg=BG
)

title_frame.pack(pady=(25, 5))


title_label = tk.Label(
    title_frame,
    text="🎯  Number Guessing",
    font=("Arial", 30, "bold"),
    fg=WHITE,
    bg=BG
)

title_label.pack()


game_label = tk.Label(
    title_frame,
    text="GAME",
    font=("Arial", 30, "bold"),
    fg=YELLOW,
    bg=BG
)

game_label.pack()


subtitle_label = tk.Label(
    window,
    text="Think you can guess the secret number?",
    font=("Arial", 13),
    fg=LIGHT_BLUE,
    bg=BG
)

subtitle_label.pack(pady=(0, 20))


# =========================
# MAIN AREA
# =========================

main_frame = tk.Frame(
    window,
    bg=BG
)

main_frame.pack()


# =========================
# LEFT SIDE
# =========================

left_frame = tk.Frame(
    main_frame,
    bg=CARD,
    width=650,
    height=430
)

left_frame.pack(side="left", padx=(25, 10))
left_frame.pack_propagate(False)


# Difficulty title

difficulty_label = tk.Label(
    left_frame,
    text="Choose Difficulty",
    font=("Arial", 15, "bold"),
    fg=WHITE,
    bg=CARD
)

difficulty_label.pack(pady=(25, 10))


# Difficulty buttons

difficulty_frame = tk.Frame(
    left_frame,
    bg=CARD
)

difficulty_frame.pack()


easy_button = tk.Button(
    difficulty_frame,
    text="EASY\n1 - 50",
    font=("Arial", 11, "bold"),
    fg=WHITE,
    bg=GREEN,
    activebackground=GREEN,
    activeforeground=WHITE,
    relief="flat",
    width=12,
    height=2,
    command=choose_easy,
    cursor="hand2"
)

easy_button.pack(side="left", padx=5)


medium_button = tk.Button(
    difficulty_frame,
    text="MEDIUM\n1 - 100",
    font=("Arial", 11, "bold"),
    fg=WHITE,
    bg=CARD_2,
    activebackground=GREEN,
    activeforeground=WHITE,
    relief="flat",
    width=12,
    height=2,
    command=choose_medium,
    cursor="hand2"
)

medium_button.pack(side="left", padx=5)


hard_button = tk.Button(
    difficulty_frame,
    text="HARD\n1 - 500",
    font=("Arial", 11, "bold"),
    fg=WHITE,
    bg=CARD_2,
    activebackground=GREEN,
    activeforeground=WHITE,
    relief="flat",
    width=12,
    height=2,
    command=choose_hard,
    cursor="hand2"
)

hard_button.pack(side="left", padx=5)


# Guess section

guess_title = tk.Label(
    left_frame,
    text="Enter Your Guess",
    font=("Arial", 19, "bold"),
    fg=WHITE,
    bg=CARD
)

guess_title.pack(pady=(35, 15))


# Input box

guess_entry = tk.Entry(
    left_frame,
    font=("Arial", 20),
    justify="center",
    width=18,
    bg="#091B3A",
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)

guess_entry.pack(ipady=10)


# Guess button

guess_button = tk.Button(
    left_frame,
    text="▶   GUESS",
    font=("Arial", 14, "bold"),
    fg=WHITE,
    bg=PURPLE,
    activebackground=PINK,
    activeforeground=WHITE,
    relief="flat",
    width=25,
    height=2,
    command=check_guess,
    cursor="hand2"
)

guess_button.pack(pady=18)


# Result

result_label = tk.Label(
    left_frame,
    text="Make your guess!",
    font=("Arial", 16, "bold"),
    fg=WHITE,
    bg=CARD
)

result_label.pack(pady=5)


# Hint

hint_label = tk.Label(
    left_frame,
    text="💡 Hint: The number is between 1 and 50.",
    font=("Arial", 11),
    fg=YELLOW,
    bg=CARD
)

hint_label.pack(pady=10)


# History

history_label = tk.Label(
    left_frame,
    text="Your guesses:  —",
    font=("Arial", 10),
    fg=GRAY,
    bg=CARD
)

history_label.pack(pady=5)


# =========================
# RIGHT SIDE
# =========================

right_frame = tk.Frame(
    main_frame,
    bg=CARD,
    width=250,
    height=430
)

right_frame.pack(side="right", padx=(10, 25))
right_frame.pack_propagate(False)


# Attempts

attempts_title = tk.Label(
    right_frame,
    text="🏆  ATTEMPTS",
    font=("Arial", 15, "bold"),
    fg=YELLOW,
    bg=CARD
)

attempts_title.pack(pady=(30, 5))


attempts_label = tk.Label(
    right_frame,
    text="0",
    font=("Arial", 42, "bold"),
    fg=GREEN,
    bg=CARD
)

attempts_label.pack()


attempts_text = tk.Label(
    right_frame,
    text="Attempts",
    font=("Arial", 11),
    fg=GRAY,
    bg=CARD
)

attempts_text.pack(pady=(0, 25))


# Target

target_label = tk.Label(
    right_frame,
    text="🎯",
    font=("Arial", 55),
    bg=CARD
)

target_label.pack()


good_luck = tk.Label(
    right_frame,
    text="Good Luck!",
    font=("Arial", 20, "bold"),
    fg=YELLOW,
    bg=CARD
)

good_luck.pack(pady=5)


message = tk.Label(
    right_frame,
    text="You can do it!",
    font=("Arial", 12),
    fg=LIGHT_BLUE,
    bg=CARD
)

message.pack()


# =========================
# RESTART BUTTON
# =========================

restart_button = tk.Button(
    window,
    text="↻   RESTART GAME",
    font=("Arial", 13, "bold"),
    fg=WHITE,
    bg=CARD_2,
    activebackground=PURPLE,
    activeforeground=WHITE,
    relief="flat",
    width=25,
    height=2,
    command=restart_game,
    cursor="hand2"
)

restart_button.pack(pady=20)


# =========================
# ENTER KEY
# =========================

window.bind("<Return>", check_guess)


# =========================
# START GAME
# =========================

start_game(1, 50)


# Put cursor inside input box
guess_entry.focus()


# Start program
window.mainloop()