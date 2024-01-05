#Οι απαραίτητες βιβλιοθήκες
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk,Image


def calculate_y_values(expression, x_values):
    '''Η συνάρτηση calculate_y_values θέτει τις τιμές των y ως συνάρτηση των τιμών των x, 
    όπου x θα έιναι τα στοιχεία του παρακάτω λεξικού.'''
    functions = {
        'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 'sinh': np.sinh, 'cosh': np.cosh,
        'tanh': np.tanh, 'sqrt': np.sqrt, 'abs': np.abs, 'π': np.pi,
        'arcsin': np.arcsin, 'arccos': np.arccos, 'arctan': np.arctan, 'tan': np.tan,
        'exp': np.exp, 'ln': np.log, 'log': np.log10 , 'sqrt': np.sqrt
        }
     # Λεξικό με διάφορες συναρτήσεις της numpy
    functions['x'] = x_values
    y_values = eval(expression, functions)
    return y_values


class FunctionGrapher:
    '''Κλάση η οποία με τη χρήση της tkinter σχεδιάζει το περιεχόμενο του παραθύρου στο οποίο θα σχεδιαστεί η συνάρτηση.'''
    def __init__(self, master):
        self.master = master
        self.master.configure(bg = "#91BFFF")
        self.master.geometry('1920x1080')
        self.master.title("Σχεδίαση γραφικής παράστασης συνάρτησης μιας μεταβλητής")

        self.label_instruction = ttk.Label(self.master, text="Εισάγετε την συνάρτησή σας:",font=55)
        self.label_instruction.pack(pady=30)
        

        self.entry_function = ttk.Entry(self.master, width = 50)
        self.entry_function.pack(pady = 60,padx=100)

        self.plot_button = ttk.Button(self.master,text="Σχεδιασμός Γραφικής Παράστασης", cursor='hand2',command=self.plot_function)
        self.plot_button.place(x = 1129, y = 144)
        self.master.bind('<Return>', lambda event: self.plot_function())

        self.menu_button = ttk.Button(self.master,text="Εμφάνιση Μενού Τελεστών και Συναρτήσεων",cursor='hand2',
                                      command=self.show_menu)
        self.menu_button.place(x=837, y=185)
        
                      
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
        self.toolbar_frame = ttk.Frame(self.master)
        

    def plot_function(self):
        '''Η συνάρτηση plot_function διαμορφώνει το πλαίσιο της γραφικής παράστασης, την σχεδιάζει,
        την οριεθετεί, και κάνει διακριτούς τους άξονες x και y.'''
        user_function = self.entry_function.get()
       
        x_values = np.linspace(-1000, 1000, 150000)       
        y_values = calculate_y_values(user_function, x_values)

        self.ax.clear()
        self.ax.plot(x_values, y_values, label ='Συνάρτηση')
        self.ax.set_xlabel('Άξονας των x')
        self.ax.set_ylabel('Άξονας των y')
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)

        self.ax.axvline(x = 0, color = 'black')
        self.ax.axhline(y = 0, color = 'black')

        self.ax.set_title('Γραφική Παράσταση')
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()


    def show_menu(self):
        '''H συνάρτηση show_menu είναι υπεύθυνη για την εμφάνιση του Μενού Τελστών και Συναρτήσεων 
        που είναι απαραίτητοι για την σωστή λειτουργία του προγράμματος.'''
        
        
        self.menu_window =tk.Toplevel()
        self.menu_window.title('Μενού Τελεστών και Συναρτήσεων')
        self.menu_window.iconbitmap('FunctionGrapherIco.ico')
        self.menu_window.geometry('1600x900')
        self.menu_frame = tk.Frame(self.menu_window)
        self.menu_frame.pack(fill = 'both', expand = 1)
        self.img = ImageTk.PhotoImage(Image.open('Menu.jpg'))
        self.menu_label= tk.Label(self.menu_frame,image=self.img)
        self.menu_label.configure(bg='#34425d')
        self.menu_label.pack(fill='both',expand=1)

       
'''Κυρίως πρόγραμμα'''
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('1920x1080')
    root.iconbitmap('FunctionGrapherIco.ico')
    app = FunctionGrapher(root)
    root.mainloop() 