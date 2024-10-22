#practica 11
#colorama_time

from time import sleep
from colorama import init, Fore, Back, Cursor, Style;
import os
import textwrap
from itertools import cycle;

        
def e1():
    error=0;
    nombresl=[]
    lista=[]
    i=0;
    try:
        x=1;
        y=5;
        init(autoreset = True);
        while x < 80:#largo de x
            print(Cursor.POS(x,5) + Fore.RED + Style.BRIGHT + Back.RED + ":");
            print(Cursor.POS(x,20) + Fore.RED + Style.BRIGHT + Back.RED + ":");
            x=x+1;
        while y < 20:#largo de y
            print(Cursor.POS(1,y) + Fore.RED + Back.RED + ":");
            print(Cursor.POS(79,y) + Fore.RED + Back.RED + ":");
            y=y+1;
        while True:
            print(Cursor.POS(4,8) + "ingrese un: 0, para dejar de ingresar nombres.");
            print(Cursor.POS(4,9) + "ingrese el nombre a agregar: ", end='');
            nom=str(input());
            if nom == "0":#si el valor es cero cerramos el bucle
                conjuntoN=set(nombresl);
                nombresl=list(nombresl);
                print(Cursor.POS(4,11) + "ingrese la letra final que desea buscar de cada nombre: ", end='');
                let=(input());
                while i < len(nombresl):
                    lf=nombresl[i]
                    lf= lf[-1];
                    if let == lf:#selecciona todos las cadenas que acaben con el valor ingresado
                        lista.append(nombresl[i]);
                    i=i+1
                print(Cursor.POS(4,13)+"nombres encontrados: ",lista)
                sleep(7)
                os.system("CLS")
                menu();
                break;#regresamos al menu
            nombresl.append(nom);#agregamos los valores a la lista            
                
    except:
        print("dato invalido");
        falla();
        error=error+1;
    return error


def e2():#ingresa cadenas y devuelve la mas corta
    lista=[];
    try:
        x=1;#donde empieza x
        y=5;#donde empieza y
        init(autoreset = True);
        while x < 60:#largo de x
            print(Cursor.POS(x,5) + Fore.RED + Style.BRIGHT + Back.CYAN + ":");
            print(Cursor.POS(x,20) + Fore.RED + Style.BRIGHT + Back.CYAN + ":");
            x=x+1;
        while y < 20:#largo de y
            print(Cursor.POS(1,y) + Fore.RED + Back.CYAN + ":V");
            print(Cursor.POS(58,y) + Fore.RED + Back.CYAN + "V:");
            y=y+1;
        print(Cursor.POS(4,6) + "presione (0) para salir");
        while True:
            print(Cursor.POS(4,7)+"ingrese las palabras a agregar: ", end='');
            pal=str(input());
            conjunto=set(lista);
            if pal == "0":#acaba el ciclo
                print(Cursor.POS(4,12) + min(conjunto));
                sleep(3)
                os.system("CLS")
                menu();
                break;
            lista.append(pal);      



    except:
        print("dato invalido");
        falla();
        error=error+1;
        e2();
    return error

def e3():#ingresa cadenas e imprime el prefijo comun de todas.
    lista=[];
    cont=0;
    try:
        x=1;#donde empieza x
        y=5;#donde empieza y
        init(autoreset = True);
        while x < 60:#largo de x
            print(Cursor.POS(x,5) + Fore.RED + Style.BRIGHT + Back.YELLOW + ":");
            print(Cursor.POS(x,20) + Fore.RED + Style.BRIGHT + Back.YELLOW + ":");
            x=x+1;
        while y < 20:#largo de y
            print(Cursor.POS(1,y) + Fore.RED + Back.YELLOW + ":");
            print(Cursor.POS(58,y) + Fore.RED + Back.YELLOW + ":");
            y=y+1;
        for i in cycle(" "):
                print(Cursor.POS(4,7) + "escribe la cadena numero o (no) para salir:" ,cont+1);
                cad=str(input(""));
                lista.append(cad);
                conj=set(lista);
                cont=cont+1;
                if cad == "no":#acaba el ciclo
                    lista.remove("no");
                    n=0;
                    m=1;
                    x=lista[n];
                    y=lista[m];
                    for i in range(len(lista)):#muestra el prefijo mas largo
                        pre=x[:i];
                        pref=y[:i];
                    if (pre == pref):
                        print(Cursor.POS(4,10) + "el prefijo comun mas corto es" ,pref[:-1]);
                        sleep(5)
                        menu();
                        break
                        menu();
                    else:#muestra mensaje que no hay prefijo
                        print("no hay prefijo comun mas corto");
                        sleep(4)
                        menu();
                        break
                    break
                    sleep(7)
                    os.system("CLS")
                    menu();
                    break
    except:
        print("has introducido un dato erroneo, el programa se cerrara");



