#NOTE -- need to place used classes into seperate files and import them into main file to maintain clean code - will do soon

#import modules
import tkinter as tk
#create root of gui
root = tk.Tk()

#Application class for creating and initializing the application, child of tk
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.test_list = []
        self.selected_test = None
        
        #adjusting outer most GUI layout and options
        self.master.title("FireGuard Test")
        self.master.configure(background="#F4F6F6")
        self.master.attributes("-fullscreen",True)

        #create basic widgets
        self.create_widgets()
        
    #Function for creating baseline widgets
    def create_widgets(self):
        self.exit_btn = tk.Button(master=self.master, text="Exit", fg="red",
                                  command=self.master.destroy).grid(row=0,column=1)
        self.test_sect = tk.Frame(master=self.master, relief="raised",bd=2,bg="#FFFFFF",
                                  width=250,height=8000)#height of 8k - unsure of how to dynamically fit height
        self.test_sect.grid(row=0, column=0,rowspan=800)
       
    #Function for adding seperate tests to main application
    def add_test(self, test):
        self.test_list.append(test)

    #Function that plots generated tests
    def generate_tests(self):
        for i in range(len(self.test_list)):
            print(self.test_list[i])
            #grid the test class buttons intervaled with i
            self.test_list[i].test_btn.grid(row=18+i+i+i+i+i+i,column=0)#this works for setting interval distances between tests - find better solution later
            pass

    #Function for choosing the test to take
    def selection(self,test):
        self.selected_test = test
        print(test.test_name)
        print(self.selected_test)
        pass

#class for creating instances of different tests to add to application
class Test():
    def __init__(self, parent, questions=None, answers=None, test_name=None):
        self.parent=parent
        self.test_name=test_name
        self.test_btn = tk.Button(master=self.parent.master, bg="#88F19E", fg="white",padx=24,#make buttons more visually appealing
                                  pady=10, bd=2, relief='groove',text=self.test_name)
        self.test_btn.configure(font=("Roboto", 12, "bold"),command=lambda: self.parent.selection(self))#tell Application which test is being selected
        self.questions = questions
        self.answers = answers
        
#NOTE -- maybe use linked list data structure for maintaining order of questions in a test

#class for maintaining a given tests questions order
class Questions_List():
    def __init__(self, question):
        self.question = question
        self.next_question = next_question
        pass

#A Node class that will connect questions in a test, as well as hold the question data 
class Question():
    def __init__(self, package, next_question=None):
        self.package = package
        self.next_question = next_question
        pass

# Main functin for initializing the application and executing primary statements

def main():
    
    #instance of Application running mainloop
    app = Application(master=root)

    
    #testing
    t1q = ["q1","q2"]
    t1a = ["a1","a2"]
    test1 = Test(app, t1q, t1a, "test1 name")
    t2q = ["q3","q4"]
    t2a = ["a3", "a4"]
    test2 = Test(app, t2q, t2a, "test2 name")
    #testing
    app.add_test(test1)
    app.add_test(test2)
    
    app.generate_tests()
    app.mainloop()

main()

