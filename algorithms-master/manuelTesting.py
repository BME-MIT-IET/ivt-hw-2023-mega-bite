import tkinter as tk
from tkinter import ttk
# import your algorithms here:
from algorithms import maths
from algorithms import bit
from algorithms import sort
from algorithms import strings
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("AlgorithmTester")
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2, Page3, Page4):
            frame = F(container, self)
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = ttk.Button(self, text ="maths",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        button2 = ttk.Button(self, text ="bit",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
        button3 = ttk.Button(self, text ="sort",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)          
  
        button4 = ttk.Button(self, text ="strings",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 4, column = 1, padx = 10, pady = 10) 

class Page1(tk.Frame):
    def runNumberOfDigits(self):
        input_data = self.input_entry1.get()
        output_data = maths.num_digits(int(input_data))
        self.display_output(output_data)

    def runFactorial(self):
        input_data = self.input_entry1.get()
        output_data = maths.factorial(int(input_data))
        self.display_output(output_data)

    def runPerfectSquares(self):
        input_data = self.input_entry1.get()
        output_data = maths.num_perfect_squares(int(input_data))
        self.display_output(output_data)

    def runpythagoras(self):
        input_data = self.input_entry1.get()
        input_data2 = self.input_entry2.get()
        output_data = maths.pythagoras(int(input_data),int(input_data2),"?")
        self.display_output(output_data)

    def display_output(self, output_data):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, output_data)

    def __init__(self, parent, controller):      
        tk.Frame.__init__(self, parent)
        # pages buttons
        button1 = ttk.Button(self, text ="maths",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="bit",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="sort",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)          
        button4 = ttk.Button(self, text ="strings",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 4, column = 1, padx = 10, pady = 10) 
        # test buttons
        # create a button to run Number Of Digits algorithm
        NumberOfDigits_button = ttk.Button(self, text="Test Number of Digits", command=self.runNumberOfDigits)
        NumberOfDigits_button.grid(row=1, column=2)
        # create a button to run the factorial algorithm
        Factorial_button = ttk.Button(self, text="Test Factorial", command=self.runFactorial)
        Factorial_button.grid(row=1, column=3)
        # create a button to run the perfectsquare algorithm
        PerfectSquares_button = ttk.Button(self, text="Test perfect Squares", command=self.runPerfectSquares)
        PerfectSquares_button.grid(row=1, column=4)
        # create a button to run the pythagoras algorithm
        pythagoras_button = ttk.Button(self, text="Test pythagoras", command=self.runpythagoras)
        pythagoras_button.grid(row=1, column=5)
        #create text input
        input_label1 = ttk.Label(self, text="Enter input data:")
        input_label1.grid(row=2, column=2)
        self.input_entry1 = ttk.Entry(self)
        self.input_entry1.grid(row=2, column=3)
        input_label2 = ttk.Label(self, text="    Enter input data(if needed):")
        input_label2.grid(row=2, column=4)
        self.input_entry2 = ttk.Entry(self)
        self.input_entry2.grid(row=2, column=5)
        #create text output
        self.output_text = tk.Text(self, height=2, width=40)
        self.output_text.grid(row=3, column=2,columnspan=4 )
    
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def binary_gap(self):
        input_data = self.input_entry1.get()
        output_data = bit.binary_gap(int(input_data))
        self.display_output(output_data)

    def reverse_bits(self):
        input_data = self.input_entry1.get()
        output_data = bit.reverse_bits(int(input_data))
        self.display_output(output_data)

    def count_flips_to_convert(self):
        input_data = self.input_entry1.get()
        input_data2 = self.input_entry2.get()
        output_data = bit.count_flips_to_convert(int(input_data),int(input_data2))
        self.display_output(output_data)

    def add_bitwise_operator(self):
        input_data = self.input_entry1.get()
        input_data2 = self.input_entry2.get()
        output_data = bit.add_bitwise_operator(int(input_data),int(input_data2))
        self.display_output(output_data)

    def display_output(self, output_data):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, output_data)

    def __init__(self, parent, controller):      
        tk.Frame.__init__(self, parent)
        # pages buttons
        button1 = ttk.Button(self, text ="maths",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="bit",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="sort",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)          
        button4 = ttk.Button(self, text ="strings",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 4, column = 1, padx = 10, pady = 10) 
        # test buttons
        # create a button to run binary gap algorithm
        binary_gap_button = ttk.Button(self, text="Test binary gap", command=self.binary_gap)
        binary_gap_button.grid(row=1, column=2)
        # create a button to run the reverse_bits algorithm
        reverse_bits_button = ttk.Button(self, text="Test reverse bits", command=self.reverse_bits)
        reverse_bits_button.grid(row=1, column=3)
        # create a button to run the count_flips_to_convert algorithm
        count_flips_to_convert_button = ttk.Button(self, text="Test count flips to convert", command=self.count_flips_to_convert)
        count_flips_to_convert_button.grid(row=1, column=4)
        # create a button to run the add_bitwise_operator algorithm
        add_bitwise_operator_button = ttk.Button(self, text="Test bitwise addition", command=self.add_bitwise_operator)
        add_bitwise_operator_button.grid(row=1, column=5)
        #create text input
        input_label1 = ttk.Label(self, text="Enter input data:")
        input_label1.grid(row=2, column=2)
        self.input_entry1 = ttk.Entry(self)
        self.input_entry1.grid(row=2, column=3)
        input_label2 = ttk.Label(self, text="    Enter input data(if needed):")
        input_label2.grid(row=2, column=4)
        self.input_entry2 = ttk.Entry(self)
        self.input_entry2.grid(row=2, column=5)
        #create text output
        self.output_text = tk.Text(self, height=2, width=40)
        self.output_text.grid(row=3, column=2,columnspan=4 )

