# Trabalho_IS

Nessa aplicação vão ser mandadas requisições para simular o Set e Get position de um robô. Para roda-lá primeiro é preciso executar um amqp broker localmente, para fazer a comunicação entre os serviços, depois executar o container de cada "Parte", sendo que o container da Parte 1 deve ser o último a ser executado.

### Broker
```
docker run -d --rm -p 5672:5672 -p 15672:15672 rabbitmq:3.7.6-management
```

### Parte 1
```
docker run --rm -it --network=host giovanapr/part1 python3 Parte1.py
```

### Parte 2
```
docker run --rm -it --network=host giovanapr/part2 python3 Parte2.py
```

### Parte 3
```
docker run --rm -it --network=host giovanapr/part3 python3 Parte3.py
```
