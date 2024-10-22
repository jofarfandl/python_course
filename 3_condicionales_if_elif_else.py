#practica 07
#condicionales if elif else

def e1():
    print("ejercicio 1")
    cal= float(input("Ingrese su calificacion basado en 100pts: "));
    if cal >= 80 and cal <= 100:
        print(cal);
        print("alumno aprobado ...");
    elif cal < 80 and cal > 0:
        print("alumno reprobado ...");
    else:
        print("error ... ")
e1();

def e2():
    print("\nejercicio 2")
    sue=float(input("cual es tu sueldo: "));
    if sue < 20000 and sue > 0:
        aum1=sue*1.30;
        print("el nuevo sueldo del trabajador es:",aum1);
    elif sue >= 20000 and sue < 23000:
        aum2=sue*1.15;
        print("el nuevo sueldo del trabajador es:",aum2);
    elif sue >=23000 and sue <= 25000:
        aum3=sue*1.05;
        print("el nuevo sueldo del trabajador es:",aum3);
    else:
        print("su sueldo no tiene aumento");
        print("su sueldo es:",sue);    
e2();

def e3():
    print("\nejercicio 3");
    print("nota: de la 41 a 48 horas se pagan dobles y de la 49 a 56 triples");
    base=40;
    base2=48;
    sueh=float(input("cuanto ganas por hora: "));
    hor=float(input("cuantas horas trabajas: "));
    if hor > 0 and hor < 41:
        ba= sueh * hor;
        print("su sueldo es:",ba);
    
    elif hor > 40 and hor <= 48:
        hx= hor - base;
        ba= (hx * sueh) * 2;
        print("su sueldo por horas extras trabajadas es: ",ba);
    elif hor > 48 and hor < 57:
        ba2= hor - base2;
        ba3= (ba2 * sueh) * 3;
        hx= hor - base - ba2;
        ba= hx * sueh * 2;
        sdh= ba + ba3;
        print("su sueldo por horas extras trabajadas es: ",sdh);
    else:
        print("no puedes trabajar mas de 56 horas");
e3();

def e4 ():
    print("\nejercicio 4");
    hij=int(input("cuantos hijos tienes: "));
    if hij > 0 and hij < 3:
        h2= 70;
        ed=int(input("cuantos hijos tienes de 6 a 18 años: "));
        di= ed * 10;
        viu=int(input("eres viuda? 1= si 2=no:"));
        if viu > 0 and viu < 2:
            vid= 20;
            tot=h2 + di + vid;
            print("el monto mensual obtenido es",tot);
        elif viu > 1 and viu < 3: 
            tot=h2 + di;
            print("el monto mensual obtenido es",tot);
        else:
            print("error dato no valido");
            
        
    elif hij > 2 and hij < 6:
        h3=90;
        ed=int(input("cuantos hijos tienes de 6 a 18 años:"));
        di= ed * 10;
        viu=int(input("eres viuda? 1= si 2=no:"));
        if viu > 0 and viu < 2:
            vid= 20;
            tot=h3 + di + vid;
            print("el monto mensual obtenido es",tot);
        elif viu > 1 and viu < 3: 
            tot=h3 + di;
            print("el monto mensual obtenido es",tot);
        else:
            print("error dato no valido");
         
              
    elif hij > 5:
        h4=120;
        ed=int(input("cuantos hijos tienes de 6 a 18 años: "));
        di= ed * 10;
        viu=int(input("eres viuda? 1= si 2=no: "));
        if viu > 0 and viu < 2:
            vid= 20;
            tot=h4 + di + vid;
            print("el monto mensual obtenido es: ",tot);
        elif viu > 1 and viu < 3: 
            tot=h4 + di;
            print("el monto mensual obtenido es",tot);
        else:
            print("error dato no valido");
    else:
        print("no recibes dinero porque no tienes hijos");
e4();

def e5():
    print("\nejercicio 5");
    añob=2019
    dia=int(input("cual es tu dia de nacimiento:"));
    if dia > 0  and dia < 32:
        mes=int(input("cual es tu mes de nacimiento:"));
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia > 0 and dia < 32:
            año=int(input("ingrese su año de nacimiento: "));
            edad=añob - año;
            if edad > 17 and edad < 50:
                print("podras formar parte del equipo de lacrost");
                gra=int(input("ingrese el grado escolar en el cual cursa:"));
                gru=str(input("ingrese su grupo:"));
                pro=int(input("ingrese su promedio:"));
                if pro < 60 and pro > 0:
                    print("Sentimos mucho pero no podras formar parte por tu bajo promedio");
                if pro < 101 and pro > 59:
                    hor=str(input("horario que prefiere de entrenamiento:"));
                    print("\npodras formar parte del equipo de lacrost");
                    print("grado:",gra);
                    print("grupo:",gru);
                    print("con el horario de:",hor);
                    
        if mes ==2 and dia > 0 and dia < 29:
            año=int(input("ingrese su año de nacimiento: "));
            edad= añob - año;
            if edad > 17 and edad < 50:
                print("podras formar parte del equipo de lacrost");
                gra=int(input("ingrese el grado escolar en el cual cursa:"));
                gru=str(input("ingrese su grupo:"));
                pro=int(input("ingrese su promedio:"));
                if pro < 60 and pro > 0:
                    print("Sentimos mucho pero no podras formar parte por tu bajo promedio");
                if pro < 101 and pro > 59:
                    hor=str(input("horario que prefiere de entrenamiento:"));
                    print("\npodras formar parte del equipo de lacrost");
                    print("grado:",gra);
                    print("grupo:",gru);
                    print("con el horario de:",hor);
            
        if mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia > 0 and dia <31:
            año=int(input("ingrese su año de nacimiento"));
            edad=añob - año;
            if edad > 17:
                print("podras formar parte del equipo de lacrost");
                gra=int(input("ingrese el grado escolar en el cual cursa:"));
                gru=str(input("ingrese su grupo:"));
                pro=int(input("ingrese su promedio:"));
                if pro < 60 and pro > 0:
                    print("Sentimos mucho pero no podras formar parte por tu bajo promedio");
                if pro < 101 and pro > 59:
                    hor=str(input("horario que prefiere de entrenamiento:"));
                    print("\npodras formar parte del equipo de lacrost");
                    print("grado:",gra);
                    print("grupo:",gru);
                    print("con el horario de:",hor);

    if dia > 31 and dia == 0:
        print("dia invalido");        
