# EXERCÍCIO 06 - LISTA 08 - CLASSES
print('Classe TV')
print('#########')
print()

class TV():
    def __init__(self,volume=0,canal=0):
        self.volume = volume
        self.canal = canal
    def ajusta_volume(self,volume):
       if volume <=10 and volume >=0:
            self.volume = volume
       else:
           print('Volume fora da faixa')
    def ajusta_canal(self,canal):
       if canal <=40 and canal >=0:
            self.canal = canal
       else:
           print('Canal não existe')


tv=TV()

tv.ajusta_volume(10)
tv.ajusta_canal(40)
print(vars(tv))