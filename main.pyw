from tkinter import Tk, LabelFrame, Label, Entry, Button, Radiobutton, IntVar, END

from formulas import male_bmr, female_bmr, male_calories, female_calories


def calculate():
    """Get user inputs then calculate and display BMR and calorie data."""

    # Get all input data from the GUI
    age = float(age_input.get())
    weight = float(weight_input.get())
    height = float(height_input.get())
    heartrate = float(heartrate_input.get())
    duration = float(duration_input.get())

    if gender.get() == 0:
        # Calculate data for males
        bmr = male_bmr(weight, height, age)
        gross_calories = male_calories(heartrate, weight, age, duration)
    else:
        # Calculate data for females
        bmr = female_bmr(weight, height, age)
        gross_calories = female_calories(heartrate, weight, age, duration)

    net_calories = gross_calories - (bmr / 1440 * duration)

    # Display calculated data
    bmr_output.config(text=int(bmr))
    gross_output.config(text=int(gross_calories))
    net_output.config(text=int(net_calories))


def clear():
    # Clear input fields
    bmr_output.config(text="")
    gross_output.config(text="")
    net_output.config(text="")

    # Clear output text
    age_input.delete(0, END)
    weight_input.delete(0, END)
    height_input.delete(0, END)
    heartrate_input.delete(0, END)
    duration_input.delete(0, END)


root = Tk()
root.title("Exercise Calorie Calculator")
root.bind("<Return>", lambda x: calculate())
app_title = Label(
    root, text="EXERCISE CALORIE CALCULATOR", pady=10, font=("Helvetica 12 bold")
)
app_title.grid(row=0, column=0, columnspan=2)
gender = IntVar()

# ---------------- INPUT FRAME -------------------
input_frame = LabelFrame(root, text="Input", padx=20, pady=10)
input_frame.grid(row=1, column=0, padx=10)

# Data inputs and labels
age_label = Label(input_frame, text="Age")
age_label.grid(row=0, column=0, columnspan=2)
age_input = Entry(input_frame, width=10)
age_input.grid(row=1, column=0, columnspan=2)

weight_label = Label(input_frame, text="Weight (lb)")
weight_label.grid(row=2, column=0, pady=[10, 0], columnspan=2)
weight_input = Entry(input_frame, width=10)
weight_input.grid(row=3, column=0, columnspan=2)

height_label = Label(input_frame, text="Height (in)")
height_label.grid(row=4, column=0, pady=[10, 0], columnspan=2)
height_input = Entry(input_frame, width=10)
height_input.grid(row=5, column=0, columnspan=2)

duration_label = Label(input_frame, text="Minutes")
duration_label.grid(row=6, column=0, pady=[10, 0], columnspan=2)
duration_input = Entry(input_frame, width=10)
duration_input.grid(row=7, column=0, columnspan=2)

heartrate_label = Label(input_frame, text="Heartrate")
heartrate_label.grid(row=8, column=0, pady=[10, 0], columnspan=2)
heartrate_input = Entry(input_frame, width=10)
heartrate_input.grid(row=9, column=0, columnspan=2)

# Gender radio buttons
r1 = Radiobutton(input_frame, text="Male", variable=gender, value=0)
r1.grid(row=10, column=0, pady=[10, 0])

r2 = Radiobutton(input_frame, text="Female", variable=gender, value=1)
r2.grid(row=10, column=1, pady=[10, 0])

# -------------------- OUTPUT FRAME --------------------
output_frame = LabelFrame(root, text="Output")
output_frame.grid(row=1, column=1, ipady=21, padx=10)

# Labels for text output
bmr_label = Label(output_frame, text="BMR", font="bold")
bmr_label.grid(row=1, column=0, padx=30, pady=[30, 0])
bmr_output = Label(output_frame, font=("Helvetica 15 bold"))
bmr_output.grid(row=2, column=0)

gross_label = Label(output_frame, text="Gross Calories", font="bold", padx=25)
gross_label.grid(row=4, column=0, pady=[30, 0])
gross_output = Label(output_frame, font=("Helvetica 15 bold"))
gross_output.grid(row=5, column=0)

net_label = Label(output_frame, text="Net Calories", font="bold")
net_label.grid(row=7, column=0, pady=[31, 0])
net_output = Label(output_frame, font=("Helvetica 15 bold"))
net_output.grid(row=8, column=0)

# Create the calculate button
calculate_button = Button(root, width=15, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, pady=[20, 0], padx=20)

# Create the clear button
clear_button = Button(root, width=15, text="Clear", command=clear)
clear_button.grid(row=2, column=1, pady=[20, 0])

# Create the exit button
exit_button = Button(root, width=20, text="Exit", command=root.quit)
exit_button.grid(row=3, column=0, pady=[20, 10], columnspan=2)

root.mainloop()
