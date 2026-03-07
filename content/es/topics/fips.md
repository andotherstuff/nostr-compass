---
title: "FIPS"
date: 2026-02-25
translationOf: /en/topics/fips.md
translationDate: 2026-03-07
draft: false
categories:
  - Protocol
  - Networking
  - Infrastructure
---

FIPS (Free Internetworking Peering System) es un protocolo de red mesh auto-organizado que usa pares de claves secp256k1 al estilo Nostr como identidades de nodo.

## Cómo Funciona

FIPS busca hacer que la red entre pares funcione sin servidores centrales ni autoridades de certificados. Los nodos descubren vecinos, construyen estado de enrutamiento y reenvían paquetes usando solo conocimiento local.

El diseño combina un árbol de expansión con datos de alcanzabilidad basados en filtros bloom. Cada nodo obtiene coordenadas relativas al árbol, y luego enruta de forma voraz hacia el destino. Si el enrutamiento voraz falla, el árbol aún proporciona una ruta de respaldo.

Dos capas de cifrado protegen el tráfico. El cifrado de capa de enlace (patrón Noise IK) asegura la comunicación salto a salto entre vecinos. El cifrado de capa de sesión (patrón Noise XK) proporciona protección de extremo a extremo contra enrutadores intermedios.

## Por Qué Es Importante

FIPS reutiliza el mismo modelo de claves que los desarrolladores de Nostr ya entienden, pero lo aplica al enrutamiento de paquetes en lugar de eventos sociales. Eso le da una historia de identidad simple: la identidad de red es la clave criptográfica, no una asignación IP o cadena de certificados.

El diseño agnóstico de transporte también es importante. El mismo modelo de enrutamiento e identidad puede, en principio, ejecutarse sobre UDP, Ethernet, Bluetooth o LoRa, lo que hace a FIPS interesante para entornos de red hostiles o poco fiables.

## Estado de Implementación

Según lo cubierto en Compass, la implementación actual en Rust ya incluye transporte UDP funcional y descubrimiento basado en filtros bloom. El bootstrapping basado en relays es trabajo futuro, por lo que hoy el protocolo es más un sustrato de red que un reemplazo terminado de relay Nostr.

---

**Fuentes primarias:**
- [Repositorio de FIPS](https://github.com/jmcorgan/fips)
- [Documentación de diseño](https://github.com/jmcorgan/fips/blob/master/docs/design/fips-intro.md)

**Mencionado en:**
- [Boletín #11: Noticias de FIPS](/es/newsletters/2026-02-25-newsletter/#fips-nostr-native-mesh-networking)
- [Boletín #12](/es/newsletters/2026-03-04-newsletter/)

**Ver también:**
- [Protocolo Marmot](/es/topics/marmot/)
