class Tv:
    def __init__(self, tamanho):
        self.volume = 50
        self.canal = 1
        self.tamanho = tamanho
        self.ligada = False

    def aumentar_volume(self):
        if self.volume < 99:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def mudar_canal(self,canal):
        if canal < 1 or canal > 99:
            raise ValueError('Canal inválido')

        self.canal = canal

    def ligar_desligar(self):
        if self.ligada = not self.ligada
