#!/usr/bin/env python
import pika
import sys

from datetime import datetime

def serve():
    global clientes_id
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.exchange_declare(exchange='intermediario', exchange_type='direct')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='intermediario', queue=queue_name, routing_key="server")

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        global clientes_id
        global flag_write
        decode_body =  body.decode().split("-")

        if(decode_body[0] == "\\subscribe"):
            Mensajes_enviados[decode_body[1]] = []
            id_clientes[str(clientes_id)] = decode_body[1]
            clientes_id += 1

        elif(decode_body[0] == "\\clientes"):
            return_clientes = ""
            for i, j in id_clientes.items():
                return_clientes += i + ": [Cliente " + j + "] \n"
            channel.basic_publish(
                exchange='intermediario', routing_key=decode_body[1], body=return_clientes)

        elif(decode_body[0] == "\\mensajes"):
            return_mensajes = ""
            for i in Mensajes_enviados[decode_body[1]]:
                return_mensajes += i +"\n"
            channel.basic_publish(
                exchange='intermediario', routing_key=decode_body[1], body=return_mensajes)

        elif(decode_body[0] == "\\salir"):
            for i, j in id_clientes.items():
                if(j == decode_body[1]):
                    del id_clientes[i]
                    break
        else:
            if(decode_body[0] not in id_clientes):
                channel.basic_publish(
                    exchange='intermediario', routing_key=decode_body[1], body="El destinatario no se encuentra conectado")
            elif(decode_body[1] == id_clientes[decode_body[0]]):
                channel.basic_publish(
                    exchange='intermediario', routing_key=decode_body[1], body="Ingrese un destinatario diferente a ud. mismo")
            else:
                now = datetime.now()
                localtime = now.strftime("%d/%m/%Y, %H:%M:%S")
                Mensajes_enviados[decode_body[1]].append("[" + localtime + "][Cliente " + id_clientes[decode_body[0]] + "]: " + decode_body[2])
                while(True):
                    if(flag_write == 0):
                        flag_write = 1
                        file = open("log.txt","a")
                        file.write("[" + localtime + "]["+ decode_body[1] + " -> " + id_clientes[decode_body[0]] + "]: " + decode_body[2] + "\n")
                        file.close()
                        flag_write = 0
                        break
                channel.basic_publish(
                    exchange='intermediario', routing_key= id_clientes[decode_body[0]], body="[" + localtime + "][Cliente " + decode_body[1] + "]: " + decode_body[2])


    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    Mensajes_enviados = {}
    id_clientes = {}
    clientes_id = 1
    flag_write = 0
    serve()
