import numpy as np
import pandas as pd

dados = {
    "gene_id": ["BRCA1", "TP53", "EGFR", "MTHFR"],
    "tamanho_pb": [5592, 1179, 3633, 1980],  # pares de bases
    "mutacao_identificada": [True, False, True, False]
}

df = pd.DataFrame(dados)
print("Ambiente 100% pronto! DataFrame carregado com sucesso:")
print(df)
