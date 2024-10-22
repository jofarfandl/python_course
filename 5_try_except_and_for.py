#practica 09
#try_except & for

import itertools
import statistics as stats

def e1():
    cont=0
    bol=100
    cat1=0;
    cat2=0;
    cat3=0;
    cat4=0;
    cat5=0;
    tot1=0;
    tot2=0;
    tot3=0;
    tot4= 0;
    tot5= 0;

    try:
        print("\nejercicio 1");
        bar=str(input("ingrese un (I) para ingresar un boleto. \ningrese un (F) para salir: "));#se pregunta si desea o no ingresar boletos
        if bar == "I" or bar == "i":
            print("\nel boleto vale 100");
            for i in itertools.count():#funcion for infinita
                    print("\npara dejar de pedir boletos ingrese un (0)");#valor centinela
                    ed=int(input("\ningrese la edad de la persona:"));
                    if ed > 127:#cualquier edad mayor a 127 no existe
                        print("edad invalida no existen personas con esa edad");
                        
                    elif ed < 5 and ed > 0 :#niños menores de 5 años no tienen acceso
                        print("no niños menores a 5 años...");
                    
                    elif ed > 4 and ed < 15:#se seleccionan las personas de la categoria 1
                        res= bol*.35;
                        cat1= cat1 + 1;
                        cont= cont + 1;
                        tot1= cat1 * res;
                        print("el descuento del boleto es: ",res);
                        print("la cantidad de personas con categoria 1:",cat1);

                    elif ed > 14 and ed < 20:#se seleccionan las personas de la categoria 2
                        res= bol*.25;
                        cat2= cat2 + 1;
                        cont= cont + 1;
                        tot2= cat2 * res;
                        print("el descuento del boleto es: ",res);
                        print("la cantidad de personas con categoria 2:",cat2);

                    elif ed > 19 and ed < 46:#se seleccionan las personas de la categoria 3
                        res= bol*.10;
                        cat3= cat3 + 1;
                        cont= cont + 1;
                        tot3= cat3 * res;
                        print("el descuento del boleto es: ",res);
                        print("la cantidad de personas con categoria 3:",cat3);

                    elif ed > 45 and ed < 66:#se seleccionan las personas de la categoria 4
                        res= bol*.25;
                        cat4= cat4 + 1;
                        cont= cont + 1;
                        tot4= cat4 * res;
                        print("el descuento del boleto es: ",res);
                        print("la cantidad de personas con categoria 4:",cat4);

                    elif ed > 65:#se seleccionan las personas de la categoria 5
                        res= bol*.35;
                        cat5= cat5 + 1;
                        cont= cont + 1;
                        tot5= cat5 * res;
                        print("el descuento del boleto es: ",res);
                        print("la cantidad de personas con categoria 5:",cat5);

                    elif ed == 0:#valor centinela activa la opcion de escape imprimiendo los datos deseados por el usuario
                        print("la cantidad de personas totales es:",cont);
                        print("la cantidad de personas totales de la categoria 1 son:",cat1);
                        print("la cantidad de dinero perdidad de la categoria 1 es:",tot1);
                        print("la cantidad de personas totales de la categoria 2 son:",cat2);
                        print("la cantidad de dinero perdidad de la categoria 2 es:",tot2);
                        print("la cantidad de personas totales de la categoria 3 son:",cat3);
                        print("la cantidad de dinero perdidad de la categoria 3 es:",tot3);
                        print("la cantidad de personas totales de la categoria 4 son:",cat4);
                        print("la cantidad de dinero perdidad de la categoria 4 es:",tot4);
                        print("la cantidad de personas totales de la categoria 5 son:",cat5);
                        print("la cantidad de dinero perdidad de la categoria 5 son:",tot5);
                        menu();
                            
                    else:
                        print("error...");

        elif bar == "F" or bar == "f":#regresa al menu en caso de no querer ingresar boletos
            print("\nSe ha terminado el programa, se regresará al menú")
            menu();

        else:
            print("dato invalido\n");
            e1();
            
            
    except:
        print("dato invalido...");
                   


