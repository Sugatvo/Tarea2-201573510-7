from concurrent import futures
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

from datetime import datetime



class AllClients(helloworld_pb2_grpc.AllClientsServicer):

    def getClients(self, request, context):
        for i, j in id_clientes.items():
            yield helloworld_pb2.DataReply(mensaje = i + ": [Cliente " + j + "]")


class AllMessages(helloworld_pb2_grpc.AllMessagesServicer):

    def getMessages(self, request, context):
        file = open("log.txt","r")
        for i in Mensajes_enviados[request.mensaje]:
            yield helloworld_pb2.DataReply(mensaje = i)
        file.close()


class Mensajeria(helloworld_pb2_grpc.AllClientsServicer):

    def __init__(self):
        self.flag_write = 0
        self.clientes_id = 1

    def SubscribeMessages(self, request, context):
        clientes_activos[request.mensaje] = []
        Mensajes_enviados[request.mensaje] = []
        id_clientes[str(self.clientes_id)] = request.mensaje
        self.clientes_id += 1
        while(True):
            if(len(clientes_activos[request.mensaje]) > 0):
                yield helloworld_pb2.DataReply(mensaje = clientes_activos[request.mensaje].pop(0))


    #    for i in clientes_activos:
    #        yield helloworld_pb2.DataReply(mensaje = i)
    #    while(True):
    #        if():
    #            yield helloworld_pb2.DataRequest(id= request.id, mensaje = 'Mensaje')
            #    delate mensaje

    def SendMensaje(self, request, context):

        if(request.id == id_clientes[request.destino]):
            return helloworld_pb2.DataReply(mensaje = 'Destino invalido')
        else:
            now = datetime.now()
            localtime = now.strftime("%d/%m/%Y, %H:%M:%S")
            clientes_activos[id_clientes[request.destino]].append("[" + localtime + "][Cliente " + request.id + "]: " + request.mensaje)
            Mensajes_enviados[request.id].append("[" + localtime + "][Cliente " + id_clientes[request.destino] + "]: " + request.mensaje)
            while(True):
                if(self.flag_write == 0):
                    self.flag_write = 1
                    file = open("log.txt","a")
                    file.write("[" + localtime + "]["+ request.id + " -> " + id_clientes[request.destino] + "]: " + request.mensaje + "\n")
                    file.close()
                    self.flag_write = 0
                break
            return helloworld_pb2.DataReply(mensaje = 'Mensaje enviado')

    def Salir(self, request, context):
        print("puto")
        for i, j in id_clientes.items():
            if(j == request.mensaje):
                del id_clientes[i]
                break
        return helloworld_pb2.DataReply(mensaje = 'Salio de pana')



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_AllMessagesServicer_to_server(AllMessages(), server)
    helloworld_pb2_grpc.add_AllClientsServicer_to_server(AllClients(), server)
    helloworld_pb2_grpc.add_MensajeriaServicer_to_server(Mensajeria(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    clientes_activos = {}
    Mensajes_enviados = {}
    id_clientes = {}
    cantidad_mensajes = 0
    serve()
