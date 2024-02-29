import os
import configparser
from openai import OpenAI

# Configure the API KEY

config = configparser.ConfigParser()
config.read("OPENAI_API_KEY.ini")

key = config['ChatGPT']['api_key']

client = OpenAI(api_key = key)

# Crearemos una funcion para solicitar unna dieta, tendremos que tener en cuenta lo siquiente.


# Prompt: Data una pregunta del usuario:
# 1.- Vamos a ingresar la "Edad"
# 2.- Vamos a ingresar el "Sexo biologico"
# 3.- Vamos a ingresar el "Peso de bascula" 
# 4.- Vamos a ingresar si "Hacemos actividad Fisica"
# 6.- Vamos a ingrsar el "tipo de actividad fisica"
# 5.- Vamos a ingresar si "Objetivos"

# Formato de prompt, como haremos la consulta


formato = """
Dada los siguientes datos, genera un plan alimenticio optimo, para: {nombre}
1.- Edad: {edad}
2.- Sexo biologico: {genero}
3.- Peso de bascula: {peso}
4.- Hacemos actividad Fisica: {a_fisica} 
6.- tipo de actividad fisica: {t_fisica}
5.- Objetivos a largo plazo: {objetivos}
"""
#print(formato.format(edad = edad1, persona = persona1))


def pedir_dieta(peticion :  str) -> str | None:
    #peticion = consulta(peticion)
    prompt = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature = 0,
        messages = [
            {"role": "system", "content": peticion},
        ]
    )

    #print(prompt.choices[0].message)
    return prompt.choices[0].message


def consulta(inp1, inp2, inp3, inp4, inp5, inp6, inp7):
    pregunta = formato.format(nombre = inp1, edad = inp2, genero = inp3, peso = inp4, a_fisica = inp5,
                              t_fisica = inp6, objetivos = inp7)
    return pregunta


#x1 = input("Dame tu nombre: ")
#x2 = input("Edad: ")
#x3 = input("Genero: ")
#x4 = input("Peso: ")
#x5 = input("Actividad fisica: ")
#x6 = input("Tipo de actividad fisica: ")
#x7 = input("objetivo a largo plazo: ")

#formato_bueno = consulta(x1,x2,x3,x4,x5,x6,x7)
#print(type(formato_bueno))
#print(formato_bueno)
#print(pedir_dieta(formato_bueno))





"""
response.choices[0].text

## Messages

#completion = client.chat.completions.create(
#  model="gpt-3.5-turbo",
#  messages=[
#    {"role": "system", "content": "say hi chatgpt."},
#    {"role": "user", "content": "You meet a agares?."}
#  ]
#)

#print(completion.choices[0].message)


response = OpenAI.Completion.create(
    model = "gpt-3.5-turbo", 
    prompt = "Hola chatgpt ¿como estas?",
    temperature = 0,
    max_tokens = 60,
    top_p = 1,
    frequency_penalty = 0.5,
    presence_penalty = 0
)



response = OpenAI.ChatCompletion.create(
    model = "gpt-3.5-turbo-1106",
    messages=[
        {
            "role":"user",
            "content":"dame una lista de proyectos en Python"
        }
    ]
)

print(response)
"""