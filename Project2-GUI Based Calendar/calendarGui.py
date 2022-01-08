from tkinter import*
import calendar

def Calendar_View():
    window = Tk()
    window.config(background="violet")
    window.title("Complete Year Calendar ")
    window.geometry("570x720")
    get_year = int(year_entry.get())
    window_content = calendar.calendar(get_year)
    year_cal = Label(window, text=window_content, font=("Arial", 12, "bold"))
    year_cal.grid(row=5, column=1, padx=20)
    window.mainloop()


if __name__=='__main__':
    root = Tk()
    root.config(background="yellow")
    root.title('GUI CALENDER')
    root.geometry("280x170")

    name = Label(root, text="Calendar", bg="light blue", font=("Arial", 20, "bold"))
    name.grid(row=1, column=1)

    year = Label(root, text="Enter the Year",bg="light yellow", font=("Arial", 15, "bold"))
    year.grid(row=2, column=1)

    year_entry = Entry(root, font=("Arial", 15, "bold"))
    year_entry.grid(row=3, column=1)
    
    show_button = Button(root, text="Show Calender!", fg="red", bg="black", font=("Arial", 15, "bold"), command=Calendar_View)
    show_button.grid(row=4, column=1)

    root.mainloop()
