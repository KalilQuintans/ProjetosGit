import os

class book():
    def __init__(self):

        #Titulos salvos em listas, pois como é um  codigo simples, preferi as listas do que dicionarios.
        self.titulo = [' Soneto de Fidelidade (Vinicius de Moraes)', 'Ora direis ouvir estrelas (Olavo Bilac)', 'Canção do Exílio (Gonçalves Dias)']

        #Poemas salvos em listas, poucos dados, dando preferencia para listas e nao dicionarios pois acredito que por ser simples, seria mais facil manipular
        self.livro = ['''                De tudo, ao meu amor serei atento
                Antes, e com tal zelo, e sempre, e tanto
                Que mesmo em face do maior encanto
                Dele se encante mais meu pensamento.Quero vivê-lo em cada vão momento
                E em louvor hei de espalhar meu canto
                E rir meu riso e derramar meu pranto
                Ao seu pesar ou seu contentamento.E assim, quando mais tarde me procure
                Quem sabe a morte, angústia de quem vive
                Quem sabe a solidão, fim de quem amaEu possa me dizer do amor (que tive):
                Que não seja imortal, posto que é chama
                Mas que seja infinito enquanto dure.''', 
                '''                     Ora (direis) ouvir estrelas! Certo
                Perdeste o senso!” E eu vos direi, no entanto,
                Que, para ouvi-las, muita vez desperto
                E abro as janelas, pálido de espanto…E conversamos toda a noite, enquanto
                A Via Láctea, como um pálio aberto,
                Cintila. E, ao vir do sol, saudoso e em pranto,
                Inda as procuro pelo céu deserto.Direis agora: “Tresloucado amigo!
                Que conversas com elas? Que sentido
                Tem o que dizem, quando estão contigo?”E eu vos direi: “Amai para entendê-las!
                Pois só quem ama pode ter ouvido
                Capaz de ouvir e de entender estrelas.”''', 
                '''                     Minha terra tem palmeiras,
                Onde canta o Sabiá;
                As aves, que aqui gorjeiam,
                Não gorjeiam como lá.Nosso céu tem mais estrelas,
                Nossas várzeas têm mais flores,
                Nossos bosques têm mais vida,
                Nossa vida mais amores.Em cismar, sozinho, à noite,
                Mais prazer encontro eu lá;
                Minha terra tem palmeiras,
                Onde canta o Sabiá.Minha terra tem primores,
                Que tais não encontro eu cá;
                Em cismar — sozinho, à noite —
                Mais prazer encontro eu lá;
                Minha terra tem palmeiras,
                Onde canta o Sabiá.Não permita Deus que eu morra,
                Sem que eu volte para lá;
                Sem que desfrute os primores
                Que não encontro por cá;
                Sem qu’inda aviste as palmeiras,
                Onde canta o Sabiá.''']
        self.NumPag = 0
        self.passapag = ' '

    def passaPag(self):
        while True:

            #Limpeza do terminal, experiencia mais limpa e organizada
            os.system('cls')
            print('-_-' *10, self.titulo[self.NumPag], '-_-' * 10)

            print(self.livro[self.NumPag])

            #Codigo para atualização de opções
            if self.NumPag < 2 and self.NumPag > 0:
                print('<---- Anterior      Próximo---->')
                self.passapag = input()
            elif self.NumPag == 2:
                print('<---- Anterior      Terminar---->')
                self.passapag = input()
            elif self.NumPag == 0:
                print('      Próximo---->')
                self.passapag = input()
            self.passapag.lower()


            #Codigo para atualização de página e termino
            if self.passapag == 'proximo':
                self.NumPag = self.NumPag + 1

            elif self.passapag == 'anterior':
                self.NumPag = self.NumPag - 1 
            
            elif self.passapag == 'terminar':
                os.system('cls')
                print('Muito Obrigado Por Ler')
                break
            
            
            





livro = book()

livro.passaPag()