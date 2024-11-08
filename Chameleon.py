from tkinter import *
from tkinter import messagebox
import ctypes
import keyboard
from tkinter.colorchooser import*
import re
import asyncio
import time

tk = Tk()
text = ''
tk.geometry("1024x768")
tk.iconbitmap(r'hameleon.ico')
tk.title('Chameleon - untitled')
tk.configure(background='black')
fileName = ''
fileText = ''

tab_count = 0
symbols = ["=",":"]
verbs = ['print', 'input']
expansionExport=''
a = ''

x = 1.0
y = 0.0
exceptions = [0.0]

openedFile = False

maxLine = 1.0
stopLineCheck = 0
#tk.attributes("-fullscreen", True)

#Line number
lineNumberFrame = LabelFrame(fg='turquoise', bg='black')
lineNumberFrame.pack(side=LEFT, fill=Y)

#Text
enterFrame = LabelFrame(fg='turquoise', bg='black')
enterFrame.pack(side=LEFT, fill=Y)

#Expansion
expansionFrame = LabelFrame(text='expansion', fg='turquoise', bg='black')
expansionFrame.pack(side=TOP, fill=X)

#Export
importFrame = LabelFrame(text='export', fg='turquoise', bg='black')
importFrame.pack(side=TOP, fill=X)

#Code intorpritator
checkCodeFrame = LabelFrame(text='intorpritation', fg='turquoise', bg='black')
checkCodeFrame.pack(side=TOP, fill=X)

#--------------------------------------------------------------------
def intorpritator(event):
    global tab_count, symbols, verbs
    a = entry.get(1.0, END)
    b = str(event)

    #if or while
    if "elif" in a:
        elif_function()
    if "if" in a:
        if_function()
    if "else" in a:
        else_function()
    if "for" in a:
        for_function()
    if "while" in a:
        while_function()

    #keys
    if 'Return' in b:
        new_condition()
    for s in symbols:
        if s in b:
            equally_symbols()
            colon_symbols()
            semicolon_symbols()
            break

    #verbs
    for v in verbs:
        if v in a:
            static_verbs_print()
            static_verbs_input()
#-----------------------------------------------------------------
def if_function():
    global x, y, exceptions

    x = 1.0
    y = 0.0
    stop = False

    entry.tag_config("if", foreground='purple')

    while True:
        x = entry.search('if', x, stopindex=END)
        if not x: break 
        if x in exceptions: 
            print("exceptions!!!") 
            b = len(x.split('.')[1])
            if b == 1:
                x = str(float(x) + 0.1)
            elif b == 2:
                x = str(float(x) + 0.01)
            elif b == 3:
                x = str(float(x) + 0.001)
            print('x = ' + x)
            continue
        else:
            print(x)
            b = len(x.split('.')[1])
            if b == 1:
                y = str(float(x) + 0.2)
                str(round(float(y),1))
            elif b == 2:
                y = str(float(x) + 0.02)
                str(round(float(y),2))
            elif b == 3:
                y = str(float(x) + 0.002)
                str(round(float(y),3))
            print(y)
            entry.tag_add('if', x, y)
            x = y
            if b == 1:
                y = str(float(x) + 0.1)
                str(round(float(y),1))
            elif b == 2:
                y = str(float(x) + 0.01)
                str(round(float(y),2))
            elif b == 3:
                y = str(float(x) + 0.001)
                str(round(float(y),3))
            entry.tag_remove('if', y, END)

def elif_function():
    global x, y, exceptions

    x = 1.0
    y = 0.0

    entry.tag_config("elif", foreground='purple')

    while True:
        x = entry.search('elif', x, stopindex=END)
        if not x: break
        else:
            print(x)
            b = len(x.split('.')[1])
            if b == 1:
                str(round(float(x),1))
                y = str(float(x) + 0.4)
                str(round(float(y),1))
            elif b == 2:
                str(round(float(x),2))
                y = str(float(x) + 0.04)
                str(round(float(y),2))
            elif b == 3:
                str(round(float(x),3))
                y = str(float(x) + 0.004)
                str(round(float(y),3))
            print(y)
            entry.tag_add('elif', x, y)
            if str(float(x) + 0.2) not in exceptions:
                if b == 1:
                    exceptions += [str(float(x) + 0.2)]
                    print(exceptions)
                elif b == 2:
                    exceptions += [str(float(x) + 0.02)]
                    print(exceptions)
                elif b == 3:
                    exceptions += [str(float(x) + 0.002)]
                    print(exceptions)
            x = y
            if b == 1:
                y = str(float(x) + 0.1)
            elif b == 2:
                y = str(float(x) + 0.01)
            elif b == 3:
                y = str(float(x) + 0.001)
            entry.tag_remove('elif', y, END)

