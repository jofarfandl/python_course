#practica 14

import msvcrt;
from colorama import init, Fore, Back, Cursor, Style;
import colorama;
from itertools import cycle, count;
from time import sleep
from datetime import date
import itertools
import shutil
import os
import msvcrt
import sys


def ventanas(b):
    x1=30
    y1=5
    x2=150
    y2=40
    if b == 1:
        init(autoreset=True)
        aux = x1
        x3 = x1-1
        y3= y1-1
        while x1 <= x2:
            print(Cursor.POS(x1,y1)+Back.CYAN+' ')
            print(Cursor.POS(x1,y2)+Back.CYAN+' ')
            x1+=1
        while y1 <= y2:
            print(Cursor.POS(aux,y1)+Back.CYAN+' ')
            print(Cursor.POS(x2,y1)+Back.CYAN+' ')
            y1+=1
        x4 = x3
        while x3 <= x2-1:
            print(Cursor.POS(x3,y3)+Back.LIGHTCYAN_EX+' ')
            x3+=1
        while y3 <= y2-1:
            print(Cursor.POS(x4,y3)+Back.LIGHTCYAN_EX+' ')
            y3+=1
            
    if b == 2:
        init(autoreset=True)
        aux = x1
        x3 = x1-1
        y3= y1-1
        while x1 <= x2:
            print(Cursor.POS(x1,y1)+Back.MAGENTA+' ')
            print(Cursor.POS(x1,y2)+Back.MAGENTA+' ')
            x1+=1
        while y1 <= y2:
            print(Cursor.POS(aux,y1)+Back.MAGENTA+' ')
            print(Cursor.POS(x2,y1)+Back.MAGENTA+' ')
            y1+=1
        x4 = x3
        while x3 <= x2-1:
            print(Cursor.POS(x3,y3)+Back.LIGHTMAGENTA_EX+' ')
            x3+=1
        while y3 <= y2-1:
            print(Cursor.POS(x4,y3)+Back.LIGHTMAGENTA_EX+' ')
            y3+=1
            

def menusito(a):
    if a == 1:
        print(Cursor.POS(75,18)+Back.RESET+"BIENVENIDO AL HOSPITAL");
        print(Cursor.POS(78,21)+Back.YELLOW+"Alta de pacientes");
        print(Cursor.POS(78,22)+Back.RESET+"Alta de medicos");
        print(Cursor.POS(78,23)+Back.RESET+"Alta de hospital");
        print(Cursor.POS(78,24)+Back.RESET+"Salir");
    if a == 2:
        print(Cursor.POS(75,18)+Back.RESET+"BIENVENIDO AL HOSPITAL");
        print(Cursor.POS(78,21)+Back.RESET+"Alta de pacientes");
        print(Cursor.POS(78,22)+Back.YELLOW+"Alta de medicos");
        print(Cursor.POS(78,23)+Back.RESET+"Alta de hospital");
        print(Cursor.POS(78,24)+Back.RESET+"Salir");
    if a == 3:
        print(Cursor.POS(75,18)+Back.RESET+"BIENVENIDO AL HOSPITAL");
        print(Cursor.POS(78,21)+Back.RESET+"Alta de pacientes");
        print(Cursor.POS(78,22)+Back.RESET+"Alta de medicos");
        print(Cursor.POS(78,23)+Back.YELLOW+"Alta de hospital");
        print(Cursor.POS(78,24)+Back.RESET+"Salir");
    if a == 4:
        print(Cursor.POS(75,18)+Back.RESET+"BIENVENIDO AL HOSPITAL");
        print(Cursor.POS(78,21)+Back.RESET+"Alta de pacientes");
        print(Cursor.POS(78,22)+Back.RESET+"Alta de medicos");
        print(Cursor.POS(78,23)+Back.RESET+"Alta de hospital");
        print(Cursor.POS(78,24)+Back.YELLOW+"Salir");

