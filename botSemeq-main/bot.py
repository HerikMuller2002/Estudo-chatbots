import re
import json
from random import choice

###########################################

def entrada():
    input_user = input("\nusuário: ")
    input_user = preprocessamento(input_user)
    return input_user

def resposta_bot(resposta_entrada):
    print("chatbot:",resposta_entrada,'\n')

def preprocessamento(input_user): # preparando o texto para ser processado pelo spacy
  # tirar urls
  input_user = re.sub(r"https?://[A-Za-z0-9./]+",' ',input_user)
  # tirar pontuações
  input_user = re.sub(r"[!#$%&'()*+,-./:;<=>?@[^_`{|}~]+", ' ',input_user)
  # tirar espaços em branco
  input_user = re.sub(r" +", ' ',input_user)
  return input_user

def responder_entrada(input_user):
    for palavra in input_user.split():
        if palavra.lower() in textos_problema:
            return problema_usuario()
        elif palavra.lower() in textos_boas_vindas_entrada:
            return choice(textos_boas_vindas_respostas),False
        elif palavra.lower() in textos_saida:
            return choice(textos_saida_respostas),True
        else:
            continue
    return None,False

def problema_usuario():
    with open('bd_suporte.json','r',encoding='utf-8') as db:
        bd = json.load(db)
    resposta_bot("Irei te fazer algumas perguntas para identificar o problema, ok!?")
    id = []
    classes = []
    while True:
        resposta_bot("Qual das opções o seu problema melhor se enquadra?")
        if len(classes) < 1:
            for i in bd:
                id.append(i)
                print(id.index(i),'-',i)
        else:
            for i in bd[classes[-1]]:
                id.append(i)
                print(id.index(i),'-',i)
        input_user = entrada()
        if input_user in textos_saida:
            return None,True
        if len(classes) < 1:
            if bd[id[int(input_user)]]:
                classes.append(input_user)
        else:
            
        else:
            resposta = choice(respostas_nao_entendi)
            resposta_bot(resposta)
            continue

###########################################


textos_problema = ('ajuda','ajudar','problema','problemas','problem')
respostas_nao_entendi = ('Desculpe, não entendi!','Não entendi, pode repetir?')
textos_boas_vindas_entrada = ('hey','olá','opa','oi','eae','ai','aí','ae','ola','hello','salve','eai','bem')
textos_boas_vindas_respostas = ('Hey!, se precisar de ajuda é só mandar "estou com problema!" que farei o possível para ajudar!', 'Olá!, se precisar de ajuda é só mandar "estou com problema!" que farei o possível para ajudar!', 'Oi!, se precisar de ajuda é só mandar "estou com problema!" que farei o possível para ajudar!')
textos_saida = ('sair','tchau','exit','esc','parar','acabar','obrigado')
textos_saida_respostas = ('Até breve!','Até mais!')


print("> Mande um 'Olá' para o subot!\n> Para sair digite 'sair'")
while True:
    input_user = entrada()
    resposta,parar = responder_entrada(input_user)
    if parar == True:
        resposta_bot(choice(textos_saida_respostas))
        break
    elif resposta != None:
        resposta_bot(resposta)
        continue
    else:
        resposta = choice(respostas_nao_entendi)
        resposta_bot(resposta)
        continue