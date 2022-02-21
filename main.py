import tkinter
from tkinter import *
import os
global dest_file
global dest_dir
global file_Name

# Create the Window.

root = Tk()
root.title("Recon Sniffer")
root.iconbitmap("D:\Pycharm\Python_Projects\pythonProject\Final_Project_Syn_Scanner\RS.ico")

# Set the size of the window and color of the window.

root.geometry("290x400")
root.config(bg='black', padx=5, pady=5)

# Create the "Select Interface" Widget.

def file_Select():
    from tkinter import filedialog
    global dest_file
    dest_file = filedialog.askopenfilename(title="Select a File")
    file_entry.insert(string=dest_file, index=0)

# Create File Explorer Widget.

def directory_Explorer():
    from tkinter import filedialog
    global dest_dir
    dest_dir = filedialog.askdirectory()
    directory_entry.insert(string=dest_dir, index=0)

# Create the "Run" Widget

def run():
    import pandas as pd
    import pathlib

    selected_File = file_entry.get()
    if file_entry.get() == '' or pathlib.Path(selected_File).suffix != ".csv":
        print ("Please Select a CSV file.")

    else:
        csv_file = pd.read_csv(dest_file)
        csv_file.set_index("No.")
        syn_ack = csv_file.loc[csv_file["Info"].str.contains ("SYN, ACK")]
        ack = csv_file.loc[((csv_file["Info"].str.contains("ACK")) & (~csv_file["Info"].str.contains("SYN")) & (csv_file["Info"].str.contains("Seq=1")))]
        x = (syn_ack[["Source", "Destination"]])
        y = (ack[["Source", "Destination"]])

        new_Rows_x = []
        new_Rows_2 = []
        new_Rows_Final = []

        for i in x['Source']:
            if i not in new_Rows_x:
                new_Rows_x.append(i)

        for j in x['Destination']:
            if j not in new_Rows_x:
                new_Rows_x.append(j)

        for k in y['Source']:
            if k not in new_Rows_2:
                new_Rows_2.append(k)

        for l in y['Destination']:
            if l not in new_Rows_2:
                new_Rows_2.append(l)

        for m in new_Rows_x:
            if m not in new_Rows_2:
                new_Rows_Final.append(m)

        if file_Entry.get() == '':
            file_Name = "Report.txt"
        else:
            file_Name = file_Entry.get() + ".txt"

# Write the file to the selected directory.

        selected_Path = os.path.join(dest_dir, file_Name)
        textfile = open(selected_Path, "w")
        textfile.write("The following IP addresses should be investigated for possible recon attacks:" + "\n" + "\n")
        for n in new_Rows_Final:
            textfile.write(n + "\n")
        textfile.close()

# Create "Select File" Label.

file_Button = Button(root, text="Select File", bg="black", fg="yellow", bd=3, activebackground="black", activeforeground="red", command=file_Select)
file_Button.grid(row=0, column=0, padx=5, pady=5)

file_entry = Entry(root,bg="white")
file_entry.grid(row=0, column=1, padx=5, pady=5)


# Create Save Directory Label and Entry Window.

dest_dir = os.getcwd()

directory_Button = Button(root, text="Output File Location", bg="black", fg="yellow", bd=3, activebackground="black", activeforeground="red", command=directory_Explorer)
directory_Button.grid(row=1, column=0, padx=5, pady=5)

directory_entry = Entry(root)
directory_entry.grid(row=1, column=1)


# File Name Entry.

file_Name = Label(root, text="File Name", bg="black", fg="yellow")
file_Name.grid(row=2, column=0, padx=5, pady=5)

file_Entry = Entry(root, bg="white")
file_Entry.grid(row=2, column=1)


# Create Space

spaceLabel_3=Label(root, text="", bg="black", fg="black")
spaceLabel_3.grid(row=7, column=0)


# Create Space.

spaceLabel=Label(root, text="", bg="black", fg="black")
spaceLabel.grid(row=5, column=0)


# Create the Run Button

button_run = Button(root, text="Run", bg="black", fg="yellow", width=10, activebackground="black", activeforeground="red", command=run)
button_run.grid(row=6, column=0, padx=30)

# Create more Space

spaceLabel_2=Label(root, text="", bg="black", fg="black")
spaceLabel_2.grid(row=7, column=0)

# Create the Exit Button.

button_quit = Button(root, text="Exit Program", bg="red", fg="black", activebackground="black", activeforeground="red",command=root.quit)
button_quit.grid(row=8, column=0, padx=30)


root.mainloop()