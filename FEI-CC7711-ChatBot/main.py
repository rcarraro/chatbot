from chatbot import ChatBot
import json

myChatBot = ChatBot()
#apenas carregar um modelo pronto
myChatBot.loadModel()

#criar o modelo
# myChatBot.createModel()

orientador = False
imprimir = False

def adicionar_questao(pergunta):
    tag = input("insira a tag sobre o que você está tratando: ")
    perguntas_lista = []

    while(pergunta != ""):
        perguntas_lista.append(pergunta)
        pergunta = input("Existe alguma outra pergunta que poderia ter sido feita para isso ?\nSe não tiver, apenas de um ENTER\n")
    
    resposta = input("E qual seria a resposta ?")
    add_json = {'tag': tag, 'patterns': perguntas_lista, 'responses': [resposta]}

    with open('intents.json') as arquivo:
        data = json.load(arquivo)
        data['intents'].append(add_json)
        print(data)
    with open('intents.json', 'w', encoding='utf8') as arquivo:
        jsonString = json.dumps(data,ensure_ascii=False)
        arquivo.write(jsonString)

print("Bem vindo ao Chatbot")

pergunta = "ola"
resposta, intencao = myChatBot.chatbot_response(pergunta)

while (intencao[0]['intent']!="despedida" or float(intencao[0]['probability'])*100<=78):
    pergunta = input("posso lhe ajudar com algo?")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    
    if( float(intencao[0]['probability'])*100 <=78):
        questa = int(input("não posso responder a essa questão com precisão\nSe quiser, você pode adidciona-la\n1 - Sim\n2 - Não\n"))
        if questa == 2:
            print("OK")
            pass
        elif questa == 1:
            adicionar_questao(pergunta)
            imprimir = False

    
    
    if(intencao[0]['intent'] == 'orientador_func'):
        orientador = True
    
    if(intencao[0]['intent'] == 'orientador' and orientador == False):
        resp = int(input("Você já sabe o que um orientador faz?\n1 - Sim\n2 - Não\n"))
        if resp == 2:

            print("Um orientador serve para te aconselhar e ajudar a progredir no seu TCC.")
            
            orientador = True
            imprimir = True
        elif resp == 1:
            orientador = True
            imprimir = True
    
    if(imprimir):
        print(resposta)
    
    imprimir = True

print("Foi um prazer atendê-lo")
