# Importa as bibliotecas necessárias
import requests  # Para fazer requisições HTTP
import pandas as pd  # Para manipulação de dados
from datetime import datetime  # Para trabalhar com datas e timestamps
import time  # Biblioteca de tempo (não usada neste código)

# Função para obter dados de criptomoedas da API CoinGecko
def get_crypto_data(currency='eur', limit=10):
    """
    Esta função busca dados de criptomoedas de uma API:
    - Permite escolher a moeda de referência (padrão: USD)
    - Permite definir quantas criptomoedas buscar (padrão: 100)
    - Ordena as criptomoedas por capitalização de mercado
    """
    # URL base da API CoinGecko
    base_url = "https://api.coingecko.com/api/v3/coins/markets"
    
    # Parâmetros da requisição
    params = {
        'vs_currency': currency,  # Moeda de comparação
        'order': 'market_cap_desc',  # Ordenar por capitalização de mercado
        'per_page': limit,  # Número de criptomoedas
        'sparkline': 'false'  # Não incluir dados de gráficos
    }
    
    try:
        # Faz a requisição à API
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Verifica se houve erro na requisição
        
        # Converte a resposta para um DataFrame do pandas
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        # Trata qualquer erro na requisição
        print(f"Erro ao fazer requisição: {e}")
        return None

# Função para salvar os dados em um arquivo CSV
def save_to_csv(df, filename=None):
    """
    Salva os dados em um arquivo CSV:
    - Se nenhum nome for fornecido, gera um nome com timestamp
    - Salva sem incluir o índice do DataFrame
    """
    if filename is None:
        # Gera um nome de arquivo único com data e hora atual
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'crypto_data_{timestamp}.csv'
    
    try:
        # Salva o DataFrame em um arquivo CSV
        df.to_csv(filename, index=False)
        print(f"Dados salvos com sucesso em: {filename}")
    except Exception as e:
        # Trata qualquer erro durante o salvamento
        print(f"Erro ao salvar arquivo: {e}")

# Função para exibir um resumo dos dados
def display_data_summary(df):
    """
    Mostra informações resumidas sobre as criptomoedas:
    - Total de criptomoedas
    - Top 5 criptomoedas por capitalização de mercado
    - Estatísticas básicas dos preços
    """
    if df is None or df.empty:
        print("Nenhum dado disponível para exibição")
        return
    
    print("\n=== Resumo dos Dados ===")
    print(f"Total de criptomoedas: {len(df)}")
    
    print("\nTop 5 criptomoedas por capitalização de mercado:")
    print(df[['name', 'current_price', 'market_cap']].head())
    
    print("\nEstatísticas básicas dos preços:")
    print(df['current_price'].describe())

# Função principal que coordena todo o processo
def main():
    # Obtém os dados de criptomoedas
    df = get_crypto_data()
    
    if df is not None:
        # Salva os dados em um arquivo CSV
        save_to_csv(df)
        
        # Exibe um resumo dos dados
        display_data_summary(df)

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()