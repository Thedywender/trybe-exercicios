import threading, queue

fila = queue.Queue()

for tarefa in range(1, 10):
    fila.put(tarefa)

print("Agora, nossa fila tem tamanho:", fila.qsize())

print("A fila esta vazia?", fila.empty())

elemento_da_lista = fila.get()
fila.task_done()
elemento_da_lista = fila.get()
fila.task_done()
elemento_da_lista = fila.get()
fila.task_done()

print("Variavel", elemento_da_lista)

print("Agora nossa fila tem tamanho de :", fila.qsize())

for i in range(fila.qsize()):
    print(fila.get())
