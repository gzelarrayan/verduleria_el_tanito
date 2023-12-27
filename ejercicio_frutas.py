# 1) pedimos al usuario que ingrese una fruta (manzana, banana, naranja, etc)
# 2) indicar si es banana
# 3) indicar si es citrico (naranja, mandarina, pomelo, limon, kinoto)
# 4) indicar si es mandarina
# 5) indicar si no es banana ni citrico 
""" y ahora te pido que me informes cuando no sean ni banana ni mandarina, qué hacés?
una cosa más, investigá cómo se usa el "in" en una sentencia if o elif, y fijate qué podés mejorar.
saludos.
"""
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
print("")
print("Naranja   >>   Frutilla   >>   Kiwi   >>   Mandarina   >>   Pomelo")
print("")
print("Ciruela   >>   Banana   >>   Sandía   >>   Kinoto   >>   Cereza")
print("")
print("Manzana   >>   Higos   >>   Naranja   >>   Mango   >>   Limon   >>   Melón")
print("")
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
print("")
TodasFrutas = ['Frutilla', 'Kiwi', 'Ciruela', 'Sandia', 'Cereza', 'Manzana', 'Higos', 'Mango', 'Melon']
Citricos = ['Naranja', 'Mandarina', 'Pomelo', 'Limon', 'Kinoto']
fruta = input("Ingrese una fruta: ").capitalize()
# Se convierte la fruta a mayúsculas para que las comparaciones eviten el error de usuario.
if (fruta == "Banana"):
    print("La fruta ingresada es: ",fruta)
elif (fruta in Citricos):
    print("La fruta elegida es un cítrico")
    if (fruta == "Mandarina"):
        print("Es una Mandarina")
elif (fruta not in TodasFrutas):
        print("Dato incorrecto, selecionar una fruta de la lista")
else:
    print("No es ni Banana ni Mandarina")