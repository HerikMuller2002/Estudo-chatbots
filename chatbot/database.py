import sqlite3

class Banco_dados:
    def criar_db():
        # estabelece uma conexão com o banco de dados
        conexao = sqlite3.connect('suporteBD.db')
        # cria uma tabela chamada 'mensagens' com duas colunas: 'mensagem' e 'resposta'
        cursor = conexao.cursor()
        cursor.execute('CREATE TABLE problemas (assunto TEXT, app_device TEXT, interface TEXT, modelo TEXT, problema TEXT, solucao TEXT)')
        conexao.commit()
        # fecha a conexão com o banco de dados
        conexao.close()

    def inserir_db(lista):
        # estabelece uma conexão com o banco de dados
        conexao = sqlite3.connect('suporteBD.db')
        # insere algumas mensagens e respostas na tabela
        cursor = conexao.cursor()
        for i in lista:
            cursor.execute("INSERT INTO problemas (assunto) VALUES (?)", (i[0],))
        conexao.commit()
        # fecha a conexão com o banco de dados
        conexao.close()

    def ler_db():
        # estabelece uma conexão com o banco de dados
        conexao = sqlite3.connect('suporteBD.db')
        # Executa a instrução SQL SELECT para obter os dados da coluna desejada
        cursor = conexao.cursor()
        cursor.execute("SELECT resposta FROM mensagens")
        # Iterar sobre os resultados e imprimir na tela
        dados =[]
        for resultado in cursor.fetchall():
            dados.append(resultado[0])
        # fecha a conexão com o banco de dados
        conexao.close()

        return dados
    
lista_assunto = [['COLETA PERIODICA OFF LINE'],['INFRAESTRTURA'],['MYSEMEQ'],['PORTAL'],['SISTEMA ONLINE']]
lista_app = [['SISTEMA ONLINE'],['Link','VPN'],['SOFTWARE'],['SOFTWARE'],['SOFTWARE','EQUIPAMENTOS ON']]
lista_interface = [['COLETOR','CAMERA TERMOGRÁFICA','MTE'],[['TELEFONICA BANDA LARGA','TELEFONICA DEDICADO','ALGAR DEDICADO'],['SABESP','AMBEV EUROPA','ONLINE SAZ','ONLINE NAZ','ONLINE APAC']],['Integração','Semeq AWS API','Semeq API','Semeq Web','ABI MySEMEQ App','MySEMEQ App','ABInbev Web Platform','PowerBI','Vibracao','Oleo','Termografia','PORTAL'],['Integração','Semeq AWS API','Semeq API','Semeq Web','ABI MySEMEQ App','MySEMEQ App','ABInbev Web Platform','PowerBI','Vibracao','Oleo','Termografia','PORTAL'],['Interface Online Saz','EQUIPAMENTOS ON'],[['Interface Online Saz','Interface Online Naz','Interface Online Apac'],['Sensor','Gateway']]]
lista_modelo = [[[['SMQ608','SMQ609','SMQ710','SMQ720']],[['FLUKE TI-10','FLIR']],[['SMQ945']]],[[['120MB'],['30 MB'],['40MB']],[['TUNEL1','TUNEL2']]],[[['SAP ABI SAZ','SAP ABI EUROPA','EMAINT','Historiador SABESP']]]]

Banco_dados.criar_db()
#Banco_dados.inserir_db(lista_assunto)
#Banco_dados.ler_db()
