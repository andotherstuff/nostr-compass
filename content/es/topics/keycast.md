---
title: "Keycast: Firma remota de Nostr para equipos"
date: 2026-05-21
draft: false
translationOf: /en/topics/keycast.md
translationDate: 2026-07-01
categories:
  - Signing
  - Security
  - Teams
---

Keycast es un servidor autoalojado de firma remota NIP-46 diseñado para equipos. Almacena las claves privadas de Nostr cifradas en reposo en SQLite, genera cadenas de conexión bunker NIP-46 y ejecuta procesos firmantes que aprueban o rechazan solicitudes de firma remota según políticas configurables por clave. El proyecto es mantenido por la organización Marmot Protocol.

## Cómo funciona

El servidor tiene cuatro componentes principales: una API Axum que gestiona la administración de equipos y la autenticación HTTP NIP-98, un frontend web SvelteKit que usa NIP-07 para autenticación, un gestor de firmantes que observa filas de autorización y genera un `signer_daemon` por autorización, y una base de datos SQLite con migraciones.

Los miembros del equipo inician sesión a través de su extensión de navegador NIP-07. La aplicación web solicita un evento de autenticación HTTP NIP-98 firmado localmente por la extensión, luego envía ese encabezado de autenticación a la API. La API verifica el evento, extrae la pubkey y comprueba la pertenencia al equipo. Las claves almacenadas se cifran con un archivo raíz `master.key` que debe montarse por separado de la imagen y nunca debe confirmarse en el repositorio.

El daemon firmante descifra la clave almacenada y la clave del bunker al inicio, se conecta a los relays configurados y llama a `Authorization::validate_policy` antes de aprobar cada solicitud de firma NIP-46. Las políticas especifican qué kinds de evento puede firmar una conexión bunker particular.

## Auditoría de seguridad (mayo 2026)

Una auditoría de seguridad completada en mayo de 2026 abordó problemas de autenticación, permisos, integridad de datos y dependencias. Cambios clave:

- La autenticación NIP-98 ahora requiere exactamente un tag `u` y un tag `method`, rechaza timestamps obsoletos o futuros, y valida hashes `payload` del cuerpo de la solicitud
- `ALLOWED_PUBKEYS` se analiza de forma exacta y se aplica del lado del servidor; el frontend expone `/api/config?pubkey=<hex>` para que el navegador pueda comprobar el estado de la lista de permitidos sin recibir la lista completa del servidor
- Las políticas vacías rechazan por defecto las solicitudes sign/encrypt/decrypt; la creación de políticas rechaza configuraciones de permisos desconocidas o mal formadas
- Las conexiones SQLite habilitan la aplicación de claves foráneas; la eliminación de equipos ya no pierde datos de join de permisos antes de la limpieza
- La protección de rutas del lado del servidor ahora cubre rutas de aplicación anidadas como `/teams/:id`
- Las respuestas web establecen encabezados CSP, frame, content-type, referrer, permissions y HSTS
- Una migración SQL normaliza al inicio el JSON de permisos antiguo de allowed-kinds desde `{"sign":[...]}` a `{"allowed_kinds":[...]}`

La auditoría anota los elementos residuales en [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) antes de confiar el despliegue con claves reales del equipo.

## Despliegue

El despliegue con Docker Compose monta `master.key` en los contenedores de API y firmante, ejecuta los contenedores con un UID/GID no root con un sistema de archivos raíz de solo lectura, y usa etiquetas de Caddy para enrutar `/api/*` a la API y todo lo demás a la aplicación web. La imagen publicada en `ghcr.io/marmot-protocol/keycast` se etiqueta con `master`, `latest` y `sha-<commit>`.

---

**Fuentes primarias:**
- [Repositorio de Keycast](https://github.com/marmot-protocol/keycast)
- [AUDIT.md](https://github.com/marmot-protocol/keycast/blob/master/AUDIT.md) - Resultados de la auditoría de seguridad de mayo 2026

**Mencionado en:**
- [Boletín #23: Auditoría de seguridad de Keycast completada](/es/newsletters/2026-05-21-newsletter/#keycast-security-audit-complete)

**Véase también:**
- [NIP-46: Firma remota de Nostr](/es/topics/nip-46/)
- [NIP-07: Firmante de extensión de navegador](/es/topics/nip-07/)
- [Marmot Protocol](/es/topics/marmot/)