def else_function():
    global x, y

    x = 1.0
    y = 0.0

    entry.tag_config("else", foreground='purple')

    while True:
        x = entry.search('else', x, stopindex=END)
        if not x:break
        print(x)
        b = len(x.split('.')[1])
        if b == 1:
            str(round(float(x),1))
            y = str(float(x) + 0.4)
            str(round(float(y),1))
        elif b == 2:
            str(round(float(x),2))
            y = str(float(x) + 0.04)
            str(round(float(y),2))
        elif b == 3:
            str(round(float(x),3))
            y = str(float(x) + 0.004)
            str(round(float(y),3))
        print(y)
        entry.tag_add('if', x, y)
        x = y
        if b == 1:
            y = str(float(x) + 0.4)
        elif b == 2:
            y = str(float(x) + 0.04)
        elif b == 3:
            y = str(float(x) + 0.004)
        entry.tag_remove('else', y, END)

def for_function():
    global x, y

    x = 1.0
    y = 0.0

    entry.tag_config("for", foreground='orange')

    while True:
        x = entry.search('for', x, stopindex=END)
        if not x:break
        print(x)
        b = len(x.split('.')[1])
        if b == 1:
            str(round(float(x),1))
            y = str(float(x) + 0.3)
            str(round(float(y),1))
        elif b == 2:
            str(round(float(x),2))
            y = str(float(x) + 0.03)
            str(round(float(y),2))
        elif b == 3:
            str(round(float(x),3))
            y = str(float(x) + 0.003)
            str(round(float(y),3))
        print(y)
        entry.tag_add('for', x, y)
        x = y
        if b == 1:
            y = str(float(x) + 0.3)
        elif b == 2:
            y = str(float(x) + 0.03)
        elif b == 3:
            y = str(float(x) + 0.003)
        entry.tag_remove('for', y, END)

def while_function():
    global x, y

    x = 1.0
    y = 0.0

    entry.tag_config("while", foreground='orange')

    while True:
        x = entry.search('while', x, stopindex=END)
        if not x:break
        print(x)
        b = len(x.split('.')[1])
        if b == 1:
            y = str(float(x) + 0.5)
        elif b == 2:
            y = str(float(x) + 0.05)
        elif b == 3:
            y = str(float(x) + 0.005)
        print(y)
        entry.tag_add('while', x, y)
        x = y
        if b == 1:
            y = str(float(x) + 0.5)
        elif b == 2:
            y = str(float(x) + 0.05)
        elif b == 3:
            y = str(float(x) + 0.005)
        entry.tag_remove('while', y, END)
#-----------------------------------------------------------------
def new_condition():
    global tab_count
    o = 0
    a = str(round(float(entry.index(INSERT)) - 1, 0))
    b =  str(round(float(a) + 1, 0))
    condition = entry.get(a,b)[:-1]
    print(a + ", " + b)
    print(condition)
    c = len(condition) - 1
    print(c)
    print(condition[c])

    count_tab_in_condition = condition.count("   ")
    if count_tab_in_condition != tab_count:
        tab_count = count_tab_in_condition
    if condition[c] == ":":
        tab_count += 1 
    while o < tab_count:
            entry.insert(b, "    ")
            o += 1
         #str(float(a) + 1.0)
        #entry.mark_set(INSERT, b)
        #entry.focus()
#-----------------------------------------------------------------
def equally_symbols():
    global x, y, symbols

    x = 1.0
    y = 0.0

    entry.tag_config("symbol", foreground='#CC0000')
    while True:
        x = entry.search('=', str(x), stopindex=END)
        if not x:break
        round(float(x), 3)
        print(x)
        b = len(x.split('.')[1])
        if b == 1:
            str(round(float(x),1))
            y = str(float(x) + 0.1)
            y = str(round(float(y),1))
        elif b == 2:
            str(round(float(x),2))
            y = str(float(x) + 0.01)
            y = str(round(float(y),2))
        elif b == 3:
            str(round(float(x),3))
            y = str(float(x) + 0.001)
            y = str(round(float(y),3))
        print(y)
        entry.tag_add('symbol', x, y)
        x = y
        if b == 1:
            y = str(float(x) + 0.1)
        elif b == 2:
            y = str(float(x) + 0.01)
        elif b == 3:
            y = str(float(x) + 0.001)
        entry.tag_remove('symbol', y, END)

