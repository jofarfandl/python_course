#practica 12
#menu con errores


from colorama import init, Fore, Back, Cursor, Style;
from itertools import cycle, count;
from time import sleep
import textwrap
import os
import msvcrt


def e1():#ingresa una cadena y devuelve las palabras repetidas y cuantas veces se repite
    try:
        x=1;#donde empieza x
        y=5;#donde empieza y
        init(autoreset = True);
        while x < 60:#largo de x
            print(Cursor.POS(x,5) + Fore.RED + Style.BRIGHT + Back.CYAN + ":");#primera linea de x y donde empieza
            print(Cursor.POS(x,20) + Fore.RED + Style.BRIGHT + Back.CYAN + ":");#segunda linea de x y donde empieza
            x=x+1;
        while y < 20:#largo de y
            print(Cursor.POS(1,y) + Fore.RED + Back.CYAN + ":V");#primera linea de y y donde empieza
            print(Cursor.POS(58,y) + Fore.RED + Back.CYAN + "V:");#segunada linea de y y donde empieza
            y=y+1;
        while True:
            d2 = {}
            cont=0
            L = []
            print(Cursor.POS(4,7) + "ingrese la cadena: ",end="")
            myList1=input().lower()
            pa1=myList1.split();
            h ={k:myList1.count(k) for k in list(pa1)}
            for i in h:
                L.append(h[i]);
            r = 0;
            for i in h:
                if cont%2 == 0:
                    i=i.upper()
                    d2[i] = L[r];  
                elif cont%2 != 0:
                    i=i.lower()
                    d2[i] = L[r];
                cont= cont + 1
                r = r + 1
            print(d2);
            sleep(6)
            os.system("CLS")
            menu();
            

    except:
        print("dato invalido...");

        
def e2():#ingrese un contacto y lo agrega a una agenda en caso que no exista crea el contacto(se puede modificar y poner 2 )
    os.system("CLS")
    agenda={};
    x=1;#donde empieza x
    y=5;#donde empieza y
    init(autoreset = True);
    while x < 90:#largo de x
        print(Cursor.POS(x,5) + Fore.RED + Style.BRIGHT + Back.CYAN + ":");
        print(Cursor.POS(x,20) + Fore.RED + Style.BRIGHT + Back.CYAN + ":");
        x=x+1;
    while y < 20:#largo de y
        print(Cursor.POS(1,y) + Fore.RED + Back.CYAN + ":");
        print(Cursor.POS(88,y) + Fore.RED + Back.CYAN + ":");
        y=y+1; 
    print(Cursor.POS(4,7)+"ejercicio 2");
    for i in count():
        
        print(Cursor.POS(4,8)+"ingrese el nombre de contacto: ",end="");
        contacto=str(input());
        if contacto in agenda:
            print(Cursor.POS(4,10)+"contacto encontrado:",contacto,"->",agenda[contacto])
            print(Cursor.POS(4,11)+"ingrese un -1- para modificar el numero");
            print(Cursor.POS(4,12)+"ningrese un 2 para ingresar o modificar otro numero");
            print(Cursor.POS(4,13)+"ingrese un 0 para salir:",end="");
            opc=str(input());
            if opc == "1":
                print(Cursor.POS(4,11)+"ingrese el numero modificado: ",end="");
                num=int(input());
                agenda.update({contacto:num});
                print(Cursor.POS(4,15)+ str(agenda));
                
            elif opc == "2":
                print(Cursor.POS(4,9)+"ingrese el numero 2: ");
                num2=int(input());
                agenda[contacto]=[num1,num2];
                print(Cursor.POS(4,15)+ str(agenda));

            elif opc == "0":
                menu();
                break
                
            else:
                print("dato invalido");
        elif contacto == "0":
            menu();
            break
            
                
        else:
            print(Cursor.POS(4,9)+ "no se encontro ningun contacto");
            print(Cursor.POS(4,10)+"agregue el numero del contacto: ",end="");
            num1=int(input());
            agenda[contacto]=[num1];
            print(Cursor.POS(4,15)+ str(agenda));
            
def e3():#ingresa una cadena e imprime cada letra de la cadena correspondiente con la palabra que contenga esa letra hasta la derecha
    try:
        x=1;#donde empieza x
        y=5;#donde empieza y
        init(autoreset = True);
        while x < 60:#largo de x
            print(Cursor.POS(x,5) + Fore.RED + Style.BRIGHT + Back.MAGENTA + ":");#primera linea de x y donde empieza
            print(Cursor.POS(x,20) + Fore.RED + Style.BRIGHT + Back.MAGENTA + ":");#segunda linea de x y donde empieza
            x=x+1;
        while y < 20:#largo de y
            print(Cursor.POS(1,y) + Fore.RED + Back.MAGENTA + ":V");#primera linea de y y donde empieza
            print(Cursor.POS(58,y) + Fore.RED + Back.MAGENTA + "V:");#segunada linea de y y donde empieza
            y=y+1;
        lista=[] 
        dicc={}
        lista2=[]
        print(Cursor.POS(4,7) + "agrega tu cadena :",end="");
        ca=input()
        ca2=ca.replace(" ","")
        for i in ca2:
            if i not in lista:  
                lista.append(i) 
        ca3=(ca.split(" ")); 
        for i in ca3:  
            if i not in dicc:
                dicc[i]=0 
        for i in lista: 
            for l in dicc: 
                if i in l and i not in lista2:
                    print(i,':',l);
                    lista2.append(i)
                    sleep(.5)
        os.system("CLS");
        menu();                  

    except:
        print("dato invalido...")

        

