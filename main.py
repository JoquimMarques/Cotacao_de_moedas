from kivy.app import App
from kivy.lang import Builder
from kivy.animation import Animation  # Importa o módulo de animação
import requests

# Carregar o arquivo .kv
GUI = Builder.load_file("tela.kv")

class MyApp(App):
    def build(self):
        return GUI
    
    def on_start(self):
        # Define uma animação de desvanecimento (fade-in) nos textos de moeda
        self.animate_label(self.root.ids["moeda1"], f"Dolar ${self.pegar_valores('USD')}")
        self.animate_label(self.root.ids["moeda2"], f"Euro ${self.pegar_valores('EUR')}")
        self.animate_label(self.root.ids["moeda3"], f"Bitcoin ${self.pegar_valores('BTC')}")
        self.animate_label(self.root.ids["moeda4"], f"Eterion ${self.pegar_valores('ETH')}")
    
    def pegar_valores(self, moeda):
        link= f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

    def animate_label(self, label, new_text):
        # Define o novo texto
        label.text = new_text
        # Cria uma animação que faz o texto desaparecer e reaparecer
        anim = Animation(opacity=0, duration=0.5) + Animation(opacity=1, duration=0.5)
        anim.start(label)

if __name__ == '__main__':
    MyApp().run()




