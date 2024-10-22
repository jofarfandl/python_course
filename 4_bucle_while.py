#practica 08
#bucle while

def e1():#introduce el radio de una esfera, si es menor a 0 marca error, sino muestra el radio de una esfera
    print("\nejercicio 1");
    rad=float(input("ingrese el radio de una esfera:"));
    while rad <= 0:
            print("ERROR: el radio debe ser mayor a 0");
            rad=float(input("ingrese el radio de una esfera:"));
    if rad > 0:
        are= 3.14 * rad **2;
        print("el area de una esfera de radio",rad, end="");
        print(" es:",are);



def e2(): #introduce la arista de un cubo y si es mayor a cero imprime el volumen y las veces que los solicitaste
    print("\nejercicio 2");
    cont=0
    ari=float(input("ingrese la arista de un cubo: "));
    while ari > 0:
        vol= ari ** 3;
        print("el volumen del cubo de arista: ",ari, end="");
        print(" es:",vol);
        ari=float(input("ingrese la arista de un cubo: "));
        cont= cont + 1;
    if ari <= 0:
        print("la cantidad de volumenes calculados han sido:",cont);


def e3(): #introduce la tabla de multiploicar que desees y la imprime inversamente
    print("\nejercicio 3");
    tab=float(input("ingrese la tabla de multiplicar que desee: "));
    cont= tab;
    if tab > 0:
        while cont >= 0 :
            res = tab * cont;
            print("",tab, end="");
            print(" x ", end="");
            print("",cont, end="");
            print(" = ",res);
            cont=cont - 1 ;
    else:
        print("dato invalido");

def e4(): #convierte numeros positivos en negativos
    print("\nejercicio 4");
    print("nota: si ya no quieres convertir numeros... pon un 0 o un numero negativo");
    num=float(input("ingrese el numero positivo a convertir: "));
    while num >= 1:
        ng= num * -1;
        print("",ng);
        num=float(input("ingrese el numero positivo a convertir: "));
    if num <= 0:
        print("fin...");



import statistics as stats
def e5(): #solicita las calificaciones de un grupo e imprime la moda y la calificacion mas baja y de quien fue
        print("\nejercicio 5");
        lista=[]
        an=0;
        menor=101
        cant=int(input("cuantos alumnos hay en el grupo:"));
        if cant > 0:
            while cant > 0:
                cali=input("ingrese la calificaciones del alumno:");
                
                if int(cali) >= 0 and int(cali) < 101:
                    lista.append(int(cali))
                    cant-=1
                    an=an+1;
                    print("ingreso la calificacion del alumno:",an);
                    if menor > int(cali):
                        menor = int(cali);
                        alumno = an;
                else:
                    print("calificacion invalida");   

            print("la moda de calificaciones es:",end="");
            print(stats.mode(lista))
            print("la calificacion mas baja es:",menor, end="");
            print(" del alumno:",alumno);
        else:
            print("no tienes alumnos");


            

def e6(): #imprime la cantidad de autos dependiendo de la etiqueta y el color
    print("\nejercicio 6");
    ama=0;
    ros=0;
    roj=0;
    ver=0;
    azu=0;
    tot=0
    print("ingrese un numero negativo para finalizar");
    plac=(input("ingrese el numero de placa: "));
    dig=str(plac)
    num=plac[-1];
     
    while int(num) >= 0 and int(num) <= 9:
        tot=tot+1;
        if int(num) == 1 or int(num) ==2:
            ama= ama+1;
            print("los carros con calcomania amarilla:",ama);
            plac=(input("ingrese el numero de placa: "));
            dig=str(plac)
            num=plac[-1];
        elif int(num) == 3 or int(num) ==4:
            ros=ros+1;
            print("los carros con calcomania rosa:",ros);
            plac=(input("ingrese el numero de placa: "));
            dig=str(plac)
            num=plac[-1];
        elif int(num) == 5 or int(num) == 6:
            roj=roj+1;
            print("los carros con calcomania roja:",roj);
            plac=(input("ingrese el numero de placa: "));
            dig=str(plac)
            num=plac[-1];
        elif int(num) == 7 or int(num) == 8:
            ver=ver+1;
            print("los carros con calcomania verde:",ver);
            plac=(input("ingrese el numero de placa: "));
            dig=str(plac)
            num=plac[-1];
        elif int(num) == 9 or int(num) == 0:
            azu=azu+1;
            print("los carros con calcomania azul:",azu);
            plac=(input("ingrese el numero de placa: "));
            dig=str(plac)
            num=plac[-1];

        if int(dig) < 0:
            print("el total de carros es:",tot);
            print("la cantidad de autos con calcomania amarilla es:",ama);
            print("la cantidad de autos con calcomania rosa es:",ros);
            print("la cantidad de autos con calcomania roja es:",roj);
            print("la cantidad de autos con calcomania verde es:",ver);
            print("la cantidad de autos con calcomania azul es:",azu);
            break;
        
        
    else:
        print("dato invalido");






def menu(): #este es el menu que sirve para llamar a los ejercicios

    print("");

    
    print("\nMenu:");
    print("introduce un numero entero");
    print("1.- ejercicio 1.");
    print("2.- ejercicio 2.");
    print("3.- ejercicio 3.");
    print("4.- ejercicio 4.");
    print("5.- ejercicio 5.");
    print("6.- ejercicio 6.");
    print("7.- salir.");
    ne=int(input("\ningrese el numero de ejercicio que desea realizar: "));
    if ne > 0 and ne < 8:
        while ne > 0 and ne < 8:
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
                e5();
                menu();
                
            elif ne == 6:
                e6();
                menu();
            elif ne == 7:
                print("\nfin del juego...");
                print("\npractica 08");
                print("farfan de leon jose osvaldo");
                print("tellez fernandez christian daniel");
            break;
    else:
        print("error...");
        menu();
menu();

            


    



