from tkinter import *
from PIL import ImageTk, Image
import math

from tkinter import messagebox

# from voice import*
# from DCIM import*

import turtle
from pygame import mixer
import speech_recognition

mixer.init()


# Python program to
# demonstrate printing HELLO
# using turtle

# Here frame is initialized with
# background colour as "White"


frame = turtle.Screen().bgcolor("black")
draw = turtle.Turtle()

# The colour, width and speed of the pen is initialized
draw.color("red")
draw.width(3)
draw.speed(20)

# Now lets get started with actual code
# printing letter H
draw.left(90)
draw.forward(70)
draw.penup()
draw.goto(0, 35)
draw.pendown()
draw.right(90)
draw.forward(30)
draw.penup()
draw.goto(30, 70)
draw.pendown()
draw.right(90)
draw.forward(70)

# printing letter E
draw.penup()
draw.goto(40, 0)
draw.pendown()
draw.right(180)
draw.forward(70)
draw.right(90)
draw.forward(35)
draw.penup()
draw.goto(40, 35)
draw.pendown()
draw.forward(35)
draw.penup()
draw.goto(40, 0)
draw.pendown()
draw.forward(35)

# printing letter L
draw.penup()
draw.goto(90, 70)
draw.pendown()
draw.right(90)
draw.forward(70)
draw.left(90)
draw.forward(35)

# printing letter L
draw.penup()
draw.goto(135, 70)
draw.pendown()
draw.right(90)
draw.forward(70)
draw.left(90)
draw.forward(35)

# printing letter O
draw.penup()
draw.goto(210, 70)
draw.pendown()
# centering in the screen

# turtle.destroy()

launch = messagebox.askquestion("launcher", "Open Calculator?")


