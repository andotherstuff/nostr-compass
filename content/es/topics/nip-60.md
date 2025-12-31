---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2025-12-31
draft: false
categories:
  - Cartera
  - Ecash
---

NIP-60 define cómo operan las carteras de ecash basadas en Cashu dentro de Nostr. La información de la cartera se almacena en relays, permitiendo carteras portátiles que funcionan en diferentes aplicaciones sin requerir cuentas separadas.

## Cómo Funciona

NIP-60 utiliza tres tipos de eventos almacenados en relays:

**Evento de Cartera (kind 17375):** Un evento reemplazable que contiene la configuración cifrada de la cartera, incluyendo URLs de mint y una clave privada para recibir pagos. Esta clave es separada de la clave de identidad de Nostr del usuario.

**Eventos de Token (kind 7375):** Almacenan pruebas de Cashu no gastadas y cifradas. Cuando se gastan las pruebas, el cliente elimina el evento antiguo y crea uno nuevo con las pruebas restantes.

**Historial de Gastos (kind 7376):** Registros opcionales de transacciones que muestran movimientos de fondos, con contenido cifrado y referencias a eventos de tokens creados/destruidos.

## Características Principales

- **Facilidad de uso** - Los nuevos usuarios pueden recibir ecash inmediatamente sin configuración de cuenta externa
- **Interoperabilidad** - Los datos de la cartera siguen a los usuarios a través de diferentes aplicaciones de Nostr
- **Privacidad** - Todos los datos de la cartera están cifrados con las claves del usuario
- **Gestión de pruebas** - Rastrea qué eventos de token fueron gastados para prevenir el doble gasto

## Flujo de Trabajo

1. El cliente obtiene la configuración de la cartera desde los relays
2. Los eventos de token se cargan y descifran para obtener los fondos disponibles
3. Gastar crea nuevos eventos de token y elimina los antiguos
4. Los eventos de historial opcionales registran transacciones para referencia del usuario

---

**Fuentes primarias:**
- [Especificación NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mencionado en:**
- [Boletín #3: Resumen de Diciembre](/es/newsletters/2025-12-31-newsletter/#december-recap-five-years-of-nostr-decembers)

**Ver también:**
- [NIP-57: Zaps](/es/topics/nip-57/)
- [NIP-47: Nostr Wallet Connect](/es/topics/nip-47/)
