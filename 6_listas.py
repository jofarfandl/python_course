#practica 10
#listas

from time import sleep
import itertools
from colorama import init, Fore, Back, Cursor;
import os

def e1(): #ingresa la estadia de un automovil en el estacionamiento
    dia=2400;
    pa=1000;
    for i in itertools.count():#bucle 
        print(Cursor.POS(2,20),"\nejercicio 1");
        print(Cursor.POS(2,21),"ingrese un numero negativo para salir");
        he=int(input("ingrese la hora de entrada:"));
        if he > 0000 and he < 2400:#comparamos que la hora sea correcta
            hs=int(input("ingrese la hora de salida:"));
            if hs >= 0000 and hs < 2400:#verificamos que salga el mismo dia
                hes= hs - he;
                print(hes);
                
                if hes > 100:#verifica que salga el mismo dia
                    hres=hes-100;
                    hr=hres/100;
                    tot= pa + (hr * 600);
                    print(Cursor.POS(2,24),"usted pagara:",tot);
                    sleep(4)
                    os.system("CLS")
                    break
                    menu();
                    
                elif hes < 0 and hes > -2400:#si sale en la madrugada
                    nhes=dia-he;
                    hr1=nhes-100;
                    tot2=(hr1/100)*600;
                    ntot=(hs/100)*600;
                    tot= pa + tot2 + ntot;
                    print(Cursor.POS(2,24),"usted pagara:",tot);
                    sleep(4)
                    os.system("CLS")
                    break
                    menu();
                    
                elif hes <= 100:#si estuvo menus de una hora 
                    print(Cursor.POS(2,25),"su pago es de: ",pa);
                    sleep(4)
                    os.system("CLS")
                    break
                    menu();
                    
                    
                else:
                    print("error");
            else:
                print("dato invalido");
                e1();
        elif he < 0:
            print("FIN...");
            menu();
        else:
            print("dato invalido1");
            e1();
            

def e2(): #imprime ticket de productos y los precios de los que hayas ingresado
    iva=0.15;
    cj=0;
    cap= 0;
    lista=[];
    lista1=[];
    tot=0;
    try:
        print(Cursor.POS(2,20),"\nejercicio 2");
        pp=float(input("\ningrese un numero para iniciar: "));#inicia el programa
        if pp > 0 and pp < 1000**100:
            while pp > 0:
                seguir=int(input("\ningrese un numero positivo para continuar o un (0) para imprimir el ticket o un numero negativo para salir:"));#sirve para imprimir ticket, seguir metiendo datos o cerrar el archivo
                if seguir > 0:
                    cp=str(input("\ningrese el codigo de su producto: "));#codigo producto
                    lista.append(cp);
                    mv=float(input("ingrese el precio del productor: ")); #precio del producto
                    lista1.append(mv);
                    cap= cap + 1;
                    tot= tot + mv;
                elif seguir == 0:
                    print("\nThe Kk´s: TIENDA DEPARTAMENTAL");
                    sub= tot;
                    ivas= tot*.15;
                    pf=ivas+tot;
                    print(Cursor.POS(2,32),"la cantidad de productos que llevas son:",cap);
                    print(Cursor.POS(2,33),"subtotal:",tot);
                    print(Cursor.POS(2,34),"iva:",ivas);
                    print(Cursor.POS(2,35),"precio que pagara con IVA y total:",pf);
                    for i in range(len(lista)):
                        print(Cursor.POS(2,30),lista[i],lista1[i]);
                    sleep(12)
                    os.system("CLS")
                    break
                    menu();

                elif seguir < 0:
                    print("se termino...");
                    menu();                          

        else:
             print("dato invalido");
             
    except:
        print("dato invalido");
        e2();
 