if launch == "yes":
    

    root = Toplevel()
    root.title('Smart Calculator')
    root.config(bg='#ffff99', bd=20)
    root.geometry('490x530+0+0')
    

    def click(value):

        answer = ''
        ex = entryField.get()
        import math

        if value == 'clean':
            ex = ex[0:len(ex)-1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'delete':
            entryField.delete(0, END)

        elif value == 'squareroot':
            answer = math.sqrt(eval(ex))

        elif value == 'pie':
            answer = math.pi

        elif value == 'CosΘ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'TanΘ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'SinΘ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2*math.pi

        elif value == 'Cosh':
            answer = math.cosh(eval(ex))

        elif value == 'Cosi':
            answer = math.acosh(eval(ex))

        elif value == 'Tanh':
            answer = math.tanh(eval(ex))

        elif value == 'Tani':
            answer = math.atan(eval(ex))

        elif value == 'Sinh':
            answer = math.sinh(eval(ex))

        elif value == 'Sini':
            answer = math.asinh(eval(ex))

        elif value == 'cuberoot':
            answer = eval(ex)**(1 / 3)

        elif value == 'uii':
            entryField.insert(END, '**')

        elif value == 'cube':
            answer = eval(ex)**3

        elif value == 'square':
            answer = eval(ex)**2

        elif value == "add":
            entryField.insert(END, "+")
            return

        elif value == "substract":
            entryField.insert(END, "-")
            return

        elif value == "multiply":
            entryField.insert(END, "*")
            return

        elif value == "divide":
            entryField.insert(END, "/")
            return

        elif value == 'In':
            answer = math.log2(eval(ex))

        elif value == 'degree':
            answer = math.degrees(eval(ex))

        elif value == 'radian':
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'enter':
            answer = eval(ex)

        elif value == 'equal':

            answer = eval(ex)

        elif value == 'log10':
            answer = math.log10(eval(ex))

        elif value == 'fact':
            answer = math.factorial(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    buttonhistory = Label(root, font=('serif', 16, 'bold'), text="Past History",
                          height=17, width=20, background="#ffccff", padx=00,
                          pady=00).grid(row=2, column=9, rowspan=6)

    buttonprogrammer = Button(root, font=('serif', 10, 'bold'), height=2,
                              text=" Powered By: Om ,Krishna ,Lucky ,Sakshi, Yuvraj", width=54,
                              background="#1affff").grid(row=0, column=6, columnspan=7)
    # screen
    entryField = Entry(root, font=('arial', 20, 'bold'), bg='#e6ffff', fg='black',
                       width=22, bd=8, relief=SUNKEN)
    entryField.grid(row=0, column=0, columnspan=5)

    buttonspace1 = Label(root, text="   ", font=('arial', 16, 'bold'), height=1, width=3,
                         background="#ffff99", padx=00, pady=00).grid(row=2, column=5)

    buttonspace2 = Label(root, text="   ", font=('arial', 16, 'bold'), height=1, width=2,
                         background="#ffff99", padx=00, pady=00).grid(row=2, column=8)

    def scientific():

        root.resizable()
        root.geometry('1000x530+0+0')

    def standard():
        root.resizable()
        root.geometry('490x530+0+0')

    # logic of numpad

    def action(number):
        entryField.insert(0, number)
        # button

    onepic = Image.open("onef.png")
    oneresize = onepic.resize((80, 80), Image.LANCZOS)
    oneImage = ImageTk.PhotoImage(oneresize)
    button1 = Button(root, text="1", background="#99bbff", image=oneImage,
                     command=lambda: action(1)).grid(row=2, column=1)

    twopic = Image.open("twof.png")
    tworesize = twopic.resize((80, 80), Image.LANCZOS)
    twoImage = ImageTk.PhotoImage(tworesize)
    button2 = Button(root, text="2", background="#99bbff", image=twoImage, padx=100,
                     pady=100, command=lambda: action(2)).grid(row=2, column=2)

    threepic = Image.open("threef.png")
    threeresize = threepic.resize((80, 80), Image.LANCZOS)
    threeImage = ImageTk.PhotoImage(threeresize)
    button3 = Button(root, text="3", background="#99bbff", image=threeImage,
                     padx=00, pady=00, command=lambda: action(3)).grid(row=2, column=3)

    fourpic = Image.open("fourf.png")
    fourresize = fourpic.resize((80, 80), Image.LANCZOS)
    fourImage = ImageTk.PhotoImage(fourresize)
    button4 = Button(root, text="4", background="#99bbff", image=fourImage, padx=00,
                     pady=00, command=lambda: action(4)).grid(row=3, column=1)

    fivepic = Image.open("fivef.png")
    fiveresize = fivepic.resize((80, 80), Image.LANCZOS)
    fiveImage = ImageTk.PhotoImage(fiveresize)
    button5 = Button(root, text="5", background="#99bbff", image=fiveImage, padx=00,
                     pady=00, command=lambda: action(5)).grid(row=3, column=2)

    sixpic = Image.open("sixf.png")
    sixresize = sixpic.resize((80, 80), Image.LANCZOS)
    sixImage = ImageTk.PhotoImage(sixresize)
    button6 = Button(root, text="6", background="#99bbff", image=sixImage, padx=00,
                     pady=00, command=lambda: action(6)).grid(row=3, column=3)

    sevenpic = Image.open("sevenf.png")
    sevenresize = sevenpic.resize((80, 80), Image.LANCZOS)
    sevenImage = ImageTk.PhotoImage(sevenresize)
    button7 = Button(root, text="7", background="#99bbff", image=sevenImage, padx=00,
                     pady=00, command=lambda: action(7)).grid(row=4, column=1)

    eightpic = Image.open("eightf.png")
    eightresize = eightpic.resize((80, 80), Image.LANCZOS)
    eightImage = ImageTk.PhotoImage(eightresize)
    button8 = Button(root, text="8", background="#99bbff", image=eightImage, padx=00,
                     pady=00, command=lambda: action(8)).grid(row=4, column=2)

    ninepic = Image.open("ninef.png")
    nineresize = ninepic.resize((80, 80), Image.LANCZOS)
    nineImage = ImageTk.PhotoImage(nineresize)
    button9 = Button(root, text="9", background="#99bbff", image=nineImage, padx=0,
                     pady=0, command=lambda: action(9)).grid(row=4, column=3)

    zeropic = Image.open("zerof.png")
    zeroresize = zeropic.resize((80, 80), Image.LANCZOS)
    zeroImage = ImageTk.PhotoImage(zeroresize)
    button0 = Button(root, text="0", background="#99bbff", image=zeroImage, padx=00,
                     pady=00, command=lambda: action(0)).grid(row=5, column=2)

    addpic = Image.open("add.png")
    addresize = addpic.resize((80, 80), Image.LANCZOS)
    addImage = ImageTk.PhotoImage(addresize)
    buttona = Button(root, text="+", background="#ffff1a", image=addImage, padx=00, pady=00,
                     command=lambda: (click('add'))).grid(row=2, column=4)

    substractpic = Image.open("substract.png")
    substractresize = substractpic.resize((80, 80), Image.LANCZOS)
    substractImage = ImageTk.PhotoImage(substractresize)
    buttons = Button(root, text="-", background="#ffff1a", image=substractImage, padx=00, pady=00,
                     command=lambda: (click('substract'))).grid(row=3, column=4)

    multiplypic = Image.open("multiply.png")
    multiplyresize = multiplypic.resize((80, 80), Image.LANCZOS)
    multiplyImage = ImageTk.PhotoImage(multiplyresize)
    buttonm = Button(root, text="*", background="#ffff1a", image=multiplyImage, padx=00, pady=00,
                     command=lambda: (click("multiply"))).grid(row=4, column=4)

    dividepic = Image.open("divide.png")
    divideresize = dividepic.resize((80, 80), Image.LANCZOS)
    divideImage = ImageTk.PhotoImage(divideresize)
    buttond = Button(root, text="/", background="#ffff1a", image=divideImage, padx=00, pady=00,
                     command=lambda: (click("divide"))).grid(row=5, column=4)

    equalpic = Image.open("equal.png")
    equalresize = equalpic.resize((80, 80), Image.LANCZOS)
    equalImage = ImageTk.PhotoImage(equalresize)
    buttone = Button(root, text="=", background="#99bbff", image=equalImage, padx=00, pady=00,
                     command=lambda: (click("equal"))).grid(row=5, column=3)

    fullstoppic = Image.open("fullstop.png")
    fullstopresize = fullstoppic.resize((80, 80), Image.LANCZOS)
    fullstopImage = ImageTk.PhotoImage(fullstopresize)
    buttonf = Button(root, text=".", background="#99bbff", image=fullstopImage, padx=00,
                     pady=00, command=lambda: action(".")).grid(row=5, column=1)

    clearpic = Image.open("clear.png")
    clearresize = clearpic.resize((80, 80), Image.LANCZOS)
    clearImage = ImageTk.PhotoImage(clearresize)
    buttond = Button(root, text=".", background="#ff704d", image=clearImage, padx=00, pady=00,
                     command=lambda: (click("clean"))).grid(row=2, column=0)

    deletepic = Image.open("delete.png")
    deleteresize = deletepic.resize((80, 80), Image.LANCZOS)
    deleteImage = ImageTk.PhotoImage(deleteresize)
    buttond = Button(root, text=".", background="#ff704d", image=deleteImage, padx=00, pady=00,
                     command=lambda: (click("delete"))).grid(row=3, column=0)

    micpic = Image.open("mic.png")
    micresize = micpic.resize((80, 80), Image.LANCZOS)
    micImage = ImageTk.PhotoImage(micresize)
    buttonf = Button(root, text=".", background="#ff704d", image=micImage, padx=00,
                     pady=00).grid(row=4, column=0)

    scienticpic = Image.open("scientific.png")
    scienticresize = scienticpic.resize((80, 80), Image.LANCZOS)
    scienticImage = ImageTk.PhotoImage(scienticresize)
    buttonsci = Button(root, text=".", background="#ff704d", image=scienticImage,
                       padx=00, pady=00, command=scientific).grid(row=5, column=0)

    standardpic = Image.open("standard.png")
    standardresize = standardpic.resize((80, 80), Image.LANCZOS)
    standardImage = ImageTk.PhotoImage(standardresize)
    buttonstd = Button(root, text="std", background="#ff704d", image=standardImage, padx=00,
                       pady=00, command=standard).grid(row=6, column=0)

    piepic = Image.open("pie.png")
    pieresize = piepic.resize((80, 80), Image.LANCZOS)
    pieImage = ImageTk.PhotoImage(pieresize)
    buttonpie = Button(root, text="std", background="#ffff1a", image=pieImage, padx=00,
                       pady=00, command=lambda: (click("pie"))).grid(row=6, column=1)

    squarepic = Image.open("square.png")
    squareresize = squarepic.resize((80, 80), Image.LANCZOS)
    squareImage = ImageTk.PhotoImage(squareresize)
    buttonsquare = Button(root, text="std", background="#ffff1a", image=squareImage,
                          padx=00, pady=00, command=lambda: (click("square"))).grid(row=6, column=2)

    squarerootpic = Image.open("squareroot.png")
    squarerootresize = squarerootpic.resize((80, 80), Image.LANCZOS)
    squarerootImage = ImageTk.PhotoImage(squarerootresize)
    buttonroot = Button(root, text="std", background="#ffff1a", image=squarerootImage, padx=00,
                        pady=00, command=lambda: (click("squareroot"))).grid(row=6, column=3)

    floordivisionpic = Image.open("floordivision.png")
    floordivisionresize = floordivisionpic.resize((80, 80), Image.LANCZOS)
    floordivisionImage = ImageTk.PhotoImage(floordivisionresize)
    buttonfloor = Button(root, text="std", background="#ffff1a", image=floordivisionImage, padx=00,
                         pady=00, command=lambda: action("root")).grid(row=6, column=4)

    buttontanh = Button(root, text="TanΘ", font=('arial', 16, 'bold'), height=3, width=5, background="#4B0082",
                        padx=00, pady=00, command=lambda: (click("Tanh"))).grid(row=2, column=6)

    buttontani = Button(root, text="TAN(i)", font=('arial', 16, 'bold'), height=3, width=5,
                        background="#4B0082", padx=00, pady=00,
                        command=lambda: (click("Tani"))).grid(row=2, column=7)

    buttoncosh = Button(root, text="CosΘ", font=('arial', 16, 'bold'), height=3, width=5,
                        background="#0000FF", padx=00, pady=00,
                        command=lambda: (click("Cosh"))).grid(row=3, column=6)

    buttoncosi = Button(root, text="COS(i)", font=('arial', 16, 'bold'), height=3, width=5,
                        background="BLUE", padx=00, pady=00,
                        command=lambda: (click("Cosi"))).grid(row=3, column=7)

    buttonsinh = Button(root, text="SINΘ", font=('arial', 16, 'bold'), height=3, width=5, background="#00FF00",
                        padx=00, pady=00, command=lambda: (click("Sinh"))).grid(row=4, column=6)

    buttonsini = Button(root, text="SIN(i)", font=('arial', 16, 'bold'), height=3, width=5, background="#00FF00",
                        padx=00, pady=00, command=lambda: (click("Sini"))).grid(row=4, column=7)

    buttondeg = Button(root, text="Deg", font=('arial', 16, 'bold'), height=3, width=5, background="#FFFF00",
                       padx=00, pady=00, command=lambda: (click("degree"))).grid(row=5, column=6)

    buttonrad = Button(root, text="Rad", font=('arial', 16, 'bold'), height=3, width=5, background="#FFFF00", padx=00,
                       pady=00, command=lambda: (click("radian"))).grid(row=5, column=7)

    buttonlog10 = Button(root, text="Log10", font=('arial', 16, 'bold'), height=3, width=5, background="RED",
                         padx=00, pady=00, command=lambda: (click("log10"))).grid(row=6, column=6)

    buttonfact = Button(root, text="Fact", font=('arial', 16, 'bold'), height=3, width=5, background="RED",
                        padx=00, pady=00, command=lambda: (click("fact"))).grid(row=6, column=7)


  

    root.mainloop()
