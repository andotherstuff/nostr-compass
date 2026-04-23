---
title: "NIP-60: Cashu Wallet"
date: 2025-12-31
translationOf: /en/topics/nip-60.md
translationDate: 2026-04-22
draft: false
categories:
  - Wallet
  - Ecash
---

NIP-60 define cómo operan las carteras de ecash basadas en Cashu dentro de Nostr. La información de la cartera se almacena en relays, lo que permite carteras portátiles que funcionan en diferentes aplicaciones sin requerir cuentas separadas.

## Cómo funciona

NIP-60 usa tres tipos de eventos principales almacenados en relays, más un evento auxiliar opcional para cotizaciones pendientes:

**Evento de cartera (kind 17375):** Un evento reemplazable que contiene la configuración cifrada de la cartera, incluyendo URLs de mint y una clave privada para recibir pagos. Esta clave es separada de la clave de identidad de Nostr del usuario.

**Eventos de token (kind 7375):** Almacenan pruebas de Cashu no gastadas y cifradas. Cuando las pruebas se gastan, el cliente elimina el evento antiguo y crea uno nuevo con las pruebas restantes.

**Historial de gastos (kind 7376):** Registros opcionales de transacciones que muestran movimientos de fondos, con contenido cifrado y referencias a eventos de token creados/destruidos.

**Eventos de cotización (kind 7374):** Estado cifrado opcional para cotizaciones de mint pendientes. La especificación recomienda eventos de corta vida con etiquetas de expiración, principalmente para casos donde el estado local no es suficiente.

## Modelo de estado

NIP-60 trata de la sincronización del estado de la cartera, no del acto de recibir dinero. El evento de cartera indica a un cliente qué mints y clave de cartera usar, mientras que los eventos de token son el estado de balance real porque contienen las pruebas no gastadas.

Esa distinción importa para la interoperabilidad. Dos clientes pueden mostrar la misma cartera solo si interpretan la rotación de tokens de la misma manera: gastar pruebas, publicar pruebas de reemplazo y eliminar el evento de token gastado a través de [NIP-09](/es/topics/nip-09/) para que otros clientes no sigan contando las pruebas gastadas como balance.

## Por qué importa

- **Facilidad de uso** - Los nuevos usuarios pueden recibir ecash inmediatamente sin configuración de cuenta externa
- **Interoperabilidad** - Los datos de la cartera siguen a los usuarios a través de diferentes aplicaciones de Nostr
- **Privacidad** - Todos los datos de la cartera están cifrados con las claves del usuario
- **Gestión de pruebas** - Rastrea las transiciones de estado de la cartera para que los clientes converjan en el mismo balance

## Notas de interoperabilidad

Los clientes primero buscan información de relay de cartera a través de kind 10019 y recurren a la lista de relays [NIP-65](/es/topics/nip-65/) del usuario si no hay una lista dedicada de relay de cartera. Ese fallback es útil, pero también significa que la portabilidad de la cartera depende de que los relays almacenen y sirvan los eventos de cartera cifrados.

La especificación también requiere que la clave privada de la cartera se mantenga separada de la clave de identidad de Nostr del usuario. Eso mantiene el manejo de recibos de la cartera aislado de la clave de firma principal y reduce la posibilidad de que una clave se reutilice para dos propósitos diferentes.

## Flujo de trabajo

1. El cliente obtiene la configuración de la cartera desde relays de cartera o la lista de relays del usuario
2. Los eventos de token se cargan y descifran para obtener los fondos disponibles
3. Gastar crea nuevos eventos de token y elimina los antiguos
4. Los eventos de historial opcionales registran transacciones para referencia del usuario

---

**Fuentes primarias:**
- [Especificación NIP-60](https://github.com/nostr-protocol/nips/blob/master/60.md)

**Mencionado en:**
- [Boletín #3: Resumen de diciembre](/es/newsletters/2025-12-31-newsletter/)
- [Boletín #9: NIP Deep Dive](/es/newsletters/2026-02-25-newsletter/)
- [Boletín #13: Shopstr y Milk Market](/en/newsletters/2026-03-11-newsletter/)

**Ver también:**
- [NIP-57: Zaps](/es/topics/nip-57/)
- [NIP-09: Solicitud de eliminación de eventos](/es/topics/nip-09/)
- [NIP-47: Nostr Wallet Connect](/es/topics/nip-47/)
