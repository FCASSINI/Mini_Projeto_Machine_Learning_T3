import csv
import re
import unicodedata

#--------------------------------------------------------------------------
#    AREA DA FUNÇÃO DE LEITURA DE ARQUIVO CSV
#--------------------------------------------------------------------------
def carregar_csv(caminho):
    """Carrega um arquivo CSV utilizando csv.DictReader e retorna uma lista de dicionários."""
    
    produtos = []
    
    with open(caminho, mode='r',encoding="utf-8",newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        
        for linha in leitor:
            produtos.append(linha)
            
    return produtos
    


#--------------------------------------------------------------------------
#   AREA DA FUNÇÃO DE LIMPEZA DE CATEGORIA
#--------------------------------------------------------------------------
def limpar_categoria(categoria):
    """
    Normaliza uma categoria de produto removendo
    acentuação, espaços excedentes e caracteres
    especiais, retornando uma string padronizada.
    """
        
    categoria = unicodedata.normalize("NFD", categoria)
    categoria = categoria.strip()
    categoria = categoria.lower() 
    categoria = re.sub(r'[^\w\s]',"", categoria)  
    
   
    return categoria

#--------------------------------------------------------------------------
#   AREA DA FUNÇÃO DE TRATAMENTO DAS DIMENSÕES
#--------------------------------------------------------------------------
def tratar_dimensoes(linha, medias):
    """
   Trata as dimensões de um produto,
    substituindo valores vazios pelas médias calculadas
    e convertendo valores existentes para float.

    Retorna o dicionário do produto atualizado.
    """
    if linha["product_weight_g"].strip() == "":
        linha["product_weight_g"] = medias["peso"]
    else:
        linha["product_weight_g"] = float(linha["product_weight_g"])
    if linha["product_length_cm"].strip() == "":
        linha["product_length_cm"] = medias["comprimento"]
    else:
        linha["product_length_cm"] = float(linha["product_length_cm"])
    if linha["product_height_cm"].strip() == "":
        linha["product_height_cm"] = medias["altura"]
    else:
        linha["product_height_cm"] = float(linha["product_height_cm"])
    if linha["product_width_cm"].strip() == "":
        linha["product_width_cm"] = medias["largura"]
    else:
        linha["product_width_cm"] = float(linha["product_width_cm"])
    
    return linha
    
#--------------------------------------------------------------------------
#   AREA DA FUNÇÃO DE PROCESSAMENTO DE PRODUTO
#--------------------------------------------------------------------------
def processar_produto(linha, medias):
    """
    Processa um registro de produto.

    Realiza o tratamento do campo product_category_name:
    - substitui valores vazios por 'sem categoria';
    - aplica normalização textual em categorias preenchidas.

    Retorna o dicionário do produto atualizado.
    """
    
    categoria = linha["product_category_name"]
    
    if categoria.strip() == "":
       linha["product_category_name"] = "sem categoria"
    else:
        linha["product_category_name"] = limpar_categoria(categoria)

    linha = tratar_dimensoes(linha, medias)

    return linha

#--------------------------------------------------------------------------
#   AREA DA FUNÇÃO DE CONTAGEM DE CATEGORIAS VAZIAS
#--------------------------------------------------------------------------
def contar_categorias_vazias(produtos):
    """Conta quantas linhas possuem a categoria vazia."""
       
    contador = 0
        
    for linha in produtos:
        categoria = linha["product_category_name"]
        if categoria.strip() == "":
            contador += 1
    return contador

#--------------------------------------------------------------------------
#   AREA DA FUNÇÃO DE CONTAGEM DE DIMENSÕES NULAS
#--------------------------------------------------------------------------
def contar_nulos_dimensoes(produtos):
    """Conta quantas linhas possuem dimensões nulas."""
    
    nulos = {
        "peso": 0,
        "comprimento": 0,
        "altura": 0,
        "largura": 0
    }
    
            
    for linha in produtos:
        if linha["product_weight_g"].strip() == "":
            nulos["peso"]+=1
        if linha["product_length_cm"].strip() == "":
            nulos["comprimento"]+=1
        if linha["product_height_cm"].strip() == "":
            nulos["altura"]+=1
        if linha["product_width_cm"].strip() == "":
            nulos["largura"]+=1

    return nulos

#--------------------------------------------------------------------------
#   AREA DA FUNÇÃO DE CÁLCULO DE MÉDIAS DAS DIMENSÕES
#--------------------------------------------------------------------------
def calcular_medias_dimensoes(produtos):
    """Lê um arquivo CSV e calcula a média das dimensões dos produtos."""
    
    soma = {
        "peso": 0.0,
        "comprimento": 0.0,
        "altura": 0.0,
        "largura": 0.0
    }
    
    quantidade = {
        "peso": 0,
        "comprimento": 0,
        "altura": 0,
        "largura": 0
    }
    
            
    for linha in produtos:
        if linha["product_weight_g"].strip() != "":
            soma["peso"] += float(linha["product_weight_g"])
            quantidade["peso"] += 1
        if linha["product_length_cm"].strip() != "":
            soma["comprimento"] += float(linha["product_length_cm"])
            quantidade["comprimento"] += 1
        if linha["product_height_cm"].strip() != "":
            soma["altura"] += float(linha["product_height_cm"])
            quantidade["altura"] += 1
        if linha["product_width_cm"].strip() != "":
            soma["largura"] += float(linha["product_width_cm"])
            quantidade["largura"] += 1

    medias = {
        "peso": soma["peso"] / quantidade["peso"] if quantidade["peso"] > 0.0 else 0.0,
        "comprimento": soma["comprimento"] / quantidade["comprimento"] if quantidade["comprimento"] > 0.0 else 0.0,
        "altura": soma["altura"] / quantidade["altura"] if quantidade["altura"] > 0.0 else 0.0,
        "largura": soma["largura"] / quantidade["largura"] if quantidade["largura"] > 0.0 else 0.0
    }

    return medias

#--------------------------------------------------------------------------
#   AREA DA FUNÇÃO DE TRATAMENTO DO DATASET DE PRODUTOS
#--------------------------------------------------------------------------
def tratar_dataset_produtos(produtos,medias):
    """
    Processa cada linha
    aplicando a função processar_produto e retorna uma
    lista de dicionários com os produtos tratados.
    """
    
    produtos_tratados = []
    
    for linha in produtos:
        produto_tratado = processar_produto(linha,medias)
        produtos_tratados.append(produto_tratado)
    
    return produtos_tratados