def e2():#calcula el promedio de masa segun las llantas de los vehiculos
    conta=0;#contador de autos
    contm=0;#contador de motos
    prom2= 0;#promedio de todas las motos
    prom1= 0;#promedio de todos los autos
    try:
        print("\nejercicio 2");
        llan=str(input("ingrese un (I) para empezar la llantera. \ningrese un (F) para salir: "));
        if llan == "I" or llan == "i":
            for i in itertools.count():
            
                print("\nPara finalizar la revisión de neumáticos, ingrese 0");
                tip=int(input("ingrese el tipo de vehiculo\n1.-automovil.\n2.-motocicleta:"));
                if tip == 1:
                    pre1=float(input("ingrese la presion de la llanta 1:"));
                    vol1=float(input("ingrese el volumen de la llanta 1:"));
                    pre2=float(input("ingrese la presion de la llanta 2:"));
                    vol2=float(input("ingrese el volumen de la llanta 2:"));
                    pre3=float(input("ingrese la presion de la llanta 3:"));
                    vol3=float(input("ingrese el volumen de la llanta 3:"));
                    pre4=float(input("ingrese la presion de la llanta 4:"));
                    vol4=float(input("ingrese el volumen de la llanta 4:"));
                    temp=float(input("ingrese la temperatura:"));
                    ma1= (pre1 * vol1) / .37 *(temp + 460);
                    ma2= (pre2 * vol2) / .37 *(temp + 460);
                    ma3= (pre3 * vol3) / .37 *(temp + 460);
                    ma4= (pre4 * vol4) / .37 *(temp + 460);
                    pro= (ma1 + ma2 + ma3 + ma4) / 4;
                    print("el promedio de la masa 1 es:",ma1);
                    print("el promedio de la masa 2 es:",ma2);
                    print("el promedio de la masa 3 es:",ma3);
                    print("el promedio de la masa 4 es:",ma4);
                    print("el promedio de todas las masas es:",pro);
                    conta= conta + 1;
                    prom1= (prom1 + pro) / conta;
                
                elif tip == 2:    
                    pre1=float(input("ingrese la presion de la llanta 1:"));
                    vol1=float(input("ingrese el volumen de la llanta 1:"));
                    pre2=float(input("ingrese la presion de la llanta 2:"));
                    vol2=float(input("ingrese el volumen de la llanta 2:"));
                    temp=float(input("ingrese la temperatura:"));
                    ma1= (pre1 * vol1) / .37 *(temp + 460);
                    ma2= (pre2 * vol2) / .37 *(temp + 460);
                    pro= (ma1 + ma2) / 2;
                    print("\nel promedio de la masa 1 es:",ma1);
                    print("el promedio de la masa 2 es:",ma2);
                    print("el promedio de todas las masas es:",pro);
                    contm= contm + 1;
                    prom2= (prom2 + pro) / contm;

                elif tip == 0:
                    print("la cantidad de autos son:",conta);
                    print("el promedio de masa de todos los autos es:",prom1);
                    print("\nla cantidad de motos son:",contm);
                    print("el promedio de masa de todos las motos es:",prom2);
                    print("\nSe regresera al menu");
                    menu();
                        
                else:
                    print("opcion invalida");
                    e2();       
        elif llan == "F" or llan == "f":
            print("\nSe ha terminado el programa, se regresará al menú")
            menu();
        else:
            print("invalido");
            e2();
            
    except:
        print("dato invalido");
        e2();

