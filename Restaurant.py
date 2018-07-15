from tkinter import *
import time
import random;

window = Tk()
window.title("Restaurant Management System")
window.geometry('1500x800+0+0')

head = Frame(window, bg="white", width=1000, height=50)
head.pack(side=TOP)

ls = Frame(window, width=600, height=600)
ls.pack(side=LEFT)

rs = Frame(window, width=400, height=600)
rs.pack(side=RIGHT)

# ...Titles...
MainTitle = Label(head, fg="black", bd=10, text="Restaurant Management System", font=("arial bold", 50), anchor='w')
MainTitle.grid(row=0, column=0)

Title = Label(head, fg="black", bd=10, text=time.asctime(time.localtime(time.time())), font=("arial bold", 20),
              anchor='w')
Title.grid(row=2, column=0)

# ........ Calculator .........

Input = StringVar()
operator = ''


def Click(numbers):
    global operator
    operator = operator + str(numbers)
    Input.set(operator)


def Equal():
    global operator
    result = str(eval(operator))
    Input.set(result)


def Clear():
    global operator
    operator = ""
    Input.set('0')


def Ref():
    x = random.randint(0, 10000)
    randomRef = str(x)
    rand.set(randomRef)

    COF = float(Fries.get())
    COB = float(Burger.get())
    COLM = float(Lunch_Meal.get())
    COD = float(Drinks.get())
    COCB = float(Chicken_burger.get())
    COChB = float(Cheese_burger.get())

    costoffries = COF * 25
    costofburger = COB * 35
    costoflunchmeal = COLM * 50
    costofcheeseburger = COChB * 50
    costofdrinks = COD * 35
    costofchickenburger = COCB * 60

    costofmeal = "₹", str('%.2f' % (
                costoffries + costofburger + costoflunchmeal + costofcheeseburger + costofdrinks + costofchickenburger))
    Tax1 = (
                      costoffries + costofburger + costoflunchmeal + costofcheeseburger + costofdrinks + costofchickenburger) * 0.33
    Totalcost = (costoffries + costofburger + costoflunchmeal + costofcheeseburger + costofdrinks + costofchickenburger)
    Ser_charge = ((
                              costoffries + costofburger + costoflunchmeal + costofcheeseburger + costofdrinks + costofchickenburger) / 99)
    Service = "₹", str('%.2f' % Ser_charge)
    Overallcost = "₹", str('%.2f' % (Tax1 + Totalcost + Ser_charge))
    Taxpaid = "₹", str('%.2f' % Tax1)

    Service_Charge.set(str(Service))
    Cost.set(str(costofmeal))
    Tax.set(str(Taxpaid))
    Subtotal.set(str(costofmeal))
    TotalCost.set(str(Overallcost))


def qExit():
    window.destroy()


def Reset():
    rand.set('0')
    Fries.set('0')
    Largefries.set('0')
    Burger.set('0')
    Lunch_Meal.set('0')
    Subtotal.set('0')
    TotalCost.set('0')
    Cost.set('0')
    Service_Charge.set('0.0')
    Drinks.set('0')
    Tax.set('0')
    cost.set('0')
    Chicken_burger.set('0')
    Cheese_burger.set('0')


