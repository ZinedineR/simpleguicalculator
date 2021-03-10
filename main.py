import wx
import gui
import math

saver = [] 
class CalcFrame(gui.MainFrame):
    def __init__(self,parent):
        gui.MainFrame.__init__(self,parent)
 
    #memencet =, untuk menjumlahkan hasil di text
    def solveFunc(self,event):
        try:
            result = eval(self.text.GetValue())
            self.text.SetValue(str(result))
            saver.clear()
            
        except Exception:
            print('error')
    def clearFunc(self,event):
        self.text.SetValue(str(''))
        saver.clear()
        
    def addText(self,event):
        btn = event.GetEventObject().GetLabel()
        saver.append(btn)
        self.saving()
        
    def saving(self):
        makeup = ''.join([str(elem) for elem in saver])
        self.text.SetValue(str(makeup))
        
    

 

app = wx.App(False)
frame = CalcFrame(None)
frame.Show(True)
app.MainLoop()