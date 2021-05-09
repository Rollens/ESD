
import datetime
class LFP:

#constructor
    def __init__(self,no):
        self.No = no
        self.Uninstalled = False
        self.Resistance = False
        self.Installed = False
        self.Verified = False
        self.isFinished = False
        self.UninstalledDate = None
        self.ResistanceDate = None
        self.InstalledDate = None
        self.VerifiedDate = None
        self.FininshedDate = None
        self.ESD_SN=[]
#Method
    def Done(self):
        if(self.Uninstalled and self.Resistance and self.Installed and self.Verified):
            self.isFinished = True
        return self.isFinished

    def Uninstall(self):
        self.Uninstalled = True
        self.UninstalledDate=datetime.date.today().strftime("%m/%d")

    def ReplaceResistance(self):
        self.Resistance = True
        self.ResistanceDate=datetime.date.today().strftime("%m/%d")

    def Install(self):
        self.Installed = True
        self.InstalledDate=datetime.date.today().strftime("%m/%d")
    
    def Verify(self):
        self.Verified = True
        self.VerifiedDate=datetime.date.today().strftime("%m/%d")

    def printSN(self):
        for ESD in self.ESD_SN:
            print(ESD,",")
            
    def LoadSN(self,SN):
        self.ESD_SN = SN
        
    def LoadStatus(self,Status,StatusByDate):
        c=0
        for i in Status:
            if c == 0:
                if i == self.No:
                    c=c+1
                    continue
                else:
                    print("ERROR:The machine ID is not matched.")
                    break
            elif c == 1:
                if Status[c]:
                    self.Uninstalled = True
                    self.UninstalledDate = StatusByDate[c]
                    c=c+1
            elif c == 2:
                if Status[c]:
                    self.Resistance = True
                    self.ResistanceDate = StatusByDate[c]
                    c=c+1
            elif c == 3:
                if Status[c]:
                    self.Installed = True
                    self.InstalledDate = StatusByDate[c]
                    c=c+1
            elif c == 4:
                if Status[c]:
                    self.Verified = True
                    self.VerifiedDate = StatusByDate[c]

    def LoadDone(self,DateofDone):
        self.isFinished = True
        self.isFinishedDate = DateofDone

    def showStatus(self):
        print("The Status of TP{0:03}.".format(self.No))
        if self.Uninstalled:
            print("Uninstalled O")
        else:
            print("Uninstalled X")
        if self.Resistance:
            print("Resistance O")
        else:
            print("Resistance X")
        if self.Installed:
            print("Installed O")
        else:
            print("Installed X")
        if self.Verified:
            print("Verified O")
        else:
            print("Verified X")
        print("With S/N Number")
        for s in self.ESD_SN:
            print(s)