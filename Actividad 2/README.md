# Instrucciones 

1. docker-compose build
2. docker-compose up -d --scale cliente=2
3. Esperar a que el docker de rabbitmq se encuentre en estado disponible y se pueda acceder a él.
4. Abrir 2 terminales más.
5. docker attach actividad2_servidor_1 
6. docker attach actividad2_cliente_1
7. docker attach actividad2_cliente_2

# Consideraciones
Supusimos que el chat no es un chat global entre todos los clientes sino que un chat uno-a-uno entre los clientes. Entonces, para poder enviar mensajes los clientes deben definir un destino correspondiente con el cliente al cual le quieren enviar el mensaje. Es por esto que para poder ejecutar esta especificación y los servicios requeridos, se deben realizar los siguientes comandos:

- "\clientes" : Retorna un diccionario con la información de los clientes que se encuntran conectados actualmente con el servidor.
- "\destino [INT]" : Especifica a quien enviar el mensaje mediante un entero, el cual corresponde a llave del diccionario mostrado por el comando "\clientes". 
- "\mensajes" : Retornar los mensajes enviados por el cliente con el formato "[Hora][Destino]: mensaje". 
- "\salir": Se desconeta el cliente del servidor. 

# Indicaciones para crear más clientes

Para realizar esta función mediante docker-compose, se deben realizar las siguientes lineas de comando:
- docker-compose down (Cerrar los containers anteriores)
- docker-compose up -d --scale cliente=INT (Escalar los servicios mediante el comando --scale y el número de clientes deseados)
- Luego se tienen que abrir las consolas correspondientes y realizar los "docker attach" respectivos. 
