#practica 13
#christian daniel tellez fernandez
#farfan de leon jose osvaldo

from colorama import init, Fore, Back, Cursor, Style;
import colorama;
from itertools import cycle, count;
from time import sleep
import shutil
import os
import msvcrt
from collections import Counter
import random;


def e1():#toma un archivo y lo imprime de manera inversa por renglon y cuenta palabras y letras
    pa=0
    lista=[];    
    archivo=open("pepe.txt",mode="r",encoding="cp1252");
    leer=archivo.read()
    leer1=leer[::-1]
    print(leer1)
    palabras=leer1.split()
    letras=leer1
    letras=letras.replace(" ","")
    i=0
    while i < len(palabras):
        palabra=palabras[i]
        i+=1
    print("\nNumero de palabras: ",i)
    k=0
    while k < len(letras):
        letra=letras[k]
        k+=1
    print("\nNumero de letras: ",k)
    sleep(9)
    archivo.close()
    menu();
    


        
    
def e2():#ingresa un archivo y lo copia cuantas veces se desee este es modificado con colorama
    init(autoreset = True);
    lista2=[];
    cont=cont1=0;
    try:
        nom=str(input("ingresa el nombre del archivo: "));
        archivo=open(nom,mode="r",encoding="cp1252");
        print("El nombre de este archivo es", nom);
        texto=archivo.read();
        lista1=texto.split(" ");
        print(texto)
        while True:
            opc=str(input("Quieres abrir el programa otra vez?, escribe si para continuar o presiona enter para salir: "));
            if opc == "si":
                print("El nombre de este archivo es", nom, cont+1);
                cont+=1;
                nn="pipo(" + str(cont)+").txt";#define el nuevo nombre
                shutil.copy2(nom, nn)
                for i in lista1:
                    if cont1 % 2 == 0:
                        aux=i.upper();
                        lista2.append(aux);
                    else:
                        aux2=i.lower();
                        lista2.append(aux2);
                    cont1+=1
            cont1+=1;
            bueno=" ".join(lista2);
            colors = list(vars(colorama.Fore).values())
            colored_word= [random.choice(colors) + word for word in bueno.split(" ")]
            print(' '.join(colored_word))
            archivo.close()
        
            if opc == "":
                archivo.close();
                menu();
                break
    except:
        print("haz cometido un error, por lo tanto se cerrara el programa");
        while True:
            break

def e3():#toma un archivo e imprime las veces que se repiten las palabras ingresadas por el usuario y separadas por coma

    lista=[]
    lista2=[]
    colores=[Fore.RED,Fore.GREEN];
    cont=0;
    nom=str(input("ingrese el nombre del archivo: "));
    archivo=open(nom,mode="r",encoding="cp1252");
    lines=archivo.readlines()
    print("archivo-> ",lines); 
    palabra=str(input("Escribe palabras separadas por comas: "));
    lista2 = palabra.split(",")
    print("ejemplos a buscar:",lista2)    
    for eje in lista2:
        for line in lines:
            palabra=line.split()
            for p in palabra:
                if p == eje:
                    cont=cont+1;
                    lista.append(p);
                    
                    
    print(lines);        
    counts = Counter(lista)
    print(counts)
    sleep(3)

    archivo.close();
    menu();
    


    
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
                    print(Cursor.POS(4,11)+ Fore.CYAN +"practica 13");
                    sleep(1)
                    print(Cursor.POS(4,12)+ Fore.CYAN + Style.BRIGHT + "tellez fernandez christian daniel");
                    sleep(1)
                    print(Cursor.POS(4,13)+ Fore.CYAN + Style.BRIGHT + "farfan de leon jose osvaldo");
                    sleep(3)
                    os.system("CLS")
                    print(Cursor.POS(4,12)+ Fore.RED + "fin del juego");
                    sleep(3)
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
