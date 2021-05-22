from tkinter import *
import math
#15/05/21
#Caitlin Naylor
#Job Cost/Charge Calulator

class Job:
    def __init__(self, job_num, name, distance, minutes, wof_and_tune, charge):
        self.job_num = job_num
        self.name = name
        self.distance = distance
        self.minutes = minutes
        self.wof_and_tune = wof_and_tune
        self.charge = charge

class JobCost:
    def __init__(self, parent):
        self.jobs = []
        #Add Jobs Frame
        self.add_job_frame = Frame(parent)
        self.add_job_frame.configure(pady = 10, padx = 10)
        self.add_job_frame.grid(row = 0, column = 0)

        #Company Logo
        #Suzy has supplied and given permission for this logo to be used in this programme

        self.logo = PhotoImage(file = "logo.gif")
        self.logo_label = Label(self.add_job_frame, image = self.logo)
        self.logo_label.grid(row = 0, column = 0, columnspan = 4)
            
        #Add a Job Label
        self.add_job_label = Label(self.add_job_frame, text = "Add a Job", font = ("Sans Serif", 17))
        self.add_job_label.grid(row = 1, column = 0, sticky = NW)

        #Job Number Label
        self.job_num_label = Label(self.add_job_frame, text = "Job Number", font = ("Sans Serif", 11))
        self.job_num_label.grid(row = 2, column = 0, sticky = NW)

        #Job Number Input
        self.job_num_var = IntVar()
        self.job_num_var.set("")
        self.job_num_box = Entry(self.add_job_frame, font = ("Sans Serif", 10), textvariable = self.job_num_var, width = 30)
        self.job_num_box.grid(row = 2, column = 1, columnspan = 3, sticky = NW)

        #Name Label
        self.name_label = Label(self.add_job_frame, text = "Name", font = ("Sans Serif", 11))
        self.name_label.grid(row = 3, column = 0, sticky = NW)

        #First Name Input
        self.first_name_var = StringVar()
        self.first_name_var.set("")
        self.first_name_box = Entry(self.add_job_frame, font = ("Sans Serif", 10), width = 30, textvariable = self.first_name_var)
        self.first_name_box.grid(row = 4, column = 0, sticky = NW)

        #Last Name Input
        self.last_name_var = StringVar()
        self.last_name_var.set("")
        self.last_name_box = Entry(self.add_job_frame, font = ("Sans Serif", 10), width = 30, textvariable = self.last_name_var)
        self.last_name_box.grid(row = 4, column = 1, columnspan = 3, sticky = NW)

        #First Name Label
        self.first_name_label = Label(self.add_job_frame, text = "First Name", font = ("Sans Serif", 8))
        self.first_name_label.grid(row = 5, column = 0, sticky = NW)

        #Last Name Label
        self.last_name_label = Label(self.add_job_frame, text = "Last Name", font = ("Sans Serif", 8))
        self.last_name_label.grid(row = 5, column = 1, sticky = NW)

        #Distance Travelled Label
        self.distance_label = Label(self.add_job_frame, text = "Distance Travelled to Client (km)", font = ("Sans Serif", 11))
        self.distance_label.grid(row = 6, column = 0, sticky = NW)

        #Distance Input
        self.distance_var = StringVar() #String not Int as IntVar automatically rounds down
        self.distance_var.set("")
        self.distance_box = Entry(self.add_job_frame, font = ("Sans Serif", 10), width = 30, textvariable = self.distance_var)
        self.distance_box.grid(row = 6, column = 1, columnspan = 3, sticky = NW)

        #Minutes Spent on Virus Protection Label
        self.minutes_label = Label(self.add_job_frame, text = "Minutes Spent on Virus Protection", font = ("Sans Serif", 11))
        self.minutes_label.grid(row = 7, column = 0, sticky = NW)

        #Minutes Input
        self.minutes_var = IntVar()
        self.minutes_var.set("")
        self.minutes_box = Entry(self.add_job_frame, font = ("Sans Serif", 10), width = 30, textvariable = self.minutes_var)
        self.minutes_box.grid(row = 7, column = 1, columnspan = 3, sticky = NW)

        #Wof and tune Label
        wof_and_tune_label = Label(self.add_job_frame, text = "Was a WOF and Tune Required?", font = ("Sans Serif", 11))
        wof_and_tune_label.grid(row = 8, column = 0, sticky = NW)

        #Wof and tune radiobuttons
        self.wof_tune_var = StringVar()
        self.wof_tune_var.set(0)
        self.wof_tune_rbs_names = ["Yes", "No"]
        self.wof_tune_rbs = []
        
        for i in range(len(self.wof_tune_rbs_names)):
            self.wof_tune_rbs.append(Radiobutton(self.add_job_frame, text = self.wof_tune_rbs_names[i], value = self.wof_tune_rbs_names[i],
                                          variable = self.wof_tune_var, font = ("Sans Serif", 11)))
            self.wof_tune_rbs[i].grid(row = 8, column = i +1, sticky = NW)

        #Enter Button to add a job
        #lambda code from https://www.reddit.com/r/learnpython/comments/cdfmn5/tkinter_help_command_running_before_clicked/
        self.enter_job_btn = Button(self.add_job_frame, text = "Enter", font = ("Sans Serif", 11), width = 10, command = lambda:self.store_input()) 
        self.enter_job_btn.grid(row = 9, column = 3, sticky = NE)

        #Show Jobs Buttons
        self.show_jobs_btn = Button(self.add_job_frame, text = "Show Jobs", font = ("Sans Serif", 11), width = 10, command = lambda:self.get_to_job_cards())
        self.show_jobs_btn.grid(row = 10, column = 3, pady = 5, sticky = NE)

        self.job_cards_frame = Frame(parent)

    def store_input(self):
        self.job_num = self.job_num_var.get()
        self.name = self.first_name_var.get() + " " + self.last_name_var.get()
        self.distance = float(self. distance_var.get())

        if self.distance % 1 >=0.5:
            self.distance = math.ceil(self.distance)
        else:
            self.distance = math.floor(self.distance)
            
        self.minutes = self.minutes_var.get()
        self.wof_and_tune = self.wof_tune_var.get()

        self.calc_charge()
        
        self.job = [self.job_num, self.name, self.distance, self.minutes, self.wof_and_tune, self.charge]
        
        self.jobs.append(self.job)

        #Reset Input Areas
        self.job_num_var.set("")
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.distance_var.set("")
        self.minutes_var.set("")
        self.wof_tune_var.set(0)

    def calc_charge(self):
        self.charge = 0
        if self.distance <= 5:
            self.charge += 10
        else:
            self.charge += 10 + ((self.distance - 5)*0.5)

        if self.wof_and_tune == self.wof_tune_rbs_names[0]: #yes
            self.charge += 100

        if self.minutes >0:
            self.charge += 0.80 *self.minutes

    def get_to_job_cards(self):
         self.add_job_frame.grid_remove()
         self.job_cards_frame.grid(row = 0, column = 0)

         self.test_label = Label(self.job_cards_frame, text = "Welcome to the Job Cards Frame")
         self.test_label.grid(row =1, column = 0)
              

#Main Routine
if __name__=="__main__":
    root= Tk()
    ratings = JobCost(root)
    root.title("Job Cost/Charge Calculator")
    root.mainloop()
