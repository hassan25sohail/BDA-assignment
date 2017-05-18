import matplotlib
matplotlib.use('TkAgg')
from mysqlconn import DBConnection
from twitterstream import insertTweets
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import Tkinter as Tk


class GUI:
   root = Tk.Tk()
   root.wm_title("Big data analysis assignment")
   keyword=['car']

   def __init__(self):
        self.DBC = DBConnection('localhost',3306,'root','ironhorse100','zain')
        self.con = self.DBC.connect_db()


   def graphs(self):
      f = Figure(figsize=(5, 5), dpi=100)
      a = f.add_subplot(111)
      x=insertTweets().tweets(self.keyword,self.location)
      print x
      #result = self.DBC.fetch_db("SELECT * FROM tweets WHERE keywords ='"+self.keyword+"'" )
      #print result[0]

      t=[1,2,3,-2,6]
      s=[1,2,3,4,6]

      f2 = Figure(figsize=(5, 5), dpi=100)
      a2= f2.add_subplot(111)
      t2=[1,2,3,4,6]
      s2=[1,2,3,4,6]

      a.plot(t, s)
      a2.plot(t2, s2)

      canvas = FigureCanvasTkAgg(f, master=self.root)
      canvas.get_tk_widget().pack(side=Tk.RIGHT, fill=Tk.BOTH, expand=False)
      canvas = FigureCanvasTkAgg(f2, master=self.root)
      canvas.show()
      canvas.get_tk_widget().pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=False)
      canvas._tkcanvas.pack(side=Tk.BOTTOM, fill=Tk.BOTH, expand=False)

   def helloCallBack2(self, E2=None):
      #entry is a text box and z is the value of it :)
      self.keyword = self.E2.get()
      self.location=self.E1.get()
      self.graphs()



   def controls(self):
      L1 = Tk.Label( text="keyword")
      L1.pack( side = Tk.TOP)


      self.E1 = Tk.Entry( bd =5)
      self.E1.pack(side = Tk.TOP)


      L2 = Tk.Label( text="location")
      L2.pack( side = Tk.TOP)


      self.E2 = Tk.Entry( bd =5)
      self.E2.pack(side =Tk.TOP)

      B2= Tk.Button( text ="Hello", command = self.helloCallBack2)

      B2.pack(side=Tk.TOP)
      Tk.mainloop()

a=GUI()
a.controls()


