import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import dragdrop as dd

from tkinter import *
from tkinter import filedialog   #sub module 이라서 따로 임포트 해줌



root = Tk()
root.title("PDF TOOL")
root.resizable(False, False)


# combine dnd files into one keeping the order
def combine_file():
    msgbox.showinfo("combine","going to combine")
    return 


def extract_file():
    msgbox.showinfo("extract", "going to extract")
    return 


def temp_file():
    msgbox.showinfo("Temp", "going to temp")
    return 

def setting_program():
    msgbox.showinfo("setting", "going to Setting")
    return 




#save path  (put it in the option)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected =="": #if canceled
        return

    # txt_dest_path.delete(0,END)   
    # txt_dest_path.insert(0,folder_selected)


#시작
def start():

    #파일 목록 확인
    if list_file.size() ==0:
        msgbox.showwarning("Warning","Please add file")
        return

#File Frame ()

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)   #양옆으로 쭉 채움

btn_comb_file = Button(file_frame,padx=7, pady=5, width=12, text="PDF COMBINE", command=combine_file)
btn_comb_file.pack(side="left")

btn_extract_file = Button(file_frame, padx=7, pady=5, width=12, text="PDF EXTRACT", command= extract_file)
btn_extract_file.pack(side="left")

btn_temp_file = Button(file_frame, padx=7, pady=5, width=12, text="temperary", command= temp_file)
btn_temp_file.pack(side="left")



#dnd frame (Drag drop frame)
dnd_frame = Frame(root)
dnd_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(dnd_frame)
scrollbar.pack(side="right", fill="y")
scrollbar_x = Scrollbar(dnd_frame, orient=HORIZONTAL)
scrollbar_x.pack(side="bottom", fill="x")


# check tkinter.dnd docs
# https://docs.python.org/3/library/tkinter.dnd.html#module-tkinter.dnd
# https://stackoverflow.com/questions/44887576/how-can-i-create-a-drag-and-drop-interface
# https://www.youtube.com/watch?v=JIy0QjwQBl0&ab_channel=RamonWilliams


list_file = Listbox(dnd_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set, xscrollcommand=scrollbar_x.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)
scrollbar_x.config(command=list_file.xview)

dnd = dd.DragManager()
dnd.add_dragable(list_file)



#result file path
# path_frame = LabelFrame(root, text="Save Path")
# path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

# txt_dest_path = Entry(path_frame)
# txt_dest_path.pack(side="left", fill="x", expand = True, padx=5, pady=5, ipady=4)    #ipad = innerpad

# btn_dest_path = Button(path_frame, text="", width="10", command=browse_dest_path)
# btn_dest_path.pack(side="right", padx=5, pady=5)


#setting frame
frame_setting = LabelFrame(root, text="Setting")
frame_setting.pack(padx=5, pady=5, ipady=5)


#button setting up for default save path
btn_setting_file = Button(frame_setting,padx=5, pady=5, width=12, text="Setting", command=setting_program)
btn_setting_file.pack(side="left")



#run frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_start = Button(frame_run, padx = 5, pady = 5, text ="Start", width=12, command = start)
btn_close = Button(frame_run, padx = 5, pady = 5, text ="Close", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)
btn_start.pack(side="right", padx=5, pady=5)    #닫기 먼저 오른쪽에 배치하고 그다음에 시작버튼

root.mainloop()
