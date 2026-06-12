# Passo a Passo de Execução

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.ai)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run gpt-oss "Olá!"
...
```

## Código Completo

Todo o código-fonte está no arquivo `app.py`.

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
python -m streamlit run .\src\app.py
```

## Evidencias da execução

<img width="1890" height="890" alt="image" src="https://github.com/user-attachments/assets/31f708fa-8c17-4693-b3b9-1867d70059bb" />
<img width="1893" height="1016" alt="image" src="https://github.com/user-attachments/assets/b2fae41e-897c-4282-95c7-e1f3b377f3b8" />
<img width="1896" height="897" alt="image" src="https://github.com/user-attachments/assets/3c81e28d-14bd-4295-acee-e1ef72923471" />
<img width="1898" height="1021" alt="image" src="https://github.com/user-attachments/assets/23c3ed7f-8640-4412-ad33-25dfc2fbf6f5" />
