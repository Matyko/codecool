from tkinter import *
from datetime import date

buttons_dict = {}
list_to_save = [" "," "]

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        feelings = get_list_from_file("feelings.txt")
        things_to_do = get_list_from_file("things to do.txt")
        
        self.instruction = Label(self, text="\n=== " + str(date.today()) + " ===" + "\n=== How was your day? ===\n")
        self.instruction.grid(row = 0, columnspan = 5)
        
        self.create_list_buttons_top(feelings)
        
        self.instruction = Label(self, text="\n=== What did you do? ===\n")        
        self.instruction.grid(row = 2, columnspan = 5)
        
        self.create_list_buttons_and_text(things_to_do)

        self.instruction = Label(self, text="\n=== Created by Matyi Krista ===\n")   
        self.instruction.grid(columnspan = 5)

    def create_list_buttons_top(self, list_name):        
        global buttons_dict

        for k, v in enumerate(list_name):
            self.submitButton = Button(self, text = list_name[k])
            self.submitButton.grid(row = 1, column = k)
            buttons_dict[self.submitButton] = list_name[k]
            self.submitButton.bind("<Button-1>", self.button_clicked)

    def create_list_buttons_and_text(self, list_name):
        global buttons_dict

        counter = 0
        newline = 3
        column_back = 0
        options = ["Add new", "Save", "Calendar"]

        for k, v in enumerate(list_name):
            if counter % 5 == 0 and counter != 0:
                newline += 1
                column_back += 5
            self.submitButton = Button(self, text = list_name[k])
            buttons_dict[self.submitButton] = list_name[k]
            self.submitButton.bind("<Button-1>", self.button_clicked_things)
            self.submitButton.grid(row = newline, column = (k - column_back))
            counter += 1
        
        newline += 1
        self.instruction = Label(self, text=" ")        
        self.instruction.grid(row = newline, column = 0)

        newline += 1
        for k, v in enumerate(options):
            self.submitButton = Button(self, text = options[k])
            buttons_dict[self.submitButton] = options[k]
            self.submitButton.bind("<Button-1>", self.button_clicked_options)
            self.submitButton.grid(row = newline, column = k)
        
        newline += 1
        self.instruction = Label(self, text="\n=== Your diary entry ===\n")        
        self.instruction.grid(row = newline, column = 0, columnspan = 5)

        newline += 1
        self.text = Text(self, height = 15, width = 30, wrap = WORD)
        self.text.grid(row = newline, column = 0, columnspan = 5)

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
                print(row[0])
                print(str(date.today()))
                if row[0] == str(date.today()):
                    table.remove(row)
            table.append(list_to_save)
            write_table_to_file("diary.txt", table)


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


def main():
    root = Tk()
    root.title('Matyi\'s mood diary')
    app = Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()