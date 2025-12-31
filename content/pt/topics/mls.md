---
title: "MLS (Message Layer Security)"
date: 2025-12-31
translationOf: /en/topics/mls.md
translationDate: 2025-12-31
draft: false
categories:
  - Criptografia
  - Protocolo
  - Mensagens
  - Privacidade
---

Message Layer Security (MLS) é um protocolo padronizado pelo IETF para mensagens em grupo com criptografia de ponta a ponta. Ele fornece estabelecimento eficiente de chaves com sigilo futuro e segurança pós-comprometimento para grupos que variam de dois a milhares de participantes.

## Como funciona

MLS usa uma estrutura de acordo de chaves baseada em árvore chamada TreeKEM:

1. **Pacotes de chaves**: Cada participante publica um pacote de chaves contendo sua identidade e chaves de criptografia
2. **Estado do grupo**: Uma árvore ratchet mantém o estado criptográfico do grupo
3. **Commits**: Os membros atualizam a árvore ao entrar, sair ou rotacionar chaves
4. **Criptografia de mensagens**: O conteúdo é criptografado usando chaves derivadas do segredo compartilhado do grupo

## Propriedades de segurança principais

- **Sigilo futuro**: Mensagens passadas permanecem seguras mesmo se as chaves atuais forem comprometidas
- **Segurança pós-comprometimento**: Mensagens futuras voltam a ser seguras após a rotação de chaves
- **Autenticação de membros**: Todos os membros do grupo são verificados criptograficamente
- **Operação assíncrona**: Membros podem entrar/sair sem que todos os participantes estejam online
- **Escalabilidade**: Eficiente para grupos de até 50.000 participantes

## Padronização

- **RFC 9420** (julho 2023): Especificação do protocolo MLS central
- **RFC 9750** (abril 2025): Arquitetura MLS para integração de sistemas

## Adoção no Nostr

Várias aplicações Nostr usam MLS para mensagens em grupo seguras:

- **KeyChat**: Aplicativo de mensagens criptografadas baseado em MLS para celular e desktop
- **White Noise**: Mensagens privadas usando MLS com integração do protocolo Marmot
- **Marmot Protocol**: Extensão do Nostr que fornece criptografia de grupo baseada em MLS

MLS oferece garantias de segurança mais fortes do que NIP-04 ou NIP-44 sozinhos, particularmente para chats em grupo onde os membros entram e saem dinamicamente.

## Adoção na indústria

Além do Nostr, MLS está sendo adotado por:
- Google Messages (RCS com MLS via GSMA Universal Profile 3.0)
- Apple Messages (suporte RCS anunciado para MLS)
- Cisco WebEx, Wickr, Matrix

---

**Fontes principais:**
- [RFC 9420: MLS Protocol](https://datatracker.ietf.org/doc/rfc9420/)
- [RFC 9750: MLS Architecture](https://datatracker.ietf.org/doc/rfc9750/)
- [IETF MLS Working Group](https://datatracker.ietf.org/wg/mls/about/)
- [MLS Protocol Website](https://messaginglayersecurity.rocks/)

**Mencionado em:**
- [Newsletter #3: Lançamentos](/pt/newsletters/2025-12-31-newsletter/#releases)

**Veja também:**
- [Marmot Protocol](/pt/topics/marmot/)
- [MIP-05: Notificações Push com Preservação de Privacidade](/pt/topics/mip-05/)
- [NIP-17: Mensagens Diretas Privadas](/pt/topics/nip-17/)
- [NIP-44: Cargas Úteis Criptografadas](/pt/topics/nip-44/)