def price():
    prices = Tk()
    prices.geometry("500x200+0+0")
    prices.title("Price List")
    lbl = Label(prices, font=('arial bold', 15), text="ITEM", fg="black", bd=5)
    lbl.grid(row=0, column=0)
    lbl = Label(prices, font=('arial bold', 15), text="_____________", fg="white", anchor=W)
    lbl.grid(row=0, column=2)
    lbl = Label(prices, font=('arial bold', 15), text="PRICE", fg="black", anchor=W)
    lbl.grid(row=0, column=3)
    lbl = Label(prices, font=('arial bold', 15), text="Fries Meal", anchor=W)
    lbl.grid(row=1, column=0)
    lbl = Label(prices, font=('arial bold', 15), text="25", anchor=W)
    lbl.grid(row=1, column=3)
    lbl = Label(prices, font=('arial bold', 15), text="Lunch Meal", anchor=W)
    lbl.grid(row=2, column=0)
    lbl = Label(prices, font=('arial bold', 15), text="40", anchor=W)
    lbl.grid(row=2, column=3)
    lbl = Label(prices, font=('arial bold', 15), text="Burger Meal", anchor=W)
    lbl.grid(row=3, column=0)
    lbl = Label(prices, font=('arial bold', 15), text="35", anchor=W)
    lbl.grid(row=3, column=3)
    lbl = Label(prices, font=('arial bold', 15), text="Chicken Burger", anchor=W)
    lbl.grid(row=4, column=0)
    lbl = Label(prices, font=('arial bold', 15), text="50", anchor=W)
    lbl.grid(row=4, column=3)
    lbl = Label(prices, font=('arial bold', 15), text="Cheese Burger", anchor=W)
    lbl.grid(row=5, column=0)
    lbl = Label(prices, font=('arial bold', 15), text="30", anchor=W)
    lbl.grid(row=5, column=3)
    lbl = Label(prices, font=('arial bold', 15), text="Drinks", anchor=W)
    lbl.grid(row=6, column=0)
    lbl = Label(prices, font=('arial bold', 15), text="35", anchor=W)
    lbl.grid(row=6, column=3)


caldisplay = Entry(rs, font=('times new roman', 20, 'bold'), textvar=Input, insertwidth=15, justify='right',
                   bg='light grey')
caldisplay.grid(columnspan=4)

# ...... 4th row .......

zero = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='0', bg='light grey',
              command=lambda: Click(0))
zero.grid(row=4, column=0)

clear = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='C', bg='light grey', command=Clear)
clear.grid(row=4, column=1)

equal = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='=', bg='light grey', command=Equal)
equal.grid(row=4, column=2)

divide = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='/', bg='light grey',
                command=lambda: Click("/"))
divide.grid(row=4, column=3)

# ...... 3rd row ......

one = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='1', bg='light grey',
             command=lambda: Click(1))
one.grid(row=3, column=0)

two = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='2', bg='light grey',
             command=lambda: Click(2))
two.grid(row=3, column=1)

three = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='3', bg='light grey',
               command=lambda: Click(3))
three.grid(row=3, column=2)

add = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='+', bg='light grey',
             command=lambda: Click("+"))
add.grid(row=3, column=3)

# ...... 2nd Row .......

four = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='4', bg='light grey',
              command=lambda: Click(4))
four.grid(row=2, column=0)

five = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='5', bg='light grey',
              command=lambda: Click(5))
five.grid(row=2, column=1)

six = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='6', bg='light grey',
             command=lambda: Click(6))
six.grid(row=2, column=2)

sub = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='-', bg='light grey',
             command=lambda: Click("-"))
sub.grid(row=2, column=3)

# ... 1st Row ...

seven = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='7', bg='light grey',
               command=lambda: Click(7))
seven.grid(row=1, column=0)

eight = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='8', bg='light grey',
               command=lambda: Click(8))
eight.grid(row=1, column=1)

nine = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='9', bg='light grey',
              command=lambda: Click(9))
nine.grid(row=1, column=2)

mult = Button(rs, padx=15, pady=15, font=('times new roman', 20, 'bold'), text='*', bg='light grey',
              command=lambda: Click("*"))
mult.grid(row=1, column=3)

rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Lunch_Meal = StringVar()
Subtotal = StringVar()
TotalCost = StringVar()
Cost = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Chicken_burger = StringVar()
Cheese_burger = StringVar()

# .................Labels(Meals - 1)......................

