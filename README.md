# ✈️ ETL do Aeroporto de Schiphol (AMS)

Um projeto de ETL (Extract, Transform, Load) que coleta dados do aeroporto de Schiphol, transforma-os em um formato consistente e os armazena de forma organizada para análise.  
O pipeline foi estruturado em módulos claros para facilitar manutenção, reusabilidade e escalabilidade.

## 📁 Estrutura do Projeto

- 🧠 `constants.py` — Centraliza constantes e configurações (URLs, caminhos de saída, schemas, etc.)
- 📥 `extract.py` — Responsável pela extração de dados (APIs/arquivos)
- 🔧 `transformar.py` — Limpeza e transformação (tipos, normalização, enriquecimento)
- 💾 `salvar.py` — Persistência de dados (CSV/Parquet/DB)
- 🚀 `main.py` — Orquestração do pipeline (chama extract → transform → load)

> Observação: A modularização facilita testes unitários e a evolução do pipeline (ex.: trocar fonte de dados sem impactar as demais camadas).

## 🎯 Objetivo

- Coletar informações operacionais do Aeroporto de Schiphol (ex.: voos, horários, companhias, status).
- Padronizar dados para consumo analítico.
- Salvar saídas em formato amigável a BI/Data Lake.

## 🔄 Fluxo ETL

1. 📥 Extração (`extract.py`)
   - Conecta na(s) fonte(s) de dados definida(s) em `constants.py`
   - Faz chamadas a endpoints/baixa arquivos
   - Valida resposta e gera "raw data" com logs mínimos

2. 🔧 Transformação (`transformar.py`)
   - Normaliza colunas (nomes, tipos e formatos de data/hora)
   - Trata valores ausentes e inconsistências
   - Enriquecimento (derivação de campos úteis para análise)
   - Garante conformidade com o schema esperado

3. 💾 Carga (`salvar.py`)
   - Salva dados em CSV/Parquet (ou insere em banco)
   - Cria partições por data quando aplicável
   - Versiona saídas conforme configuração

4. 🚀 Orquestração (`main.py`)
   - Coordena a execução do pipeline
   - Lê variáveis/constantes de `constants.py`
   - Implementa tratamento de erros e logging

## ⚙️ Pré-requisitos

- 🐍 Python 3.9+
- 📦 Bibliotecas comuns de dados (ex.: `requests`, `pandas`, `pyarrow`/`fastparquet`)
- 🔐 Variáveis de ambiente (se houver chaves de API)
- 📁 Permissões de escrita no diretório de saída

Exemplo de instalação:
```bash
pip install -r requirements.txt
````
## ▶️ Como Executar
Execução simples:
````bash
python main.py
````

- Parâmetros (se configurados em constants.py ou via CLI):
🛠️ DATA_INICIO, DATA_FIM
🛣️ OUTPUT_DIR
🌐 API_BASE_URL, API_KEY
🧱 SCHEMA/mapeamentos de colunas

## 🧪 Qualidade e Validações
- ✅ Tipagem explícita nas colunas principais
- 🧹 Remoção/normalização de linhas inválidas
- 🕒 Padronização de timezone e formatos de data (UTC recomendado)
- 🔁 Idempotência na carga (evita duplicidades)
- 📝 Logs por etapa (sucesso/erros)

## 📊 Saídas
- 🗂️ Formatos: parquet e/ou csv
- 🧭 Particionamento: por data_execucao (opcional)
- 🏷️ Nomes de arquivos padronizados (ex.: schiphol_flights_YYYYMMDD.parquet)

## 🛡️ Tratamento de Erros
- ⏳ Retentativas em falhas de rede na extração
- 🚫 Filtro de respostas HTTP não-200
- ⚠️ Quarentena de registros fora do schema
- 🧾 Logging com contexto (etapa, fonte, timestamp)

## 🧭 Boas Práticas Adotadas
- 📦 Separação de camadas (E, T, L, Orquestração)
- 🧩 Uso de constants.py para evitar “valores mágicos”
- 🔄 Funções puras na transformação (facilita testes)
- 🧪 Validações e logs em pontos críticos
- 📝 Nomenclatura clara e previsível de arquivos e colunas

## 🤝 Contribuições
Sinta-se à vontade para abrir issues e enviar PRs:
🐛 Bug encontrado? Abra uma issue com passos de reprodução.
💡 Melhorias? Envie um PR com descrição do impacto.
