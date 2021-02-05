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

        #create 5 col/6 row grid
        self.master.columnconfigure((0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24), weight=1)
        self.master.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18), weight=1)
        #create basic widgets
        self.create_widgets()
        
        
    #Function for creating baseline widgets
    def create_widgets(self):

        #Section for holding the created tests

        #creating and placing section to hold a list of tests
        self.test_sect = tk.Frame(master=self.master, relief="groove",bd=2,bg="#AEE8B6")
        self.test_sect.grid(row=0, column=0, rowspan=20, columnspan=1, sticky="NSEW")
        self.test_sect.columnconfigure((0,1,2,3,4),weight=1)
        #####

        #title for test section
        self.test_sect_header = tk.Label(master=self.test_sect, text="Template Title", bd=2, bg="#FFFFFF",relief="flat", width=14)
        self.test_sect_header.grid(row=1, column=2,pady=100,ipady=40)
        self.test_sect_header.configure(font=("Stencil", 16, "bold"))
        #####

        #primary header section for showing selected test title
        self.header_sect = tk.Frame(master=self.master, relief="flat",bg="#FFFFFF",highlightthickness=2)
        self.header_sect.configure(highlightbackground="black")
        self.header_sect.rowconfigure((0,1,2),weight=1)
        self.header_sect.columnconfigure((0,1,2),weight=1)
        self.header_sect.grid(row=2, column=12,rowspan=2,sticky="NSEW")
        #####
        
        #primary header
        self.header_sect_label = tk.Label(master=self.header_sect, text="No Test Selected", justify="center")
        self.header_sect_label.configure(font=("Arial", 40, "bold"),bg="#FFFFFF",width=20)
        self.header_sect_label.grid(column=1,row=1)
        #####

        #body section to hold questions in each test
        self.body_sect = tk.Frame(master=self.master, relief="groove",bg="#FFFFFF", bd=4)
        self.body_sect.rowconfigure((0,1,2,3,4), weight=1)
        self.body_sect.columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)
        self.body_sect.grid(row=5, column=6, sticky="NSEW", columnspan=13, rowspan=11)
        self.body_sect.grid_propagate(0) #this line makes body_sect stay the same size regardless of text inside of frame.
        #####

        #default label when a test has not been selected - located in body section
        self.body_sect_default_label = tk.Label(master=self.body_sect, text="Please select a test to begin.", justify="center")
        self.body_sect_default_label.configure(font=("Times New Roman",20, "bold"),bg="#FFFFFF")
        self.body_sect_default_label.grid(row=0, column=5, rowspan=2)

        #label to describe a test when selected - located in body section - replaces default label after test as been selected
        self.body_sect_description = tk.Label(master=self.body_sect, text="", justify="center")
        #label to describe a question in a given test
        self.question_label = tk.Label(master=self.body_sect, text="")

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
        self.set_test_header()
        self.body_sect_default_label.destroy()
        self.setup_test()

    def set_test_header(self):
        self.header_sect_label.config(text=self.selected_test.test_name)

    #removes default test label, creates a button to innitiate a selected test, and  shows a selected tests description
    def setup_test(self):
        self.question_label.configure(text="")
        self.body_sect_description.configure(text="")
        self.start_btn = tk.Button(master=self.body_sect,text="Start",fg="#FFFFFF",bg="#AEE8B6",justify="center")
        self.start_btn.grid(row=4, column=10, ipadx=30, ipady=6, padx=12)
        self.start_btn.configure(font=("Arial", 21, "bold"), command=lambda:self.prepare_test(self.selected_test))
        self.body_sect_description = tk.Label(master=self.body_sect, text=self.selected_test.description, justify="center", wraplength=950)
        self.body_sect_description.configure(font=("Times New Roman",18, "bold"),bg="#FFFFFF")
        self.body_sect_description.grid(row=0, column=0, rowspan=2, columnspan=11)

    #function for innitiating a selected test - activated 
    def prepare_test(self, test):
        print(test.test_name)
        self.body_sect_description.config(text="")
        self.start_btn.destroy()
        self.next_btn = tk.Button(master=self.body_sect,text="Next",fg="#FFFFFF",bg="#AEE8B6",justify="center")
        self.next_btn.grid(row=4, column=10, ipadx=30, ipady=6, padx=12)
        self.next_btn.configure(font=("Arial", 21, "bold"))
        self.start_test()

    def start_test(self):
        points = 0
        question_counter = 1
        #current_choice = tk.IntVar()
        #current_answer = tk.IntVar()
        current_question_package = self.selected_test.question_list.get_head_question()
        print(self.selected_test.question_list.get_head_question().get_question())
        self.question_label.grid(row=0, column=0, rowspan=2, columnspan=11)
        self.question_label.configure(font=("Courier New",14, "bold"),bg="#FFFFFF")


        #while current_question_package:
        self.question_label.config(text="{}. {}".format(question_counter,current_question_package.get_question()["question"]))
        next_question = current_question_package.get_next_question()
        current_choice = current_question_package.get_question()["answer"]
        
        
            
        
        
#class for creating instances of different tests to add to application
class Test():
    def __init__(self, parent, question_list=None, test_name=None,test_description=None):
        self.parent=parent
        self.question_list = question_list
        self.test_name = test_name
        self.description = test_description
        self.test_btn = tk.Button(master=self.parent.test_sect, bg="#FFFFFF", fg="black",padx=24,#make buttons more visually appealing
                                  pady=14, bd=2, relief='raised',text=self.test_name, height=1, width=8)
        self.test_btn.configure(font=("Roboto", 12, "bold"),command=lambda: self.parent.selection(self))#tell Application which test is being selected
        
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
    
    #possibly put radiobuttons inside of question class
    
# Main functin for initializing the application and executing primary statements

package1 = {"question": "In what direction does fire generally move when at the bottom of a hill?",
           "choices": {"A": "North", "B": "Uphill", "C": "Downhill"},
           "answer": "A"}

package2 = {"question": "what are you doing today?",
           "choices": {"A": "something", "B": "alot", "C": "Nothing"},
           "answer": "A"}

package3 = {"questionA": "How are you today?",
           "choices": {"A": "good", "B": "bad", "C": "Okay"},
           "answer": "A"}

package4 = {"question": "what are you doing today?",
           "choices": {"A": "something", "B": "alot", "C": "Nothing"},
           "answer": "A"}

#Initialization function
def main():
    
    #instance of Application running mainloop
    app = Application(master=root)
    
    question_1 = Question(package1)
    question_2 = Question(package2)

    question_3 = Question(package3)
    question_4 = Question(package4)
    
    question_list_1 = Questions_List(question_2)
    question_list_1.insert_begenning(question_1)

    question_list_2 = Questions_List(question_3)
    question_list_2.insert_begenning(question_4)


    test1 = Test(app, question_list_1, "Fire Behavior", "This test will assess an analysts understanding of fire and fire behavior.")
    test2 = Test(app, question_list_2, "Not Fire Behavior", "This is a 2nd test description")
    app.add_test(test1)
    app.add_test(test2)
    
    app.generate_tests()
    
    app.mainloop()

main()

