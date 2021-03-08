# Going to try to import only what I need to save on space and calculation time
# My files
from bl3data import BL3Data
from __info_function__ import Create_HotFix_File, FileChoice
from _global_lists import Mod_Header, Reg_hotfix, Search_Results
from _global_lists import List_Info
################################################################################################################################################################
# Libraies
import tkinter as tk
from tkinter import Entry, Button, Label, Tk, StringVar, Frame
from tkinter import DISABLED
################################################################################################################################################################
# Global variables
data = BL3Data()
################################################################################################################################################################
#Creates a new window for the user to see and for the commands to be used
def SelectionWindow(Func):
    # Global/Window variables
    SelectionWindow = Tk()
    Frame_Left = Frame(SelectionWindow,borderwidth = 7)
    Frame_Right = Frame(SelectionWindow,borderwidth = 7)
    Frame_Bottom = Frame(SelectionWindow,borderwidth = 7)
    # Default values for window sizes, can manipulate inside the functions
    w = 500
    h = 350 
    ws = SelectionWindow.winfo_screenwidth()
    hs = SelectionWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    # These variables will determine how many things to add to the window as i need them
    Lab, Ent, Butt = 0, 0, 0
    # Generics we can reuse for any task I have created
    Entry_1, Entry_2, Entry_3, Entry_4 = StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)
    Entry_5, Entry_6, Entry_7, Entry_8 = StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow), StringVar(SelectionWindow)
    
    # Used to grab the values the then entry textvariables,
    def Get_Val(Type):
        # Puts information into a queue to be executed later
        if Type == "ModHeader":
            A, B, C, D, E, F = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get()
            # Puts the Information to make the file into a queue to be called later
            Mod_Header.extend([A, B, C, D, E, F])
        
        # Allows for the creation of multiple regular hotixes
        elif Type == "HotFix":
            A, B, C, D, E, F, G, H = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get()
            # Info is put into a regular hotfix queue for later
            Reg_hotfix.extend([A, B, C, D, E, F, G, H])
        
        # This will help with the writting hotfixes them
        elif Type == "Update Display":
            A, B, C, D, E, F, G, H = Entry_1.get(), Entry_2.get(), Entry_3.get(), Entry_4.get(), Entry_5.get(), Entry_6.get(), Entry_7.get(), Entry_8.get()
            HotFix_Label["text"] = '{},(1,1,{},{}),{}\n,{},{},{},{}\n'.format(A, B, C, D, E, F, G, H)        
        
        # This will search the database for provided information
        elif Type == "Search":
            Search = Entry_1.get()
            Info = data.get_refs_from_data(Search)
            # This will clean out the previous entry so that it does not become cluttered
            if len(Search_Results) > 0:
                Search_Results.clear()
            for Details in Info:
                if Details[0] not in Search_Results:
                    Search_Results.append(Details[0])
            Search_Results.sort()
        

            
    
    if Func == "ModHeader":  # Creates a mod file of you to use
        SelectionWindow.title("Mod Header")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x/4, y))

        Lab = 6
        Ent = 6
        Label_1_Text = 'Name of the hotfix file: '
        Label_2_Text = 'The actual mod name: '
        Label_3_Text = 'Author(s) name: '
        Label_4_Text = 'Discription: '
        Label_5_Text = 'Version of this mod: '
        Label_6_Text = 'The catagory in which this mods fits to: '

        Button_1_Text = 'Create Mod Header'
        def Button_1_Command(): return Get_Val("ModHeader")
        Butt = 1

    #This will make the user put hotfix information into a queue to be executed later
    elif Func == "HotFix":
        SelectionWindow.title("Creating Regular Hot Fix.")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x, y/10))

        Lab = 8
        Ent = 8
        Label_1_Text = 'Hotfix Type: (hf_type)'
        Label_2_Text = '1 or 0: (notification_flag)'
        Label_3_Text = 'Map Name: (package)'
        Label_4_Text = 'JSON Path + JWP Object: (obj_name)'
        Label_5_Text = 'Attribute: (attr_name)'
        Label_6_Text = 'Lenght of the previous value, (prev_val_len)'
        Label_7_Text = 'True, False, or Leave Blank: (prev_val)'
        Label_8_Text = 'True or New Value Type (new_val)'

        Button_1_Text = "Add This Regular Hotfix To The Queue"
        def Button_1_Command(): return Get_Val("HotFix")
        Button_2_Text = "Look at what your HotFix looks like"
        def Button_2_Command(): return Get_Val("Update Display")
        Butt = 2
        HotFix_Label = Label(Frame_Bottom, text = '{hf_type},(1,1,{notification_flag},{package}),{obj_name}\n,{attr_name},{prev_val_len},{prev_val},{new_val}')
    # The user will search for a word, and puncuation does not matter, but spelling does
    elif Func == "Search":
        SelectionWindow.title("Find All References")
        SelectionWindow.geometry('%dx%d+%d+%d' % (w, h, x*1.8, y))

        Lab = 1
        Ent = 1
        Label_1_Text = 'Enter what you want to search for: \nMay take a minute or so to finish.'

        Button_1_Text = "Search"
        def Button_1_Command(): return Get_Val("Search")
        Butt = 1
    
    # Reuseable variables, saves on code space and looks nicer
    
    # Labels
    if Lab >= 1:
        Label(Frame_Left, text=Label_1_Text)
    if Lab >= 2:
        Label(Frame_Left, text=Label_2_Text)
    if Lab >= 3:
        Label(Frame_Left, text=Label_3_Text)
    if Lab >= 4:
        Label(Frame_Left, text=Label_4_Text)
    if Lab >= 5:
        Label(Frame_Left, text=Label_5_Text)
    if Lab >= 6:
        Label(Frame_Left, text=Label_6_Text)
    if Lab >= 7:
        Label(Frame_Left, text=Label_7_Text)
    if Lab >= 8:
        Label(Frame_Left, text=Label_8_Text)

    
    for c in sorted(Frame_Left.children):
        Frame_Left.children[c].pack(expand=True, fill="both")

    # Entries
    if Ent >= 1:
        Entry(Frame_Right, textvariable=Entry_1, width=80)
    if Ent >= 2:
        Entry(Frame_Right, textvariable=Entry_2, width=80)
    if Ent >= 3:
        Entry(Frame_Right, textvariable=Entry_3, width=80)
    if Ent >= 4:
        Entry(Frame_Right, textvariable=Entry_4, width=80)
    if Ent >= 5:
        Entry(Frame_Right, textvariable=Entry_5, width=80)
    if Ent >= 6:
        Entry(Frame_Right, textvariable=Entry_6, width=80)
    if Ent >= 7:
        Entry(Frame_Right, textvariable=Entry_7, width=80)
    if Ent >= 8:
        Entry(Frame_Right, textvariable=Entry_8, width=80)

    for c in sorted(Frame_Right.children):
        Frame_Right.children[c].pack(expand=True, fill="both")

    # Buttons
    if Butt >= 1:
        Button(Frame_Bottom, font=("Times New Roman", 14), text=Button_1_Text, command=Button_1_Command)
    if Butt >= 2:
        Button(Frame_Bottom, font=("Times New Roman", 14), text=Button_2_Text, command=Button_2_Command)
    
    for c in sorted(Frame_Bottom.children):
        Frame_Bottom.children[c].pack(expand=True, fill="x")
    
    Frame_Left.grid(column=0)
    Frame_Right.grid(column=1, row=0)
    Frame_Bottom.grid(row=1)
    Frame_Bottom.grid_propagate(True)
