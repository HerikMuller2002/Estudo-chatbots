import random
import sqlite3
import nltk
import spacy
import re
import string
import json
from database import Banco_dados
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer # pip install scikit-learn
from sklearn.metrics.pairwise import cosine_similarity

# python -m spacy download pt_core_news_sm => erro de linguagem

nltk.download('punkt')
nlp = spacy.load("pt_core_news_sm")

# Conectar ao banco de dados
conectar = sqlite3.connect('suporteBD.db')

# Função para pré-processar o input do usuário
def preprocess_input(user_input):
    # palavras que o modelo irá ignorar
    stop_words = spacy.lang.pt.stop_words.STOP_WORDS
    # pontuações que o modelo irá ignorar
    stop_punct = string.punctuation
    # tirar pontuações
    user_input = re.sub(r"[!#$%&'()*+,-./:;<=>?@[^_`{|}~]+", ' ',user_input)
    # tirar espaços em branco
    user_input = re.sub(r" +", ' ',user_input)
    # Tokenize o texto em palavras
    user_input = word_tokenize(user_input)
    # Converter todas as palavras para minúsculas
    user_input = [word.lower() for word in user_input]
    # Retornar as palavras como uma string única
    user_input = " ".join(user_input)
    # tirar radical (lematização)
    documento = nlp(user_input)
    user_input = []
    for token in documento:
        user_input.append(token.lemma_)
    user_input = [palavra for palavra in user_input if palavra not in stop_words and palavra not in stop_punct]
    user_input = ' '.join([str(elemento) for elemento in user_input if not elemento.isdigit()])
    return user_input

def tf_idf(fonte):
    fonte.append(user_input)
    tfidf = TfidfVectorizer()
    palavras_vetorizadas = tfidf.fit_transform(fonte)
    similaridade = cosine_similarity(palavras_vetorizadas[-1], palavras_vetorizadas)
    print('similaridade 1:',similaridade)
    indice_sentenca = similaridade.argsort()[0][-2]
    print('\nsimilaridade 2:',indice_sentenca)
    vetor_similar = similaridade.flatten()
    print('\nsimilaridade 3:',vetor_similar)
    vetor_similar.sort()
    print('\nsimilaridade 4:',vetor_similar)
    vetor_encontrado = vetor_similar[-2]
    return vetor_encontrado,indice_sentenca

# Função para obter uma resposta do chatbot
def get_response(user_input):
    # Pré-processar o input do usuário
    user_input = preprocess_input(user_input)
    resposta_chatbot = ''
    lista = []
    db = Banco_dados.ler_db()
    for i in db:
        a = preprocess_input(i)
        lista.append(a)
    vetor_encontrado,indice_sentenca = tf_idf(lista)
    if (vetor_encontrado == 0):
        vetor_encontrado,indice_sentenca = tf_idf(db)
        if (vetor_encontrado == 0):
            resposta_chatbot = 'Desculpe, mas não entendi!'
        else:
            resposta_chatbot = db[indice_sentenca]
        return resposta_chatbot
    else:
        resposta_chatbot = db[indice_sentenca]
        return resposta_chatbot

    '''# Verificar se a entrada do usuário corresponde a alguma chave em nosso dicionário de respostas
    for key in responses.keys():
        if user_input in key.lower():
            # Escolher uma resposta aleatória para essa chave
            return responses[key][random.randint(0, len(responses[key])-1)]
    # Se a entrada do usuário não corresponder a nenhuma chave em nosso dicionário de respostas, realizar uma consulta no banco de dados
    c = conn.cursor()
    c.execute("SELECT resposta FROM tabela WHERE pergunta=?", (user_input,))
    result = c.fetchone()
    if result is not None:
        return result[0]
    # Se a consulta não retornar resultados, retornar uma resposta padrão
    return "Desculpe, eu não entendi o que você disse."

# Loop principal do chatbot
while True:
    # Obter a entrada do usuário
    user_input = input("Usuário: ")
    # Obter uma resposta do chatbot
    bot_response = get_response(user_input)
    # Imprimir a resposta do chatbot
    print("ChatBot:", bot_response)'''



textos_saida = ('sair','tchau','exit','esc')
while True:
  user_input = input('Usuário: ').lower()
  if user_input not in textos_saida:
    print('Chatbot:',get_response(preprocess_input(user_input)))
  else:
    print('Chatbot: Até breve!')
    break