1 docker-compose build
2 docker-compose up -d --scale cliente=2
3 abrir 2 terminales más
4 docker attach actividad1_servidor_1
5 docker attach actividad1_cliente_1
6 docker attach actividad1_cliente_2
