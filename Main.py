#import modules
import tkinter as tk

#create root of gui
root = tk.Tk()

#Application class for creating and initializing the application, child of tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.testlist = []
        self.create_widgets()
        
    #Function for creating baseline widgets
    def create_widgets(self):
        self.exit_btn = tk.Button(self.master, text="Exit", fg="red",
                                  command=self.master.destroy).grid(row=1,column=1)
        self.test = tk.Label(self.master, text="eeepepepee").grid(row=0,column=4)
    #Function for adding seperate tests
    def add_test(self, test):
        self.testlist.append(test)

#class for creating instances of different tests to add to application
class Test:
    def __init__(self, questions, answers, test_name):
        self.questions = questions
        self.answers = answers
        self.test_name = test_name

# for testing
t1q = ["whats up", "hows it goin", "who are you"]
t1a = ["not much","okay","aaron"]
t1n = "First test"
test1 = Test(t1q,t1a,t1n)
print(test1.questions[0])
print(test1.answers[0])
# for testing

# Main functin for initializing the application and executing primary statements

def main():
    
    #instance of Application running mainloop
    app = Application(master=root)
    
    app.add_test(test1)
    app.mainloop()

main()
