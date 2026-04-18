def calcular_pago_final():
    print("--- SISTEMA DE CAJA: TIENDA DE VIDEOJUEGOS ---")
    
    try:
    
        precio = float(input("Ingrese el precio del videojuego: Q"))
        es_vip = input("¿El cliente es miembro VIP? (Sí/No): ").strip().lower()

     
        if precio >= 500:
            subtotal = precio * 0.90
            print(f"Aplicado descuento del 10% por precio mayor a Q500. Nuevo subtotal: Q{subtotal:.2f}")
        else:
            subtotal = precio
            print("No aplica el primer descuento por precio base.")

       
        if es_vip in ["sí", "si", "s"]:
            precio_final = subtotal * 0.85
            print(f"Aplicado descuento VIP adicional del 15%.")
        else:
            precio_final = subtotal
            print("No se aplica descuento VIP.")

        print("-" * 45)
        print(f"EL PRECIO FINAL A PAGAR ES: Q{precio_final:.2f}")
        print("-" * 45)

    except ValueError:
        print("Error: Por favor, ingrese un número válido para el precio.")

calcular_pago_final()
