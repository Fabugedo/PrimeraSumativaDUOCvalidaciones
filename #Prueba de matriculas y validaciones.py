#Prueba de matriculas y validaciones
fechas_ingresadas = []
patentes_ingresadas = []
while True:
  print("")
  print("Bienvenido a KUMOO RACING")
  print("por favor seleccione la opción, que desea navegar: ")
  print("1. Ingresar camioneta.")
  print("2. Registro mantenimiento.")
  print("3. consultar camioneta.")
  print("4. salir.")
  valormenu = int(input("ingrese su opción: "))

  if valormenu==1:
      print("")
      print("")
      print("A seleccionado: Ingresar camioneta.")
      print("A continuación se solicitaran los datos de su vehiculo.")
      lista=[]
      añocamio = int(input("ingrese el año de su vehiculo para su validación,si desea finalizar escriba *9* en la caja : "))
      lista.append(añocamio)
      if añocamio==9:
        print("cerrando el menú.")
        break
      if 1975<=añocamio<=2024:
        print("su vehiculo cumple con los requisitos para su ingreso.")
        print("")
        print("")
      else:
        print("su vehiculo no cumple con los requisitos para su ingreso.")
        continue

      print("A continuación se validará la placa del vehiculo.")
      print("por favor, ingrese su patente, respetando los siguientes formatos:")
      print("AA1111 o BBBB10")


      patente = str(input("ingrese su patente, si desea finalizar escriba *9* en la caja : "))
      if patente=="9":
          print("cerrando el menú.")

      if len(patente)==6:
        lista.append(patente)
        patentes_ingresadas.append(patente)
        print("su patente cumple con los requisitos para su ingreso.")
        print("validando formato")
        if patente[:2].isalpha() and patente[2:].isdigit():
          print("su patente cumple con los requisitos para su ingreso.")
          print("su patente ingresada es", patentes_ingresadas)

        elif patente[:4].isalpha() and patente[4:].isdigit():
          print("su patente cumple con los requisitos para su ingreso.")
          print("su patente ingresada es", patentes_ingresadas)

        else:
          print("su patente no cumple con los requisitos para su ingreso.")
      else:
        print("su patente no cumple con los requisitos para su ingreso.")

      print()
      print()
      print("A continuación seleccione el tipo de tracción")
      print("1. traccion simple (4x2).")
      print("2. traccion doble (4x4).")
      traccionmenu = int(input("ingrese su opción: "))
      lista.append(traccionmenu)
      if traccionmenu==1:
        print("su traccion es simple.")
      elif traccionmenu==2:
        print("su traccion es doble.")
      else:
        print("su ingreso no es valido.")
      print()
      print()

      print("A continuación se debe ingresar la marca de su vehiculo.")
      while True:
        marcamenu = str(input("ingrese su marca, si desea finalizar escriba *9* en la caja : ")).strip()
        lista.append(marcamenu)
        if marcamenu=="9":
          print("cerrando el menú.")
          break
        elif marcamenu:
          print("Su marca ingresada es", marcamenu)
          print("Su marca a sido registrada en el sistema")
          break
        else:
          print("Se debe ingresar un valor, intente nuevamente.")
      print("")
      print("")

      print("Para finalizar, por favor ingrese el modelo de su vehiculo, si desea finalizar escriba *9* en la caja :")
      while True:
        modelomenu = str(input("ingrese su modelo, si desea finalizar escriba *9* en la caja : ")).strip()
        lista.append(modelomenu)
        if modelomenu=="9":
          print("cerrando el menú.")
          break
        elif modelomenu:
          print("su modelo ingresado es ", modelomenu)
          print("su modelo a sido registrado en el sistema")
          print("Todos los datos de su camioneta han sido registrados")
          break
  if valormenu==2:
    print("")
    print("")
    print("A seleccionado: Registro mantenimiento.")
    print("A continuación se solicitaran los datos de su vehiculo.")
    print("Para continuar, debemos confirmar que la patente se encuentre registrada en el sistema.")
    print("por favor ingrese su patente, respetando los siguientes formatos:")
    print("AA1111 o BBBB10")
    valipatente=str(input("ingrese su patente, en la caja : "))
    if valipatente in patentes_ingresadas:
      print("Su patente se encuentra en nuestra base de datos")
      print("")
      print("")
    else:
      print("Su patente no se encuentra en nuestra base de datos")
      continue
    print("A continuación ingrese la fecha del mantenimiento.")
    dia=int(input("ingrese el dia del mantenimiento escogiendo la fecha entre 1 y 31: "))
    if 1<= dia <=31:
      print("su dia es valido.")
    else:
      print("su dia no es valido.")
    mes=int(input("ingrese el mes del mantenimiento escogiendo el mes entre 1 y 12: "))
    if 1<= mes <=12:
      print("su mes es valido.")
    else:
      print("su mes no es valido.")
    año=int(input("ingrese el año del mantenimiento entre 1970 a 2024: "))
    if 1970<= año <=2024:
      print("su año es valido.")
    else:
      print("su año no es valido.")
    fechas_ingresadas.append(dia)
    fechas_ingresadas.append(mes)
    fechas_ingresadas.append(año)
    print("Su fecha de mantenimiento corresponde a: ", fechas_ingresadas)
    print("")
    print("")
    print("Por ultimo")
    mecaob = str(input("ingrese su observación, en la caja : ")).strip()
    if mecaob:
      print("Se a tomado nota de su observación.")
    else:
      print("No habrá observación para el mecánico")
    lista.append(mecaob)
    lista.append(fechas_ingresadas)
    lista.append(modelomenu)
    lista.append(marcamenu)
    lista.append(patentes_ingresadas)
  if valormenu==3:
    print("")
    print("")
    print("A seleccionado: consultar camioneta.")
    print("A continuación deberá ingresar patente de su camioneta.")
    print("por favor ingrese su patente, respetando los siguientes formatos:")
    print("AA1111 o BBBB10")
    valpatente=str(input("ingrese su patente en la caja : "))
    if valpatente in patentes_ingresadas:
      print("Su patente se encuentra en nuestra base de datos")
    else:
      print("Su patente no se encuentra en nuestra base de datos")
      continue
    print("A continuación se mostrarán todos los datos de su camioneta.")
    print("Sus datos son los siguientes" )
    etiquetas = ["año", "patente", "traccion", "marca", "modelo", "observación", "fecha de mantenimiento"]
    datos = [añocamio, patente, traccionmenu, marcamenu, modelomenu, mecaob, fechas_ingresadas]
    for etiqueta, dato in zip(etiquetas, datos):
      print(etiqueta + ":", end=" ")
      print(dato)
    print("")
    print("")
  if valormenu==4:
    print("cerrando el menú.")
    print("Gracias por atenderse con nosotros.")
    break