class Page3(tk.Frame):
    def bubble_sort(self):
        input = self.input_entry1.get()
        strinput_data=input.split(",")
        input_data = [eval(i) for i in strinput_data]
        output_data = sort.bubble_sort(input_data)
        self.display_output(output_data)

    def bucket_sort(self):
        input = self.input_entry1.get()
        strinput_data=input.split(",")
        input_data = [eval(i) for i in strinput_data]
        output_data = sort.bucket_sort(input_data)
        self.display_output(output_data)

    def merge_sort(self):
        input = self.input_entry1.get()
        strinput_data=input.split(",")
        input_data = [eval(i) for i in strinput_data]
        output_data = sort.merge_sort(input_data)
        self.display_output(output_data)

    def quick_sort(self):
        input = self.input_entry1.get()
        strinput_data=input.split(",")
        input_data = [eval(i) for i in strinput_data]
        output_data = sort.quick_sort(input_data)
        self.display_output(output_data)

    def display_output(self, output_data):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, output_data)

    def __init__(self, parent, controller):      
        tk.Frame.__init__(self, parent)
        # pages buttons
        button1 = ttk.Button(self, text ="maths",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="bit",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="sort",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)          
        button4 = ttk.Button(self, text ="search",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 4, column = 1, padx = 10, pady = 10) 
        # test buttons
        # create a button to run buble sort algorithm
        bubble_sort_button = ttk.Button(self, text="Test bubble sort", command=self.bubble_sort)
        bubble_sort_button.grid(row=1, column=2)
        # create a button to run the bucket sort algorithm
        bucket_sort_button = ttk.Button(self, text="Test bucket sort", command=self.bucket_sort)
        bucket_sort_button.grid(row=1, column=3)
        # create a button to run the merge sort algorithm
        merge_sort_button = ttk.Button(self, text="Test merge sort", command=self.merge_sort)
        merge_sort_button.grid(row=1, column=4)
        # create a button to run the quick sort algorithm
        quick_sort_button = ttk.Button(self, text="Test quick sort", command=self.quick_sort)
        quick_sort_button.grid(row=1, column=5)
        #create text input
        input_label1 = ttk.Label(self, text="Enter input data: ")
        input_label1.grid(row=2, column=2)
        input_label2 = ttk.Label(self, text="     list separetad by ,")
        input_label2.grid(row=2, column=3)
        self.input_entry1 = ttk.Entry(self)
        self.input_entry1.grid(row=2, column=4)
        
        
        #create text output
        self.output_text = tk.Text(self, height=2, width=40)
        self.output_text.grid(row=3, column=2,columnspan=4 )

class Page4(tk.Frame):
    def atbash(self):
        input_data = self.input_entry1.get()
        output_data = strings.atbash(input_data)
        self.display_output(output_data)

    def reverse_vowel(self):
        input_data = self.input_entry1.get()
        output_data = strings.reverse_vowel(input_data)
        self.display_output(output_data)

    def convert_morse_word(self):
        input_data = self.input_entry1.get()
        output_data = strings.convert_morse_word(input_data)
        self.display_output(output_data)

    def rotate(self):
        input_data = self.input_entry1.get()
        input_data2 = self.input_entry2.get()
        output_data = strings.rotate(input_data,int(input_data2))
        self.display_output(output_data)

    def display_output(self, output_data):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, output_data)

    def __init__(self, parent, controller):      
        tk.Frame.__init__(self, parent)
        # pages buttons
        button1 = ttk.Button(self, text ="maths",
        command = lambda : controller.show_frame(Page1))
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        button2 = ttk.Button(self, text ="bit",
        command = lambda : controller.show_frame(Page2))
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="sort",
        command = lambda : controller.show_frame(Page3))
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)          
        button4 = ttk.Button(self, text ="strings",
        command = lambda : controller.show_frame(Page4))
        button4.grid(row = 4, column = 1, padx = 10, pady = 10) 
        # test buttons
        # create a button to run atbash algorithm
        add_binary_button = ttk.Button(self, text="Test atbash", command=self.atbash)
        add_binary_button.grid(row=1, column=2)
        # create a button to run the reverse vowel algorithm
        reverse_vowel_button = ttk.Button(self, text="Test reverse vowel", command=self.reverse_vowel)
        reverse_vowel_button.grid(row=1, column=3)
        # create a button to run the morse code conversion algorithm
        convert_morse_word_button = ttk.Button(self, text="Test convert morse word", command=self.convert_morse_word)
        convert_morse_word_button.grid(row=1, column=4)
        # create a button to run the rotate algorithm
        rotate_button = ttk.Button(self, text="Test rotate", command=self.rotate)
        rotate_button.grid(row=1, column=5)
        #create text input
        input_label1 = ttk.Label(self, text="Enter input data: ")
        input_label1.grid(row=2, column=2)
        self.input_entry1 = ttk.Entry(self)
        self.input_entry1.grid(row=2, column=3)
        input_label2 = ttk.Label(self, text="Enter input data:(if needed)")
        input_label2.grid(row=2, column=4)
        self.input_entry2 = ttk.Entry(self)
        self.input_entry2.grid(row=2, column=5)
        #create text output
        self.output_text = tk.Text(self, height=2, width=40)
        self.output_text.grid(row=3, column=2,columnspan=4 )
  


app = tkinterApp()
app.mainloop()