################################################################################################################################################################
# Main menu.
if __name__ == "__main__":
    MainWindow = tk.Tk()
    MainWindow.title("Hot Fix Generator")
    w = 500
    h = 350 
    ws = MainWindow.winfo_screenwidth()
    hs = MainWindow.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    MainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    Button(text="Add To Mod Header Queue",font=("Times New Roman", 14), command=lambda: SelectionWindow("ModHeader"))
    Button(text="Add To Regular HotFix Queue", font=("Times New Roman", 14), command=lambda: SelectionWindow("HotFix"))
    Button(text="Add To Table HotFix Queue", font=("Times New Roman", 14), state=DISABLED)
    Button(text="Choose JSON File To Look Through", font=("Times New Roman", 14), command=lambda: FileChoice())
    Button(text="Database Search", font=("Times New Roman", 14), command=lambda: SelectionWindow("Search"))
    Button(text="Stored Information", font=("Times New Roman", 14), command=lambda: List_Info())
    Button(text="Create Your HotFix File\nNOTE: Fill Out Queues Before Clicking", font=("Times New Roman", 14), command=lambda: Create_HotFix_File())
    
    # Formats all my wigits the same way
    for c in sorted(MainWindow.children):
        MainWindow.children[c].pack(expand=True, fill="both")
    MainWindow.mainloop()
################################################################################################################################################################
