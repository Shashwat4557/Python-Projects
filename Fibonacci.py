import tkinter as tk

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

def generate_fibonacci_sequence():
    try:
        n = int(entry.get())
        if n < 1:
            result_label.config(text="Please enter a positive integer.")
        else:
            fib_sequence = generate_fibonacci(n)
            result_label.config(text=f"Fibonacci Sequence: {fib_sequence}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a positive integer.")


window = tk.Tk()
window.title("Fibonacci Generator")


label = tk.Label(window, text="Enter the number of Fibonacci terms:")
label.pack(pady=10)
entry = tk.Entry(window)
entry.pack()
generate_button = tk.Button(window, text="Generate Fibonacci Sequence", command=generate_fibonacci_sequence)
generate_button.pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack()


window.mainloop()