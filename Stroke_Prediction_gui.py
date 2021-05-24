import tkinter as tk
import pickle

class StrokePrediction(tk.Tk):
    def __init__(self):
        super().__init__()
        width = 410
        height = 400
        self.geometry(f"{width}x{height}")
        self.minsize(width,height)
        self.maxsize(width,height)
        self.title('Stoke Prediction Model')
    def Header(self):
        Heading = tk.Label(text='Stroke Prediction Model',font='arial 18 bold')
        Heading.pack(pady=15)
        # Importing Model ---------------
        with open('Stroke_Prediction_Model','rb') as P_Model:
            self.Model = pickle.load(P_Model)
        # ----------------------------
    def command_button(self):
        Age = self.AgeVar.get()
        Hypertension =  self.tension_var.get()
        Heart_Disease =  self.Heart_var.get()
        Married = self.Married_var.get()
        Glucose_Level =  self.Glucose_var.get()
        array = [[Age,Hypertension,Heart_Disease,Married,Glucose_Level]]
        probability = self.Model.predict_proba(array)
        YesP = str(probability[0][0] * 100)[0:5]
        NoP = str(probability[0][1] * 100)[0:5]
        self.footer(YesP,NoP)
    def body(self):
        self.F1 = tk.Frame(self)
        self.F1.pack()
        self.F2 = tk.Frame(self)
        self.F2.pack(pady=(8,0),padx=(0,35))
        self.F3 = tk.Frame(self)
        self.F3.pack(pady=(4,0), padx=(0, 30))
        self.F4 = tk.Frame(self)
        self.F4.pack(pady=(4, 0), padx=(0, 30))
        self.F5 = tk.Frame(self)
        self.F5.pack()
        #-------------------
        self.AgeVar = tk.IntVar() # First Variable for Model
        self.AgeLabel = tk.Label(self.F1, text='Age:', font='arial 12')
        self.Age = tk.Entry(self.F1, borderwidth=0,textvariable=self.AgeVar, font='arial 12',width=10)
        self.Age.pack(side=tk.RIGHT, padx=(20,40))
        self.AgeLabel.pack(padx=(0,80))
        # --------------------
        self.tension_var = tk.IntVar() # Second Variable for Model
        self.tension_var.set(1)
        self.tension_Label = tk.Label(self.F2, text='Hypertension:', font='arial 12')
        self.tension_1 = tk.Radiobutton(self.F2,text='Yes',font='arial 12',variable=self.tension_var, value=1 )
        self.tension_2 = tk.Radiobutton(self.F2, text='No', font='arial 12', variable=self.tension_var, value=0)
        self.tension_Label.pack(side=tk.LEFT)
        self.tension_1.pack(padx=(35,0),side=tk.LEFT)
        self.tension_2.pack()
        # --------------------
        self.Heart_var = tk.IntVar()  # Third Variable for Model
        self.Heart_var.set(1)
        self.Heart_Label = tk.Label(self.F3, text='Heart Disease:', font='arial 12')
        self.Heart_1 = tk.Radiobutton(self.F3, text='Yes', font='arial 12', variable=self.Heart_var, value=1)
        self.Heart_2 = tk.Radiobutton(self.F3, text='No', font='arial 12', variable=self.Heart_var, value=0)
        self.Heart_Label.pack(side=tk.LEFT)
        self.Heart_1.pack(padx=(30,0), side=tk.LEFT)
        self.Heart_2.pack()
        # ---------------------
        self.Married_var = tk.IntVar()  # Fourth Variable for Model
        self.Married_var.set(1)
        self.Married_Label = tk.Label(self.F4, text='Married:', font='arial 12')
        self.Married_1 = tk.Radiobutton(self.F4, text='Yes', font='arial 12', variable=self.Married_var, value=1)
        self.Married_2 = tk.Radiobutton(self.F4, text='No', font='arial 12', variable=self.Married_var, value=0)
        self.Married_Label.pack(side=tk.LEFT)
        self.Married_1.pack(padx=(75, 0), side=tk.LEFT)
        self.Married_2.pack()
        # ------------------------
        self.Glucose_var = tk.IntVar()  # Fiveth Variable for Model
        self.glucose_Label = tk.Label(self.F5, text='Glucose Level:', font='arial 12')
        self.glucoselavel = tk.Entry(self.F5,borderwidth=0, textvariable=self.Glucose_var, font='arial 12', width=10)
        self.glucose_Label.pack(side=tk.LEFT,)
        self.glucoselavel.pack(padx=(40,40),pady=7)
        # _____________________________
        # Button For Predict Probabily

    def Button(self):
        self.but = tk.Button(text='Check Probability',font='arial 11',width=20,relief=tk.GROOVE,borderwidth=0,bg='Light gray',command=self.command_button)
        self.but.pack(pady=10)
        self.Repo = tk.Label()  # Footer Label
        self.Repo.pack(padx=(0,40))
    def footer(self, YesP,NoP):
        line = f'''
        The Probability to Be Stroked : {float(YesP)}%
        The Probability to Not Stroked :{float(NoP)}%
        '''
        self.Repo.config(text=line,font='arial 13')
if __name__ == '__main__':
    Model = StrokePrediction()
    Model.Header()
    Model.body()
    Model.Button()


    Model.mainloop()
