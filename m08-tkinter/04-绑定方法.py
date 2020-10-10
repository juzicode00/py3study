'''
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.9.5
'''
print('\n')
print('-----欢迎来到www.juzicode.com')
print('-----公众号: 桔子code/juzicode \n')   


from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
from tkinter import filedialog

class GuiWindow():
    def __init__(self):
        self.root=Tk()
        self.root.title('桔子code')
        self.root.geometry('500x300')

        #创建菜单栏
        self.menu_bar = Menu(self.root)
        self.root['menu'] = self.menu_bar
        #创建一级菜单
        self.menu_file = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="文件", menu=self.menu_file)
        #创建二级菜单
        self.menu_file.add_command(label='保存', command = None) #command对应要执行的动作
        self.menu_file.add_command(label='退出', command = self.root.quit)


        #添加fame
        self.frame_base = ttk.Frame(self.root,width =20, height = 30)
        self.frame_base.pack(side=TOP,fill=BOTH,padx = 10)   

        self.select_file_button = Button(self.frame_base,width =12,text='选择文件',command= self.select_file_button_command)
        self.select_file_button.pack(side=LEFT, padx=5, pady=2,fill=BOTH)
        self.select_file_entry = Entry(self.frame_base, text='选择文件:', width=40)
        self.select_file_entry.pack(side=LEFT, padx=5, pady=5,fill=BOTH,expand=1)  #
        self.select_file_clear_button = Button(self.frame_base,width =12,text='清除状态栏',command= None)
        self.select_file_clear_button.pack(side=LEFT, padx=5, pady=2)  # fill=BOTH,

   
        #添加tab控件
        self.tab_all = ttk.Notebook(self.root) 
        self.tab_all.pack(expand=1, fill=BOTH)  

        self.tab_1 = Frame(self.tab_all)
        self.tab_all.add(self.tab_1, text=' tab1 ')  
        self.tab_2 = Frame(self.tab_all)
        self.tab_all.add(self.tab_2, text=' tab2 ') 

        self.tab_1_radio_var = IntVar()
        self.tab_1_radio_method1 = Radiobutton(self.tab_1, text="方法1", variable=self.tab_1_radio_var, value=1, command=None)  
        self.tab_1_radio_method1.pack(side = BOTTOM)  #grid( row=1 ,column=0)
        self.tab_1_radio_method2 = Radiobutton(self.tab_1, text="方法2", variable=self.tab_1_radio_var, value=2, command=None) 
        self.tab_1_radio_method2.pack(side = BOTTOM)  #grid(row=2,column=0, )


        #frame中添加frame
        self.frame_status = ttk.Frame(self.root) 
        self.frame_status.pack(side=TOP,fill=BOTH,padx = 10)  

        self.frame_status_sub1 = ttk.Frame(self.frame_status) ##frame中添加下级frame
        self.frame_status_sub1.pack(side=TOP, fill=BOTH,padx = 10,pady = 10 )

        self.quit_button = Button(self.frame_status_sub1,text='退出',width = 10,padx=10,command=None)
        self.quit_button.pack(side = RIGHT)
        self.status_clear_button = Button(self.frame_status_sub1,text='清除',width = 10,padx=10,command=None)
        self.status_clear_button.pack(side = RIGHT)

        self.text_status = ScrolledText(self.frame_status,wrap = WORD,width =50, height = 50) 
        self.text_status.pack(side = BOTTOM ,fill=BOTH, )
 
    def select_file_button_command(self):
        self.selected_file = filedialog.askopenfilename()
        print('selected_file:',self.selected_file)
        self.select_file_entry.delete(0, END)
        self.select_file_entry.insert(0, self.selected_file)



if __name__ == "__main__":
    gw = GuiWindow()
    gw.root.mainloop()