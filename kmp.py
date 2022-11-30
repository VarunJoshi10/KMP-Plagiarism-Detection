import re
import os
from tkinter import *
from tkinter import filedialog,ttk,messagebox
from tkinter.filedialog import askopenfile


def computeLPSArray(pat, M, lps):
    len = 0
    lps[0]
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

def KMPSearch(pat, text, p):

    M = len(pat)
    N = len(text)
    lps = [0]*M
    j = 0 
    computeLPSArray(pat, M, lps)
 
    i = 0 
    while i < N:
        if pat[j].lower() == text[i].lower():
            i += 1
            j += 1
 
        if j == M:
            p +=1
            j = lps[j-1]
            break

        elif i < N and pat[j].lower() != text[i].lower():
            if j != 0:
                j = lps[j-1]
            else:
                i += 1      
    return p

def plag():    
    Text = open(root_file,"r")
    text = Text.read()

    pattern_file = open(plagiarised_file,"r").read()
    sentences = re.split(r'[\.\?!\r\n]', pattern_file)
    counter_matched = 0
    counter_total = 0
    p=0
    for pattern in sentences:
        pattern = pattern.strip()
        if len(pattern) > 0:
            counter_total +=1
            counter_matched += KMPSearch(pattern, text,p)
            
    messagebox.showinfo("Plag Percentage","Match percentage = %0.2f%%" % (counter_matched*100/counter_total))
    l1.destroy()
    l2.destroy()    

def root_select():
   file = filedialog.askopenfile(mode='r')
   global root_file
   if file:
      root_file = os.path.abspath(file.name)
      global l1
      l1=Label(root, text="The File is located at : " + str(root_file), font=('Aerial 9')).place(x=50,y=130)

def plag_select():
   file = filedialog.askopenfile(mode='r')
   global plagiarised_file
   if file:
      plagiarised_file = os.path.abspath(file.name)
      global l2
      l2=Label(root, text="The File is located at : " + str(plagiarised_file), font=('Aerial 9')).place(x=50,y=200)

#GUI
root=Tk()
root.title("Plagiarism Checker")
root.geometry("400x400")
label=Label(root,text="Plagiarism Checker",font=('Arial',20))
label.place(x=100,y=50)
btn1=Button(root,text="Select Root File",command=root_select)
btn1.place(x=120,y=100)
btn2=Button(root,text="Select Plagiarised File",command=plag_select)
btn2.place(x=120,y=170)
btn3=Button(root,text="Check Plagiarism",command=plag)
btn3.place(x=120,y=240)
root.mainloop()

