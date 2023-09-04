import ttkbootstrap as ttk

class Calculator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        ttk.Style().configure("TButton", font=("Arial 15"))
        self.digitsVar = ttk.StringVar(value=0)
        self.equation = ""
        self.currentNumber = ""
        self.isClear = True
        self.pack(fill=ttk.BOTH, expand=ttk.YES)
        self.createDisplay()
        self.createNumPad()

    def createDisplay(self):
        container = ttk.Frame(master=self)
        container.pack(fill="x", pady=35, padx=8)

        display = ttk.Label(container, foreground="#fff", textvariable=self.digitsVar, font=("Arial", 34, "bold"), anchor="e")
        display.pack(fill="x")

    def createNumPad(self):
        container = ttk.Frame(master=self)
        container.pack(fill=ttk.BOTH, expand=ttk.YES)

        matrix = [
            ["%", "CE", "C", "÷"],
            [7, 8, 9, "×"],
            [4, 5, 6, "−"],
            [1, 2, 3, "+"],
            ["±", 0, ".", "="]
        ]

        for indexA, row in enumerate(matrix):
            container.rowconfigure(indexA, weight=1)
            for indexB, text in enumerate(row):
                container.columnconfigure(indexB, weight=1)
                button = self.createNumButton(parent=container, buttonText=text)
                button.grid(row=indexA, column=indexB, sticky="news", padx=5, pady=5)

    def createNumButton(self, parent, buttonText):
        if buttonText == "CE" or buttonText == "C":
            button = ttk.Button(parent, text=buttonText, style="warning-outline", padding=20, width=4, command=lambda: self.clearButtonPress(buttonText))
        elif isinstance(buttonText, int):
            button = ttk.Button(parent, text=buttonText, style="secondary", padding=20, width=4, command=lambda: self.numericButtonPress(buttonText))
        elif buttonText in ["÷", "×", "+", "−"]:
            button = ttk.Button(parent, text=buttonText, style="dark", padding=20, width=4, command=lambda: self.operationButtonPress(buttonText))
        elif buttonText == "=":
            button = ttk.Button(parent, text=buttonText, style="info", padding=20, width=4, command=self.evaluteEquation)
        else:
            button = ttk.Button(parent, text=buttonText, style="dark", padding=20, width=4, command=lambda: self.modificationButtonPress(buttonText))
        return button

    def numericButtonPress(self, diget):
        if self.isClear == True:
            self.digitsVar.set(value=diget)
            self.currentNumber = str(diget)
            self.isClear = False
        else:
            self.digitsVar.set(value=self.digitsVar.get() + str(diget))
            self.currentNumber += str(diget)  

    def clearButtonPress(self, clearType):
        if clearType == "C":
            self.digitsVar.set(value=0)
            self.equation = ""
            self.currentNumber = ""
            self.isClear = True
        elif clearType == "CE" and len(self.equation) > 0 and self.currentNumber != "":
            index = self.digitsVar.get().rfind(self.currentNumber.replace("-", "−"))
            self.digitsVar.set(self.digitsVar.get()[0:index])
            self.currentNumber = ""
            self.equation = self.equation[0:index]

    def operationButtonPress(self, operation):
        ops = { "÷": "/", "×": "*", "−": "-" }

        self.digitsVar.set(value=self.digitsVar.get() + operation)
        self.equation += self.currentNumber
        try:
            self.equation += ops[operation]
        except KeyError:
            self.equation += operation
        self.currentNumber = ""
        self.isClear = False

    def modificationButtonPress(self, modifier):
        if modifier == "." and "." not in self.currentNumber:
            self.digitsVar.set(value=self.digitsVar.get() + modifier)
            if self.isClear:
                self.currentNumber += "0" + modifier
            else:
                self.currentNumber += modifier
            self.isClear = False
        elif modifier == "±" and self.isClear == False and self.currentNumber != "":
            index = self.digitsVar.get().rfind(self.currentNumber)
            if "-" not in self.currentNumber:
                self.digitsVar.set(self.digitsVar.get()[0:index] + "−" + self.currentNumber)
                self.currentNumber = "-" + self.currentNumber
                self.equation = self.equation[0:index]
            else:
                self.currentNumber = self.currentNumber[1:]
                print(self.digitsVar.get())
                self.digitsVar.set(self.digitsVar.get()[0:index - 1] + self.currentNumber)
                print("before:", self.equation)
                self.equation = self.equation[0:index]
                print("after:", self.equation)
        elif modifier == "%" and self.isClear == False:
            index = self.digitsVar.get().rfind(self.currentNumber)
            self.currentNumber = str(float(self.currentNumber) / 100)
            self.digitsVar.set(self.digitsVar.get()[0:index - 1] + self.currentNumber)

    def evaluteEquation(self):
        print("equatino:", self.equation)
        print("currentNumber", self.currentNumber)
        if self.equation != self.currentNumber:
            self.equation += self.currentNumber
            with open("log.txt", "a") as data:
                print(self.equation, file=data)
            self.equation = str(eval(self.equation))
            self.currentNumber = self.equation
            self.digitsVar.set(value=self.equation.replace("-", "−"))
            self.equation = ""

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    root.title("Calculator")
    root.geometry("320x500")
    root.resizable(False, False)
    root.iconbitmap("calc_icon.ico")
    Calculator(root)
    root.mainloop()