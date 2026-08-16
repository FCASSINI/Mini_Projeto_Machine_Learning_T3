from funcoes import carregar_csv
from funcoes import contar_categorias_vazias
from funcoes import contar_nulos_dimensoes
from funcoes import calcular_medias_dimensoes
from funcoes import tratar_dataset_produtos
from funcoes import analisar_datas_entregas
from funcoes import tratar_datas_pedidos
from funcoes import contar_pedidos_cancelados

## ÁREA DE EXECUÇÃO (Leitura de Dados), aqui vc digita o seu caminho inicial para o arquivo CSV.
print("Iniciando a leitura dos dados...\n")

# ==================================================
# ETAPA 0 - CONFIGURAÇÃO
# ==================================================

caminho_produtos = "dados/olist_products_dataset.csv"
caminho_pedidos = "dados/olist_orders_dataset.csv"

# ==================================================
# ETAPA 1 - CARGA DOS DADOS
# ==================================================

produtos = carregar_csv(caminho_produtos)
pedidos = carregar_csv(caminho_pedidos)

# ==================================================
# ETAPA 2 - DIAGNÓSTICO DOS DADOS BRUTOS
# ==================================================

total_produtos = len(produtos)
total_pedidos = len(pedidos)

total_vazias = contar_categorias_vazias(produtos)

nulos_dimensoes = contar_nulos_dimensoes(produtos)

medias_dimensoes = calcular_medias_dimensoes(produtos)

#ANALISANDO OS PEDIDOS AGORA
analise_entregas = analisar_datas_entregas(pedidos)

#CONTAGEM DE PEDIDOS CANCELADOS
total_cancelados = contar_pedidos_cancelados(pedidos)

# ==================================================
# ETAPA 3 - TRATAMENTO DOS DADOS
# ==================================================

produtos_tratados = tratar_dataset_produtos(produtos,medias_dimensoes)

pedidos_tratados = tratar_datas_pedidos(pedidos)

# ==================================================
# ETAPA 4 - RELATÓRIO FINAL
# ==================================================

total_valores_dimensional_corrigidos = sum(nulos_dimensoes.values())
total_valores_ausentes_corrigidos = total_vazias + total_valores_dimensional_corrigidos

print("="*60)
print("RELATÓRIO FINAL")
print("="*60)

print("\nETAPA 1 - CARGA DOS DADOS")
print("-"*60)

print(f"{'Produtos carregados:':<45}{total_produtos}")
print(f"{'Pedidos carregados:':<45}{total_pedidos}")


print("\nETAPA 2 - DIAGNOSTICO DOS DADOS BRUTOS")
print("-"*60)

print(f"{'Categorias vazias encontradas':<45}{total_vazias}")

print(f"{'Peso ausente':<45}{nulos_dimensoes['peso']}")
print(f"{'Comprimento ausente':<45}{nulos_dimensoes['comprimento']}")
print(f"{'Altura ausente':<45}{nulos_dimensoes['altura']}")
print(f"{'Largura ausente':<45}{nulos_dimensoes['largura']}")

print()

print(f"{'Total de valores dimensionais ausentes':<45}{total_valores_dimensional_corrigidos}")

print(f"{'Pedidos sem data de entrega':<45}{analise_entregas['sem_data_entrega']}")

print(f"{'Pedidos cancelados sem data de entrega':<45}{analise_entregas['sem_data_cancelados']}")

print(f"{'Pedidos sem data com outros status':<45}{analise_entregas['sem_data_outros_status']}")

print(f"{'Total de pedidos cancelados':<45}{total_cancelados}")

print("\nETAPA 3 - TRATAMENTO DOS DADOS")
print("-"*60)

print(f"{'Pedidos tratados':<45}{len(pedidos_tratados)}")
print(f"{'Produtos tratados':<45}{len(produtos_tratados)}")

print()

print(f"{'Categorias substituidas por sem categoria':<45}{total_vazias}")
print(f"{'Valores ausentes corrigidos':<45}{total_valores_ausentes_corrigidos}")

print()

print("Médias utilizadas na substituição")
print(f"{'Peso médio (g)':<45}{medias_dimensoes['peso']:.2f}")
print(f"{'Comprimento médio (cm)':<45}{medias_dimensoes['comprimento']:.2f}")
print(f"{'Altura média (cm)':<45}{medias_dimensoes['altura']:.2f}")
print(f"{'Largura média (cm)':<45}{medias_dimensoes['largura']:.2f}")

print("\nCONCLUSÃO DA ANÁLISE")
print("-" * 60)

print(
    "A hipótese de que todos os pedidos sem data de entrega "
    "estavam cancelados foi rejeitada."
)

print(
    f"Dos {analise_entregas['sem_data_entrega']} pedidos sem data de entrega, "
    f"{analise_entregas['sem_data_cancelados']} estavam cancelados."
)

print("=" * 60)
print("PROCESSAMENTO FINALIZADO COM SUCESSO")
print("=" * 60)
