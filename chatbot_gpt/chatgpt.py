import openai
from random import choice

while True:
    # api openai key
    openai.api_key = "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"

    # definindo o modelo
    model_engine = "text-davinci-003"

    # input do usuário
    print()
    txt_usuario = input('usuário: ').lower()

    lista_perguntas_boasvindas = ['oi','olá','opa','eai']
    lista_respostas_boasvindas = ['Olá, o que posso ajudar?','Hey, como posso ajudar?', 'Eai, tudo bem?']
    lista_despedida = ['Até mais!','Tchau, tchau!', 'Foi bom conversar com você!']
    lista_saida = ['sair','exit','tchau']

    if txt_usuario not in lista_saida:
        if txt_usuario not in lista_perguntas_boasvindas:
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=txt_usuario,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5
            )
            response = completion.choices[0].text
        else:
            response = choice(lista_respostas_boasvindas)
        print("chatbot:",response)
    else:
        print("chatbot:",choice(lista_despedida))
        break