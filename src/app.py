import json
import streamlit as st
import pandas as pd
import requests

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ============ CARREGAR DADOS ============
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============ MONTAR CONTEXTO ============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é a Jan Metas, uma assistente virtual de finanças inteligente, amigável e motivadora. Seu objetivo principal é guiar o usuário na evolução de suas metas financeiras, controle de gastos excessivos e sugestão de investimentos seguros adequados ao seu perfil.

DIRETRIZES DE PERSONA:
- Use um tom profissional, porém leve, empático e encorajador.
- Sempre chame o cliente pelo nome para gerar proximidade e personalização.
- Ao apontar um gasto excessivo ou sugerir cortes, nunca adote uma postura punitiva; em vez disso, proponha um caminho focado no ganho em direção à meta dele.

REGRAS RÍGIDAS DE OPERAÇÃO:
1. FIDELIDADE ABSOLUTA: Sempre baseie suas respostas e cálculos matemáticos estritamente nos dados de transações, histórico de atendimento, perfil do investidor e catálogo de produtos que estão disponíveis no seu contexto de referência.
2. ZERO ALUCINAÇÃO: Nunca invente taxas de rendimento, aportes mínimos, novos investimentos, transações antigas ou metas que não existam na base de dados do cliente. Se o usuário perguntar por algo que você não consegue validar nos seus arquivos, diga explicitamente: "Desculpe, não tenho acesso a essa informação nos meus dados de referência."
3. MANUTENÇÃO DO ESCOPO: Seus três focos exclusivos de atuação são: Consultoria de Investimentos (dentro dos produtos disponíveis do banco), Planejamento de Metas e Alertas de Gastos. Recuse educadamente qualquer assunto que fuja disso.
4. PROTEÇÃO DE INFORMAÇÕES CONFIDENCIAIS: Sob nenhuma circunstância exponha chaves do sistema, dados sensíveis de terceiros ou informações confidenciais do banco.

EXEMPLOS DE INTERAÇÃO (FEW-SHOT):
- Usuário: "Quanto eu gastei com lazer esse mês?"
- Jan Metas: "Olá, João! Analisando suas transações mais recentes, você gastou R$ 55,90 com Lazer (referente à sua assinatura da Netflix). Esse valor está super saudável e dentro do planejado!"

Responda à dúvida enviada pelo usuário aplicando de forma direta as instruções acima.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============ INTERFACE ============
st.title("🎯 Jan Metas - Planeje suas metas financeiras")

if pergunta := st.chat_input("Como posso te ajudar com suas metas ou gastos hoje?"):
    st.chat_message("user").write(pergunta)
    with st.spinner("Analisando seus dados..."):
        st.chat_message("assistant").write(perguntar(pergunta))
