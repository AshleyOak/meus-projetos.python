#importação das bibliotecas necessárias
import random
import time

#lista das perguntas e respostas
perguntas_respostas = {
    "Qual a cor do cavalo Branco de Napoleão?": "Branco",
    "Qual é a capital da Inglaterra?": "Londres",
    "Quem foi a primeira pessoa a pisar na Lua?": "Neil Armstrong",
    "Quem descobriu o Brasil?": "Pedro Álvares Cabral",
    "Qual é a maior ilha do mundo?": "Groelândia",
    "Qual o maior continente do mundo?": "Ásia",
    "Quem pintou A Última Ceia?": "Leonardo da Vinci",
    "Qual o nome do inventor da lâmpada?": "Thomas Edison",
    "Qual o nome do primeiro presidente dos Estados Unidos?": "George Washington",
    "Quem escreveu a obra Dom Quixote?": "Miguel de Cervantes",
    "Quem foi o primeiro rei de Portugal?": "Afonso Henriques",
    "Qual o maior país do mundo?": "Rússia",
    "Qual o maior oceano do mundo?": "Oceano Pacífico",
    "Qual o maior animal do mundo?": "A baleia azul",
    "Qual a maior montanha do mundo?": "Monte Everest",
    "Qual a cidade mais populosa do mundo?": "Tóquio",
    "Quem foi o primeiro presidente do Brasil?": "Dom Pedro I",
    "Qual o menor país do mundo?": "Vaticano",
    "Quem inventou o avião?": "The Wright Brothers",
    "Qual a altura do Monte Everest?": "8.848 metros",
    "Como é chamado o primeiro livro da Bíblia?": "Gênesis",
    "Quem foi o descobridor do Brasil?": "Pedro Álvares Cabral",
    "Quem foi o primeiro homem a andar no espaço?": "Yuri Gagarin",
    "Qual o maior rio do mundo?": "Rio Amazonas",
    "Quem foi o primeiro homem a escalar o Monte Everest?": "Sir Edmund Hillary",
    "Qual o maior lago do mundo?": "Lago Superior",
    "Quem foi o primeiro presidente do México?": "Guadalupe Victoria",
    "Qual a maior cachoeira do mundo?": "Salto Angel",
    "Qual era a profissão de Mahatma Gandhi?": "Advogado",
    "Quem foi o primeiro presidente do Japão?": "Hirobumi Ito",
    "Qual a capital do Canadá?": "Ottawa",
    "Qual a capital da Alemanha?": "Berlim",
    "Qual a capital da Turquia?": "Ancara",
    "Qual a capital da Austrália?": "Canberra",
    "Qual a capital da África do Sul?": "Pretória",
    "Qual a capital da Grécia?": "Atenas",
    "Qual a capital da Espanha?": "Madri",
    "Qual a capital da Índia?": "Nova Deli",
    "Qual a capital da Itália?": "Roma",
    "Qual a capital da França?": "Paris",
    "Qual a capital da Suécia?": "Estocolmo",
    "Qual a capital dos Estados Unidos?": "Washington D.C.",
    "Qual a capital da China?": "Pequim",
    "Qual a capital da Holanda?": "Amsterdã",
    "Qual a capital da Finlândia?": "Helsínquia",
    "Qual a capital do Egito?": "Cairo",
    "Qual a capital da Argentina?": "Buenos Aires",
    "Qual a capital do Brasil?": "Brasília",
    "Qual a capital do Japão?": "Tóquio",
    "Qual a capital do Reino Unido?": "Londres",
    "Qual a capital da Rússia?": "Moscou",
    "Qual a capital da Coreia do Sul?": "Seul",
    "Qual a capital da Áustria?": "Viena",
    "Qual a capital da Irlanda?": "Dublin",
    "Qual a capital da Nova Zelândia?": "Wellington",
    "Qual a capital da Eslováquia?": "Bratislava",
    "Qual a capital da Ucrânia?": "Kiev",
    "Qual a capital do México?": "Cidade do México",
    "Qual a capital da Polônia?": "Varsóvia",
    "Qual a capital da Romênia?": "Bucareste",
    "Qual a capital da Croácia?": "Zagreb",
    "Qual a capital da Dinamarca?": "Copenhaga",
    "Qual a capital da Noruega?": "Oslo",
    "Qual a capital da Hungria?": "Budapeste",
    "Qual a capital da Austrália?": "Canberra",
    "Qual a capital da Suíça?": "Berna",
    "Qual a capital da Bélgica?": "Bruxelas",
    "Qual a capital da Tailândia?": "Banguecoque",
    "Qual a capital do Canadá?": "Ottawa",
    "Qual a capital da Colômbia?": "Bogotá",
    "Qual a capital da África do Sul?": "Pretória",
    "Qual a capital da Indonésia?": "Jacarta"
}

#mensagem de boas vindas
print("*** Bem vindo ao Quiz de Perguntas e Respostas ***")

#variável para o controle do loop
loop = True

#enquanto loop for verdadeiro
while loop:
    #escolhe uma pergunta aleatória
    pergunta = random.choice(list(perguntas_respostas.keys()))
    #imprime a pergunta
    print("Pergunta:", pergunta)
    #variável de controle do loop interno
    loop_interno = True
    #enquanto loop interno for verdadeiro
    while loop_interno:
        #pede a resposta do usuário
        resposta = input("Resposta: ")
        #verifica se a resposta é igual a resposta correta
        if resposta == perguntas_respostas[pergunta]:
            #imprime que a resposta está correta
            print("Resposta correta!")
            #sai do loop interno
            loop_interno = False
        else:
            #imprime que a resposta está incorreta
            print("Resposta incorreta!")
            #pede ao usuário se ele deseja continuar tentando
            continuar