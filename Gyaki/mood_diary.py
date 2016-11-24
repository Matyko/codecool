from tkinter import *
import tkinter as tk
from datetime import date

buttons_dict = {}
list_to_save = [" "," "]

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    
    def refresh(self):
        self.destroy()
        Application(root)
    
    def create_widgets(self):
        feelings = get_list_from_file("feelings.txt")
        things_to_do = get_list_from_file("things to do.txt")
        options = ["Save", "Statistics", "Activities", "Quit"]

        for k, v in enumerate(options):
            self.submitButton = Button(self, text = options[k])
            buttons_dict[self.submitButton] = options[k]
            self.submitButton.bind("<Button-1>", self.button_clicked_options)
            self.submitButton.grid(row = 0, column = k, pady = 5, padx = 5)
        
        
        self.instruction = Label(self, text="\n=== " + str(date.today()) + " ===" + "\n=== How was your day? ===\n")
        self.instruction.grid(row = 1, columnspan = 5)
        
        self.create_list_buttons_top(feelings)
        
        self.instruction = Label(self, text="\n=== What did you do? ===\n")        
        self.instruction.grid(row = 3, columnspan = 5)
        
        self.create_list_buttons_and_text(things_to_do)

        self.instruction = Label(self, text="\n=== Created by Matyi Krista ===\n")   
        self.instruction.grid(columnspan = 5)

    def create_list_buttons_top(self, list_name):        
        global buttons_dict
        
        for k, v in enumerate(list_name):
            self.submitButton = Button(self, text = list_name[k])
            self.submitButton.grid(row = 2, column = k, padx=5)
            buttons_dict[self.submitButton] = list_name[k]
            self.submitButton.bind("<Button-1>", self.button_clicked)

    def create_list_buttons_and_text(self, list_name):
        global buttons_dict

        counter = 0
        newline = 4
        column_back = 0

        for k, v in enumerate(list_name):
            if counter % 5 == 0 and counter != 0:
                newline += 1
                column_back += 5
            self.submitButton = Button(self, text = list_name[k])
            buttons_dict[self.submitButton] = list_name[k]
            self.submitButton.bind("<Button-1>", self.button_clicked_things)
            self.submitButton.grid(row = newline, column = (k - column_back), pady = 5)
            counter += 1
        
        newline += 1
        self.instruction = Label(self, text=" ")        
        self.instruction.grid(row = newline, column = 0)
        
        newline += 1
        self.instruction = Label(self, text="\n=== Your diary entry ===\n")        
        self.instruction.grid(row = newline, column = 0, columnspan = 5)

        newline += 1
        self.text = Text(self, height = 8, width = 30, wrap = WORD)
        self.text.grid(row = newline, column = 0, columnspan = 5)

        newline += 1
        self.instruction = Label(self, text="\n=== Additional notes ===\n")        
        self.instruction.grid(row = newline, column = 0, columnspan = 5)

        newline += 1
        self.notes = Entry(self, width = 45)
        self.notes.grid(row = newline, column = 0, columnspan = 5, pady=10)

    def button_clicked(self, event):
        global list_to_save
        list_to_save = [" "," "]
        list_to_save[0] = str(date.today())
        list_to_save[1] = buttons_dict[event.widget]
        self.text.delete(0.0, END)
        self.text.insert(INSERT, str(date.today()) + "\nToday was: " + buttons_dict[event.widget] + "\n\nWhat I did today:\n\n")
    
    def button_clicked_things(self, event):
        global list_to_save
        if buttons_dict[event.widget] not in list_to_save:     
            list_to_save.append(buttons_dict[event.widget])
        self.text.insert(INSERT, buttons_dict[event.widget] + ", ")

    
    def button_clicked_options(self, event):
        global list_to_save
        if buttons_dict[event.widget] == "Save":
            table = get_table_from_file("diary.txt")
            for row in table:
                if row[0] == str(date.today()):
                    table.remove(row)
            if list_to_save[0] != " ":
                list_to_save.append(self.notes.get())
                table.append(list_to_save)
            write_table_to_file("diary.txt", table)
            self.refresh()
        if buttons_dict[event.widget] == "Statistics":
            self.logs()
        if buttons_dict[event.widget] == "Activities":
            self.create_submit_window("Add or Remove activity")
        if buttons_dict[event.widget] == "Quit":
            quit()

    def create_submit_window(self, title):
        t = tk.Toplevel(self)
        t.wm_title(title)
        self.instruction = Label(t, text="\nAdd or remove new activity")
        self.instruction.grid()
        self.submitted = Entry(t)
        self.submitted.grid(padx = 10, pady = 10)
        self.submitButton = Button(t, text = "Submit", command=self.savetext)
        self.submitButton.grid(pady = 10)
    
    def day_counter(self, mood):
        days = 0
        table = get_table_from_file("diary.txt")
        for row in table:
            if row [1] == mood:
                days += 1
        return days
    
    def logs(self):
        l = tk.Toplevel(self)
        l.wm_title("Statistics")
        feelings = get_list_from_file("feelings.txt")
        self.instruction = Label(l, text="Enter the date to check:")
        self.instruction.grid(row=0, pady=10)
        self.date_entry_year = Entry(l, width = 4)
        self.date_entry_year.grid(row = 0, column = 1, padx=10 )
        self.date_entry_month = Entry(l, width = 2)
        self.date_entry_month.grid(row = 0, column = 2, padx=10 )
        self.date_entry_day = Entry(l, width = 2)
        self.date_entry_day.grid(row = 0, column = 3, padx=10 )
        self.submitButton = Button(l, text = "Get diary entry of that date", command=self.one_log_check)
        self.submitButton.grid(pady = 10)
        for feeling in feelings:
            self.number_days = Label(l, text="Number of " + feeling + " days: " + str(self.day_counter(feeling)))
            self.number_days.grid(padx = 20, pady = 20, sticky = W)
    
    def one_log_check(self):
        dates = []
        table = get_table_from_file("diary.txt")
        dates.append(self.date_entry_year.get())
        dates.append(self.date_entry_month.get())
        dates.append(self.date_entry_day.get())
        date = "-".join(dates)       
        for row in table:
            if row[0] == date:
                minusdate = row[2:]
                minusall = minusdate[:-1]
                activities = ", ".join(minusall)
                self.one_log(row[1], activities, date, row[-1])
    
    def one_log(self, mood, activities, date, note):
        o = tk.Toplevel(self)
        o.wm_title("Diary entry of: " + date)
        print(date, activities, note)
        self.diary_entry = Label(o, text= date + "\n\nToday was " + mood + "\n\nWhat I did today:\n\n" + activities + "\n\n" + note)
        self.diary_entry.grid(padx=10, pady=10) 

    def savetext(self):
        list_of_activities = get_list_from_file("things to do.txt")
        new_activity = self.submitted.get()
        if new_activity in list_of_activities:
            list_of_activities.remove(new_activity)
        else:
            list_of_activities.append(new_activity)
        with open("things to do.txt", "w") as file:
            for item in list_of_activities:
                file.write("%s\n" % item)
        self.refresh()


def get_list_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    read_list = [element.replace("\n", "") for element in lines]
    return read_list

def write_table_to_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")

            

def get_table_from_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]  
    return table


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Matyi\'s mood diary')
    app = Application(root)
    root.mainloop()
