from tkinter import *
import tkinter.messagebox

class CauHoi:
    def __init__(self, answer):
        greeting = Label(root, text = "Chào em, anh đứng đây từ chiều, anh hỏi em 1 câu nhé", bg = 'white', fg = 'green')
        greeting.grid(row = 1, column = 1, sticky = E)

        self.printButton = Button(root, text = "Hỏi em đi anh ơi ư ư", command = self.printQuestion)
        self.printButton.grid(row = 2, column = 1, sticky = W)

        self.printButton = Button(root, text = "Anh biến đi", command = self.printMessage)
        self.printButton.grid(row = 2, column = 4)

    def printMessage(self):
        tkinter.messagebox.showwarning('Chọn sai rồi', "Em chọn thế là không đúng rồi, chọn lại đi em!!!")

    def printQuestion(self):
        question1 = Label(root, text = "Em yêu anh đúng k 😊?", bg = "white", fg = "red")
        question1.grid(row = 4, column = 1)
    
        self.printButton = Button(root, text = "Đúng rồi ạ", command = self.printAnswer)
        self.printButton.grid(row = 5, column = 1, sticky = W)
        self.printButton = Button(root, text = "Có ứt", command = self.printMessage)
        self.printButton.grid(row = 5, column = 4)
     
    def printAnswer(self):
        tkinter.messagebox.showinfo("Good choice baby", "Anh cũng iu em hí hí 😘😘😘")
        self.quitButton = Button(root, text = "Quit", command = root.quit)
        self.quitButton.grid(row = 5, column = 7)

def disable_event():
    pass

root = Tk()
root.title('Lời tỏ tình dễ thương')
root.protocol("WM_DELETE_WINDOW", disable_event)
a = CauHoi(root)
root.mainloop()