import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import dragdrop as dd
import os
import pdfedit

from tkinter import *
from tkinter import filedialog   #sub module 이라서 따로 임포트 해줌



root = Tk()
root.title("PDF TOOL")
root.resizable(False, False)

currMode = "init"

# combine dnd files into one keeping the order
def combine_file():
    list_file.delete(0,END)
    global currMode
    currMode = "comb"
    reset_label()
    txt_current.config(text="Combine PDF files")
    txt_explanation.config(text="select two or more PDF files to Combine. \n currently support jpeg, png files as well (converted to PDF page")
    txt_filename1.config(state='normal')
    txt_filename2.config(state='disabled')
    txt_pageNum.config(state='disabled')
    
    # msgbox.showinfo("combine","going to combine")
    files = filedialog.askopenfilenames(title="Select files to combine", filetypes =(("pdf file", "*.pdf"), ("모든 파일", "*.*")), \
        initialdir = os.getcwd())
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
    txt_explanation.config(text="select a PDF file to extract part of the pages. \n put page number you want to extract together \nNO COMMA ex) 1 2 3 5")
    txt_filename1.config(state='normal')
    txt_filename2.config(state='disabled')
    txt_pageNum.config(state='normal')

    files = filedialog.askopenfilename(title="Select a PDF file to extract", filetypes =(("pdf file", "*.pdf"), ("모든 파일", "*.*")), \
    initialdir = os.getcwd())

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

    files = filedialog.askopenfilename(title="Select a PDF file to split", filetypes =(("pdf file", "*.pdf"), ("All files", "*.*")), \
    initialdir = os.getcwd())

    list_file.insert(END,files)


def setting_program():
    global currMode
    currMode = "setting"
    reset_label()
    list_file.delete(0,END)
    msgbox.showinfo("setting", "going to Setting")
    txt_current.config(text="Select Mode")
    txt_filename1.config(state='disabled')
    txt_filename2.config(state='disabled')
    txt_pageNum.config(state='disabled')
    return 

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
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes =(("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir = os.getcwd())
            # initialdir = r"C:\Users\Jay Kim\Desktop\pythonworkspace")  #r 넣으면 탈출문자든 뭐든 상관없이 뒤에 경로 그대로 쓰겠다는거임 \\ 같이 쓸 필요 없이
    #사용자가 선택한 파일들
    for file in files:
        list_file.insert(END,file)




#save path  (put it in the option)
def browse_dest_path():
    folder_selected = filedialog.askdirectory(title="select directory", initialdir = os.getcwd())
    if folder_selected =="": #if canceled
        return

    txt_dest_path.delete(0,END)   
    txt_dest_path.insert(0,folder_selected)


#시작
def start():

    #파일 목록 확인
    if list_file.size() ==0:
        msgbox.showwarning("Warning","Please add file")

    try:
        if currMode == "comb":
            pdfedit.pdf_combine(list_file.get(0,END), txt_filename1.get())
        elif currMode == "extract":
            pdfedit.pdf_extract(list_file.get(0), strToint(txt_pageNum.get()), txt_filename1.get())
        elif currMode == "split":
            pdfedit.pdf_split(list_file.get(0), strToint(txt_pageNum.get()), txt_filename1.get(), txt_filename2.get())
    except Exception as err:  #예외처리
        msgbox.showerror("error", err)
    else:
        msgbox.showwarning("Done","Completed")
    
  

#File Frame ()

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)   #양옆으로 쭉 채움

btn_comb_file = Button(file_frame,padx=7, pady=5, width=12, text="PDF COMBINE", command=combine_file)
btn_comb_file.pack(side="left")

btn_extract_file = Button(file_frame, padx=7, pady=5, width=12, text="PDF EXTRACT", command= extract_file)
btn_extract_file.pack(side="left")

btn_split_file = Button(file_frame, padx=7, pady=5, width=12, text="PDF SPLIT", command= split_file)
btn_split_file.pack(side="left")

# maybe delete setting button (no need)
btn_setting_file = Button(file_frame,padx=5, pady=5, width=12, text="Setting", command=setting_program)
btn_setting_file.pack(side="left")


#current frame with file name
frame_current = LabelFrame(root, text="")
frame_current.pack(fill="x", padx=10, pady=20, ipady=50)

txt_current = Label(frame_current, text="Current Mode", font = ("Arial", 15))
txt_current.pack()


txt_explanation = Label(frame_current, text="", font = ("Arial", 10))
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



#file list frame (Drag drop frame)
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

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



#result file path
path_frame = LabelFrame(root, text="Save Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)


txt_dest_path = Entry(path_frame)
txt_dest_path.insert(END, os.getcwd())
txt_dest_path.pack(side="left", fill="x", expand = True, padx=5, pady=5, ipady=4)    #ipad = innerpad

btn_dest_path = Button(path_frame, text="Browse", width="10", command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)







#run frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_start = Button(frame_run, padx = 5, pady = 5, text ="Start", width=12, command = start)
btn_close = Button(frame_run, padx = 5, pady = 5, text ="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start.pack(side="right", padx=5, pady=5)    #닫기 먼저 오른쪽에 배치하고 그다음에 시작버튼

root.mainloop()
