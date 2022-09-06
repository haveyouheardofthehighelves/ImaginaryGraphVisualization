from sympy import symbols, preorder_traversal, Float
import re
import sys
import subprocess
import math


def separate(somelist):
    imaginary = []
    real = []
    for expression in somelist:
        if 'i' in expression:
            if len(expression) > 2:
                imaginary.append(expression[:-2])
            elif len(expression) == 2:
                imaginary.append(str(-1))
            else:
                imaginary.append(str(1))
        else:
            real.append(expression)
    return real, imaginary


def transform(pretrans):
    newstring = ""
    for i in pretrans:
        if i == 'a':
            newstring += "(a*i)"
        elif i == 'b':
            newstring += "(b*i)"
        else:
            newstring += i
    return newstring


def angletransform(pretrans, oor):
    angle = 2 * math.pi / oor  # factor of rotation
    tangle = angle
    expressionlist = []
    for j in range(oor - 1):
        sinepart = str(math.sin(tangle))
        cospart = str(math.cos(tangle))
        newstring = ""
        for i in pretrans:
            if i == 'a':
                newstring += "(a*(" + cospart + "+i*" + sinepart + "))"
            elif i == 'b':
                newstring += "(b*(" + cospart + "+i*" + sinepart + "))"
            else:
                newstring += i
        expressionlist.append(newstring)
        print(newstring)
        tangle += angle
    return expressionlist


# a^4 = a(cos0+isin0)^4
# factor of rotation = 4
# angle = 2pi/4 = pi/2
# pi/2, pi, 3pi/2, 2pi

# what gets preserved during these sitautions and why?

def rewrite_imaginary(someList):
    for expression in someList:
        if 'i' in expression and expression[-1] != 'i':
            imagine = expression.split("i**")
            thenumber = int(imagine[1])
            if (thenumber - 3) % 4 == 0:
                if expression[0] == '-':
                    someList[someList.index(expression)] = imagine[0][1:] + "i"
                else:
                    addminus = '-'
                    addminus += imagine[0] + "i"
                    someList[someList.index(expression)] = addminus
            elif (thenumber - 1) % 4 == 0:
                someList[someList.index(expression)] = imagine[0] + "i"
            elif thenumber % 4 == 0:
                someList[someList.index(expression)] = imagine[0][0:-1]
            elif thenumber % 2 == 0:
                if expression[0] == '-':
                    someList[someList.index(expression)] = imagine[0][1:-1]
                else:
                    addminus = '-'
                    addminus += imagine[0][0:-1]
                    someList[someList.index(expression)] = addminus


def import_libraries(filename):
    f = open(filename, "w")
    f.write("import numpy as np\n")
    f.write("import matplotlib.pyplot as plt\n")
    f.write("import sys\n")
    f.close()


def Write_graph(somelist, filename, title):
    if len(somelist) <= 0:
        print("\nno " + title + " part\n")
        return
    title_ext = ""
    f = open(filename, "a")
    f.write("a = np.linspace(-10, 10, 100)\n")
    f.write("b = np.linspace(-10, 10, 100)\n")
    f.write("a, b = np.meshgrid(a, b)\n")
    f.write("z = ")
    sumstring = ""
    for i in somelist:
        sumstring += i
        sumstring += "+"
    sumstring = sumstring[:-1:]
    test = sympy.expand(sumstring)
    newstring = str(test)
    ex2 = test
    for a in preorder_traversal(ex2):
        if isinstance(a, Float):
            ex2 = ex2.subs(
                a, round(a, 7))

    ex2 = str(ex2)

    if ex2.strip() == "0":
        print("\nno " + title + " part\n")
        f.close()
        return
    newlist = ex2.split('+')
    if len(newlist) > 1:
        for i in range(len(newlist) - 1):
            f.write("(" + newlist[i] + ")")
            f.write('+')
            title_ext += (newlist[i] + "+")
        f.write("(" + newlist[-1] + ")\n")
        title_ext += newlist[-1]
    else:
        a = newlist[0]
        if a.isdigit():
            f.write(a + "+ (a-a)\n")
        else:
            f.write(newlist[0] + "\n")
        title_ext += newlist[0]
    f.write("fig = plt.figure(figsize=[12, 8])\n")
    f.write("fig.suptitle(" + "'" + title + ": " + title_ext + "'" + ")\n")
    f.write("ax = plt.axes(projection='3d')\n")
    f.write("ax.plot_surface(a, b, z)\n")
    f.close()


