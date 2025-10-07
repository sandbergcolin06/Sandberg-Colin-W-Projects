from tkinter import *
class CalculatorFunctions:
    def __init__(self):
        self.cptSto = 0
        self.nSto = None
        self.iperySto = None
        self.pvSto = None
        self.fvSto = None
        self.pmtSto = None
        self.entry= ''
    #financial functions
    def pmt_func(self, entry_line):
        try:
            entry_line.set("PMT = " + self.entry)
            self.pmtSto = float(self.entry)
        except ValueError:
            self.entry = str(eval(self.entry))
            entry_line.set("PMT = " + self.entry)
            self.pmtSto = float(self.entry)
    def n_func(self, entry_line):
        try:
            entry_line.set("N = " + self.entry)
            self.nSto = float(self.entry)
        except ValueError:
            self.entry = str(eval(self.entry))
            entry_line.set("N = " + self.entry)
            self.nSto = float(self.entry)
    def cpt_func(self):
        self.cptSto += 1
    def ipery_func(self, entry_line):
        try:
            entry_line.set("I/Y = " + self.entry)
            self.iperySto = float(self.entry)
        except ValueError:
            self.entry = str(eval(self.entry))
            entry_line.set("I/Y = " + self.entry)
            self.iperySto = float(self.entry)
    def pv_func(self, entry_line):
        try:
            entry_line.set("PV = " + self.entry)
            self.pvSto = float(self.entry)
        except ValueError:
            self.entry = str(eval(self.entry))
            entry_line.set("PV = " + self.entry)
            self.pvSto = float(self.entry)
    def fv_func(self, entry_line):
        if (self.cptSto != 1):
            try:
                entry_line.set("FV = " + self.entry)
                self.fvSto = self.entry
            except ValueError:
                self.entry = str(eval(self.entry))
                entry_line.set("FV = " + self.entry)
                self.fvSto = self.entry
        else:
            if(self.pmtSto == None):
                if(self.iperySto == None or self.nSto == None or self.pvSto == None):
                    self.entry = 0
                    entry_line.set(self.entry)
                    self.cptSto -= 1
                else:
                    self.entry = str(self.pvSto*((1+self.iperySto)**self.nSto))
                    entry_line.set("Fv = " + self.entry)
                    self.cptSto -= 1
            elif(self.pvSto == None):
                if(self.iperySto == None or self.pmtSto == None or self.nSto == None):
                    self.entry = 0
                    entry_line.set(self.entry)
                    self.cptSto -= 1
                else:
                    self.entry = str(self.pmtSto*((((1+self.iperySto)**self.nSto) - 1) / self.iperySto))
                    entry_line.set("Fv = " + self.entry)
                    self.cptSto -= 1
            elif(self.pmtSto is not None and self.pvSto is not None and self.nSto is not None and self.iperySto is not None):
                self.entry = str((self.pmtSto*((((1+self.iperySto)**self.nSto) - 1) / self.iperySto))+(self.pvSto*((1+self.iperySto)**self.nSto)))
                entry_line.set("Fv = " + self.entry)
                self.cptSto -= 1
            elif(self.iperySto == None or self.nSto == None):
                self.entry = 0
                entry_line.set(self.entry)
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
