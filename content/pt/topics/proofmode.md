---
title: "ProofMode"
date: 2026-07-15
translationOf: /en/topics/proofmode.md
translationDate: 2026-07-15
draft: false
categories:
  - Media
  - Provenance
---

[ProofMode](https://proofmode.org/) é um kit de ferramentas de proveniência de mídia de código aberto, construído pelo Guardian Project, WITNESS e Okthanks, que anexa dados verificáveis de autenticidade e cadeia de custódia a fotos e vídeos no momento da captura. Não é específico do Nostr; clientes Nostr que carregam dados ProofMode estão integrando um padrão externo existente em vez de uma nova camada de protocolo.

## Como funciona

O componente Capture do ProofMode incorpora metadados de proveniência diretamente nos arquivos de mídia durante a captura, suportando os mesmos padrões interoperáveis utilizados pela Content Authenticity Initiative (CAI), Content Credentials (CR) e C2PA. Um componente Verify separado inspeciona arquivos de áudio, imagem e vídeo para verificar nesses metadados sinais de geração por IA ou edição posterior, e um componente Preserve lida com o armazenamento redundante e descentralizado dos dados de prova subjacentes para arquivamento de longo prazo. Um SDK Develop permite que aplicativos integrem captura e verificação sem construir o formato de proveniência por conta própria.

## Por que importa

Para um cliente Nostr de vídeo ou imagem, carregar dados ProofMode significa que um visualizador tem uma forma externa e multiplataforma de verificar se uma peça de mídia foi capturada conforme declarado e não foi alterada silenciosamente desde então, sem depender do cliente de publicação ou relay como fonte de confiança. Essa distinção importa mais para uma cópia baixada ou recodificada de um clipe: dados de proveniência que sobrevivem ao download e a qualquer marca d'água que um cliente aplique são o que torna a atestação ainda verificável depois que o arquivo deixa o aplicativo que o produziu.

## Implementações

- [Divine](https://github.com/divinevideo/divine-mobile) - cliente Nostr de vídeos curtos; carrega dados de proveniência ProofMode através de downloads de clipes com marca d'água

---

**Fontes primárias:**
- [ProofMode](https://proofmode.org/)

**Mencionado em:**
- [Newsletter #17](/pt/newsletters/2026-04-29-newsletter/)
- [Newsletter #31: Divine Mobile 1.0.16 traz um editor de vídeo mais profundo, criptografia em repouso e proveniência ProofMode](/pt/newsletters/2026-07-15-newsletter/#divine-mobile-1016-ships-a-deeper-video-editor-at-rest-encryption-and-proofmode-provenance)

**Veja também:**
- [Blossom](/pt/topics/blossom/)
