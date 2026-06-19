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


    muestra_busqueda = input(str("Registre numero de muestra a buscar: ")).strip().upper()

    for x in muestras_lab:
        if x == muestra_busqueda:
            print (x), "Se encuentra en el sistema, a continuacion vera sus opciones."

            print("""
            ---- Seccion de gestion ----
                  
             1. Modificar Estado de Muestra
             2. Eliminar  Muestra

                  """)
            submuestra_input=int(input("Ingrese opcion: "))
    
            if submuestra_input == 1:

                nuevo_estadomuestra = str(input("Ingrese nuevo estado: "))
                muestras_lab.insert[muestras_lab.index(muestra_busqueda)[2]]
                return
            
            elif submuestra_input == 2:
                muestras_lab.remove(muestras_lab.index(muestra_busqueda))
                return
            
            else:
                print("Opcion no valida.")
        
   

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
        