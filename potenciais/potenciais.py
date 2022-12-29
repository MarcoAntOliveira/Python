import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt
#cria uma planilha mas não faz parte do codigo de potenciais
""""
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
"""
reaction = "O2 (g) + 2H2O + 4e- =  4OH- (aq)"
#lê a panilha em questão  
tab = pd.read_excel("potenciais.xlsx")
#display(tab)
#mostra em qual posição está a reação de redução
display(tab["Meia-reação"] == reaction)
#salva na variavel a posição onde está a reação
pot = tab.loc[tab["Meia-reação"] == reaction,"E0 /V"]
#imprimi o potencial padrão  
print(pot.head())
