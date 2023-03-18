from ast import For
from dataclasses import replace
from distutils import text_file
from hashlib import new
from logging import root
from operator import le
from tkinter import *
from tkinter import filedialog
import tkinter
from tkinter import messagebox
from tkinter.ttk import Separator
from tokenize import String


top = Tk()
top.minsize(600,400)
top.title('tp compilaction')
top["bg"] ="palevioletred"
menubar = Menu(top)
top.config(menu=menubar)

file_menu = Menu(
    menubar,
    tearoff=0
)

   

def openfile():  
    text_file = filedialog.askopenfile(filetypes = (("Text files", "*.txt"), ("All files", "*.*"))).name
    text_file = open(text_file, 'r')              
    content = text_file.read()
    BOX.delete('1.0', END)
    BOX.insert(END, content)
def savefile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text file", ".txt"), ("all files", ".*")])
    filetext = str(BOX.get("1.0",END))
    file.write(filetext)
    file.close()
file_menu.add_command(label="Open", command=openfile)
file_menu.add_command(label="Save", command=savefile)
file_menu.add_separator() 
def exit():
    i=0
    res = messagebox.askquestion('Exit','EXITE!')
    if (res=="yes"):
       top.destroy()
    else :
        i+=1
# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=exit  
)
menubar.add_cascade(
    label="File",
    menu=file_menu
)
analyse_menu = Menu(
    menubar,
    tearoff=0
)
operateur = ['+', '-', '*', '/','=',':=','<','>']    
separateur = ['(',')',',',';',':']
sig = ['+', '-']
nmbr =['0','1','2','3','4','5','6','7','8','9']
alph = ['a','b','c','d','e','f','i','j','k','l','m','n','o','p','q','r','s','t','v','v','w','X','z','']
cle=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','U','V','W','X','Y','Z']
i=0
fat = []
for i in range(21):
    ligne = []
    for j in range(11):
        ligne.append(-1)
    fat.append(ligne)
for L in fat :
    fat [0] [1] = 1
    fat [0] [2] = 2
    fat [0] [4] = 4
    fat [0] [5] = 5
    fat [0] [7] = 8
    fat [0] [8] = 11
    fat [0] [9] = 15
    fat [0] [7] = 11
    fat [0] [9] = 15
    fat [2] [3] =3
    fat [5] [4] =5
    fat [5] [5] =6
    fat [6] [4] =7
    fat [7] [5] =7
    fat [9] [4] =10
    fat [8] [4] =9
    fat [8] [7] =10
    fat [11] [5] =11
    fat [12] [5] =13
    fat [12] [7] =16
    fat [13] [5] =13
    fat [13] [6] =14
    fat [14] [5] =15
    fat [15] [5] =15
    fat [17] [5] =18
    fat [17] [9] =18
    fat [18] [5] =17
    fat [18] [8] =20
    fat [18] [9] =17
    fat [19] [8] =20    
    fat [20] [8] =19
def type(c):
    if c in separateur:
          return 0
    elif c in operateur:
          return 1
    elif c in ["<",">"]:
          return 2
    elif c in ["+"]:
          return 3
    elif c in nmbr:
          return 4
    elif c in ["&"]:
          return 5
    elif c in alph:
          return 6
    elif c in ["_"]:
          return 7
    elif c in ["="]:
          return 8
    elif c in ["."]:
          return 9
    elif c in ["|"]:
          return 10
    elif c in ["-"]:
          return 11
    elif c in ["#"]:
          return 12
    elif c in cle:
          return 13
    else :
          return -1


