import dataset

miBase = dataset.connect("sqlite:///base.db")
tabla = miBase["Productos"]

def mostrar_productos():
    print("\n    ---Lista de Productos---   ")
    if len(tabla) == 0:
        print("No hay productos en el sistema.")
    else:
        for item in tabla:
            print(f"ID: {item['id']} | Producto: {item['Nombre']} | Precio: ${item['Precio']} | Categoria: {item['Categoria']}")
    print("     ----------------------   ")

while True:
    opciones = input("\n---Bienvenido al Sistema de Productos---\n\nA. Agregar Producto\nB. Buscar Producto\nL. Listar Productos\nAC. Actualizar Producto\nN. Borrar Producto por Nombre\nID. Borrar Producto por ID\nS. Salir del Sistema\n\nElija la acción que desea ejecutar: ").strip().upper()
    
    if opciones == "A":
        nuevoproducto = input("Que producto desea agregar?: ").strip().title()
        nuevoprecio = float(input("Precio del producto?: ").strip())
        nuevacategoria = input("Categoria del producto?: ").strip().title()

        agregar = {"Nombre": nuevoproducto,"Precio": nuevoprecio,"Categoria": nuevacategoria}
        tabla.insert(agregar)
        print(f"{nuevoproducto} agregado con éxito!")
        
    elif opciones == "B":
        buscausuario = input("Que producto desea buscar?: ").strip().title()
        encontrado = tabla.find_one(Nombre=buscausuario)
        
        if encontrado != None:
            print(f"{buscausuario} está disponible en sistema! (ID: {encontrado['id']} | Precio: ${encontrado['Precio']} | Categoria: {encontrado['Categoria']})")
        else:
            print(f"{buscausuario} no está en sistema")
    
    elif opciones == "L":
        mostrar_productos()

    elif opciones == "AC":
        mostrar_productos()
        
        if len(tabla) > 0:
            idBuscar = int(input("Ingrese el ID del producto a actualizar: ").strip())
            encontrado = tabla.find_one(id=idBuscar)
            
            if encontrado != None:
                nombreActualizar = input("Nombre nuevo: ").strip().title()
                precioActualizar = float(input("Precio nuevo: ").strip())
                catActualizar = input("Categoria nueva: ").strip().title()
                
                actualizar = {"id": idBuscar,"Nombre": nombreActualizar,"Precio": precioActualizar,"Categoria": catActualizar}
                tabla.upsert(actualizar, ["id"])
                print("Producto actualizado con éxito!")
            else:
                print("ERROR, ese ID no existe.")

    elif opciones == "N":
        mostrar_productos()
        
        if len(tabla) > 0:
            eliminausuario = input("Ingrese el Nombre del producto a borrar: ").strip().title()
            encontrado = tabla.find_one(Nombre=eliminausuario)
            
            if encontrado != None:
                confirmacion = input(f"Confirme si desea eliminar '{eliminausuario}' con S/N: ").strip().upper()
                if confirmacion == "S":
                    tabla.delete(Nombre=eliminausuario)
                    print(f"{eliminausuario} eliminado con éxito!")
                else:
                    print("Operación cancelada.")
            else:
                print("ERROR, el producto no se encuentra en la base de datos.")

    elif opciones == "ID":
        mostrar_productos()
        
        if len(tabla) > 0:
            borrar_id = int(input("Ingrese el ID del producto a borrar: ").strip())
            encontrado = tabla.find_one(id=borrar_id)
            
            if encontrado != None:
                confirmacion = input(f"Confirme si desea eliminar '{encontrado['Nombre']}' con S/N: ").strip().upper()
                if confirmacion == "S":
                    tabla.delete(id=borrar_id)
                    print("Producto eliminado con éxito!")
                else:
                    print("Operación cancelada.")
            else:
                print("ERROR, ese ID no existe.")

    elif opciones == "S":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción incorrecta, elija una opción válida del menú.")
