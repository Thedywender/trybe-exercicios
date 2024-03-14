import threading, queue

fila_2 = queue.Queue()


def worker():
    while True:
        elemento = fila_2.get()
        print(f"Trabalhando na tarefa {elemento}")
        print(f"Finalizando a tarefa {elemento}")
        fila_2.task_done()


threading.Thread(target=worker, daemon=True).start()

for elemento in range(30):
    fila_2.put(elemento)
print("Todas as requisições foram enviadas!\n", end="")

fila_2.join()
print("Todo o trabalho foi concluido!")
