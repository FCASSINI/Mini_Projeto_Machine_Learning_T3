import csv
import re


def ler_csv(caminho):
    """
    Lê um arquivo CSV utilizando csv.DictReader,
    exibe os cinco primeiros registros e retorna
    a quantidade total de registros encontrados.
    """
        
    with open(caminho, mode='r',encoding="utf-8",newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        
        contador = 0
        
        for linha in leitor:
            contador += 1
            
            if contador <=5:
                print(linha)
                
    return contador


def limpar_categorias(categoria):
    """
    Limpa a coluna 'product_category_name' do arquivo CSV"""
    
    categoria = categoria.lower() 
    categoria = categoria.strip()
   
    return categoria
    
                

    