def e4():
    lista=[];
    try:
        x=1;#donde empieza x
        y=5;#donde empieza y
        init(autoreset = True);
        while x < 60:#largo de x
            print(Cursor.POS(x,5) + Fore.MAGENTA + Style.BRIGHT + Back.MAGENTA + ":");
            print(Cursor.POS(x,20) + Fore.MAGENTA + Style.BRIGHT + Back.MAGENTA + ":");
            x=x+1;
        while y < 20:#largo de y
            print(Cursor.POS(1,y) + Fore.MAGENTA + Back.MAGENTA + ":V");
            print(Cursor.POS(58,y) + Fore.MAGENTA + Back.MAGENTA + ":V");
            y=y+1;
        while True:
            print(Cursor.POS(4,7) + "ingrese la frase: ", end='');
            cn=str(input());
            print(Cursor.POS(4,10) + "ingrese el numero: ", end='');
            d=int(input());
            for line in (textwrap.wrap(cn, width = d)):#dividimos la frase en la cantidad de caracteres seleccionados por el usuario
                lista.append(line);
                conjunto=set(lista);
                print(conjunto);
            sleep(10)
            menu();
            break;
            
    except:
        print("dato invalido");
        falla();
        error=error+1;
        e4();


def falla():
    for x in range(100,138):
        print(Cursor.POS(x,18) + Fore.RED + Back.RED + " ");
        print(Cursor.POS(x,22) + Fore.RED + Back.RED + " ");
    for y in range(18,22):
        print(Cursor.POS(80,y) + Fore.RED + " ");
        print(Cursor.POS(117,y) + Fore.RED + " ");
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
        
        while z < 120:#marco de errores
            print(Cursor.POS(z,5) + Fore.RED + Back.RED + ":");
            print(Cursor.POS(z,20) + Fore.RED  + Back.RED + ":");
            z=z+1;
        while w < 20:
            print(Cursor.POS(65,w) + Fore.RED + Back.RED + ":");
            print(Cursor.POS(119,w) + Fore.RED + Back.RED + ":");
            w=w+1;
        print(Cursor.POS(66,7)+ "errores totales");
        print(Cursor.POS(66,8)+ "errores en el ejercicio 1:");
        print(Cursor.POS(66,9)+ "errores en el ejercicio 2:");
        print(Cursor.POS(66,10)+ "errores en el ejercicio 3:");
        print(Cursor.POS(66,11)+ "errores en el ejercicio 4:");
        print(Cursor.POS(66,12)+ "errores en el menu:");
        
        while x < 60:#marcos de menu
            print(Cursor.POS(x,5) + Fore.BLUE + Style.BRIGHT + Back.BLUE + ":");
            print(Cursor.POS(x,20) + Fore.BLUE + Style.BRIGHT + Back.BLUE + ":");
            x=x+1;
        while y < 20:
            print(Cursor.POS(1,y) + Fore.BLUE + Back.BLUE + ":");
            print(Cursor.POS(59,y) + Fore.BLUE + Back.BLUE + ":");
            y=y+1;
        print(Cursor.POS(4,7)+"      Menu:");
        print(Cursor.POS(4,8) + Fore.RED +"1.- ejercicio 1");
        print(Cursor.POS(4,9) + Fore.CYAN +"2.- ejercicio 2");
        print(Cursor.POS(4,10) + Fore.YELLOW +"3.- ejercicio 3");
        print(Cursor.POS(4,11) + Fore.MAGENTA +"4.- ejercicio 4");
        print(Cursor.POS(4,12) + Fore.GREEN +"5.- salir");
        print(Cursor.POS(4,13)+"ingrese el numero de ejercicio que desea realizar: ", end='');
        ne=int(input());
        if ne > 0 and ne <=5:
            while ne > 0 and ne <= 5:#comparamos el valor ingresado por el usuario
                if  ne == 1:
                    os.system("CLS");
                    e1();
                    
                elif ne == 2:
                    os.system("CLS")
                    e2();
                    
                    
                elif ne == 3:
                    os.system("CLS")
                    e3();
                    
                    
                elif ne == 4:
                    os.system("CLS")
                    e4();
                    

                elif ne == 5:#sale del programa
                    print(Cursor.DOWN(5) + "Has decidido salir...");
                    os.system("CLS")
                    sleep(1)
                    print(Cursor.POS(4,11)+ Fore.CYAN +"practica 11");
                    sleep(1)
                    print(Cursor.POS(4,12)+ Fore.CYAN + Style.BRIGHT +"farfan de leon jose osvaldo");
                    sleep(1)
                    print(Cursor.POS(4,13)+ Fore.CYAN + Style.BRIGHT + "tellez fernandez christian daniel ");
                    sleep(3)
                    os.system("CLS")
                    print(Cursor.POS(4,12)+ Fore.RED + "fin del juego");
                    sleep(3)
                    break;
                break;
            else:
                falla();
                variable = variable +1;
                
                menu();
        else:
            falla();
            menu();
    except:
        falla();
        menu();

menu();
