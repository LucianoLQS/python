print("-----Hola bienvenido al promedio de tus notas----");
print("--------------------------------------------------------");
print("Ponga la primera nota");
nota1 = float(input(""));
print("Ponga la segunda nota");
nota2 = float(input(""));
print("Ponga la tercera nota");
nota3=  float(input(""));
promedio = (nota1+nota2+nota3)/3;
if (promedio>20):
    print("ERROR")
elif (promedio<11):
    print("Estas Desaprobado")
    print("Tú promedio es",promedio);
elif (promedio>11):
    print("Estas Aprobado")
    print("Tú promedio es",promedio);
elif (promedio==11):
    print("Estas normal")
    print("Tú promedio es",promedio);
else:
    print("xd")



