# Consumidor de API CoinGecko

Este projeto é um script Python que consome a API do CoinGecko para obter dados de criptomoedas, processa esses dados e os salva em formato CSV.

## Funcionalidades

- Obtém dados de criptomoedas da API CoinGecko
- Salva os dados em arquivo CSV com timestamp
- Exibe resumo dos dados coletados
- Tratamento de erros robusto
- Configurações personalizáveis

## Requisitos

- Python 3.x
- requests
- pandas

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_SEU_REPOSITORIO]
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Execute o script principal:
```bash
python consumir_api.py
```

## Configurações

O script permite configurar:
- Moeda de referência (padrão: USD)
- Limite de criptomoedas (padrão: 100)

## Licença

Este projeto está sob a licença MIT. 