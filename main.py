import tkinter as tk
import random

def generate_numbers(n=80):
    return [random.randint(0, 9) for _ in range(n)]

def display_numbers(numbers, display_time=10):
    root = tk.Tk()
    root.title("Memorize these numbers")
    root.attributes("-fullscreen", True)  # Set fullscreen mode

    # Create a frame for the timer
    timer_frame = tk.Frame(root)
    timer_frame.pack(pady=20)
    time_label = tk.Label(timer_frame, text=f"Time remaining: {display_time} seconds", font=('Arial', 24))
    time_label.pack()

    # Create a frame for the numbers
    numbers_frame = tk.Frame(root)
    numbers_frame.pack(expand=True)

    for i in range(10):  # 10 rows
        for j in range(8):  # 8 columns
            label = tk.Label(numbers_frame, text=str(numbers[i*8 + j]), font=('Arial', 24), borderwidth=2, relief="solid", width=4, height=2)
            label.grid(row=i, column=j, padx=10, pady=10)

    def update_timer(remaining):
        if remaining > 0:
            time_label.config(text=f"Time remaining: {remaining} seconds")
            root.after(1000, update_timer, remaining - 1)
        else:
            root.destroy()

    update_timer(display_time)
    root.mainloop()

def get_user_input(time_limit=300):
    user_numbers = []

    def on_submit():
        for entry in entries:
            try:
                user_numbers.append(int(entry.get()))
            except ValueError:
                user_numbers.append(-1)  # Placeholder for invalid input
        root.destroy()

    def on_key_press(event, idx):
        if event.char.isdigit():
            next_idx = (idx + 1) % len(entries)
            entries[next_idx].focus_set()
            entries[idx].delete(0, tk.END)
            entries[idx].insert(0, event.char)

    root = tk.Tk()
    root.title("Enter the numbers you remember")
    root.attributes("-fullscreen", True)  # Set fullscreen mode

    # Create a frame for the timer
    timer_frame = tk.Frame(root)
    timer_frame.pack(pady=20)
    time_label = tk.Label(timer_frame, text=f"Time remaining: {time_limit // 60}:{time_limit % 60:02d} minutes", font=('Arial', 24))
    time_label.pack()

    # Create a frame for the entries
    entries_frame = tk.Frame(root)
    entries_frame.pack(expand=True)

    entries = []

    for i in range(10):  # 10 rows
        for j in range(8):  # 8 columns
            entry = tk.Entry(entries_frame, font=('Arial', 24), borderwidth=2, relief="solid", width=4)
            entry.grid(row=i, column=j, padx=10, pady=10)
            entry.bind('<KeyRelease>', lambda event, idx=len(entries): on_key_press(event, idx))
            entries.append(entry)

    submit_button = tk.Button(root, text="Submit", command=on_submit, font=('Arial', 24))
    submit_button.pack(pady=20)

    def update_timer(remaining):
        if remaining > 0:
            time_label.config(text=f"Time remaining: {remaining // 60}:{remaining % 60:02d} minutes")
            root.after(1000, update_timer, remaining - 1)
        else:
            root.destroy()

    update_timer(time_limit)
    root.mainloop()
    return user_numbers

def check_numbers(original_numbers, user_numbers):
    correct_count = 0
    for i in range(len(original_numbers)):
        if original_numbers[i] == user_numbers[i]:
            correct_count += 1
    return correct_count

def memory_game():
    numbers = generate_numbers()
    display_time = 10  # seconds

    display_numbers(numbers, display_time)
    user_numbers = get_user_input(time_limit=300)  # 5 minutes = 300 seconds
    correct_count = check_numbers(numbers, user_numbers)

    print(f"You remembered {correct_count} numbers correctly!")

if __name__ == "__main__":
    memory_game()