def falla():
    for x in range(80,118):
        print(Cursor.POS(x,18) + Fore.RED + "x");
        print(Cursor.POS(x,22) + Fore.RED + "x");
    for y in range(18,22):
        print(Cursor.POS(80,y) + Fore.RED + "x");
        print(Cursor.POS(117,y) + Fore.RED + "x");
    print(Fore.RED + Cursor.POS(87,20) + "error... dato invalido");
    sleep(2);
    for x in range(79,118):
        print(Fore.RESET + Cursor.POS(x,18) + " ");
        print(Fore.RESET + Cursor.POS(x,19) + " ");
        print(Fore.RESET + Cursor.POS(x,20) + " ");
        print(Fore.RESET + Cursor.POS(x,20) + " ");
        print(Fore.RESET + Cursor.POS(x,20) + " ");

def menu():
    os.system("CLS")

    try:
        x=1;
        y=5;
        z=65
        w=5;
        init(autoreset = True);
        while x < 60:#marcos de menu
            print(Cursor.POS(x,5) + Fore.BLUE  + Back.CYAN + ":");
            print(Cursor.POS(x,20) + Fore.BLUE  + Back.CYAN + ":");
            x=x+1;
        while y < 20:
            print(Cursor.POS(1,y) + Fore.BLUE + Back.CYAN + ":");
            print(Cursor.POS(59,y) + Fore.BLUE + Back.CYAN + ":");
            y=y+1;
        while z < 120:#marco de errores
            print(Cursor.POS(z,5) + Fore.RED + Back.RED + ":");
            print(Cursor.POS(z,14) + Fore.RED  + Back.RED + ":");
            z=z+1;
        while w < 14:
            print(Cursor.POS(65,w) + Fore.RED + Back.RED + ":");
            print(Cursor.POS(119,w) + Fore.RED + Back.RED + ":");
            w=w+1;
        err1=0;
        err2=0;
        err3=0;
        errme=0;    
      
        print(Cursor.POS(66,6)+ "VENTANA DE ERRORES");
        print(Cursor.POS(66,7)+ "Errores totales:..............");
        print(Cursor.POS(66,8)+ "Errores en el", Fore.RED + "ejercicio 1:....");
        print(Cursor.POS(66,9)+ "Errores en el", Fore.BLUE + "ejercicio 2:....");
        print(Cursor.POS(66,10)+ "Errores en el", Fore.YELLOW + "ejercicio 3:....");
        print(Cursor.POS(66,11)+ "Errores en", Fore.CYAN +  "menu:..............",errme);

        print(Cursor.POS(4,7)+"      Menu:");
        print(Cursor.POS(4,8) + Fore.RED +"1.- Ejercicio 1");
        print(Cursor.POS(4,9) + Fore.BLUE +"2.- Ejercicio 2");
        print(Cursor.POS(4,10) + Fore.YELLOW +"3.- Ejercicio 3");
        print(Cursor.POS(4,12) + Fore.GREEN +"4.- salir");
            
        print(Cursor.POS(4,16)+"Ingrese el numero de ejercicio a realizar: ", end='');
        ne=int(input());
        if ne > 0 and ne <=4:#compara la eleccion y manda al ejercicio seleccionado
            while ne > 0 and ne <= 4:
                if ne == 1:
                    os.system("CLS");
                    e1();
                elif ne == 2:
                    os.system('CLS');
                    e2();
                elif ne == 3:
                    os.system("CLS");
                    e3();     
                elif ne == 4:
                    os.system("CLS");
                    print(Cursor.POS(4,11)+ Fore.CYAN +"practica 12");
                    sleep(1)
                    print(Cursor.POS(4,12)+ Fore.CYAN + Style.BRIGHT + "farfan de leon jose osvaldo ");
                    sleep(1)
                    print(Cursor.POS(4,13)+ Fore.CYAN + Style.BRIGHT + "tellez fernandez christian daniel");
                    sleep(3)
                    os.system("CLS")
                    print(Cursor.POS(4,12)+ Fore.RED + "fin del juego");
                    sleep(3)
                    break;
                break;
            break;
        else:
            falla();
            menu();
    except:
        falla();
        menu();
    return errme


menu();

