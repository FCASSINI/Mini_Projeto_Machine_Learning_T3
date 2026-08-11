from funcoes import ler_csv
from funcoes import limpar_categorias

## 1. ÁREA DE EXECUÇÃO (Leitura de Dados), aqui vc digita o seu caminho inicial para o arquivo CSV.
print("Iniciando a leitura dos dados...\n")

##Insira aqui o caminho do arquivo CSV que deseja ler, por exemplo: "dados/olist_orders_dataset.csv"
caminho_arquivo = "dados/olist_products_dataset.csv"

total_resultados = ler_csv(caminho_arquivo)

print(f"Total de linhas lidas: {total_resultados}")
