#Sistema Rápido de Trazabilidad de Muestras de Laboratorio 

muestras_lab=[]

#------------------------------------------------------------
#Definiciones de opciones disponibles en el menu del sistema
#------------------------------------------------------------

#-------------------
#Registro de muestra
#-------------------
def registro_muestra():

    try:
        num_muestra = str(input("Registre numero de muestra: ")).strip().upper()
        nombre_paciente = str(input("Registre nombre del paciente: ")).upper()
        temp_muestra = int(input("Registre temperatura de muestra (en C*): "))

    except ValueError:
        print("Error de valor!")
        return
    #----------------------
    #Logica de temperaturas
    #----------------------

    if temp_muestra < 2 or temp_muestra > 8:
        print("Temperatura fuera de rango establecido por codigo")
        print("Estado: RECHAZADO")
        estado_muestra = "RECHAZADO"
        

    elif temp_muestra > 2 and temp_muestra < 8:
        print("Muestra dentro de rango estandar.")
        print("Estado: PENDIENTE")
        estado_muestra = "PENDIENTE"

    #Añadir a lista de muestras de laboratorio.
    
    idmuestra = [num_muestra, nombre_paciente, estado_muestra]
    
    muestras_lab.append(idmuestra)
    return

#-------------------
#Busqueda de muestras
#-------------------

#Gestion de muestras
#-------------------
def gestion_muestras():

    if len(muestras_lab) == -1:
        print("Lista de muestra vacia, intente mas tarde.")

    muestra_busqueda = input(str("Registre numero de muestra a buscar: ")).strip().upper()

    for x in muestras_lab:
        if x == muestra_busqueda:
            print(f"{x} encontrado en lista")

            print("""-- Opciones de muestra -- """)
            print("1. Modificar muestra")
            print("2. Eliminar Muestra")
            input_submuestra = int(input("Ingrese Opcion: "))
        
            if input_submuestra == 1:
                muestras_lab.index(muestra_busqueda)
                return
        
            elif input_submuestra == 2:
                return

            else:
                print("No encontrado, intente nuevamente.")
                return
            
    #------------------------
    #Modificacion de muestras
    #------------------------
            print("""-- Opciones de muestra -- """)
            print("1. Modificar muestra")
            print("2. Eliminar Muestra")
        input_submuestra = int(input("Ingrese Opcion: "))
        
        if input_submuestra == 1:
            muestras_lab.index(muestra_busqueda)

        return

#Menu
def menu_sistema():
    
    print("""
          
------------------ Sistema de Trazabilidad de Muestras de Laboratorio ------------------
                     -- Sistema de Información del Laboratorio --

            1. Registros de Muestras
            2. Busqueda y gestion de Muestras
            3. Salida
          
          """)

#Programa
while True:

    menu_sistema()
    
    menu_input = input("Ingrese opcion: ").strip().upper()

    if menu_input == "1":
        registro_muestra()

    elif menu_input == "2":
        gestion_muestras()

    elif menu_input == "3":
        break

    else:
        print("Opcion no valida intente nuevamuente")
        