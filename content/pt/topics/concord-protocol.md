---
title: "Concord Protocol"
date: 2026-07-15
draft: false
translationOf: /en/topics/concord-protocol.md
translationDate: 2026-07-15
categories:
  - Protocol
  - Messaging
---

Concord é um protocolo aberto com licença MIT para comunidades e canais criptografados de ponta a ponta sobre Nostr, definido pelas [especificações CORD-01 a CORD-07](https://github.com/concord-protocol/concord). [Vector](https://github.com/VectorPrivacy/Vector) o adotou como transporte padrão para sua funcionalidade de Chats em Grupo a partir da v0.4.0, chamando-o de "nosso protocolo de mensagens personalizado" em suas próprias notas de lançamento, mas a especificação é publicada separadamente do Vector e já tem implementações independentes.

## Como funciona

Concord divide o que um servidor de comunidade estilo Discord normalmente faz em peças que não precisam confiar em ninguém: relay apenas armazenam blobs criptografados endereçados a labels rotativos, possuir a chave de uma sala é o que torna alguém membro, e a autoridade sobre papéis, expulsões e banimentos é um registro assinado enraizado na identidade do proprietário que cada cliente verifica localmente em vez de confiar em um servidor para aplicá-lo. Cada evento durável viaja no mesmo envelope de três camadas: um wrapper kind 1059 assinado pela chave de stream derivada do plano, contendo um selo assinado pela chave real do autor, contendo um rumor sem assinatura que carrega o evento funcional. Um rumor de mensagem de chat é um evento kind 9 simples:

```json
{
  "kind": 9,
  "pubkey": "<author>",
  "content": "Hey chat!",
  "tags": [
    ["channel", "<channel_id>"],
    ["epoch", "0"]
  ]
}
```

O tráfego de controle, chat e livro de visitas cada um recebe seu próprio plano envolvido com gift-wrap [NIP-59](/pt/topics/nip-59/), de modo que um relay que hospeda todos os três ainda não consegue distinguir uma mensagem de controle de uma mensagem de chat de uma entrada de livro de visitas sem a chave da sala. A especificação é dividida em sete documentos CORD: streams privados (01), comunidades e membros (02), canais (03), papéis (04), convites (05), recriptografia e refundação para cortar acesso de membros removidos (06), e áudio/vídeo via um intermediário de tokens cegos (07). A membresia em si não tem lista do lado do servidor: quem consegue descriptografar o plano é membro, e remover alguém de verdade significa rotacionar a comunidade para uma nova época de chave e entregá-la apenas a quem permanece, em vez de deletar uma linha de uma tabela.

## Diferenças em relação ao Marmot

Concord e [Marmot](/pt/topics/marmot/) resolvem mensagens em grupo criptografadas sobre Nostr com criptografia diferente para formas de grupo diferentes, e a própria comparação do projeto Concord é explícita sobre a divisão: Marmot superpõe [MLS](/pt/topics/mls/) sobre Nostr para sigilo futuro e segurança pós-compromisso, usando pacotes de chaves por dispositivo e commits ordenados que avançam todo o grupo em sincronia. Isso compra garantias fortes, a um custo que escala com mudanças de membresia, bem adequado a grupos pequenos e de alto risco onde entradas e saídas são raras. Concord em vez disso dá a cada membro a mesma chave de sala e recriptografa toda a sala na remoção em vez de avançar por commit, trocando algumas das garantias criptográficas do MLS por um modelo que permanece econômico à medida que uma comunidade cresce para centenas ou milhares de membros casuais e de alta rotatividade, a forma que comunidades estilo Discord realmente tomam.

## Por que o Vector mudou

As próprias [notas de lançamento do Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) descrevem Concord apenas como "nosso protocolo de mensagens personalizado" para Chats em Grupo, sem expor o raciocínio diretamente. O encaixe com a justificativa publicada do Concord é claro de qualquer forma: Chats em Grupo em um cliente como o Vector são exatamente o caso de membresia grande, aberta e frequentemente mutável onde o estado MLS por dispositivo do Marmot se torna o caminho mais caro, e o design assíncrono e dobrável do Concord é construído para esse caso. [Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0) aposentou Marmot para Chats em Grupo em favor de Concord, e o histórico existente de grupos Marmot não foi transferido na mudança. [v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1) lançou "Concord v2" quatro dias depois com melhorias de privacidade e estabilidade. Na mesma semana, [Amethyst fez merge da sua própria implementação limpa e compatível a nível de protocolo](https://github.com/vitorpamplona/amethyst/pull/3566), e o cliente estilo Discord da Soapbox, [Armada](https://gitlab.com/soapbox-pub/armada), já constrói sua funcionalidade de Comunidades sobre a mesma especificação como implementação de referência. Três clientes independentes convergindo em uma especificação aberta em dias é um caminho rápido para interoperabilidade real entre clientes, vale rastrear contra quantos dos demais clientes de chat em grupo do Nostr permanecem no Marmot.

## Implementações

- [Vector](https://github.com/VectorPrivacy/Vector) - mensageiro Nostr de binário único focado em privacidade; primeiro cliente Concord em produção, na v0.4.0
- [Armada](https://gitlab.com/soapbox-pub/armada) (Soapbox) - cliente de comunidade estilo Discord; implementação de referência, backend no repositório separado `armada-relay`
- [Amethyst](https://github.com/vitorpamplona/amethyst) - cliente Nostr rico em funcionalidades para Android e multiplataforma; reimplementação de sala limpa compatível a nível de protocolo com Armada ([PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566))

---

**Fontes primárias:**
- [Especificações do protocolo Concord (CORD-01 a CORD-07)](https://github.com/concord-protocol/concord)
- [Notas de lançamento do Vector v0.4.0](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.0)
- [Notas de lançamento do Vector v0.4.1](https://github.com/VectorPrivacy/Vector/releases/tag/v0.4.1)
- [Amethyst PR #3566](https://github.com/vitorpamplona/amethyst/pull/3566)

**Mencionado em:**
- [Newsletter #31: Vector v0.4.0 move os Chats em Grupo de Marmot para Concord, e Amethyst lança seu próprio cliente Concord dias depois](/pt/newsletters/2026-07-15-newsletter/#vector-v040-moves-group-chats-from-marmot-to-concord-and-amethyst-ships-its-own-concord-client-days-later)
- [Newsletter #31: Amethyst lança uma implementação limpa de Concord para comunidades criptografadas de ponta a ponta](/pt/newsletters/2026-07-15-newsletter/#amethyst-ships-a-clean-room-concord-implementation-for-end-to-end-encrypted-communities)

**Veja também:**
- [Marmot Protocol](/pt/topics/marmot/)
- [MLS (Message Layer Security)](/pt/topics/mls/)
- [NIP-46: Nostr Connect](/pt/topics/nip-46/)