def colon_symbols():
    global x, y, symbols

    x = 1.0
    y = 0.0

    entry.tag_config("symbol", foreground='#CC0000')
    while True:
        x = entry.search(':', str(x), stopindex=END)
        if not x:break
        round(float(x), 3)
        print(x)
        b = len(x.split('.')[1])
        if b == 1:
            str(round(float(x),1))
            y = str(float(x) + 0.1)
            y = str(round(float(y),1))
        elif b == 2:
            str(round(float(x),2))
            y = str(float(x) + 0.01)
            y = str(round(float(y),2))
        elif b == 3:
            str(round(float(x),3))
            y = str(float(x) + 0.001)
            y = str(round(float(y),3))
        print(y)
        entry.tag_add('symbol', x, y)
        x = y
        if b == 1:
            y = str(float(x) + 0.1)
        elif b == 2:
            y = str(float(x) + 0.01)
        elif b == 3:
            y = str(float(x) + 0.001)
        entry.tag_remove('symbol', y, END)

def semicolon_symbols():
    global x, y, symbols

    x = 1.0
    y = 0.0

    entry.tag_config("symbol", foreground='#CC0000')
    while True:
        x = entry.search(';', str(x), stopindex=END)
        if not x:break
        round(float(x), 3)
        print(x)
        b = len(x.split('.')[1])
        if b == 1:
            str(round(float(x),1))
            y = str(float(x) + 0.1)
            y = str(round(float(y),1))
        elif b == 2:
            str(round(float(x),2))
            y = str(float(x) + 0.01)
            y = str(round(float(y),2))
        elif b == 3:
            str(round(float(x),3))
            y = str(float(x) + 0.001)
            y = str(round(float(y),3))
        print(y)
        entry.tag_add('symbol', x, y)
        x = y
        if b == 1:
            y = str(float(x) + 0.1)
        elif b == 2:
            y = str(float(x) + 0.01)
        elif b == 3:
            y = str(float(x) + 0.001)
        entry.tag_remove('symbol', y, END)
#-----------------------------------------------------------------
def static_verbs_print():
    global x, y, verbs

    x = 1.0
    y = 0.0

    entry.tag_config("verb", foreground='blue')
    while True:
        x = entry.search('print', str(x), stopindex=END)
        if not x:break
        round(float(x), 3)
        print(x)
        b = len(x.split('.')[1])
        if b == 1:
            str(round(float(x),1))
            y = str(float(x) + 0.5)
            y = str(round(float(y),1))
        elif b == 2:
            str(round(float(x),2))
            y = str(float(x) + 0.05)
            y = str(round(float(y),2))
        elif b == 3:
            str(round(float(x),3))
            y = str(float(x) + 0.005)
            y = str(round(float(y),3))
        print(y)
        entry.tag_add('verb', x, y)
        x = y
        if b == 1:
            y = str(float(x) + 0.1)
        elif b == 2:
            y = str(float(x) + 0.01)
        elif b == 3:
            y = str(float(x) + 0.001)
        entry.tag_remove('verb', y, END)

def static_verbs_input():
    global x, y, verbs

    x = 1.0
    y = 0.0

    entry.tag_config("verb", foreground='blue')
    while True:
        x = entry.search('input', str(x), stopindex=END)
        if not x:break
        round(float(x), 3)
        print(x)
        b = len(x.split('.')[1])
        if b == 1:
            str(round(float(x),1))
            y = str(float(x) + 0.5)
            y = str(round(float(y),1))
        elif b == 2:
            str(round(float(x),2))
            y = str(float(x) + 0.05)
            y = str(round(float(y),2))
        elif b == 3:
            str(round(float(x),3))
            y = str(float(x) + 0.005)
            y = str(round(float(y),3))
        print(y)
        entry.tag_add('verb', x, y)
        x = y
        if b == 1:
            y = str(float(x) + 0.1)
        elif b == 2:
            y = str(float(x) + 0.01)
        elif b == 3:
            y = str(float(x) + 0.001)
        entry.tag_remove('verb', y, END)