def hospital():
    lista = []
    nom = {}
    dire = {}
    analisis = {}
    os.system("CLS");
    ventanas(2);
    while True:
        cont=0
        print(Cursor.POS(31,6)+"ingrese (1) para ver los datos del hospital,(2) para modificar los datos del hospital,(Enter) para regresar al menu: ",end="");
        var=input();
        for x in range(31,145):
            print(Fore.RESET + Cursor.POS(x,6) + " ");
        if var == "1":
            archivo=open("d03-p14-farfan-tellez-H.txt",mode="r",encoding="cp1252");
            texto=archivo.readlines();
            
            for i in texto:
                print(Cursor.POS(31,7+cont) + (i))
                cont=cont + 1
            archivo.close();
            sleep(3)
            for x in range(31,145):
                print(Fore.RESET + Cursor.POS(x,6) + " ");
                print(Fore.RESET + Cursor.POS(x,7) + " ");
                print(Fore.RESET + Cursor.POS(x,8) + " ");
                print(Fore.RESET + Cursor.POS(x,9) + " ");
            
        elif var == "2":
            archivo=open("d03-p14-farfan-tellez-H.txt",mode="r",encoding="cp1252");
            print(Cursor.POS(31,6)+"ingrese el dato a modificar: nombre, direccion, estudios: ", end="");
            opc=input();
            opc2=(str(opc)+":");
            print(Cursor.POS(31,7)+"usted modificara:",opc);
            print(Cursor.POS(31,8)+"ingrese el nuevo dato: ",end="");
            nd=input();
            m=str(opc2)+" "+str(nd);
            print(Cursor.POS(31,9)+"se actualizo el dato: ",m);
            sleep(1)
            linea2=""
            linea3=""
            while True:
                linea = archivo.readline()
                if not linea:
                    break
                if opc.lower() in linea:
                    linea= linea.replace(linea,m + "\n")
                    linea2 = linea;
                linea3 = (linea3 + linea);
            archivo.close();
            archivo = open("d03-p14-farfan-tellez-H.txt",mode ="w+",encoding="cp1252");
            archivo.write(linea3);
            archivo.close()
            for x in range(31,140):
                print(Fore.RESET + Cursor.POS(x,6) + " ");
                print(Fore.RESET + Cursor.POS(x,7) + " ");
                print(Fore.RESET + Cursor.POS(x,8) + " ");
                print(Fore.RESET + Cursor.POS(x,9) + " ");
        elif var == "":
            menu();
            break

