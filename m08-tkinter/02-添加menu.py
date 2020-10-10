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


if __name__ == "__main__":
    gw = GuiWindow()
    gw.root.mainloop()