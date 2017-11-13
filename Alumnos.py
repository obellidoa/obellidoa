print("Bievenido al Asistente del Estudiante Irresponsable.")
print("En este programa te ayudaremos a salvar el semestre.")
print("Aunque no garantizamos nada, la verdad.")
print("Primero, dinos tu nombre:")
nombre=input("")
print("Muy bien, ", nombre, ", en el Asistente del Estudiante Irreponsable tenemos varias funciones.")
print("La primera función es el -placeholder-, para usar esta función, presiona 1.")
def seleccion ():
    f_seleccionada = input("Elije una opción: ").strip().lower()
    if f_seleccionada == '1':
        print("Bienvenido al -placeholder-, esta función te ayudará a monitorerar tus notas.")
        print("Primero dinos, ¿el curso que llevas incluye pesos en el cálculo de promedio?")
        print("Si no incluye pesos, presiona 1.")
        print("Si incluye pesos, presiona 2.")
        def seleccion_prom ():
            prom_seleccionado = int()
            if prom_seleccionado==1:
              notas_normal = []
              normal_num_prom = int(input("¿Cuántas calificaciones hay en el curso?"))
            for i in range(normal_num_prom):
                notas_normal.append(int(input("Ingresa una calificación:")))
                if 0 in notas_normal:
                    print("-")
            suma_prom_normal=sum(int(i) for i in notas_normal)
            prom_final_normal=suma_prom_normal/normal_num_prom
            if prom_final_normal==20:
                print("Felicidades, has conseguido una nota perfecta.")
            elif prom_final_normal<20 and prom_final_normal>12:
                print("Muy bien, te esforzaste.")
            elif prom_final_normal==11:
                print("Por poco.")
            elif prom_final_normal<10.5:
                print("Anda diciéndole a tus padres lo de la bica")
            else:
                print("Opción invalida. Intenta nuevamente.")
            return True
        while seleccion_prom():
            pass
    else:
         print("Opción invalida. Intenta nuevamente.")
    return True
while seleccion():
        pass
