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
        self.master.configure(background="#F5F5F5")
        self.master.attributes("-fullscreen",True)
        #self.master.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,8,19,20),weight=1)
        #self.master.columnconfigure(0, weight=1)

        #create 5 col/6 row grid
        self.master.columnconfigure((0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24), weight=1)
        self.master.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18), weight=1)
        #create basic widgets
        self.create_widgets()
        
        
    #Function for creating baseline widgets
    def create_widgets(self):

        #Section for holding the created tests
        self.test_sect = tk.Frame(master=self.master, relief="groove",bd=2,bg="#AEE8B6")
        self.test_sect.grid(row=0, column=0, rowspan=20, columnspan=1, sticky="NSEW")
        self.test_sect.columnconfigure((0,1,2,3,4),weight=1)
        
        self.test_sect_header = tk.Label(master=self.test_sect, text="Template Title", bd=2, bg="#FFFFFF",relief="flat", width=14)
        self.test_sect_header.grid(row=1, column=2,pady=100,ipady=40)
        self.test_sect_header.configure(font=("Stencil", 16, "bold"))

        self.header_sect = tk.Frame(master=self.master, relief="flat",bg="#FFFFFF",highlightthickness=2)
        self.header_sect.configure(highlightbackground="black")
        self.header_sect.rowconfigure((0,1,2),weight=1)
        self.header_sect.columnconfigure((0,1,2),weight=1)
        self.header_sect.grid(row=2, column=12,rowspan=2,sticky="NSEW")
        
        self.header_sect_label = tk.Label(master=self.header_sect, text="No Test Selected", justify="center")
        self.header_sect_label.configure(font=("Arial", 40, "bold"),bg="#FFFFFF",width=20)
        self.header_sect_label.grid(column=1,row=1)

        self.body_sect = tk.Frame(master=self.master, relief="groove",bg="#FFFFFF", bd=4)
        self.body_sect.rowconfigure((0,1,2,3,4), weight=1)
        self.body_sect.columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)
        self.body_sect.grid(row=5, column=6, sticky="NSEW", columnspan=13, rowspan=11)

        self.body_sect_default_label = tk.Label(master=self.body_sect, text="Please select a test to begin.", justify="center")
        self.body_sect_default_label.configure(font=("Times New Roman",20, "bold"),bg="#FFFFFF")
        self.body_sect_default_label.grid(row=0, column=5, rowspan=2)

    #Function for adding seperate tests to main application
    def add_test(self, test):
        self.test_list.append(test)

    #Function that plots generated tests
    def generate_tests(self):
        for i in range(len(self.test_list)):
            print(self.test_list[i])
            #grid the test class buttons intervaled with i
            self.test_list[i].test_btn.grid(row=5+i,column=2, pady=24)#this works for setting interval distances between tests - find better solution later

    #Function for choosing the test to take
    def selection(self,test):
        self.selected_test = test
        print(test.test_name)
        print(self.selected_test)
        question = self.questions.get_head_question()
        print(question.get_next_question().get_question())
        self.set_test_header()
        self.body_sect_default_label.destroy()
        self.create_test_start_btn()

    def set_test_header(self):
        self.header_sect_label.config(text=self.selected_test.test_name)

    def create_test_start_btn(self):
        self.start_btn = tk.Button(master=self.body_sect,text="Start",fg="#FFFFFF",bg="#AEE8B6",justify="center")
        self.start_btn.grid(row=4, column=10, ipadx=30, ipady=6, padx=12)
        self.start_btn.configure(font=("Arial", 21, "bold"))
        
#class for creating instances of different tests to add to application
class Test():
    def __init__(self, parent, questions=None, answers=None, test_name=None):
        self.parent=parent
        self.test_name=test_name
        self.test_btn = tk.Button(master=self.parent.test_sect, bg="#FFFFFF", fg="black",padx=24,#make buttons more visually appealing
                                  pady=14, bd=2, relief='raised',text=self.test_name, height=1, width=8)
        self.test_btn.configure(font=("Roboto", 12, "bold"),command=lambda: self.parent.selection(self))#tell Application which test is being selected
        self.questions = questions
        self.answers = answers
        
#NOTE -- maybe use linked list data structure for maintaining order of questions in a test

#class for maintaining a given tests questions order
class Questions_List():
    def __init__(self, question):
        self.head_question = question
        
    def get_head_question(self):
        return self.head_question
    
    def insert_begenning(self, question):
        new_question = question
        new_question.set_next_question(self.head_question)
        self.head_question = new_question

    def remove_question(self, question_to_remove):
        current_question = self.get_head_question()
        if current_question.get_question() == current_question:
            self.head_question = current_question.get_next_question()
        else:
            while current_question:
                next_question = current_question.get_next_question()
                if next_question.get_value() == question_to_remove:
                    current_question.set_next_question(next_question.get_next_question())
                    current_question = None
                else:
                    current_question = next_quetion

    
#A Node class that will connect questions in a test, as well as hold the question data 
class Question():
    def __init__(self, package, next_question=None):
        self.package = package
        self.next_question = next_question
        pass

    def set_next_question(self, next_question):
        self.next_question = next_question

    def get_next_question(self):
        return self.next_question

    def get_question(self):
        return self.package
# Main functin for initializing the application and executing primary statements

package1 = {"question": "How are you today?",
           "choices": {"A": "good", "B": "bad", "C": "Okay"},
           "answer": "A"}

package2 = {"question2": "How are you today?",
           "choices": {"A": "good", "B": "bad", "C": "Okay"},
           "answer": "A"}
def main():
    
    #instance of Application running mainloop
    app = Application(master=root)
    question_1 = Question(package1)
    question_2 = Question(package2)
    question_list_1 = Questions_List(question_1)
    question_list_1.insert_begenning(question_2)
    
    #testing
    t1q = ["q1","q2"]
    t1a = ["a1","a2"]
    test1 = Test(app, t1q, t1a, "Test 1")
    t2q = ["q3","q4"]
    t2a = ["a3", "a4"]
    test2 = Test(app, t2q, t2a, "Test 2")
    app.questions = question_list_1
    #testing
    app.add_test(test1)
    app.add_test(test2)
    
    app.generate_tests()
    
    app.mainloop()

main()

