---
title: "Bitcredit"
date: 2026-03-25
translationOf: /en/topics/bitcredit.md
translationDate: 2026-04-01
draft: false
categories:
  - Finance
  - Commerce
  - Infrastructure
---

Bitcredit es un sistema de financiación comercial con letras de cambio electrónicas para empresas. El sitio público presenta Bitcredit Core como software para emitir, endosar, pagar y gestionar letras de cambio electrónicas, mientras que el repositorio open-source del núcleo implementa una capa de transporte Nostr junto con la lógica de negocio y los crates de persistencia.

## Cómo Funciona

Bitcredit modela el crédito comercial como letras de cambio electrónicas, o ebills. Un comprador emite una ebill con una fecha de vencimiento futura, el tenedor puede endosarla a otra empresa, y el tenedor final puede solicitar el pago al vencimiento.

El sitio de Bitcredit también describe una vía de liquidez basada en mint. En lugar de esperar al vencimiento, un tenedor puede solicitar una oferta de un mint de Bitcredit, recibir ecash inmediatamente, y luego usar ese ecash para pagar a proveedores o trabajadores.

## Notas de Implementación

El repositorio `Bitcredit-Core` divide el sistema en múltiples crates Rust. `bcr-ebill-core` maneja el modelo de datos, `bcr-ebill-api` contiene la lógica de negocio, `bcr-ebill-persistence` maneja el almacenamiento, y `bcr-ebill-transport` proporciona la API de transporte de red con una implementación Nostr.

Esa arquitectura importa porque Bitcredit no es solo un sitio web o un flujo de billetera. Es un sistema de documentos comerciales con transporte, estado y lógica de liquidación separados en componentes reutilizables, incluyendo un punto de entrada WASM para despliegues web.

## Trabajo Reciente

Compass cubrió Bitcredit por primera vez en marzo de 2026 cuando `v0.5.3` añadió campos de API para acciones de pago de letras y estado de letras, y corrigió el manejo de direcciones de firma para firmantes anónimos. La siguiente versión, `v0.5.4`, continuó ese trabajo de API adaptando `BitcreditBillResult`, refinando el estado de pago y aceptación, y añadiendo un manejo más explícito para campos opcionales.

Esos cambios son pequeños comparados con el concepto más amplio de Bitcredit, pero muestran hacia dónde se mueve la implementación: mejor ergonomía del frontend, estado del ciclo de vida de letras más claro, y mejor manejo para flujos de firma anónimos o tipo portador.

---

**Fuentes primarias:**
- [Sitio web de Bitcredit](https://www.bit.cr/)
- [Bitcredit: Cómo funciona](https://www.bit.cr/how-it-works)
- [Repositorio Bitcredit-Core](https://github.com/BitcreditProtocol/Bitcredit-Core)
- [Índice de documentación de Bitcredit-Core](https://github.com/BitcreditProtocol/Bitcredit-Core/blob/master/docs/index.md)
- [Bitcredit v0.5.3](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.3)
- [Bitcredit v0.5.4](https://github.com/BitcreditProtocol/Bitcredit-Core/releases/tag/v0.5.4)
- [PR #846: Improve Status Flags and Add Payment Actions](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/846)
- [PR #849: Fix signing address and signatory for anon signers](https://github.com/BitcreditProtocol/Bitcredit-Core/pull/849)

**Mencionado en:**
- [Newsletter #13: Bitcredit v0.5.3](/en/newsletters/2026-03-11-newsletter/#bitcredit-v053)
