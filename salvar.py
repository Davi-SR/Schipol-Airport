import pandas as pd
import os
def salvar(dir_arquivos, planilhas, planilhas_nomes):
    for planilha, nome in zip(planilhas, planilhas_nomes):
        df = pd.DataFrame(planilha)
        arquivo = os.path.join(dir_arquivos, nome+'.csv')
        df.to_csv(path_or_buf=arquivo, sep=';', index = False)