from tkinter import *
class CalculatorFunctions:
    def __init__(self):
        self.cptSto = 0
        self.nSto = ''
        self.iperySto = ''
        self.pvSto = ''
        self.fvSto = ''
        self.pmtSto = ''
        self.entry= ''
    #financial functions
    def n_func(self, entry_line):
        entry_line.set("N = " + self.entry)
        self.nSto = float(self.entry)
    def cpt_func(self):
        self.cptSto += 1
    def ipery_func(self, entry_line):
        entry_line.set("I/Y = " + self.entry)
        self.iperySto = float(self.entry)
    def pv_func(self, entry_line):
        entry_line.set("PV = " + self.entry)
        self.pvSto = float(self.entry)
    def fv_func(self, entry_line):
        if (self.cptSto != 1):
            entry_line.set("FV = " + self.entry)
            self.fvSto = self.entry
        else:
            if(self.pmtSto == ''):
                if(self.iperySto != float or self.nSto != float or self.pvSto != float):
                    self.entry = 0
                    entry_line.set(self.entry)
                    self.cptSto -= 1
            else:
                self.entry = str(self.pvSto*((1+self.iperySto)**self.nSto))
                entry_line.set("Fv = " + self.entry)
                self.cptSto -= 1
    #other functions
    def square_root(self, entry_line):
        total = str(eval('(' + self.entry + ') **  (1/2)'))
        entry_line.set(total)
    def inverse(self, entry_line):
        total = str(eval('1/'+self.entry))
        entry_line.set(total)
    def equal_press(self, entry_line):
        try:
            total = str(eval(self.entry))
            entry_line.set(total)
        except:
            entry_line.set('Error')
            self.entry = ''
    def press(self, num, entry_line):
        self.entry = self.entry + str(num)
        entry_line.set(self.entry)
    def clear(self, entry_line):
        self.entry = ''
        entry_line.set('')
    def delete(self, entry_line):
        self.entry = self.entry[0:-1]
        entry_line.set(self.entry)
