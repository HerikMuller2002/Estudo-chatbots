import nltk # pip install nltk
import re # pip install re
import string
import spacy #pip install spacy

from spacy.lang.pt.examples import sentences
from nltk.chat.util import Chat, reflections
from bs4 import BeautifulSoup # pip install bs4
from urllib.request import urlopen
from random import choice, randint
from sklearn.metrics.pairwise import cosine_similarity

# pip install lxml => erro de parser
# python -m spacy download pt_core_news_sm => erro de linguagem

txt_url = urlopen("https://pt.wikipedia.org/wiki/Pizza").read()
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
  texto = re.sub(r"https?://[A-Za-z0-9./]+",'',texto)
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
textos_boas_vindas_respostas = ('olá, bem-vindo!', 'oi, bem-vindo!')

def responder_saudacao(texto):
  for palavra in texto.split():
    if palavra.lower() in textos_boas_vindas_entrada:
      return choice(textos_boas_vindas_respostas)

palavras_vetorizadas[0].todense()