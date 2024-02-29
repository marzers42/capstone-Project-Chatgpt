Asistente Virtual para dieta y entrenador personal

app.py -> frontend de la aplicacion
project -> backend de la aplicacion

- ¿Que necesitamos?
	- Peso, composicion corporal
	- Altura
	- Dias de entrenamiento
	- algunas alergias conocidas

- La pregunta se hara a ChatGPT se guardara. junto con la rutina. El reto es justo el seguimiento y avances de la persona, una vbez dada la informacion se establecen parametros para lograr la evolucion deseada.

- imprimir en pantalla la dieta, porciones.

A esta aplicacion la llamaremos "entrenador virtual"

El objetivo es intentar automatizar el campo del Fitness, si podemos simplificar los datos claro esta.


Informacion complementaria:

- Crearemos una base de datos en la cual vamos a guardar estas consultas y de facil acceso (futuras consultas)
	- ¿Que informacion vamos a almacenar en esta BD?
		- Determinar necesidades
		- Calcular micronutrientes
			- Objetivos (input a guardar)
			- Edad
			- Sexo
			- Peso
			- Actividad Fisica

			Macro Nutrientes (output a guardar)
			- Carbohidratos
			- Proteinas
			- Grasas