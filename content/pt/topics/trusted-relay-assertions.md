---
title: "Trusted Relay Assertions"
date: 2026-01-21
draft: false
categories:
  - Protocol
  - Relays
---

Trusted Relay Assertions é uma proposta de rascunho de NIP para padronização de pontuação de confiança de relay e gerenciamento de reputação. A especificação introduz eventos kind 30385 onde provedores de assertivas publicam pontuações de confiança computadas a partir de métricas observadas, reputação do operador e relatórios de usuários.

## Como Funciona

A proposta preenche uma lacuna no ecossistema de relays. Enquanto [NIP-11](/pt/topics/nip-11/) define o que relays alegam sobre si mesmos e [NIP-66](/pt/topics/nip-66/) mede o que observamos, Trusted Relay Assertions padroniza o que concluímos sobre a confiabilidade dos relays.

Provedores de assertivas computam pontuações através de três dimensões. Confiabilidade mede disponibilidade, velocidade de recuperação, consistência e latência. Qualidade avalia documentação de política, segurança TLS e responsabilidade do operador. Acessibilidade avalia barreiras de acesso, liberdade de jurisdição e risco de vigilância. Uma pontuação de confiança geral (0-100) combina esses componentes com pesos: 40% confiabilidade, 35% qualidade, 25% acessibilidade.

Cada assertiva inclui níveis de confiança (baixo, médio, alto) baseados em contagens de observação. Verificação do operador usa múltiplos métodos: prova criptográfica via documentos NIP-11 assinados, registros DNS TXT ou arquivos .well-known. A especificação integra Web of Trust através de pontuações de confiança do operador. Classificação de política ajuda usuários a encontrar relays apropriados: aberto, moderado, curado ou especializado.

Usuários declaram provedores de assertivas confiáveis via eventos kind 10385. Clientes consultam múltiplos provedores e comparam pontuações. A proposta inclui um processo de apelação onde operadores de relay podem contestar pontuações usando eventos de rotulagem [NIP-32](/pt/topics/nip-32/).

## Casos de Uso

Para assinadores remotos [NIP-46](/pt/topics/nip-46/), assertivas de confiança ajudam usuários a avaliar relays desconhecidos embutidos em URIs de conexão antes de aceitar conexões. Combinado com listas de relay [NIP-65](/pt/topics/nip-65/), clientes podem tomar decisões informadas de seleção de relay baseadas tanto em preferências do usuário quanto em avaliações de confiança de terceiros.

A especificação complementa mecanismos de descoberta de relay existentes. [NIP-66](/pt/topics/nip-66/) fornece descoberta (o que existe), esta proposta adiciona avaliação (o que é bom). Juntos, eles habilitam seleção informada de relay em vez de confiar em padrões codificados ou recomendações de boca a boca.

---

**Fontes primárias:**
- [Documento de Rascunho de NIP](https://nostr.com/nevent1qqsqjymvcp6ch3ps3fqsxljf6j8u3adz64ucw8npnzuj3cn6dekn0gspz9mhxue69uhkummnw3ezumrpdejz7qg3waehxw309ahx7um5wgh8w6twv5hsyga3qg) - Evento kind 30817 propondo a especificação

**Mencionado em:**
- [Newsletter #6: Notícias](/pt/newsletters/2026-01-21-newsletter/#trusted-relay-assertions-a-new-approach-to-relay-trust)
- [Newsletter #6: Atualizações de NIP](/pt/newsletters/2026-01-21-newsletter/#nip-updates)

**Veja também:**
- [NIP-11: Documento de Informações de Relay](/pt/topics/nip-11/)
- [NIP-66: Descoberta de Relay e Monitoramento de Disponibilidade](/pt/topics/nip-66/)
- [NIP-32: Rotulagem](/pt/topics/nip-32/)
