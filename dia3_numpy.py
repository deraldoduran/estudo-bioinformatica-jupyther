import numpy as np

# 1. Definindo dados do experimento
genes = ["TP53", "BRCA1", "EGFR", "MTHFR", "TNF"]
pacientes = ["Controle_1", "Controle_2", "Tratado_1", "Tratado_2"]

# 2. Criando uma matriz 2D (5 genes x 4 pacientes) com valores simulados de expressão gênica
# Valores variando de 10.0 a 100.0
np.random.seed(42)  # Garante que os números sorteados sejam sempre os mesmos
matriz_expressao = np.random.uniform(low=10.0, high=100.0, size=(5, 4))

print("=== Matriz de Expressão (5 genes x 4 pacientes) ===")
print(matriz_expressao)
print("\nDimensões da matriz (shape):", matriz_expressao.shape)
print("Tipo dos dados (dtype):", matriz_expressao.dtype)
# 3. Calculando médias com axis
# axis=1 calcula a média andando pelas colunas (para cada gene)
media_por_gene = np.mean(matriz_expressao, axis=1)

# axis=0 calcula a média andando pelas linhas (para cada paciente)
media_por_paciente = np.mean(matriz_expressao, axis=0)

print("\n=== Média de expressão por gene ===")
for gene, media in zip(genes, media_por_gene):
    print(f"Gene {gene}: {media:.2f}")

print("\n=== Média geral por paciente ===")
for paciente, media in zip(pacientes, media_por_paciente):
    print(f"Paciente {paciente}: {media:.2f}")

   # 4. Fatiamento (Slicing): Isolando o grupo Tratado vs Controle
expressao_controle = matriz_expressao[:, 0:2]  # todas as linhas, colunas 0 e 1
expressao_tratado = matriz_expressao[:, 2:]    # todas as linhas, colunas 2 em diante

# Média de cada grupo
media_controle = np.mean(expressao_controle, axis=1)
media_tratado = np.mean(expressao_tratado, axis=1)

# Fold Change (variação de expressão induzida pelo tratamento): Tratado / Controle
fold_change = media_tratado / media_controle

print("\n=== Efeito do Tratamento (Fold Change) ===")
for gene, fc in zip(genes, fold_change):
    status = "HIPEREXPRESSO (Superexpresso)" if fc > 1.2 else "Sem alteração relevante"
    print(f"Gene {gene}: Fold-Change = {fc:.2f} -> {status}")