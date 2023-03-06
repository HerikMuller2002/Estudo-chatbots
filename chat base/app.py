import nltk # pip install nltk
import re # pip install re
import string
import spacy #pip install spacy
import requests
import numpy as np

from os import system
from spacy.lang.pt.examples import sentences
from nltk.chat.util import Chat, reflections
from bs4 import BeautifulSoup # pip install bs4
from urllib.request import urlopen
from random import choice, randint
from sklearn.metrics.pairwise import cosine_similarity # pip install scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer # pip install scikit-learn
from flask import Flask, request, jsonify

nltk.download('punkt')
#system('cls')

# pip install lxml => erro de parser
# python -m spacy download pt_core_news_sm => erro de linguagem

txt_url = urlopen("https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial").read()
txt_html = BeautifulSoup(txt_url, 'lxml').find_all('p')
texto_pag_web = ''
for i in txt_html:
  texto_pag_web += i.text.lower()

lista_sentencas = nltk.sent_tokenize(texto_pag_web)

nlp = spacy.load("pt_core_news_sm")

# palavras que o modelo irá ignorar
stop_words = spacy.lang.pt.stop_words.STOP_WORDS
# pontuações que o modelo irá ignorar
stop_punct = string.punctuation

def preprocessamento(texto): #preparando o texto para ser processado pelo spacy
  # tirar urls
  texto = re.sub(r"https?://[A-Za-z0-9./]+",' ',texto)
  # tirar espaços em branco
  texto = re.sub(r" +", ' ',texto)
  # tirar radical (lematização)
  documento = nlp(texto)
  lista = []
  for token in documento:
    lista.append(token.lemma_)
  lista = [palavra for palavra in lista if palavra not in stop_words and palavra not in stop_punct]
  lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])
  return lista

# guardar as sentenças que serão pré-processadas pela função em uma lista
lista_sentencas_preprocessada = []
for i in range(len(lista_sentencas)):
  lista_sentencas_preprocessada.append(preprocessamento(lista_sentencas[i]))

textos_boas_vindas_entrada = ('hey', 'olá', 'opa', 'oi', 'eae')
textos_boas_vindas_respostas = ('hey, como posso ajudar?', 'olá, como posso ajudar?', 'oi, como posso ajudar?')
textos_saida = ('sair','tchau','exit','esc')

def responder_saudacao(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_boas_vindas_entrada:
      return choice(textos_boas_vindas_respostas)
    
def responder(texto_usuario):
  resposta_chatbot = ''
  lista_sentencas_preprocessada.append(texto_usuario)
  tfidf = TfidfVectorizer()
  palavras_vetorizadas = tfidf.fit_transform(lista_sentencas_preprocessada)
  similaridade = cosine_similarity(palavras_vetorizadas[-1], palavras_vetorizadas)
  indice_sentenca = similaridade.argsort()[0][-2]
  vetor_similar = similaridade.flatten()
  vetor_similar.sort()
  vetor_encontrado = vetor_similar[-2]
  if (vetor_encontrado == 0):
    resposta_chatbot = 'Desculpe, mas não entendi!'

    return resposta_chatbot
  else:
    resposta_chatbot = lista_sentencas[indice_sentenca]

    return resposta_chatbot
  
'''while True:
  texto_usuario = input('Usuário: ').lower()
  if texto_usuario not in textos_saida:
    if responder_saudacao(texto_usuario) != None:
      print('Chatbot:',responder_saudacao(texto_usuario))
    else:
      print('Chatbot:',responder(preprocessamento(texto_usuario)))
      lista_sentencas_preprocessada.remove(preprocessamento(texto_usuario))
  else:
    print('Chatbot: Até breve!')
    break'''

# api com flask
app = Flask(__name__)
@app.route("/<string:txt>", methods=["POST"])

def conversar (txt):
  resposta =''
  texto_usuario = txt.lower()
  if responder_saudacao(texto_usuario) != None:
    resposta = responder_saudacao(texto_usuario) 
  else:
    resposta = responder(preprocessamento(texto_usuario))
    lista_sentencas_preprocessada.remove(preprocessamento(texto_usuario))
  
  return jsonify({"texto_respondido":resposta})

app.run(port=5000,debug=False)