def pacientes():
    np = 0;             
    a = 0;
    b = 0;
    aux = 0;
    cont= 0;
    npl=["1"]
    while True:
        ventanas(2);
        init(autoreset=True)
        lista = []
        al=""
        al2=""
        print(Cursor.POS(31,6) + "si quiere ver los datos de un paciente presione (1) y si quiere agregar un paciente presione (2),\n"+Cursor.POS(31,7) + "si quieres dar de alta un paciente presione (3): ",end="");
        da=input()
        archivo=open("d03-p14-farfan-tellez-P.txt",mode="r+",encoding="cp1252");
        if da == "1":
            print(Cursor.POS(31,8) + "ingrese el ID del paciente a buscar: ",end="")
            bp=input()
            paci=archivo.readlines()
            for i in paci:
                if 'ID:' + str(bp) + '\n' == i:
                    lista.append(i);
                    a = 1;
                    b = 1;
                elif a < 6 and b == 1 :
                    lista.append(i)
                    a+=1
            for i in lista:
                print(Cursor.POS(31,9+cont) + str(i))
                cont=cont + 1;
            print(Cursor.POS(31,15) + "ingrese ENTER para salir",end="")
            sa=input()
            if sa == "":
                os.system("cls")
                ventanas(2)
        elif da == "2":
            os.system("cls")
            ventanas(2)
            print(Cursor.POS(31,6) + "ingrese (SI) para poner un paciente, ingrese un (NO) para dejar de poner: ",end="");
            pa=input()
            if pa == "SI" or pa == "si" or pa == "Si":
                np=int(npl[-1]) + 1;
                today= date.today();
                archivo=open("d03-p14-farfan-tellez-P.txt",mode="a",encoding="cp1252");
                print(Cursor.POS(31,7) + "la fecha de ingreso es:",today);
                print(Cursor.POS(31,8) + "ingrese el nombre del paciente: ",end="");
                nomp=input()
                print(Cursor.POS(31,9) + "ingrese la edad: ",end="")
                ed=input()
                print(Cursor.POS(31,10) + "ingrese sus antecedentes medicos: ",end="")
                am=input()
                print(Cursor.POS(31,11) + "ingrese el tipo de analisis que realizara: ",end="");
                ta=input()
                print(Cursor.POS(31,12) + "registrando datos...",end="");
                sleep(2)
                print(Cursor.POS(31,13) + "id --> ",np);
                sleep(.5)
                np2 = 'ID:'+str(np)
                archivo.write(np2);
                archivo.write('\n');        
                print(Cursor.POS(31,14) + "paciente --> ",nomp);
                sleep(.5)
                nomp = 'paciente --> '+str(nomp)
                archivo.write(nomp);
                archivo.write('\n');
                print(Cursor.POS(31,15) + "fecha de ingreso --> ",today);
                sleep(.5)
                fdi = 'fecha de ingreso --> '+str(today)
                archivo.write(fdi);
                archivo.write('\n');
                print(Cursor.POS(31,16) + "edad --> ",ed);
                sleep(.5)
                ed = 'edad --> '+str(ed)
                archivo.write(ed);
                archivo.write('\n');
                print(Cursor.POS(31,17) + "antecedente medico --> ",am);
                sleep(.5)
                am = 'antecedentes medicos --> '+str(am)
                archivo.write(am);
                archivo.write('\n');
                print(Cursor.POS(31,18) + "tipo de analisis --> ",ta);
                sleep(.5)
                ta = 'tipo de analisis -->'+str(ta)
                archivo.write(ta);
                archivo.write('\n');
                archivo.write('\n');
                aux = np 
                npl.append(np)
                archivo.close();
                sleep(4)
                os.system("cls")
                ventanas(2)
                
            elif pa == "no" or pa == "NO" or pa == "No":
                print(Cursor.POS(31,8) + "cargando...")
                sleep(2)
                menu()
            else:
                print("error");
                
        elif da == "3":
            print(Cursor.POS(31,8) + "ingrese el paciente (ID) que dara de alta: ",end="");
            alta=input()
            archivo=open("d03-p14-farfan-tellez-P.txt",mode="r",encoding="cp1252");
            for i in itertools.count():
                al=archivo.readline();
                if not al:
                    break
                if alta in al:
                    al=al.replace(al,"alta\n")
                al2=al2 + al
            archivo=open("d03-p14-farfan-tellez-P.txt",mode="w",encoding="cp1252");
            archivo.write(al2)
            archivo.close()
            print(Cursor.POS(31,15) + "ingrese ENTER para salir",end="")
            sa=input()
            if sa == "":
                os.system("cls")
                ventanas(2)
        elif da == "":
            menu()
        else:
            print("error");
    


