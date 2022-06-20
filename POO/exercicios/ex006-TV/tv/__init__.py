class TV(object):
    def __init__(self):
        self.ligada = False
        self.canal = 1
        self.volume = 0
        self.max_canal = 10
        self.max_volume = 10

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def aumentar_canal(self):
        if self.canal < self.max_canal:
            self.canal += 1
        else:
            self.canal = 1

    def diminuir_canal(self):
        if self.canal > 1:
            self.canal -= 1
        else:
            self.canal = self.max_canal

    def aumentar_volume(self):
        if self.volume < self.max_volume:
            self.volume += 1
        else:
            self.volume = self.max_volume

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            self.volume = 0

    def __str__(self):
        if self.ligada:
            return 'TV: Ligada\nCanal: {}\nVolume: {}'.format(self.canal, self.volume)
        else:
            return 'TV: Desligada'