e5();


def e6():
    print("\nejercicio 6");
    num=str(input("ingrese su numero de placa: "));
    mi=int(input("ingrese las millas recorridas: "));
    if mi > 80:
         print("Esta arriba del limite de velocidad");
         kil=int(input("escriba los kilometros recorridos: "));
         if kil > 200 and kil < 350:
                print("Hace falta mantenimiento al auto.");
                kpl=int(input("cuantos kilometros recorre su auto por litro. de 10 16 kilometros: "));  
                if kpl < 17 and kpl > 13:
                    print("consume poca gasolina");
                    con=100 / kpl;
                    print("para recorrer 100k su auto requiere de gasolina: ",con);
                elif kpl < 14 and kpl > 9:
                    print("consume algo de gasolina");
                    con=100 / kpl;
                    print("para recorrer 100k su auto requiere de gasolina: ",con);
                else:
                    print
         elif kil > 0:
            kpl=int(input("cuantos kilometros recorre su auto por litro. de 10 16 kilometros: "));  
            if kpl < 17 and kpl > 13:
                print("consume poca gasolina");
                con=100 / kpl;
                print("para recorrer 100k su auto requiere de gasolina: ",con);
            elif kpl < 14 and kpl > 9:
                print("consume algo de gasolina");
                con=100 / kpl;
                print("para recorrer 100k su auto requiere de gasolina: ",con);
                    
    else:
         kil=int(input("escriba los kilometros recorridos"));
         if kil > 200 and kil < 350:
                print("Hace falta mantenimiento al auto.");
                kpl=int(input("cuantos kilometros recorre su auto por litro. de 10 16 kilometros: "));  
                if kpl < 17 and kpl > 13:
                    print("consume poca gasolina");
                    con=100 / kpl;
                    print("para recorrer 100k su auto requiere de gasolina: ",con);
                elif kpl < 14:
                    print("consume algo de gasolina");
                    con=100 / kpl;
                    print("para recorrer 100k su auto requiere de gasolina: ",con);
         elif kil > 0:
            kpl=int(input("cuantos kilometros recorre su auto por litro. de 10 16 kilometros: "));  
            if kpl < 17 and kpl > 13:
                print("consume poca gasolina");
                con=100 / kpl;
                print("para recorrer 100k su auto requiere de gasolina: ",con);
            elif kpl < 14:
                print("consume algo de gasolina");
                con=100 / kpl;
                print("para recorrer 100k su auto requiere de gasolina: ",con);

e6();


def e7():
    print("\nejercicio 7");
    num=int(input("cual es el numero de jugador:"));
    tir=int(input("cuantos tiros anoto el jugador:"));
    fall=int(input("cuantos tiros fallo el jugador:"));
    if tir > 0 and fall > 0:
            tot = tir + fall;
            print("el total de tiros del jugador",num, end="");
            print(" es:",tot);
            pun=int(input("cuantos puntos anoto el jugador:"));
            if pun == (tir * 3) or pun < (tir * 3):
                if pun > 2 and pun < 7:
                    print("Anoto pocos puntos");
                elif pun < 16 and pun > 6:
                    print("Anoto puntos aceptables");
                    enc= pun / 3 ;
                    print("la cantidad de puntos de 3 anotados en promedio podria haber sido: %0.0f"%enc);
                elif pun < 23 and pun > 15:
                    print("Felicidades por sus anotaciones");
                    enc=pun / 3;
                    print("la cantidad de puntos de 3 anotados en promedio podria haber sido: %0.0f"%enc);
            else:
                print("los datos no cuadran");
    else:
        pun=int(input("cuantos puntos anoto el jugador:"));
        if pun == (tir * 3) or pun < (tir * 3):
            if pun > 2 and pun < 7:
                print("Anoto pocos puntos");
            elif pun < 16 and pun > 6:
                print("Anoto puntos aceptables");
                enc=pun / 3;
                print("la cantidad de puntos de 3 anotados en promedio podria haber sido: %0.0f"%enc);
            elif pun < 23 and pun > 15:
                    print("Felicidades por sus anotaciones");
                    enc=pun / 3;
                    print("la cantidad de puntos de 3 anotados en promedio podria haber sido: %0.0f"%enc);
        else:
            print("los datos no cuadran");

e7();

print("\npractica 07");
print("jose osvaldo farfan de leon");
print("christian daniel tellez fernandez");



