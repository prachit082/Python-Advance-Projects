    #Importing tkinter module
from tkinter import *
    #importing calendar module
import calendar

    #function to show calendar of the given year
def showCalender():
        gui = Tk()
        gui.config(background='grey')
        gui.title("Calender for the year")
        gui.geometry("550x600")    

        year_field = Entry(gui)    # Define year_field as an entry widget
        year_field.grid(row=0, column=0, padx=20, pady=20)    # Place the entry widget in the GUI

        def showCalendarYear():
            year = int(year_field.get())
            gui_content = calendar.calendar(year)
            calYear = Label(gui, text=gui_content, font="Consolas 10 bold")
            calYear.grid(row=5, column=1, padx=20)

        show_button = Button(gui, text="Show Calendar", command=showCalendarYear)
        show_button.grid(row=1, column=0, padx=20, pady=10)

        gui.mainloop()

if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calender")
    new.geometry("250x140")
    cal = Label(new, text="Calender",bg='grey',font=("times", 28, "bold"))
    year = Label(new, text="Enter year", bg='dark grey')
    year_field=Entry(new)
    button = Button(new, text='Show Calender',
fg='Black',bg='Blue',command=showCalender)

    #putting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    new.mainloop()