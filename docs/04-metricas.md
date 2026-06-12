# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:**
- Olá, João!
Analisando suas transações recentes, você gastou **R 570,00** com alimentação este mês (R 450,00 no supermercado + R$ 120,00 no restaurante). Se precisar de ajuda para otimizar esse gasto ou direcionar parte desses recursos para a sua reserva de emergência, estou à disposição! `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:**
- Olá João!
Com base no seu objetivo de construir uma reserva de emergência e considerando o perfil moderado, o Tesouro Selic é a melhor opção disponível:
- Baixo risco (igual ao da caderneta de poupança, porém com rentabilidade maior) - Liquidez diária, permitindo resgate a qualquer momento – perfeito para emergências - Aporte mínimo de R$ 30,00, compatível com o seu orçamento atual
Se quiser diversificar um pouco mais dentro da mesma faixa de risco, você também pode considerar o CDB Líquida Diária (aproveita a rentabilidade diária e é igualmente seguro), mas o Tesouro Selic já atende muito bem à sua meta.
Qualquer dúvida sobre como abrir a aplicação ou quanto aportar, estou aqui para ajudar!


- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Olá João! Desculpe, não tenho acesso a informações sobre previsão do tempo em meus dados de referência. Posso ajudar com qualquer dúvida relacionada às suas finanças, metas ou investimentos que estejam dentro do escopo da minha atuação. Como posso auxiliá-lo hoje?
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Desculpe, João, mas eu não tenho informações sobre o produto XYZ em nossa base de dados atual. Se precisar saber mais sobre os produtos que temos disponíveis, ficarei feliz em ajudar!
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- A assistente funcionou super bem, inclusive respondendo de forma assertiva a cenários que eu não esperava que ela cobrisse. Demonstrou ótima retenção de escopo, reagiu muito bem às perguntas e transmitiu total segurança durante toda a interação.
**O que pode melhorar:**
- Como próximos passos para otimização do projeto, planejo expandir a base de dados de referência e realizar uma engenharia de prompt mais enxuta (prompt trimming). Essa abordagem visa reduzir a latência e o consumo de tokens na API local do Ollama, garantindo um tempo de resposta menor para o usuário final sem degradar a qualidade do modelo.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência: Longa (devido à execução em hardware local), porém com entregas altamente satisfatórias no conteúdo.
- Tokens/Custos: Altos por requisição; necessita de refatoração do prompt para otimizar o desempenho do modelo.
- Erros/Logs: Mínimos e previsíveis, manifestando-se apenas nas validações de segurança e fora de escopo.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