def medicos():
    nm = 0;             
    a = 0;
    b = 0;
    aux = 0;
    cont= 0;
    nml=["1"]
    while True:
        ventanas(1);
        init(autoreset=True)
        lista = []
        al=""
        al2=""
        print(Cursor.POS(31,6) + "si quiere ver los datos de un medico presione (1) y si quiere contratar nuevo medico presione (2),\n"+Cursor.POS(31,7) + "si desea ver analisis de paciente(3): ",end="");
        da=input()
        archivo=open("d03-p14-farfan-tellez-M.txt",mode="r+",encoding="cp1252");
        if da == "1":
            print(Cursor.POS(31,8) + "ingrese la cedula del medico a buscar: ",end="")
            bp=input()
            paci=archivo.readlines()
            for i in paci:
                if 'Cedula:' + str(bp) + '\n' == i:
                    lista.append(i);
                    a = 1;
                    b = 1;
                elif a < 6 and b == 1 :
                    lista.append(i)
                    a+=1
            for i in lista:
                print(Cursor.POS(31,9+cont) + str(i))
                cont=cont + 1;
            print(Cursor.POS(31,15) + "ingrese ENTER para salir",end="")
            sa=input()
            if sa == "":
                os.system("cls")
                ventanas(1)
        elif da == "2":
            os.system("cls")
            ventanas(1)
            print(Cursor.POS(31,6) + "ingrese (SI) para poner un medico, ingrese un (NO) para dejar de poner: ",end="");
            pa=input()
            if pa == "SI" or pa == "si" or pa == "Si":
                nm=int(nml[-1]) + 1;
                today= date.today();
                archivo=open("d03-p14-farfan-tellez-M.txt",mode="a",encoding="cp1252");
                print(Cursor.POS(31,7) + "la fecha de hoy es:",today);
                print(Cursor.POS(31,8) + "ingrese el nombre del medico: ",end="");
                nomp=input()
                print(Cursor.POS(31,9) + "ingrese cargo que desempeña: ",end="")
                ed=input()
                print(Cursor.POS(31,12) + "registrando datos...",end="");
                sleep(2)
                print(Cursor.POS(31,13) + "cedula --> ",nm);
                sleep(.5)
                nm2 = 'Cedula:'+str(nm)
                archivo.write(nm2);
                archivo.write('\n');        
                print(Cursor.POS(31,14) + "Medico --> ",nomp);
                sleep(.5)
                nomp = 'medico --> '+str(nomp)
                archivo.write(nomp);
                archivo.write('\n');
                print(Cursor.POS(31,16) + "cargo que desempeña --> ",ed);
                sleep(.5)
                ed = 'cargo que desempeña --> '+str(ed)
                archivo.write(ed);
                archivo.write('\n');
                archivo.write('\n');
                aux = nm;
                nml.append(nm)
                archivo.close();
                sleep(4)
                os.system("cls")
                ventanas(1)
                
            elif pa == "no" or pa == "NO" or pa == "No":
                print(Cursor.POS(31,8) + "cargando...")
                sleep(2)
            else:
                print("error");
                
        elif da == "3":
            archiv=open("d03-p14-farfan-tellez-P.txt",mode="r+",encoding="cp1252");
            print(Cursor.POS(31,8) + "ingrese el ID del paciente a buscar para dar sus resultados: ",end="")
            bp=input()
            paci=archiv.readlines()
            for i in paci:
                if 'ID:' + str(bp) + '\n' == i:
                    lista.append(i);
                    a = 1;
                    b = 1;
                elif a < 6 and b == 1 :
                    lista.append(i)
                    a+=1
            for i in lista:
                print(Cursor.POS(31,9+cont) + str(i))
                cont=cont + 1;
            print(Cursor.POS(31,15) + "Ingrese resultados de paciente",end="");
            rmp=input()
            archi=open("d03-p14-farfan-tellez-M.txt",mode="a",encoding="cp1252")
            archi.write(rmp)
            archivo.close
            print(Cursor.POS(31,20) + "ingrese ENTER para salir",end="")
            sa=input()
            if sa == "":
                os.system("cls")
                ventanas(1)
        elif da == "":
            menu()
        else:
            print("error");
    

def menu():
    os.system("CLS");
    ventanas(1);
    cont = 0
    print(Cursor.POS(1,1) + "farfan de leon jose osvaldo")
    print(Cursor.POS(1,2) + "tellez fernandez christian daniel")
    print(Cursor.POS(1,3) + "FarCharc's")
    while True:
        init(autoreset = True);
        tecla = msvcrt.getwch();
        if tecla == chr(224):
            tecla = msvcrt.getwch();
            if tecla == chr(72):
                cont = cont - 1;
                if cont < 1:
                    cont = 1
                    
                if cont == 1:
                    menusito(1);
                    
                elif cont == 2:
                    menusito(2);
                    
                elif cont == 3:
                    menusito(3);
                    
                elif cont == 4:
                    menusito(4);
                    
                
            elif tecla == chr(80):
                cont = cont + 1
                if cont > 4:
                    cont = 4
                if cont == 1:
                    menusito(1);
                    
                elif cont == 2:
                    menusito(2);
                    
                elif cont == 3:
                    menusito(3);
                    
                elif cont == 4:
                    menusito(4);
                    
                    
        elif tecla == '1':
            cont = 1
            menusito(1);
            
        elif tecla == '2':
            cont = 2;
            menusito(2);
            
        elif tecla == '3':
            cont = 3
            menusito(3);
            
        elif tecla == '4':
            cont = 4
            menusito(4);
            
            
        elif tecla == chr(13):
            if cont == 1:
                os.system("CLS");
                pacientes();
            elif cont == 2:
                os.system("CLS");
                medicos();
            elif cont == 3:
                os.system("CLS");
                hospital();
            elif cont == 4:
                os.system("CLS");
                sys.exit()
                    
            
        else:
            pass

menu()
        
