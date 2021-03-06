import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import os
import pdfedit
from pathlib import Path

from tkinter import *
from tkinter import filedialog   #sub module 이라서 따로 임포트 해줌



root = Tk()
root.title("PDF TOOL")
root.geometry('600x700')
root.resizable(False, False)


initialPath = Path(os.getcwd()).parent
currMode = "init"

# combine dnd files into one keeping the order
def combine_file():
    list_file.delete(0,END)
    global currMode
    currMode = "comb"
    reset_label()
    txt_current.config(text="Combine PDF files")
    txt_explanation.config(text="select two or more PDF files to Combine. \n currently support jpg, jpeg, png files as well (converted to PDF page)")
    txt_filename1.config(state='normal')
    txt_filename2.config(state='disabled')
    txt_pageNum.config(state='disabled')
    btn_add_file.config(state='normal')
    btn_del_file.config(state='normal')
    
    files = filedialog.askopenfilenames(title="Select files to combine", filetypes =(("pdf file", "*.pdf"), ("All files", "*.*")), \
        initialdir = initialPath)
    for file in files:
        list_file.insert(END,file)

    # need to convert image Files


    return 

def extract_file():
    list_file.delete(0,END)
    global currMode
    currMode = "extract"
    reset_label()
    txt_current.config(text="Extract pages from a PDF file")
    txt_explanation.config(text="select a PDF file to extract part of the pages. \n put page number you want to extract together. NO COMMA ex) 1 2 3 5")
    txt_filename1.config(state='normal')
    txt_filename2.config(state='disabled')
    txt_pageNum.config(state='normal')
    btn_add_file.config(state='normal')
    btn_del_file.config(state='normal')

    files = filedialog.askopenfilename(title="Select a PDF file to extract", filetypes =(("pdf file", "*.pdf"), ("All files", "*.*")), \
    initialdir = initialPath)

    if files:
        list_file.insert(END,files)


def split_file():
    list_file.delete(0,END)
    global currMode
    currMode = "split"
    reset_label()
    txt_current.config(text="split a PDF File into two files")
    txt_explanation.config(text="select a PDF file to split. put one page number to split. \n ex) for a PDF file with 4 pages, putting 2 will return two files (1 and 2,3,4)")
    txt_filename1.config(state='normal')
    txt_filename2.config(state='normal')
    txt_pageNum.config(state='normal')
    btn_add_file.config(state='normal')
    btn_del_file.config(state='normal')

    files = filedialog.askopenfilename(title="Select a PDF file to split", filetypes =(("pdf file", "*.pdf"), ("All files", "*.*")), \
    initialdir = initialPath)
    if files:
        list_file.insert(END,files)



def strToint(pageNumString):
    map_obj = map(int,pageNumString.split())
    listInt = list(map_obj)
    for a in range(len(listInt)):
        listInt[a] -= 1
    return listInt

def reset_label():
    txt_filename1.delete(0,END)
    txt_filename1.insert(0, "File Name 1")
    txt_filename2.delete(0,END)
    txt_filename2.insert(0, "File Name 2")
    txt_pageNum.delete(0,END)
    txt_pageNum.insert(0, "Page Number")


def add_file():
    if (currMode == 'split' or currMode == 'extract') and list_file.size() >= 1:
        msgbox.showwarning("Warning","Can only have one file")
        return

    files = filedialog.askopenfilenames(title="Select files to add", filetypes =(("PDF files", "*.pdf"), ("All files", "*.*")), \
        initialdir = initialPath)
            # initialdir = r"C:\Users\Jay Kim\Desktop\pythonworkspace")  #r 넣으면 탈출문자든 뭐든 상관없이 뒤에 경로 그대로 쓰겠다는거임 \\ 같이 쓸 필요 없이
    #사용자가 선택한 파일들
    for file in files:
        list_file.insert(END,file)



def del_file():

    for index in reversed(list_file.curselection()):
        list_file.delete(index)

def up_file():

    indexs = list_file.curselection()
    if not indexs:
        return

    for ind in indexs:
        if ind == 0:
            return
        item = list_file.get(ind)
        list_file.delete(ind)
        list_file.insert(ind-1, item)

    # tolist = list(indexs)
    # for i in range(len(tolist)):
    #     tolist[i] -= 1
    # indexs = tuple(tolist)
    # list_file.selection_set(indexs)



def down_file():
    indexs = list_file.curselection()
    if not indexs:
        return

    for ind in reversed(indexs):
        if ind == (list_file.size()-1):
            return
        item = list_file.get(ind)
        list_file.delete(ind)
        list_file.insert(ind+1, item)
       
    # tolist = list(indexs)
    # for i in range(len(tolist)):
    #     tolist[i] += 1
    # indexs = tuple(tolist)
    # list_file.selection_set(indexs)




#save path  (put it in the option)
def browse_dest_path():
    
    folder_selected = filedialog.askdirectory(title="select directory", initialdir = initialPath)
    if folder_selected =="": #if canceled
        return

    txt_dest_path.config(state='normal')
    txt_dest_path.delete(0,END)   
    txt_dest_path.insert(0,folder_selected)
    txt_dest_path.config(state='disabled')


