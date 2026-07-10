---
title: "NIP-82: Aplicações de Software"
date: 2026-06-17
draft: false
translationOf: /en/topics/nip-82.md
translationDate: 2026-07-01
categories:
  - Discovery
  - Apps
---

NIP-82 define um evento de aplicação de software para que clientes Nostr possam renderizar aplicações (APKs Android, apps iOS, apps web, binários desktop) como objetos de primeira classe em feeds e superfícies de descoberta. A especificação substitui a abordagem antiga de descrever apps por meio de notas genéricas kind 1 ou recomendações de handler [NIP-89](/pt/topics/nip-89/) por um evento dedicado e estruturado que carrega metadados da aplicação, capturas de tela, links de repositório e identidade do autor.

## Como funciona

Uma aplicação de software NIP-82 é um único evento replaceable endereçado pela pubkey do autor e pela tag `d`. O evento carrega:

- Tags `name`, `description`, `icon`, `image` para exibição
- Tags `repository` e `web` para URLs de código-fonte e página inicial
- Tag `platforms` enumerando os alvos suportados (android, ios, web, linux, macos, windows)
- Tags `download` para cada binário específico de plataforma ou URL web
- Tags `screenshots` carregando URLs das imagens das capturas de tela da aplicação
- Tags de tópico `t` para categorização
- Tag `version` para a versão publicada atual

Um cliente navegando por um feed NIP-82 pode mostrar o card da aplicação, linkar para o repositório canônico e expor as capturas de tela sem precisar recorrer a raspar um post longo do Nostr ou uma loja de apps de terceiros. A pubkey do autor é a fonte da verdade para a aplicação, então um cliente pode verificar se o publicador corresponde à identidade esperada do desenvolvedor antes de promover um link de download.

## Semântica de feed

Eventos NIP-82 são endereçáveis, então cada aplicação tem um evento replaceable canônico por autor. Um desenvolvedor que publica uma nova versão substitui o evento anterior no local, e os assinantes veem a atualização sem gerenciar o histórico de eventos. Clientes que queiram um changelog podem se inscrever no evento endereçável e renderizar as atualizações de versão como atividade na superfície da aplicação.

A especificação se compõe com o [NIP-89](/pt/topics/nip-89/) (Application Handlers): um evento NIP-82 descreve a aplicação como um artefato, enquanto um evento NIP-89 descreve que a aplicação pode manipular kinds de evento específicos. Clientes podem usar um sem o outro, mas o par oferece uma superfície de descoberta (NIP-82) e uma superfície de delegação (NIP-89) que funcionam juntas.

## Implementações

- [Amethyst v1.12.0](https://github.com/vitorpamplona/amethyst/releases/tag/v1.12.0) traz um feed dedicado de aplicações de software NIP-82 com uma tela de detalhes, informações do autor e capturas de tela ([PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036), [PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078), [PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200))

---

**Fontes primárias:**
- [Especificação NIP-82](https://github.com/nostr-protocol/nips/blob/master/82.md)
- [Amethyst PR #3036](https://github.com/vitorpamplona/amethyst/pull/3036) - Adiciona suporte a Aplicações de Software NIP-82 com feed dedicado
- [Amethyst PR #3078](https://github.com/vitorpamplona/amethyst/pull/3078) - Adiciona tela dedicada de detalhes de app de software NIP-82
- [Amethyst PR #3200](https://github.com/vitorpamplona/amethyst/pull/3200) - Melhora a interface de app de software NIP-82 com informações do autor e capturas de tela

**Mencionado em:**
- [Newsletter #27: Amethyst v1.12.0 traz carteiras Cashu, nutzaps, um driver CLINK e auto-recuperação Tor](/pt/newsletters/2026-06-17-newsletter/#amethyst-v1120-ships-cashu-wallets-nutzaps-a-clink-driver-and-tor-self-heal)

**Veja também:**
- [NIP-89: Application Handlers](/pt/topics/nip-89/)
