class proleter:
    def __init__(self,name,wage):
        self.name = name
        self.wage = wage
    def info(self):
        print("Name:",self.name)
        print("Wage:",self.wage)
    def set_name(self,x):
        self.name = x
    def set_wage(self,x):
        self.wage = x
class Company:
    def __init__(self,workers):
        self.workers = []
    def addworker(self,newslave):
        if isinstance(newslave,proleter):
            self.workers.append(newslave.name)
    def display(self):
        print(self.workers)

w1 = proleter("wojak",100)
w2 = proleter("wojak2",100)
w1.info()
w3 = proleter("wojak3",100)
Google = Company(w1)
Google.addworker(w2)
Google.display()