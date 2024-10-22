#practica 06
#funciones

def e1():
    t1=20;
    t2=70;
    t3=80;
    e=90;
    
    exa1=0.2*e;
    tar1=(t1+t2+t3)/3;
    pro_tar1=0.8*tar1;
    promedio1=exa1+pro_tar1;

    exa2=0.45*e;
    tar2=(t1+t2+t3)/3;
    pro_tar2=0.55*tar2;
    promedio2=exa2+pro_tar2;

    exa3=0.85*e;
    tar3=(t1+t2+t3)/3;
    pro_tar3=0.15*tar3;
    promedio3=exa3+pro_tar3;

    print("ejercicio 1");
    print("matematicas:");
    print("el porcentaje obtenido del examen es",exa1);
    print("el porcentaje obtenido de las tareas es:",pro_tar1);
    print("el promedio general es:",promedio1);
    
    print("fisica:");
    print("el porcentaje obtenido del examen es",exa2);
    print("el porcentaje obtenido de las tareas es:",pro_tar2);
    print("el promedio general es:",promedio2);

    print("quimica:");
    print("el porcentaje obtenido del examen es",exa3);
    print("el porcentaje obtenido de las tareas es:",pro_tar3);
    print("el promedio general es:",promedio3);
e1();

def e2():
    c_i=200;
    g=c_i*.073;
    print("\nejercicio 2");
    print("La ganancia de dinero es:",g);
e2();

def e3():
    v1=20;
    v2=15;
    v3=30;
    v4=10;
    v5=25;
    v6=40;
    v7=50;
    v8=90;
    v9=5;
    v10=40;
    sb=2500;
    tv=v1+v2+v3+v4+v5+v6+v7+v8+v9+v10;
    com=tv*.15;
    csb=(com/12)+sb;
    print("\nejercicio 3");
    print("la comision por año es:",com);
    print("el sueldo base mas la comision por mes es:",csb);
e3();

def e4():
    p=100;
    tot=p*.845;
    print("\nejercicio 4");
    print("el precio a pagar sera:",tot);
e4();

def e5():
    cal1=50;
    cal2=50;
    cef=50;
    tf=50;
    prom2p=((cal1+cal2)/2)*.55;
    ref=cef*.30;
    rtf=tf*.15;
    promg=ref+rtf+prom2p;
    print("\nejercicio 5");
    print("el promedio final es:",promg);
e5();

def e6():
    nh=140;
    nm=60;
    tp=nh+nm;
    ph=nh*100/tp;
    pm=nm*100/tp;
    print("\nejercicio 6");
    print("porcentaje de hombres:",ph)
    print("porcentaje de mujeres:",pm)
e6();

def e7():
    an=2001;
    aa=2019;
    edad=aa-an;
    print("\nejercicio 7");
    print("el año de nacimiento es",an);
    print("la edad es:",edad);
e7();


def e8():
    pa=10000
    g=pa*.30;
    t=pa*.30;
    p=pa*.40;
    print("\nejercicio 8");
    print("la cantidad que recibe ginecologia es:",g);
    print("la cantidad que recibe traumatologia es:",t);
    print("la cantidad que recibe pediatria es:",p);
e8();

def e9():
    pa=400;
    gan=pa*.15;
    pv=gan+pa;
    print("\nejercicio 9");
    print("su precio de venta debe ser:",pv);
e9();

def e10():
    t1=90;
    t2=60;
    t3=45;
    tp=t1+t2+t3/3;
    print("\nejercicio 10");
    print("el tiempo promedio en minutos es:",tp);
e10();


def e11():

    d1=100
    d2=200
    d3=300
    st=d1+d2+d3;
    p1=d1*100/st;
    p2=d2*100/st;
    p3=d3*100/st;
    print("\nejercicio 11");
    print("el porcentaje de inversion de la persona 1 es:",p1);
    print("el porcentaje de inversion de la persona 2 es:",p2);
    print("el porcentaje de inversion de la persona 3 es:",p3);
e11();

print("\npractica 06");
print("jose osvaldo farfan de leon");
print("christian daniel tellez fernandez");

