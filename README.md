# Consumidor de API CoinGecko

Este projeto é um script Python que consome a API do CoinGecko para obter dados de criptomoedas, processa esses dados e os salva em formato CSV.

## Funcionalidades

- Obtém dados de criptomoedas da API CoinGecko
- Salva os dados em arquivo CSV com timestamp
- Exibe resumo dos dados coletados
- Suporta múltiplas moedas de conversão

## Requisitos

- Python 3.x
- requests
- pandas

## Configurações

O script permite configurar:
- Moeda de referência (padrão: USD)
- Limite de criptomoedas (padrão: 100)

## Exemplos de Uso

### Conversão em Diferentes Moedas

Você pode facilmente obter dados de criptomoedas em diferentes moedas:

```python
# Dados em Dólar (padrão)
get_crypto_data()  

# Dados em Euros
get_crypto_data(currency='eur')

# Dados em Reais
get_crypto_data(currency='brl')
```

### Comparativo de Preços

Exemplo de variação de preços para Bitcoin:
| Moeda   | Preço    |
|---------|----------|
| Reais   | R$ 92.792|
| Euros   | € 107.161|
| Dólares | $ 588.632|

## Dicas

- Use o parâmetro `limit` para alterar o número de criptomoedas
- O arquivo CSV é gerado automaticamente com um timestamp único
- Verifique o resumo dos dados exibido no console após a execução

## Contribuições

Sinta-se à vontade para fazer fork e melhorar o projeto!