def e3(): #muestra el precio de el huevo basado en la calidad de la gallina
    calt=0
    cal=0;
    cont=0;
    pt= 0;
    try:
        print("\nejercicio 3");
        gran=str(input("ingrese un (I) para empezar la granja. \ningrese un (F) para salir: "));
        if gran == "I" or gran == "i":
            print("para finalizar el programa ingrese 1000");
            for i in itertools.count():
                pg=float(input("ingrese el peso (en kilogramos) de la gallina: "));
                if pg > 1.6 and pg < 7:
                    al=float(input("ingrese la altura de la gallina en cm: "));
                    if al > 24 and al< 61:
                        hue=int(input("ingrese la cantidad de huevos que pone la gallina: "));
                        if hue >= 0 and hue < 4:
                            cal= (pg * (al / 10)) / hue;
                            print("calidad de gallina",cal);
                            cont= cont + 1;
                            calt= (calt+cal)/ cont;  
                            if  calt < 9 and calt >= 0:
                                pt= 0.80 * calt;
                            elif calt > 8 and calt < 15:
                                pt= 1* calt;
                            elif calt >= 15:
                                pt= 1.2*calt;
                                
                        else:
                            print("no pueden poner esa cantidad de huevos");
                            e3();
                    else:
                        print("no existen gallinas asi...");
                        e3();
                elif pg == 1000:
                    print("\nel precio del kilo de huevo por tus gallinas es:",pt)
                    menu();
                else:
                    print("no existen gallinas asi...");
                    e3();
                    
        elif gran == "F" or gran == "f":
            print("\nSe ha terminado el programa, se regresará al menú")
            menu();
        else:
            print("invalido");
            e3();
    except:
        print("dato invalido");
        e3();

def e4(): #ingrese el numero de diputados a favor, en contra o si se abstienen,mostrando el porcentaje de las 3 opciones
    cont=0
    fav=0
    con=0
    abst=0
    try:
        print("\nejercicio 4");
        gran=str(input("ingrese un (I) para empezar el programa de diputados. \ningrese un (F) para salir: "));
        if gran == "I" or gran == "i":
            for i in range(500):
                print("ingrese (0)para salir");
                print("\n1.-a favor del tratado de libre comercio");
                print("2.-en contra del tratado de libre comercio");
                print("3.-se absiene de opinar");
                nd=int(input("ingrese el numero que corresponda a su voto:"));
                if nd >= 1 and nd <= 3:
                    if nd == 1:
                        fav=fav+1
                        cont=cont+1
                        print("A favor");
                    elif nd == 2:
                        con=con+1
                        cont=cont+1
                        print("En contra");
                    elif nd == 3:
                        abst=abst+1
                        cont=cont+1
                        print("se abstienen");
                    else:
                        print("invalido");
                        e4();
                    
                 
                elif nd == 0:               
                    prom1=((fav*100)/cont);
                    prom2=((con*100)/cont);
                    prom3=((abst*100)/cont);
                    print("\nel porcentaje de diputados a favor es:",prom1);
                    print("el porcentaje de diputados en contra es:",prom2);
                    print("el porcentaje de diputados que se abstienen es:",prom3);
                    menu();

                else:
                    print("dato invalido");
        elif gran == "F" or gran == "f":
            print("\nSe ha terminado el programa, se regresará al menú")
            menu();
    except:
        print("dato invalido...")

def e5():#convierte numeros enteros en hexadecimales de manera regresiva dandose un punto de partida
    try:
        print("\nejercicio 5");
        gran=str(input("ingrese un (I) para empezar el programa de hexadecimales. \ningrese un (F) para salir: "));
        if gran == "I" or gran == "i":
            for i in itertools.count():
                h=int(input("ingrese el numero positivo que quiere que se cuente de forma regresiva en enteros: "));
                lista=[];
                for i in range(1,h+1):
                    lista.append(hex(h));
                    h=h-2;
                    if h == - 2:
                        print("la cuenta regresiva en hexadecimal es:",lista);
                        menu();
        elif llan == "F" or llan == "f":
            print("\nSe ha terminado el programa, se regresará al menú")
            menu();
    except:
        print("dato invalido...");
        e5();

        
    



