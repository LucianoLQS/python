nombre=input("ingrese su nombre\n")
edad=int(input("Ingrese su edad\n"))
premiun=str.upper(input("¿Cuenta con suscripción Premiun? (S/N)\n"))
if edad>=18 and premiun=="S":
    print("Hola",nombre,"cuenta con acceso completo")
elif edad<=18 and premiun=="S":
    print("Hola",nombre,"cuenta con acceso límitado por edad")
else:
    print("Hola",nombre,"no cuenta con acceso")

