from funcoes import carregar_csv
from funcoes import contar_categorias_vazias
from funcoes import contar_nulos_dimensoes
from funcoes import calcular_medias_dimensoes
from funcoes import tratar_dataset_produtos


## 1. ÁREA DE EXECUÇÃO (Leitura de Dados), aqui vc digita o seu caminho inicial para o arquivo CSV.
print("Iniciando a leitura dos dados...\n")

#ETAPA 0 - DEFINIÇÃO DO CAMINHO DO ARQUIVO CSV
##Insira aqui o caminho do arquivo CSV que deseja ler, por exemplo: "dados/olist_orders_dataset.csv"
caminho_arquivo = "dados/olist_products_dataset.csv"
caminho_pedidos = "dados/olist_orders_dataset.csv"

#ETAPA 1 - CARGA DOS DADOS
#Produtos representa os dados brutos
produtos = carregar_csv(caminho_arquivo)
pedidos = carregar_csv(caminho_pedidos)

#ETAPA 2 - DIAGNÓSTICOS
total_resultados = len(produtos)
total_pedidos = len(pedidos)
total_vazias = contar_categorias_vazias(produtos)
nulos_dimensoes = contar_nulos_dimensoes(produtos)
medias_dimensoes = calcular_medias_dimensoes(produtos)

#ETAPA 3 - TRATAMENTO DOS DADOS
#Produtos_tratados representa ja os dados tratados, com as dimensões nulas substituidas pelas médias e categorias vazias com "sem categoria"
produtos_tratados = tratar_dataset_produtos(produtos,medias_dimensoes)


print(f"Total de linhas lidas: {total_resultados}")
print(f"Total de pedidos: {total_pedidos}")
print(f"Total de categorias vazias: {total_vazias}")
#print("Categorias vazias nos produtos brutos:", contar_categorias_vazias(produtos))
print(f"Total de dimensões nulas: {nulos_dimensoes}")
print(f"Médias das dimensões: {medias_dimensoes}")
print(f"Produtos processados: {len(produtos)}")
#print(f"Exemplo de produto processado: {produtos[0]}")
#print(f"Tipo do peso do primeiro produto: {type(produtos[0]['product_weight_g'])}")
print(f"Total de produtos carregados: {len(produtos)}")

print(
    "Categorias vazias nos dados brutos:",
    contar_categorias_vazias(produtos)
)

contador_sem_categoria = 0

for produto in produtos_tratados:
    if produto["product_category_name"] == "sem categoria":
        contador_sem_categoria += 1

print(
    "Sem categoria nos dados tratados:",
    contador_sem_categoria
)