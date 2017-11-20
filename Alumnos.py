import os

print("Bievenido al Asistente del Estudiante Irresponsable.\nEn este programa te ayudaremos a salvar el semestre.\n\n..."
      "Aunque, la verdad, no garantizamos nada.\n")
nick=str(input("Primero, dinos tu nombre: "))
print("\nBienvenido, "+nick+", al Asistente del Estudiante Irreponsable.")


def seleccion():
    print("¿Qúe deseas hacer hoy?:\n")
    print(
        " - Calcular mis promedios. Para usar esta función, presiona 1.\n - Ver mis proyectos pendientes. Para usar esta"
        " función, presiona 2.\n - Ver mi horario. Para usar esta función, presiona 3.\n - Ver mi rol de "
        "exámenes. Para usar esta función, presiona 4.\n ")
    f_sel = int(input("Elige una opción: "))
    def calc_promedio():
        print("\n-----CALCULADORA DE PROMEDIOS-----\nEsta función te ayudará a monitorerar tus notas.\nPrimero dinos, ¿el "
              "curso que llevas incluye pesos en el cálculo de promedio?")
        while True:
            print(" - Si no incluye pesos, presiona 1.\n - Si incluye pesos, presiona 2.")
            sist_cal = int(input("Elige una opción.\n"))
            notas = []
            num_notas = int(input("¿Cuántas calificaciones hay en el curso? "))
            if sist_cal == 1:
                for i in range (1,num_notas+1):
                    notas.append(int(input("Ingrese la nota N°"+str(i)+": ")))
                promedio = sum(notas)/num_notas
            elif sist_cal == 2:
                pesos = []
                acumulado = 0
                for i in range (1,num_notas+1):
                    notas.append(int(input("Ingrese la nota N°" + str(i) + ": ")))
                    pesos.append(int(input("Ingrese el peso de la nota N°"+str(i)+": ")))
                    acumulado += notas[i-1]*pesos[i-1]
                promedio = acumulado/sum(pesos)
            else:
                print("Opción Inválida, inténtelo nuevamente")

            print("Tu promedio es "+str(promedio))
            if promedio == 20:
                print("Felicidades, has conseguido una nota perfecta.")
            elif promedio >= 11 and promedio < 20:
                print("Muy bien, te esforzaste.")
            elif promedio >= 10.5 and promedio < 11:
                print("Por poco.")
            elif promedio < 10.5:
                print("Anda diciéndole a tus padres lo de la bica")
            else:
                print("Opción invalida. Intenta nuevamente.")
            cont = str(input("¿Calcular el promedio de otro curso? [y/n]"))
            if cont == "n":
                break

    def ver_proyectos():
        print("\n-----VISUALIZADOR DE PROYECTOS-----\n\nEsta función te permitirá ver tus proyectos pendientes. Además "
              "podrás añadir nuevos proyectos.\n¿Qué es lo que deseas hacer?\n - Ver mis proyectos pendientes. Presiona"
              " 1.\n - Agregar un nuevo proyecto. Presiona 2.\n")
        proy_accion = int(input("Elige una opción: "))

        if proy_accion == 1:
            print("Esta es tu lista de proyectos pendientes:\n")
            lista_proyectos = open("proyectos.txt", 'r')
            print(lista_proyectos.read())
        elif proy_accion == 2:
            proy = str(input("¿En qué consiste tu nuevo proyecto final? "))
            fecha = str(input("Ingrese la fecha de entrega [dd/mm]: "))
            lista_proyectos = open("proyectos.txt", 'w')
            lista_proyectos.write(proy+"   "+fecha+"\n")
            lista_proyectos = open("proyectos.txt", 'r')
            print("Esta es tu lista de proyectos pendientes:\n")
            print(lista_proyectos.read())

    def ver_horario():
        print("\n-----VISUALIZADOR DE HORARIO-----\nHorario 2017-2:\n")
        horario = open("horario.txt",'r')
        print(horario.read())
        os.system('pause')

    def rol_examenes():
        print("\n-----ROL DE EXAMENES-----\nCiclo 2017-2:")
        rol = open("rol.txt", 'r')
        print(rol.read())
        os.system('pause')

    options = {1 : calc_promedio,
               2 : ver_proyectos,
               3 : ver_horario,
               4 : rol_examenes}
    options[f_sel]()

# while True:
seleccion()