#-----------------------------------------------------------------
def light_theme():
    entry.configure(background='#4C9900',fg='black')
    tk.configure(background='#4C9900')
    expansionFrame.configure(background='#4C9900',fg='black')
    importFrame.configure(background='#4C9900',fg='black')

    expansionInfo.configure(background='#4C9900',fg='black')
    importFile.configure(background='#4C9900',fg='black', activebackground='white')

    pas.configure(background='#4C9900',fg='black', activebackground='white')
    txt.configure(background='#4C9900',fg='black', activebackground='white')
    py.configure(background='#4C9900',fg='black', activebackground='white')
    bat.configure(background='#4C9900',fg='black', activebackground='white')
    cs.configure(background='#4C9900',fg='black', activebackground='white')

def dark_theme():
    entry.configure(background='black',fg='turquoise')
    tk.configure(background='black')
    expansionFrame.configure(background='black',fg='turquoise')
    importFrame.configure(background='black',fg='turquoise')

    expansionInfo.configure(background='black',fg='turquoise')
    importFile.configure(background='black',fg='turquoise', activebackground='turquoise')

    pas.configure(background='black',fg='turquoise', activebackground='turquoise')
    txt.configure(background='black',fg='turquoise', activebackground='turquoise')
    py.configure(background='black',fg='turquoise', activebackground='turquoise')
    bat.configure(background='black',fg='turquoise', activebackground='turquoise')
    cs.configure(background='black',fg='turquoise', activebackground='turquoise')
#-----------------------------------------------------------------
def check():
    #text = entry.get(2.0, 3.0)
    text= entry.cget('height')
    print(text)

def delete():
    entry.delete(1.0, END)

def save():
    global fileText
    text = entry.get(1.0, END)
    fileText = text
    ctypes.windll.user32.MessageBoxW(0, "File saved.", "Save", 0)

def undo():
    global fileText

    if fileText != '':
        entry.delete(1.0, END)
        entry.insert(1.0, fileText)
        ctypes.windll.user32.MessageBoxW(0, "The last save has been uploaded.", "Undo", 0)
    else:
        ctypes.windll.user32.MessageBoxW(0, "Not a single save was made during this session!", "Undo", 0)

def about():
    ctypes.windll.user32.MessageBoxW(0, "The project involves the creation of a universal environment for programming and working with text. Developer: Mr_next (INPH).", "About project", 0)

def help_f():
    ctypes.windll.user32.MessageBoxW(0, """Buttons:
About - brief information about the project. 
New - create a new file. Entering a name without an extension. 
Open - opening a file. Entering a name with an extension!
Save - create a checkpoint in the editor. 
Undo - rollback to the checkpoint. 
Clear - clear the input field. 
Help - opens a menu with buttons.  
Exit - exit the program.""", "Help", 0)

def fileOpen():
    global fileName
    
    window = Toplevel()
    window.geometry('150x75')
    nameLabel = Label(window, text = "Please, enter file name:")
    nameLabel.pack(side=TOP)
    nameEntry = Entry(window)
    nameEntry.pack(side=TOP)
    def saveFileName():
        global fileName, fileText, openedFile

        name_file = nameEntry.get()
        fileName = name_file.replace('.txt', '')
        fileName = name_file.replace('.pas', '')
        fileName = name_file.replace('.py', '')
        fileName = name_file.replace('.bat', '')
        with open(name_file, "r") as file:
            fileText = file.read()
        entry.delete(1.0, END)
        entry.insert(1.0, fileText)
        tk.title('Chameleon - ' + name_file)
        openedFile = True
        window.destroy()

    button = Button(window, text='Aply', command =   saveFileName)
    button.pack()
    
def  new():
    global fileName

    name_file = ''
    window = Toplevel()
    window.geometry('150x75')
    nameLabel = Label(window, text = "Please, enter file name:")
    nameLabel.pack(side=TOP)
    nameEntry = Entry(window)
    nameEntry.pack(side=TOP)
    def saveFileName():
        global fileName, fileText
        print("aaaaa")
        #print(nameEntry.get())
        name_file = nameEntry.get()
        entry.delete(1.0, END)
        fileName = name_file
        print(fileName)
        tk.title('Chameleon - ' + fileName)
        fileText = ''
        openedFile = False
        window.destroy()

    button = Button(window, text='Aply', command =   saveFileName)
    button.pack()
    
#--------------------------------------------------------------------

