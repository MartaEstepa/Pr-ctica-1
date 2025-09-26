edad = int(input("Dime tu edad: "))
nivel_fisico = (int(input("Dime tu nivel físico entre el 1 y el 10: ")))


if nivel_fisico < 1 or nivel_fisico > 10:
    print("¡Evalua tu físico entre el uno y el diez!")
elif edad < 18:
    print("Debes ser mayor de edad.")
elif nivel_fisico < 5:
    print("Debes estar en mejor forma.")
else:
    print("¡Listo para despegar!")