lblreference = Label(ls, font=('arial bold', 15), text='Order No.', bd=15, anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(ls, font=('arial bold', 15), textvariable=rand, bd=10, insertwidth=5, justify='right')
txtreference.grid(row=0, column=1)

lblFries = Label(ls, font=('arial bold', 15), text='Fries Meal', bd=15, anchor='w')
lblFries.grid(row=1, column=0)
txtFries = Entry(ls, font=('arial bold', 15), textvariable=Fries, bd=10, insertwidth=5, justify='right')
txtFries.grid(row=1, column=1)

lblBurger = Label(ls, font=('arial bold', 15), text='Burger Meal', bd=15, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger = Entry(ls, font=('arial bold', 15), textvariable=Burger, bd=10, insertwidth=5, justify='right')
txtBurger.grid(row=2, column=1)

lblLunch_Meal = Label(ls, font=('arial bold', 15), text='Lunch Meal', bd=15, anchor='w')
lblLunch_Meal.grid(row=3, column=0)
txtLunch_Meal = Entry(ls, font=('arial bold', 15), textvariable=Lunch_Meal, bd=10, insertwidth=5, justify='right')
txtLunch_Meal.grid(row=3, column=1)

lblChicken = Label(ls, font=('arial bold', 15), text='Chicken Burger', bd=15, anchor='w')
lblChicken.grid(row=4, column=0)
txtChicken = Entry(ls, font=('arial bold', 15), textvariable=Chicken_burger, bd=10, insertwidth=5, justify='right')
txtChicken.grid(row=4, column=1)

lblCheese = Label(ls, font=('arial bold', 15), text='Cheese Burger', bd=15, anchor='w')
lblCheese.grid(row=5, column=0)
txtCheese = Entry(ls, font=('arial bold', 15), textvariable=Cheese_burger, bd=10, insertwidth=5, justify='right')
txtCheese.grid(row=5, column=1)

# ...............Labels (Meals-2)...............

lblDrinks = Label(ls, font=('arial bold', 15), text='Drinks', bd=15, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(ls, font=('arial bold', 15), textvariable=Drinks, bd=10, insertwidth=5, justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(ls, font=('arial bold', 15), text='Cost', bd=15, anchor='w')
lblCost.grid(row=1, column=2)
txtCost = Entry(ls, font=('arial bold', 15), textvariable=Cost, bd=10, insertwidth=5, justify='right')
txtCost.grid(row=1, column=3)

lblService = Label(ls, font=('arial bold', 15), text='Service', bd=15, anchor='w')
lblService.grid(row=2, column=2)
txtService = Entry(ls, font=('arial bold', 15), textvariable=Service_Charge, bd=10, insertwidth=5, justify='right')
txtService.grid(row=2, column=3)

lblTax = Label(ls, font=('arial bold', 15), text='Tax', bd=15, anchor='w')
lblTax.grid(row=3, column=2)
txtTax = Entry(ls, font=('arial bold', 15), textvariable=Tax, bd=10, insertwidth=5, justify='right')
txtTax.grid(row=3, column=3)

lblSubtotal = Label(ls, font=('arial bold', 15), text='Subtotal', bd=15, anchor='w')
lblSubtotal.grid(row=4, column=2)
txtSubtotal = Entry(ls, font=('arial bold', 15), textvariable=Subtotal, bd=10, insertwidth=5, justify='right')
txtSubtotal.grid(row=4, column=3)

lblTotalCost = Label(ls, font=('arial bold', 15), text='Total Cost', bd=15, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(ls, font=('arial bold', 15), textvariable=TotalCost, bd=10, insertwidth=5, justify='right')
txtTotalCost.grid(row=5, column=3)

# ..................... Buttons .....................
Price = Button(ls, padx=15, pady=5, font=('arial bold', 16), width=10, bd=15, text="Price", command=price)
Price.grid(row=7, column=0)

Total = Button(ls, padx=15, pady=5, font=('arial bold', 15), width=10, bd=15, text="Total", command=Ref)
Total.grid(row=7, column=1)

Reset = Button(ls, padx=15, pady=5, font=('arial bold', 15), width=10, bd=15, text="Reset", command=Reset)
Reset.grid(row=7, column=2)

Exit = Button(ls, padx=15, pady=5, font=('arial bold', 15), width=10, bd=15, text="Exit", command=qExit)
Exit.grid(row=7, column=3)

window.mainloop()