#시작
def start():

    #파일 목록 확인
    if list_file.size() ==0:
        msgbox.showwarning("Warning","Please add file")

    try:
        if currMode == "comb":
            pdfedit.pdf_combine(list_file.get(0,END), txt_filename1.get(), txt_dest_path.get())
            msgbox.showwarning("Done","Completed")
        elif currMode == "extract":
            pdfedit.pdf_extract(list_file.get(0), strToint(txt_pageNum.get()), txt_filename1.get(), txt_dest_path.get())
            msgbox.showwarning("Done","Completed")
        elif currMode == "split":
            pdfedit.pdf_split(list_file.get(0), strToint(txt_pageNum.get()), txt_filename1.get(), txt_filename2.get(), txt_dest_path.get())
            msgbox.showwarning("Done","Completed")
    except Exception as err:  #예외처리
        msgbox.showerror("error", err)

  

#File Frame ()

file_frame = Frame(root, width=550, height=40)
file_frame.pack(fill="x", padx=5, pady=5)   #양옆으로 쭉 채움
file_frame.propagate(0)

btn_comb_file = Button(file_frame,padx=7, pady=5, width=12, text="PDF COMBINE", command=combine_file)
btn_comb_file.pack(side="left")

btn_extract_file = Button(file_frame, padx=7, pady=5, width=12, text="PDF EXTRACT", command= extract_file)
btn_extract_file.pack(side="left")

btn_split_file = Button(file_frame, padx=7, pady=5, width=12, text="PDF SPLIT", command= split_file)
btn_split_file.pack(side="left")



#current frame with file name
frame_current = LabelFrame(root, height=140)
frame_current.pack(fill="x", padx=5, pady=5, ipady=20)
frame_current.propagate(0)

txt_current = Label(frame_current, text="Current Mode", font = ("Arial", 15))
txt_current.pack()


txt_explanation = Label(frame_current, text="select option above. \n -------------------------------------", font = ("Arial", 10))
txt_explanation.pack()

txt_filename1 = Entry(frame_current)
txt_filename1.insert(END, "File Name 1")
txt_filename1.config(state = 'disabled')
txt_filename1.pack(side="left", expand = True, padx=10, pady=5, ipady=4) 
txt_filename2 = Entry(frame_current)
txt_filename2.insert(END, "File Name 2")
txt_filename2.config(state = 'disabled')
txt_filename2.pack(side="left", expand = True, padx=10, pady=5, ipady=4) 

txt_pageNum = Entry(frame_current)
txt_pageNum.insert(END, "Page Number")
txt_pageNum.config(state = 'disabled')
txt_pageNum.pack(side="left", expand = True, padx=10, pady=5, ipady=4) 


btn_add_file = Button(frame_current, padx=7, pady=5, width=12, text="Add Files", command= add_file)
btn_add_file.place(x=20, y= 140)
btn_add_file.config(state='disabled')


btn_del_file = Button(frame_current, padx=7, pady=5, width=12, text="Delete Files", command= del_file)
btn_del_file.place(x=445, y = 140)
btn_del_file.config(state='disabled')


#file list frame (Drag drop frame)
list_frame = Frame(root, height=300)
list_frame.pack(fill="x", padx=5, pady=5)
list_frame.propagate(0)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")
scrollbar_x = Scrollbar(list_frame, orient=HORIZONTAL)
scrollbar_x.pack(side="bottom", fill="x")


# check tkinter.dnd docs  (maybe later)
# https://docs.python.org/3/library/tkinter.dnd.html#module-tkinter.dnd
# https://stackoverflow.com/questions/44887576/how-can-i-create-a-drag-and-drop-interface
# https://www.youtube.com/watch?v=JIy0QjwQBl0&ab_channel=RamonWilliams


list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar_x.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)
scrollbar_x.config(command=list_file.xview)

btn_up_file = Button(list_frame, padx=7, pady=5, width=5, text="Up", command= up_file)
btn_up_file.place(x=510, y= 100)

btn_down_file = Button(list_frame, padx=7, pady=5, width=5, text="Down", command= down_file)
btn_down_file.place(x=510, y = 135)



#result file path
path_frame = LabelFrame(root, text="Save Path", width=550, height=70)
path_frame.pack(fill="x", padx=5, pady=5)
path_frame.propagate(0)


txt_dest_path = Entry(path_frame)
txt_dest_path.insert(END, initialPath)
txt_dest_path.pack(side="left", fill="x", expand = True, padx=5, pady=5, ipady=4)    #ipad = innerpad
txt_dest_path.config(state='disabled')

btn_dest_path = Button(path_frame, text="Browse", width="10", command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)







#run frame
frame_run = Frame(root, width=550, height=100)
frame_run.pack(fill="x", padx=5, pady=5)
frame_run.propagate(0)

btn_start = Button(frame_run, padx = 5, pady = 5, text ="Start", width=12, command = start)
btn_close = Button(frame_run, padx = 5, pady = 5, text ="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start.pack(side="right", padx=5, pady=5)    #닫기 먼저 오른쪽에 배치하고 그다음에 시작버튼

root.mainloop()
