# from tkinter import*
# from PIL import ImageTk, Image
# import math
# from main import*
# from DCIM import*


# root=Tk()
# root.title('Smart Calculator')
# root.config(bg='#C3C3C3',bd='30')
# root.geometry('680x486+50+10')



def click(value):
  answer=''
  ex=entryField.get()
  import math
  
  if value=='C':
    ex=ex[0:len(ex)-1]
    entryField.delete(0,END)
    entryField.insert(0,ex)

  elif value=='CE':
     entryField.delete(0,END)

  elif value=='√':  
    answer=math.sqrt(eval(ex))
    
  elif value=='π':
    answer=math.pi


  elif value=='CosΘ':
    answer=math.cos(math.radians(eval(ex)))


  elif value=='TanΘ':
    answer=math.tan(math.radians(eval(ex)))

  elif value=='SinΘ':
    answer=math.sin(math.radians(eval(ex)))


  elif value=='2π':
    answer=2*math.pi
    


  elif value=='Cosh':
    answer=math.cosh(eval(ex))


  elif value=='Tanh':
    answer=math.tanh(eval(ex))


  elif value=='Sinh':
    answer=math.sinh(eval(ex))



  elif value=='∛':
    answer=eval(ex)**(1/3)

  elif value=='x\u02b8':
    entryField.inser(END,'**')
    


  elif value=='x\u0083':
    answer= eval(ex)**3

  elif value=='x\u00B2':
    answer= eval(ex)**2



  elif value==chr(247):
    entryField.insert(END,"/")
    return

  elif value=='In':
    answer= math.log2(eval(ex))

  elif value=='deg':
    answer=math.degrees(eval(ex))


  elif value=='rad':
    answer=math.radians(eval(ex))


  elif value=='e':
    answer=math.e
 
  elif value=='enter':
    answer=eval(ex)

  elif value=='=':
  
    answer=eval(ex)


  elif value=='log10':
    answer=math.log10(eval(ex))


  elif value=='x!':
    answer=math.factorial(ex)

  else:
    entryField.insert(END,value)
    return


  entryField.delete(0,END)
  entryField.insert(0,answer)



root.mainloop()