def e3(): #ingresa la cantidad de dias y los convierte a meses, años y semanas
    año= 0;#declaramos contadores
    mes= 0;
    sem= 0;
    dia= 0;
    cont=0;#contador para detectar años bisiestos
    mes1=1;
    error=0#contador para los errores
    bis=0;
    try:
        print(Cursor.POS(2,20),"ejercicio 3");
        tdias=int(input("\ningrese la cantidad de dias: "));
        #verificamos que los dias sean mayores a 0.
        if tdias > 0:#verificamos que los dias sean masyores a 0.
            for i in itertools.count():
                #verificamos que el total de dias sea mayor a 365
                if tdias >= 365:
                    año= año + 1;
                    tdias= tdias - 365;
                    #incrementamos nuestro contador de años bisiestos
                    cont=cont+1;
                    #si los dias son mayores a 365 y los años son igual a 3 sumar un año bisiesto
                    if tdias <= 365 and cont==3:
                        año= año + 1;
                        tdias= tdias - 366;
                        cont=0;#nuestro contador vuelve a cero.
                        bis=bis+1;
                elif tdias > 30 and tdias < 365:
                    #verificamos que nuestro contador se compare para agregar el mes con los dias correctos.
                    if mes1==1 or mes1==3 or mes1==5 or mes1==7 or mes1==8 or mes1==10 or mes1==12:
                        mes= mes + 1;
                        tdias= tdias - 31;
                        mes1= mes1 + 1;
                    elif mes1==2 and cont !=3 :
                        mes= mes + 1;
                        tdias= tdias - 28;
                        mes1= mes1 + 1;
                    elif mes1==4 or mes1==6 or mes1==9 or mes1==11:
                        mes= mes + 1;
                        tdias= tdias - 30;
                        mes1= mes1 + 1;
                    elif mes1==2 and cont ==3:
                        mes= mes + 1;
                        tdias= tdias - 29;
                        cont=0;
                        mes1= mes1 + 1;
                            
                elif tdias >= 7 and tdias < 32:#calculamos las semana
                    sem= sem + 1;
                    tdias= tdias-7;
                
                        
                if tdias < 7:#si los dias son menores a 7 se acaba el ciclo e imprimimos
                    print(Cursor.POS(2,25),"la cantidad de años es:",año);
                    print(Cursor.POS(2,26),"la cantidad de meses es:",mes);
                    print(Cursor.POS(2,27),"la cantidad de semanas es:",sem);
                    print(Cursor.POS(2,28),"la cantidad de dias es:",tdias);
                    print(Cursor.POS(2,30),"la cantidad de años bisiestos detectados es:",bis);
                    año=0;
                    mes=0;
                    sem=0;
                    tdias=0;
                    bis=0;
                    sleep(5);
                    os.system("CLS")
                    break
                    e3();
        elif tdias == 0:
            print(Cursor.POS(2,26),"fin de calendario");
            menu();
                    
        else:
            print("no existen dias asi");
            error=error+1;
            e3();
    except:
        print("DATO INVALIDO");
        e3();






def e4(): #ingresa numeros,si ingresa numeros negativos los devuelve como un (-1)
    lista=[]
    cont1=0;
    try:
        print(Cursor.POS(2,20),"\nejercicio 4");
        print(Cursor.POS(2,21),"\ningrese un numero negativo para terminar");
        for i in itertools.count():#bucle infinito para agregar productos
            num=int(input("ingrese los numeros que desea agregar"));
            if num >= 0:#comparamos que los numeros sean positivos
                if num in lista:#si nuestro numero esta en la lista
                    num=-1;#asignamos a la variable num un -1
                    lista.append(int(num));#agregamos el numero a la lista
                    print(Cursor.POS(2,24),lista);
                    cont1=cont1+1;
                    print(Cursor.POS(2,28),"se repite:",cont1);     
                else:#si el numero no esta enla lista lo agregamos
                    lista.append(int(num));
                    print(Cursor.POS(2,24),lista);        
            elif num < 0 :#si el numero es negativo finalizamos el programa
                print("fin del juego");
                print(Cursor.POS(2,25),"las veces que se repitieron numeros fueron:",cont1);
                os.system("CLS")
                break
                menu();             
    except:
        print("dato invalido...");
        e4();

def menu():
    try:
        x=1;#donde empieza x
        y=3;#donde empieza y
        init(autoreset = True);
        while x < 55:#largo de x
            print(Cursor.POS(x,3) + Fore.BLUE + Back.BLUE + ".");#primera linea de x y donde empieza
            print(Cursor.POS(x,15) + Fore.BLUE + Back.BLUE + ".");#segunda linea de x y donde empieza
            x=x+1;
        while y < 15:#largo de y
            print(Cursor.POS(1,y) + Fore.GREEN + Back.GREEN + ".");#primera linea de y y donde empieza
            print(Cursor.POS(54,y) + Fore.GREEN + Back.GREEN + ".");#segunada linea de y y donde empieza
            y=y+1;
        print(Cursor.POS(2,4)+ Fore.YELLOW + "      Menu:");
        print(Cursor.POS(2,5),"1.- ejercicio 1");
        print(Cursor.POS(2,6),"2.- ejercicio 2");
        print(Cursor.POS(2,7),"3.- ejercicio 3");
        print(Cursor.POS(2,8),"4.- ejercicio 4");
        print(Cursor.POS(2,9),"5.- salir");
        ne=int(input("ingrese el numero de ejercicio que desea realizar: "));
        if ne > 0 and ne <=5:
            while ne > 0 and ne <= 5:
                if  ne == 1:
                    e1();
                    menu();
                    
                elif ne == 2:
                    e2();
                    menu();
                    
                elif ne == 3:
                    e3();
                    menu();
                    
                elif ne == 4:
                    e4();
                    menu();

                elif ne == 5:
                    print(Cursor.POS(2,11),"fin del juego");
                    print(Cursor.POS(2,12)+ Fore.RED +"practica 10");
                    print(Cursor.POS(2,13)+ Fore.RED +"farfan de leon jose osvaldo");
                    print(Cursor.POS(2,14)+ Fore.RED +"tellez fernandez christian daniel ");
                    sleep(5)
                    break
            else:
                print("error...");
                menu();
        else:
            print("dato invalido");
            menu();
    except:
        print("Dato invalido...");
        menu();

menu();







