cliente = [["ID","Nombre Completo","Dirección","Celular","Correo","Edad"]]
cliente.append([input("ingrese ID cliente:"),
                  input("ingrese Nombre Cliente: "),
                  input("ingrese Dirección Cliente: "),
                  input("ingrese Nro Celular Cliente: "),
                  input("ingrese Correo Electrónico Cliente: "),
                  input("ingrese Edad Cliente: ")
                 ]) 
   
for i in range(len(cliente)):
    for j in range(len(cliente[i])):
        print(f"{cliente[i][j]}, ", end=' ')
    print()

