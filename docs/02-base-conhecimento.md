# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Informações Cruciais extraídas para o Escopo | Como a Jan Metas vai usar isso? (Utilização no Agente) |
| :--- | :--- | :--- | :--- |
| `perfil_investidor.json` | JSON | Metas ativas, prazos, renda mensal (`R$ 5.000,00`), perfil moderado e reserva atual (`R$ 10.000,00`). | **Core do Planejamento:** Identificar o teto de gastos, calcular a distância matemática para atingir as metas (Reserva e Apartamento) e filtrar produtos adequados. |
| `transacoes.csv` | CSV | Registro detalhado de entradas e saídas categorizadas (moradia, alimentação, transporte, saúde, lazer). | **Motor de Alertas:** Somar os gastos mensais por categoria, projetar a capacidade de poupança no mês atual e emitir alertas se o usuário estourar o limite saudável de despesas. |
| `historico_atendimento.csv` | CSV | Registro cronológico das últimas dúvidas resolvidas do cliente sobre investimentos e acompanhamento de metas. | **Contextualização e Memória:** Evitar respostas repetitivas, sabendo exatamente que o cliente já compreendeu o básico de CDB/Tesouro e que já vinha acompanhando sua reserva. |
| `produtos_financeiros.json` | JSON | Catálogo de produtos com foco em liquidez, rendimento (CDI/Selic), aportes mínimos e perfis de risco. | **Tomada de Decisão:** Casar o dinheiro que sobra das `transacoes.csv` com produtos de risco baixo/médio que acelerem as metas do `perfil_investidor.json`. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os arquivos originais foram modificados e expandidos para criar um ecossistema de dados 100% conectado com o problema do João Silva. Foram aplicadas as seguintes melhorias técnicas:

1. **Sincronismo Financeiro Real (`transacoes.csv`):** As saídas foram totalizadas em exatamente `R$ 2.488,90`. Com a entrada de `R$ 5.000,00`, calculamos dinamicamente que restou um saldo positivo exato de `R$ 2.511,10` em Outubro de 2025 para aportes na meta.
2. **Histórico Enriquecido (`historico_atendimento.csv`):** Adicionamos uma nova linha de interação datada de `2025-10-12` focada estritamente em "Metas financeiras", onde o cliente validou o progresso da reserva. Isso dá gancho direto para a assistente dar continuidade ao assunto.
3. **Segurança de Dados:** Omitimos dados sensíveis como números de conta, CPF ou chaves bancárias, operando estritamente com dados de comportamento financeiro estruturado.
---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

A arquitetura do agente utiliza uma estratégia híbrida de carregamento para otimização de tokens de contexto:

- No início da sessão, os scripts do backend (fs.readFile) realizam o parse dos arquivos .json e .csv.
- Os dados brutos passam por um método de agregação e limpeza que calcula os somatórios de gastos e o status atual das metas.
- Essas informações consolidadas são instanciadas em variáveis de ambiente do código e injetadas dinamicamente como strings estruturadas dentro do bloco de referências do prompt que será enviado à LLM.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

As variáveis são injetadas de forma dinâmica no system prompt delimitadas por tags estruturadas. Isso cria uma barreira rígida que impede a IA de inventar saldos ou mentir sobre o catálogo de produtos disponíveis.

```javascript
// Exemplo de como o backend monta a chamada para a API da LLM
const systemPrompt = `
Você é a Jan Metas, uma assistente virtual de finanças com perfil amigável, motivador e focado em metas. 
Sua principal diretriz é a fidelidade absoluta aos dados fornecidos. Não alucine e não invente dados fora do contexto de referência. Se não souber baseado nos dados, diga que não tem acesso a essa informação.

<CONTEXTO_REFERENCIA>
DADOS DO CLIENTE:
- Nome: \${perfil.nome}
- Perfil: \${perfil.perfil_investidor}
- Objetivo Principal: \${perfil.objetivo_principal}
- Reserva Atual: R$ \${perfil.reserva_emergencia_atual} (Meta: R$ \${perfil.metas[0].valor_necessario})

RESUMO DE GASTOS (Processado a partir do transacoes.csv):
- Moradia: R$ \${gastosPorCategoria.moradia}
- Alimentação: R$ \${gastosPorCategoria.alimentacao}
- Transporte: R$ \${gastosPorCategoria.transporte}
- Saúde: R$ \${gastosPorCategoria.saude}
- Lazer: R$ \${gastosPorCategoria.lazer}
- Total de saídas: R$ \${totalSaidas}
- Saldo Disponível para Aporte no Mês: R$ \${rendaMensal - totalSaidas}

PRODUTOS DISPONÍVEIS PARA RECOMENDAÇÃO:
\${produtos.map(p => `- \${p.nome} (Categoria: \${p.categoria}, Risco: \${p.risco}, Indicado para: \${p.indicado_para})`).join('\n')}
</CONTEXTO_REFERENCIA>

Responda à dúvida do usuário de forma assertiva utilizando as regras acima.
`;
```

---

## Exemplo de Contexto Montado

Aqui está a representação exata de como a estrutura limpa e processada se materializa para o cérebro da Jan Metas ao iniciar o diálogo com o cliente fictício:

DADOS DO CLIENTE:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Construir reserva de emergência
- Reserva atual: R$ 10.000,00 (meta: R$ 15.000,00 - Prazo: 2026-06)

RESUMO DE GASTOS:
- Moradia: R$ 1.380,00
- Alimentação: R$ 570,00
- Transporte: R$ 295,00
- Saúde: R$ 188,00
- Lazer: R$ 55,90
- Total de saídas: R$ 2.488,90
- Saldo Livre Calculado: R$ 2.511,10

PRODUTOS DISPONÍVEIS PARA EXPLICAR:
- Tesouro Selic (risco baixo - Indicado para: Reserva de emergência e iniciantes)
- CDB Liquidez Diária (risco baixo - Indicado para: Quem busca segurança com rendimento diário)
- LCI/LCA (risco baixo - Indicado para: Quem pode esperar 90 dias (isento de IR))
- Fundo Multimercado (risco médio - Indicado para: Perfil moderado que busca diversificação)
- Fundo de Ações (risco alto - Indicado para: Perfil arrojado com foco no longo prazo)

