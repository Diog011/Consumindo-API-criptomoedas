import requests
import pandas as pd
from datetime import datetime
import time

def get_crypto_data(currency='usd', limit=100):
    """
    Obtém dados de criptomoedas da API CoinGecko.
    
    Args:
        currency (str): Moeda de referência (default: 'usd')
        limit (int): Número máximo de criptomoedas a serem retornadas (default: 100)
    
    Returns:
        pandas.DataFrame: DataFrame com os dados das criptomoedas
    """
    base_url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': currency,
        'order': 'market_cap_desc',
        'per_page': limit,
        'sparkline': 'false'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Levanta exceção para erros HTTP
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")
        return None

def save_to_csv(df, filename=None):
    """
    Salva o DataFrame em um arquivo CSV.
    
    Args:
        df (pandas.DataFrame): DataFrame a ser salvo
        filename (str, optional): Nome do arquivo. Se None, gera um nome com timestamp
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'crypto_data_{timestamp}.csv'
    
    try:
        df.to_csv(filename, index=False)
        print(f"Dados salvos com sucesso em: {filename}")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

def display_data_summary(df):
    """
    Exibe um resumo dos dados coletados.
    
    Args:
        df (pandas.DataFrame): DataFrame com os dados das criptomoedas
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

def main():
    # Obtém os dados
    df = get_crypto_data()
    
    if df is not None:
        # Salva os dados
        save_to_csv(df)
        
        # Exibe o resumo
        display_data_summary(df)

if __name__ == "__main__":
    main()