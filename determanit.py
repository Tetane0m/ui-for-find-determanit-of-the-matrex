import random
import matplotlib.pylab as plt
from tkinter import *
from tkinter import messagebox, Frame
from tkinter import colorchooser

# Function to choose the background and primary colors
def choice_color():
    global pri_c, sec_c, welcome_label

    # Ask user if they want to change the background color
    x = messagebox.askyesno("Background Color", "Do you want to change the background color for the program?")
    if x:
        x = colorchooser.askcolor()
        if x[1] is not None:
            pri_c = x[1]
            # Update the background color of specific items
            item = [welcome_label, m, root, button_frame, home_frame, info_label, first_frame]
            for i in item:
                i.config(bg=pri_c)

    # Ask user if they want to change the primary color
    x2 = messagebox.askyesno("Button Color", "Do you want to change the primary color for the program?")
    if x2:
        x = colorchooser.askcolor()
        if x[1] is not None:
            try:
                sec_c = x[1]
                # Update the primary color of specific items
                welcome_label.config(fg=sec_c)
                item = [back_btn, color_btn, btn_1, btn_2, btn_3, btn_4]
                for i in item:
                    i.config(bg=sec_c)

                word = [label1, label2]
                for j in word:
                    j.config(fg=sec_c)

                entry1.config(highlightcolor=sec_c)
                entry2.config(highlightcolor=sec_c)
            except:
                pass

# Function to navigate to the home screen
def home():
    global home_frame, button_frame, info_label, back_btn, color_btn

    item_frame.destroy()
    root.bind("<Return>", "")
    home_frame = Frame(first_frame, bg=pri_c)
    info_label = Label(home_frame, text=my_text, font=font(16), bg=pri_c, fg='white')

    button_frame = Frame(home_frame, bg=pri_c)
    back_btn = Button(button_frame, fg="white", text='Back', font=font(18), command=sc_fr_ge, bg=sec_c, width=12,
                      activeforeground=sec_c, activebackground='#222222')
    color_btn = Button(button_frame, fg="white", text='Settings', font=font(18), command=choice_color, bg=sec_c,
                       width=12,
                       activeforeground=sec_c, activebackground='#222222')

    home_frame.pack()
    info_label.pack(pady=50, anchor='center')
    button_frame.pack()
    back_btn.grid(row=1, column=1, padx=10)
    back_btn.bind("<Enter>", lambda x: back_btn.config(bg=hover_color))
    back_btn.bind("<Leave>", lambda x: back_btn.config(bg=sec_c))

    color_btn.grid(row=1, column=2, padx=10)
    color_btn.bind("<Enter>", lambda x: color_btn.config(bg=hover_color))
    color_btn.bind("<Leave>", lambda x: color_btn.config(bg=sec_c))

# Function to restart the program
def restart():
    global count, my_array

    entry1.config(state='normal')
    entry2.config(state='normal')
    entry1.delete(0, END)
    entry2.delete(0, END)
    count = 0
    my_array = []

    messagebox.showinfo("Restart", "Restart complete. You can start from the beginning")

    # Rebind the Enter key to the show function
    root.bind("<Return>", show)

    # Change the button text and command to the show function
    btn_1.config(command=show, text='Next')


def determinate(*args):
    def find_determinant(matrix):
        # Base case: matrix of size 1x1
        if len(matrix) == 1:
            return matrix[0][0]

        det = 0
        sign = 1
        for i in range(len(matrix)):
            # Compute the cofactor of matrix[0][i]
            submatrix = []
            for j in range(1, len(matrix)):
                row = []
                for k in range(len(matrix)):
                    if k != i:
                        row.append(matrix[j][k])
                submatrix.append(row)

            # Recursively compute determinant of submatrix
            sub_det = find_determinant(submatrix)

            # Update determinant using the Laplace expansion formula
            det += sign * matrix[0][i] * sub_det
            sign *= -1

        return det

    result = find_determinant(my_array)
    messagebox.showinfo("Result", f"The determinant of your array is {result}")
    restart()


def show(*args):
    global count

    try:
        if int(entry1.get()) <= 1 or int(entry1.get()) >= 12 or len(entry1.get()) > 2:
            if int(entry1.get()) >= 12:
                return messagebox.showerror("Error", 'Too much dimension to calculate 1 in dimension')
            else:
                return messagebox.showerror("Error", 'Enter only positive integer number more than 1 in dimension')

        # Work part !!!!!!!!
        try:
            dimension = int(entry1.get())
            number = entry2.get().split(',')
            if len(number) != dimension:
                messagebox.showerror("Invalid input", f'Enter exactly the number that fits the dimension like:\n'
                                                      f'3 dimensions:\n'
                                                      f'--> Enter 3 elements like: {random.randrange(-70, 70)}, '
                                                      f'{random.randrange(-70, 70)}, {random.randrange(-70, 70)}\n'
                                                      f'2 dimensions:\n'
                                                      f'--> Enter two elements like: {random.randrange(-70, 70)}, '
                                                      f'{random.randrange(-70, 70)}\n'
                                                      f'\nThe numbers should be between -70 and 70.')

            else:
                for i in range(dimension):
                    try:
                        error = 0
                        if (float(number[i]) >= 70 or float(number[i]) <= -70) and error == 0:
                            return messagebox.showerror("Invalid input", 'Please enter only numbers in the range of -70 and +70!')
                    except:
                        return messagebox.showerror("Invalid input", 'Please enter only numbers!')

                entry1.config(state='disabled')
                row = []
                for i in number:
                    row.append(eval(i))
                my_array.append(row)
                count += 1
                entry2.delete(0, END)
                if count == dimension:
                    entry2.config(state='disabled')
                    btn_1.config(text="Calculate", command=determinate)
                    root.bind("<Return>", determinate)
        except SyntaxError:
            messagebox.showerror("Invalid input", 'Please enter the correct input in the correct form')

    except ValueError:
        messagebox.showerror("Error", 'Enter only positive integer number more than 1 in dimension')