def Lexicale(event=""):
    BOX1.configure(state='normal')
    BOX1.delete('1.0', END)
    BOX11 = BOX.get("1.0","end-1c")
    BOX11 = BOX11.replace("\n"," ")
    i=0
    while i<len (BOX11):
        BOX11 = BOX11.replace("  "," ")
        i+=1
    i=0
    BOX12 ="" 
    while i <=len(BOX11)-1:
        if BOX11[i]!="$":
            BOX12+=BOX11[i]
        elif BOX11[i] == "$":
            i+=1
            while BOX11[i]!="$":
                if i<len (BOX)-1:
                    i+=1
                else :
                    BOX12 =BOX12.replace(" ","#")
                    BOX1.insert(1.0,BOX12)
                    return 0
        i+=1
    
    BOX12 =BOX12.replace(" ","#")
    BOX13=""
    j=0
    while j<len(BOX12):
        num=""
        if BOX12[j] in separateur:
            BOX13 +="#"+ BOX12[j]+ "#"
            j+=1
        elif BOX12[j] in operateur:
            BOX13 +="#"+ BOX12[j]+ "#"
            j+=1
        elif BOX12[j] in operateur and BOX12[j+1] =='#':
            BOX13 += BOX12[j]
            j+=1
        elif BOX12[j] in operateur and BOX12[j+1] !='#':
            BOX13 += BOX12[j]+ "#"
            j+=1
        elif BOX12[j] in operateur and BOX12[j+1] =='#':
            BOX13 += BOX12[j]
            j+=1
        elif BOX12[j] in operateur and BOX12[j-1] =='#':
            BOX13 += BOX12[j]+ "#"
            j+=1
        elif BOX12[j] in separateur and BOX12[j-1] =='#':
            BOX13 += BOX12[j]+ "#"
            j+=1
        elif BOX12[j] in operateur and BOX12[j+1] !='#' and BOX12[j-1] !='#':
            BOX13 += "#"+ BOX12[j]+ "#"
            j+=1
        elif BOX12[j] in operateur and BOX12[j+1] =='#'and BOX12[j-1] =='#':
            BOX13 += BOX12[j]
            j+=1
        else :
            BOX13 += BOX12[j]
            j+=1
            
    BOX13 = BOX13.replace( "##",'#')
    
    BOX13 =BOX13.replace("+#+#","+#+")
    BOX13 =BOX13.replace("-#-#","-#-")
    BOX13 =BOX13.replace("+#-#","+#-")
    BOX13 =BOX13.replace("-#+#","-#+")
    BOX13 =BOX13.replace("/#+#","/#+")
    BOX13 =BOX13.replace("*#+#","*#+")
    BOX13 =BOX13.replace("/#-#","/#-")
    BOX13 =BOX13.replace("*#-#","*#-")
    BOX13 =BOX13.replace("=#-#","=#-")
    BOX13 =BOX13.replace("=#+#","=#+")
    BOX13 =BOX13.replace(":#=#",":=#")
    BOX13 =BOX13.replace("<#=#","#<=#")
    BOX13 = BOX13.replace( "##",'#')
    BOX13 = BOX13+"#"
    BOX13 = BOX13.replace( "##",'#')     
    BOX13 =BOX13.replace("i#+#+","i#++#")
    BOX13 =BOX13.replace("i#-#-","i#--#")
    BOX13 =BOX13.replace("i#-#+","i#-+#")
    BOX13 =BOX13.replace("i#+#-","i#+-#")
    i=0
    BOX14 =""
    while i < len(BOX13)-1:
        if BOX13[i] in sig and BOX13[i+1]not in nmbr :
            BOX14 += BOX13[i]+ "#"
            #i+=1
        else :
            BOX14 += BOX13[i]
        i+=1
    BOX14 = BOX14.replace("#+#.","#+.")
    BOX14 = BOX14.replace("#+12#","#+12#")
    BOX14 = BOX14.replace("#-#.","#-.")
    BOX14 = BOX14.replace("#;#-##","#;#-")
    BOX14 = BOX14.replace("#;#+##","#;#+")
    BOX14 =BOX14.replace("i#+#+","i#++#")
    BOX14 =BOX14.replace("i#-#-","i#--#")
    BOX14 =BOX14.replace("i#-#+","i#-+#")
    BOX14 =BOX14.replace("i#+#-","i#+-#")
    BOX14 =BOX14.replace("+#+","++")
    BOX14 =BOX14.replace("+#+","--")
    BOX14 = BOX14.replace( "##",'#')
            
    
    BOX1.insert(1.0,BOX14+"#")
    BOX1.configure(state='disabled')
    print(BOX14)
    x=0
    t=""
    while x < len(BOX14):
        tc = BOX14[x]
        cc = type(tc)
        if cc == 0:
          print(tc + ":  separator\n")
        elif cc == 1:
          print(tc + ": operator\n")
        elif cc == 2:
          print(tc + ":  operator type two\n")
        elif cc == 3:
          print(tc + ": charachter and sign\n")
        elif cc == 4:
          print(tc + ": number\n")
        elif cc == 5:
            print(tc + ": this charachter is AND\n")
        elif cc == 6:
            print(tc + ": alphabetic\n")
        elif cc == 7:
            print(tc + ":  charachter is '_'\n")
        elif cc == 8:
            print(tc + ":  equale sign\n")
        elif cc == 9:
            print(tc + ": point\n")
        elif cc == 11:
            print(tc + ": minous sign\n")
        elif cc == 12:
            print("\n")
        elif cc == 13:
            print("MOT CLE")
        else :
            print(tc + ": reuur!!!\n")
        x+=1

top.bind('<Control-l>',Lexicale)

analyse_menu.add_command(label='Lexicale',command=Lexicale)
analyse_menu.add_command(label='Syntaxique')
analyse_menu.add_command(label='Sementique')

# add the analyse menu to the menubar
menubar.add_cascade(
    label="Analyse",
    menu=analyse_menu
)
BOX = Text (top, width=30, height=20)
BOX.grid(row=5, column=100, pady=60, padx=60)
BOX1 = Text(top, width=30, height=20)
BOX1.grid(row=5, column=105, pady=60, padx=60)
top.mainloop()