def e6():#pedir codigo y calificaciones de clase de programando con campos
    calt=0;
    cal1=0;
    cod1=0;
    cal2=0;
    cod2=0;
    x=3
    prom=0;
    prom3=0;
    lista1=[]
    lista2=[]
    try:
        print("\nejercicio 6");
        var=str(input("ingrese una (I) para empezar la clase\ningrese una (N) para salir salir"));
        if var == "I" or var == "i":
            for i in itertools.count():
                print("\ningrese un 0 para terminar");
                cod=int(input("ingrese el codigo del alumno"));
                if cod > 0 and cod <= 999999999:
                    pra1=float(input("Ingrese su calificacion en la practica 1: "))
                    pra2=float(input("Ingrese su calificacion en la practica 2: "))
                    pra3=float(input("Ingrese su calificacion en la practica 3: "))
                    
                    if pra1 < 0 or pra1 > 100 or pra2 < 0 or pra2 > 100 or pra3 < 0 or pra3 > 100:
                        print("la calificacion debe ser un numero del 0-100\n")
                        
                    elif pra1 >= 0 or pra1 <= 100 or pra2 >= 0 or pra2 <= 100 or pra3 >= 0 or pra3 <= 100:
                        prom1=(pra1 + pra2 + pra3)/3;
                        if prom1 > prom3:
                            lista1=[]
                            lista2=[]
                            lista1.append(int(prom1))
                            lista2.append(int(cod))
                            prom3 = prom1;
                        elif prom1 == prom3:
                            lista1.append(int(prom1))
                            lista2.append(int(cod))
                        else:
                            print("ok");
                            
                elif cod==0:
                    print("los codigos de los alumnos con el mejor promedio son:",end="");
                    print(lista2);
                    print("el promedio es:",end="");
                    print(lista1);
                    e6();

                            
                else:
                    print("codigo invalido");
                                
        elif var == "N" or var == "n":
            print("fin del juego");
            menu();
        else:
            print("dato invalido");
            e6();
    except:
        print("dato invalido...");
        e6();

        
def e7():#caja registradora que lleva el control del dinero, ventas e iva.
    iva=0.16;
    cj=0;
    try:
        print("\nejercicio 7");
        care= str(input("ingrese una (I) para empezar la venta\ningrese una (F) para salir salir:"))
        if care == "I" or care == "i":
            for i in itertools.count():
                  print("Nota: para salir del programa presione (0)");
                  mv=float(input("\ningrese la cantidad a pagar: "));
                  if mv > 0 and mv < 1000**100:
                      print("el IVA es:",iva);
                      pt=(mv * iva);
                      pf=(mv + pt);
                      print("precio que pagara con IVA:",pf);
                      print("\ndinero de la caja registradora es:",cj);
                      din=float(input("ingrese con cuanto pagara:"));
                      if din < pf:
                          print("invalido");
                      elif din >= pf:
                          print("transaccion realizada");
                          cam=din - pf;
                          if cj < cam:
                              print("falta cambio");
                          elif cj >= cam:
                                print("su cambio es: ",cam);
                                cj=cj + pf;
                                cj=cj - cam;
                                         
                  elif mv == 0:
                        care = str(input("vuelva a presionar (0)"));
                        print("dinero disponible",cj);
                        menu();
                        
        elif care == "F" or care == "f":
              print("se ha cerrado la caja registrado, se redigira al menu.");
              menu();

        else:
             print("dato invalido")
             e7();
    except:
        print("dato invalido");
        menu();





def menu(): #el menu que sirve para llamar a los diferentes ejercicios
    try:
        print("\ningrese 1 para ejecutar el ejercicio 1.\ningrese 2 para ejecutar el ejercicio 2.\ningrese 3 para ejecutar el ejercicio 3.\ningrese 4 para ejecutar el ejercicio 4.\ningrese 5 para ejecutar el ejercicio 5.\ningrese 6 para ejecutar el ejercicio 6.\ningrese 7 para ejecutar el ejercicio 7.\ningrese el numero 8 para salir.\n"); 
        a=int(input("ingrese el ejercicio que desea ejecutar:"));
        for i in itertools.count():
            if a == 1: 
                return e1()
            elif a == 2:
                return e2()
            elif a == 3:
                return e3()
            elif a == 4:
                return e4()
            elif a == 5:
                return e5()
            elif a == 6:
                return e6()
            elif a == 7:
                return e7()
            elif a == 8:
                print("\nfin del juego");
                print("practica 09");
                print("farfan de leon jose osvaldo");
                print("tellez fernandez christian daniel");

                break
            else:
                print("dato invalido...");
                return menu()
    except:
        print("dato invalido");
        menu();
menu();


