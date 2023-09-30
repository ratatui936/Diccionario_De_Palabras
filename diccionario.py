meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD":"una cara de risa",
            "CREEPY":"algo aterrador que da miedo",
            "BOOMER":"Persona que se aferra mucho al pasado",
            "PA":"para",
            "TROLlEAR": "hacer una broma"
            }

print("hola, bienvenido a la aplicacion de diccionario de palabras modernas.")


 

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    

    if word in meme_dict:
        print("el significado de ",word," es: ",meme_dict[word])

    else:
        print("lo sentimos no tenemos esta palabra")