def pas():
    global expansionExport,a
    expansionInfo.config(text = "expansion: pas")
    expansionExport = 'pas'
    a = expansionExport
    print(a)

def txt():
    global expansionExport,a
    expansionInfo.config(text = "expansion: txt")
    expansionExport = 'txt'
    a = expansionExport
    print(a)

def py():
    global expansionExport, a
    expansionInfo.config(text = "expansion: py")
    expansionExport = 'py'
    a = expansionExport
    print(a)

def bat():
    global expansionExport, a
    expansionInfo.config(text = "expansion: bat")
    expansionExport = 'bat'
    a = expansionExport

def cs():
    global expansionExport, a
    expansionInfo.config(text = "expansion: cs")
    expansionExport = 'cs'
    a = expansionExport

def export():
    global a, fileName, fileText, openedFile
    save()
    fileName = fileName.replace('.txt', '')
    fileName = fileName.replace('.pas', '')
    fileName = fileName.replace('.py', '')
    fileName = fileName.replace('.bat', '')
    print(fileName)
    #if a != 'py' and a != 'pas':
        #a = 'txt'
    if fileName == '':
        file = open('Untitled' + '.' + a, "w+")
        #text = entry.get(1.0, END)
        file.write(fileText)
        file.close()
    else:
        print("fileName is " + fileName)
        file = open(fileName + '.' + a, "w+")
        #text = entry.get(1.0, END)
        file.write(fileText)
        file.close()
    ctypes.windll.user32.MessageBoxW(0, "The file has been successfully exported", "Export", 0)

#--------------------------------------------------------------------

mainmenu = Menu(expansionFrame, fg='turquoise', bg='black')
theme_menu = Menu(tearoff=0)
mainmenu.configure(background='black')
mainmenu.add_command(label = "About", command= about)
mainmenu.add_command(label = "New", command= new)
mainmenu.add_command(label = "Open", command= fileOpen)
mainmenu.add_command(label = "Save", command= save)
mainmenu.add_command(label = "Undo", command= undo)  
mainmenu.add_command(label = "Clear", command= delete)
mainmenu.add_cascade(label='Theme', menu=theme_menu)
theme_menu.add_command(label='Dark', command=dark_theme)
theme_menu.add_separator()
theme_menu.add_command(label='Light', command=light_theme)
mainmenu.add_command(label = "Help", command= help_f)
mainmenu.add_command(label = "Exit", command= tk.destroy)
 
tk.config(menu = mainmenu)
 
entry = Text(enterFrame, width = 100, fg='turquoise', bg='black', insertbackground='white')
entry.pack(side=LEFT, fill=Y)

scroll = Scrollbar(enterFrame, command=entry.yview)
scroll.pack(side=LEFT, fill=Y)

entry.config(yscrollcommand=scroll.set)


#my_entry.insert(0,'Username')
#my_entry.pack(padx = 5, pady = 5)

pas = Button(expansionFrame, text='.pas', command = pas, height = 2, fg='turquoise', bg='black', activebackground='turquoise')
pas.pack(side=TOP, fill=X)
txt = Button(expansionFrame, text='.txt', command = txt, height = 2, fg='turquoise', bg='black', activebackground='turquoise')
txt.pack(side=TOP, fill=X)
py = Button(expansionFrame, text='.py', command = py, height = 2, fg='turquoise', bg='black', activebackground='turquoise')
py.pack(side=TOP, fill=X)
bat = Button(expansionFrame, text='.bat', command = bat, height = 2, fg='turquoise', bg='black', activebackground='turquoise')
bat.pack(side=TOP, fill=X)
cs = Button(expansionFrame, text='.cs', command = cs, height = 2, fg='turquoise', bg='black', activebackground='turquoise')
cs.pack(side=TOP, fill=X)

expansionInfo = Label(importFrame, text = "expansion:", fg='turquoise', bg='black')
expansionInfo.pack()
importFile = Button(importFrame, text='export', command = export, height = 2, fg='turquoise', bg='black', activebackground='turquoise')
importFile.pack(side=TOP, fill=X)

#checkCode = Button(checkCodeFrame, text='intorpritate', height=2, command=intorpritator, fg='turquoise', bg='black', activebackground='turquoise')
#checkCode.pack(fill=X)
#--------------------------------------------------------------------

entry.bind("<KeyRelease>", intorpritator)
#entry.bind('<Return>', new_condition)
tk.mainloop()
#intorpritate()
#Mr_next_nikola