def instructions():
    print("\n -g to enter main function of program, no argument afterwards")
    print("Anything being multiplied must be separated by * EX: ab must be a*b")
    print("Can use a,b for polynomials, and imaginary numbers can be represented by i")
    print("You can select aspects of graph once graph is parsed")
    print("-h to print this message again\n")


def showplot(filename):
    f = open(filename, "a")
    f.write("plt.show()\n")
    subprocess.Popen(["python", filename])


def split(somestring):
    somestring = somestring.lower()
    try:
        ex = sympy.expand(somestring)
    except Exception as e:
        print("\ninvalid input, use -h command for clearer instructions")
        exit(1)

    ex = str(ex)
    # print(ex)
    ostring = ""
    for i in range(len(ex)):
        if ex[i] == '-' and i != 0:
            if ex[i - 1] != 'e':
                ostring += '+-'
            else:
                ostring += '-'
        else:
            ostring += ex[i]

    ostring = re.sub(r"\s+", "", ostring, flags=re.UNICODE)
    returnlist = ostring.split('+')
    return returnlist


def printmenu():
    print("\n[1] for original real part:")
    print("[2] for original imaginary part:")
    print("[3] for transformed real part:")
    print("[4] for transformed imaginary part:")
    print("[5] roots of unity rotation")
    print("[6] print menu")
    print("[q] to quit\n")


def rootsofunity(fraction):
    a_splitlist = angletransform(gfg_exp, int(fraction))
    x = input("enter state of rotation between 1 - " + str(int(fraction)) + ": ")
    while x != 'q':
        if x.isdigit() and (0 < int(x) <= int(fraction)):
            if int(x) == int(fraction):
                print("input is equivalent to original graph")
            else:
                anglegraph = split(a_splitlist[int(x) - 1])
                rewrite_imaginary(anglegraph)
                print(anglegraph)
                r_angle, i_angle = separate(anglegraph)
                import_libraries("myfile.py")
                Write_graph(r_angle, "myfile.py", "Real Rotated by a factor of " + x + "/" + fraction)
                showplot("myfile.py")

                import_libraries("other.py")
                Write_graph(i_angle, "other.py", "Imaginary Rotated by a factor of " + x + "/" + fraction)
                showplot("other.py")
        x = input("enter state of rotation between 1 - " + str(int(fraction)) + " (q to exit to menu): ")


def menuoptions():
    printmenu()
    condition = input("enter input: ")

    while condition != "q":
        if condition == "1":
            import_libraries("myfile.py")
            Write_graph(realist, "myfile.py", "og-real")
            showplot("myfile.py")
        elif condition == "2":
            import_libraries("myfile.py")
            Write_graph(imaginarylist, "myfile.py", "og-imaginary")
            showplot("myfile.py")
        elif condition == "3":
            import_libraries("myfile.py")
            Write_graph(t_realist, "myfile.py", "transformed-real")
            showplot("myfile.py")
        elif condition == "4":
            import_libraries("myfile.py")
            Write_graph(t_imaginarylist, "myfile.py", "transformed-imaginary")
            showplot("myfile.py")
        elif condition == "5":
            fraction = input("Select fraction of rotation: ")
            rootsofunity(fraction)
            printmenu()
        elif condition == "6":
            printmenu()
        elif condition == "q":
            exit(1)
        else:
            print("invalid input\n")
        condition = input("\nenter input: ")


x, y, z = symbols('a b i')

if len(sys.argv) >= 2:
    if sys.argv[1] == "-h":
        instructions()
        exit(1)
else:
    gfg_exp = input("Enter a expression: ")


splitlist = split(gfg_exp)

t_splitlist = split(transform(gfg_exp))
rewrite_imaginary(splitlist)
rewrite_imaginary(t_splitlist)
realist, imaginarylist = separate(splitlist)
t_realist, t_imaginarylist = separate(t_splitlist)

print("og-realpart: " + str(realist))
print("og-imaginarypart: " + str(imaginarylist))
print("transformed-realpart " + str(t_realist))
print("transformed-imaginarypart " + str(t_imaginarylist))

menuoptions()
