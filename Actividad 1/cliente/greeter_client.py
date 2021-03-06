from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

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
def threaded(stub2):
    for response1 in stub2.SubscribeMessages(helloworld_pb2.DataReply(mensaje = getIP())):
        print(response1.mensaje)


def run():
    with grpc.insecure_channel('servidor:50051') as channel:
        stub = helloworld_pb2_grpc.AllClientsStub(channel)
        stub2 = helloworld_pb2_grpc.MensajeriaStub(channel)
        stub3 = helloworld_pb2_grpc.AllMessagesStub(channel)
        start_new_thread(threaded, (stub2,))
        destino = 0
        while(True):
            r_input = input("")
            if(r_input == "\\clientes"):
                print("Tu eres el cliente: " + getIP())
                for response in stub.getClients(helloworld_pb2.DataReply(mensaje=getIP())):
                    print(response.mensaje)
            elif(r_input == "\\mensajes"):
                for response3 in stub3.getMessages(helloworld_pb2.DataReply(mensaje= getIP())):
                    print(response3.mensaje)
            elif(r_input.split(" ")[0] == "\\destino"):
                destino = r_input.split(" ")[1]
            elif(r_input == "\\salir"):
                response2 = stub2.Salir(helloworld_pb2.DataReply(mensaje=getIP()))
                print(response2.mensaje)
                break
            else:
                if(destino != 0):
                    response2 = stub2.SendMensaje(helloworld_pb2.DataRequest(id = getIP(), destino = destino, mensaje = r_input))
                    if(response2 == "Error1"):
                        destino = 0
                        print("Ingrese un destinatario diferente a ud. mismo")
                    elif(response2 == "Error2"):
                        destino = 0
                        print("El destinatario no se encuentra conectado")
                else:
                    print("Ingrese un destinatario valido")



if __name__ == '__main__':
    logging.basicConfig()
    run()
