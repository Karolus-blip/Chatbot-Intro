print("¡Hola! Soy Wormbook, tu librero virtual.")
nombre = input("¿Cuál es tu nombre? ")
print(f"¡Encantado de conocerte, {nombre}!")
mensaje = input("Dime, ¿en qué te puedo ayudar? ").lower()

if "pedido" in mensaje or "llega" in mensaje:
    print("Parece que tu problema es un pedido no recibido. No te preocupes, vamos a solucionarlo.")

elif "roto" in mensaje or "dañado" in mensaje:
    print("Siento mucho escuchar eso, pero no te preocupes. Vamos a resolverlo, ¿te parece?")

elif "inventario" in mensaje or "stock" in mensaje:
    print("Parece que tienes una duda de inventario. ¿Qué autor(a) te interesa o qué título buscabas?")

elif "devolución" in mensaje or "reembolso" in mensaje:
    print("Parece que necesitas ayuda con una devolución o reembolso.")

else:
    print("Una disculpa, no capté bien lo que me dijiste. ¿Me lo pdrías repetir, por favor?")
