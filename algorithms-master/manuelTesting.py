import tkinter as tk
from tkinter import ttk

# import your algorithms here:
from algorithms import maths


class AlgorithmTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Tester")

        # choose the algorithm to test

        # create a label and entry for the input data
        input_label = ttk.Label(root, text="Enter input data:")
        input_label.grid(row=0,rowspan=2, column=0)
        self.input_entry = ttk.Entry(root)
        self.input_entry.grid(row=0, column=1)

        # create a button to run the num_digits algorithm
        dfs_button = ttk.Button(root, text="Test Number of Digits", command=self.runNumberOfDigits)
        dfs_button.grid(row=2, column=0)

        # create a button to run the factorial algorithm
        bfs_button = ttk.Button(root, text="Test Factorial", command=self.runFactorial)
        bfs_button.grid(row=2, column=1)

         # create a button to run the perfectsquare algorithm
        bfs_button = ttk.Button(root, text="Test perfect Squares", command=self.runPerfectSquares)
        bfs_button.grid(row=2, column=2)

        # create a text box to display the output
        self.output_text = tk.Text(root, height=20, width=40, )
        self.output_text.grid(row=3, column=0,columnspan=3)

    def runNumberOfDigits(self):
        input_data = self.input_entry.get()
        output_data = maths.num_digits(int(input_data))
        self.display_output(output_data)

    def runFactorial(self):
        input_data = self.input_entry.get()
        output_data = maths.factorial(int(input_data))
        self.display_output(output_data)

    def runPerfectSquares(self):
        input_data = self.input_entry.get()
        output_data = maths.num_perfect_squares(int(input_data))
        self.display_output(output_data)

    def display_output(self, output_data):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, output_data)

root = tk.Tk()
app = AlgorithmTester(root)
root.mainloop()