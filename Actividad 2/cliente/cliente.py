#!/usr/bin/env python
import pika
import sys

from _thread import *
import threading
import socket

def getIP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return host_ip

    except:
        print("Unable to get IP")


print_lock = threading.Lock()
def threaded(channel):
    #Conexion al servidor
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='intermediario', queue=queue_name, routing_key=getIP())

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(body.decode())

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
    connection.close()


def run():
    #Conexion al servidor
    print("Bienvenido cliente: " + getIP())
    
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.exchange_declare(exchange='intermediario', exchange_type='direct')

    channel.basic_publish(
        exchange='intermediario', routing_key="server", body="\\subscribe-" + getIP())
    start_new_thread(threaded, (channel,))

    destino = 0
    while(True):
        r_input = input("")
        if(r_input == "\\clientes" or r_input == "\\mensajes"):
            channel.basic_publish(
                exchange='intermediario', routing_key="server", body=r_input + "-" + getIP())

        elif(r_input.split(" ")[0] == "\\destino"):
            destino = r_input.split(" ")[1]

        elif(r_input == "\\salir"):
            channel.basic_publish(
                exchange='intermediario', routing_key="server", body="\\salir-" + getIP())
            print("Bye")
            break

        else:
            if(destino != 0):
                message = destino + "-" + getIP() + "-" + r_input
                channel.basic_publish(
                    exchange='intermediario', routing_key="server", body=message)
            else:
                print("Ingrese un destinatario valido")

    connection.close()


if __name__ == '__main__':
    run()