def sc_fr_ge():
    global sec_frame, entry1, entry2, x_point, info_label, start_btn2, wel_frame, home_frame, btn_1
    global btn_2, btn_3, btn_4, y_point, count, btn_1, label1, label2, item_frame, my_array

    def grid_item(it, r, c):
        return it.grid(row=r, column=c)

    # Initialize global variables
    count = 0
    my_array = []

    wel_frame.destroy()

    try:
        home_frame.destroy()
    except:
        pass

    item_frame = Frame(first_frame, bg=pri_c)

    # Create labels and entries
    label1 = Label(item_frame, text=f'Dimension of the matrix like: {random.randrange(2, 12)}', font=font(18),
                   fg=sec_c, bg=pri_c, padx=10, pady=10)
    entry1 = Entry(item_frame, width=24, font=font(20, "b"), highlightcolor=sec_c, highlightthickness=4)

    label2 = Label(item_frame, text='Enter row by row and press (Next)', fg=sec_c, font=font(18), bg=pri_c, padx=10,
                   pady=10)
    entry2 = Entry(item_frame, width=24, font=font(20, "b"), highlightcolor=sec_c, highlightthickness=4)

    # Create buttons
    btn_1 = Button(item_frame, fg="white", width=15, text='Next', font=font(17), command=show, bg=sec_c,
                   activeforeground=sec_c, activebackground='#222222')
    btn_1.bind("<Enter>", lambda x: btn_1.config(bg=hover_color))
    btn_1.bind("<Leave>", lambda x: btn_1.config(bg=sec_c))

    btn_2 = Button(item_frame, fg="white", width=15, text='Exit', font=font(17), command=root.destroy, bg=sec_c,
                   activeforeground=sec_c, activebackground='#222222')
    btn_2.bind("<Enter>", lambda x: btn_2.config(bg=hover_color))
    btn_2.bind("<Leave>", lambda x: btn_2.config(bg=sec_c))

    btn_3 = Button(item_frame, fg="white", width=15, text='Restart', font=font(17), command=restart, bg=sec_c,
                   activeforeground=sec_c, activebackground='#222222')
    btn_3.bind("<Enter>", lambda x: btn_3.config(bg=hover_color))
    btn_3.bind("<Leave>", lambda x: btn_3.config(bg=sec_c))

    btn_4 = Button(item_frame, fg="white", width=15, text='Home', font=font(17), command=home, bg=sec_c,
                   activeforeground=sec_c, activebackground='#222222')
    btn_4.bind("<Enter>", lambda x: btn_4.config(bg=hover_color))
    btn_4.bind("<Leave>", lambda x: btn_4.config(bg=sec_c))

    # Pack the item frame
    item_frame.pack(pady=70)

    # Grid the labels, entries, and buttons
    grid_item(label1, 1, 1)
    grid_item(entry1, 1, 2)
    grid_item(label2, 2, 1)
    grid_item(entry2, 2, 2)
    root.bind("<Return>", show)
    btn_1.grid(row=3, column=1, pady=30)
    btn_2.grid(row=3, column=2, pady=30)
    btn_3.grid(row=4, column=1, pady=5)
    btn_4.grid(row=4, column=2, pady=5)


# Refresh program
my_array = []
pri_c = '#000'
hover_color = "#3e3a4d"
sec_c = '#3e10e6'
count = 0
my_text = 'Hi my name is Haider and I\'m the designer of this program. \n' \
          'This program is written in Python. \n' \
          'With this program, you can calculate the determinant of a matrix. \n' \
          'you can find determinant from 2x2 matrix till 12x12 matrix \n' \
          'You only have to:\n' \
          '1_ Enter the dimension of the matrix. \n' \
          '2_ Enter row by row on that matrix. \n' \
          'Good luck!'

wel_text = 'Welcome everyone! I hope you will enjoy this program. \n' \
           'Make sure to contact me to provide feedback!'


def font(*args):
    if len(args) == 1:
        return "consolas", args[0], "italic"
    else:
        return "consolas", args[0], "bold"


# Create window
root = Tk()
root.config(bg=pri_c)
root.geometry('900x600')
root.title("Determinate Matrix")
root.resizable(False, False)

# Create welcome labels
welcome_label = Label(root, text="Welcome", font=font(55), fg=sec_c, bg=pri_c)
m = Message(root, text=wel_text, width=800, font=font(18), bg=pri_c, fg='white')
welcome_label.pack(pady=10)
m.pack(anchor='center')

first_frame = Frame(root, bg=pri_c)
wel_frame = Frame(first_frame, bg=pri_c)
start_btn = Button(wel_frame, text='Start', fg="white", font=font(24), command=sc_fr_ge, bg=sec_c, width=6,
                   activeforeground=sec_c, activebackground='#222222')
start_btn.bind("<Enter>", lambda x: start_btn.config(bg=hover_color))
start_btn.bind("<Leave>", lambda x: start_btn.config(bg=sec_c))

first_frame.pack()
wel_frame.pack(pady=20, anchor='center')
start_btn.pack()

root.mainloop()
