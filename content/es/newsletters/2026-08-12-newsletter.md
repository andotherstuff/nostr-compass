---
title: "Nostr Compass #35"
date: 2026-08-12
publishDate: 2026-08-12
translationOf: /en/newsletters/2026-08-12-newsletter.md
translationDate: 2026-08-12
draft: false
type: newsletters
description: "Herramientas de identidad poscuántica, mensajería cifrada y firma más robustas, ajustes comunitarios portátiles y trabajo de protocolo en NIPs y Concord."
---

Bienvenidos de nuevo a [Nostr Compass](https://nostrcompass.org), tu guía semanal de Nostr.

**Esta semana:** [nostr-wot-extension](https://github.com/nostr-wot/nostr-wot-extension) añade claves poscuánticas y mensajes protegidos opcionales junto a identidades de Nostr existentes. [Divine](https://github.com/divinevideo/divine-mobile) refuerza el aislamiento de cuentas, la validación de mensajes privados y la confirmación de publicación; [MDK](https://github.com/marmot-protocol/mdk) fortalece la convergencia y recuperación de grupos cifrados; y [Amber](https://github.com/greenart7c3/Amber) hace explícitas las decisiones de firma agrupadas. Las versiones mejoran las conexiones de monedero, el chat cifrado, el descubrimiento social, la sincronización entre dispositivos y la firma remota, mientras que el trabajo de protocolo abarca identidad y comunidades cifradas. Los análisis en profundidad explican las solicitudes de borrado autenticadas y las denuncias descentralizadas.

## Historias Principales

### nostr-wot-extension 0.4.0 añade claves poscuánticas junto a una identidad de Nostr

[nostr-wot-extension 0.4.0](https://github.com/nostr-wot/nostr-wot-extension/releases/tag/v0.4.0) es una extensión de navegador para gestionar identidades de Nostr y firmar. Las cuentas creadas a partir de una semilla de 24 palabras pueden derivar ahora claves de cifrado ML-KEM-1024 y de firma ML-DSA-87 junto a su clave de Nostr existente. Un flujo de un clic publica una atestación de kind `10203` que vincula la pubkey de Nostr con ambas pubkeys poscuánticas e incluye una prueba de posesión ML-DSA. Las cuentas importadas desde un mnemónico de 12 palabras, un `nsec` sin envoltorio, un firmante remoto o una clave de solo lectura no pueden usar el flujo de derivación, y la extensión explica esa limitación en la vista de cuenta.

La versión también añade mensajes directos poscuánticos opcionales. Combina el secreto compartido ML-KEM con la [clave de conversación cifrada de NIP-44](https://github.com/nostr-protocol/nips/blob/master/44.md) existente mediante HKDF, y mantiene las capas normales de gift-wrap de [NIP-59](/es/topics/nip-59/) (envolturas que ocultan metadatos) para la entrega por relay. El cifrado nunca recurre silenciosamente a un camino anterior después de que el destinatario opte por el nuevo, mientras que el descifrado selecciona automáticamente la ruta adecuada. Esto protege la nueva ruta de mensajes frente a una recuperación posterior de una clave privada de Nostr actual, pero no sustituye las firmas de eventos secp256k1; la versión deja explícitamente esa migración mayor para una futura coordinación con relays y clientes.

### Divine Mobile 1.0.19 refuerza cuentas, mensajes privados y publicación

[Divine Mobile 1.0.19](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.19) es un cliente móvil de vídeo corto que publica y recupera vídeos a través de Nostr. Su selector de cuentas construye ahora cada identidad iniciada en torno a un contenedor con alcance de cuenta, y una corrección de publicación evita que un vídeo se envíe bajo la cuenta equivocada. Las rutas de publicación en relay esperan ahora una respuesta `OK` con semántica explícita de éxito, mientras que un frame `CLOSED` del relay puede terminar su propia consulta pendiente en lugar de dejar la petición colgada.

[El manejo de mensajes privados](https://github.com/divinevideo/divine-mobile/pull/6368) rechaza campos rumor no autenticados y sellos sin firmar, restaura cuatro casos de mensajes faltantes y enruta las conversaciones de grupo de participantes totalmente seguidos hacia la bandeja de entrada. La versión también conserva las tags de eventos de vídeo direccionables cuando se actualizan las listas y consume las solicitudes de borrado observadas para que los vídeos eliminados desaparezcan del estado local. Esos cambios siguen al trabajo de tiempo de espera por consulta de relay cubierto la semana pasada, pero desplazan el foco del aislamiento de recuperación hacia los límites de identidad, la validación de mensajes y la confirmación de publicación.

### MDK 0.9.11 refuerza la convergencia y recuperación de grupos Marmot

[MDK 0.9.11](https://github.com/marmot-protocol/mdk/releases/tag/v0.9.11) es un kit de desarrollo en Rust para Marmot, un protocolo de mensajería de grupo cifrada transportado sobre Nostr. La versión construye un sistema mayor de convergencia y recuperación en torno a la máquina de estados del grupo: los pasos de convergencia obsoletos se reabren en la punta actual del grupo, las proyecciones de capacidad entrantes se confirman de forma atómica, los mensajes diferidos reciben vidas acotadas entre reinicios, y los puntos de control direccionados por commit ayudan a recuperar las propias bifurcaciones de commit de una identidad. Los envíos no estables pueden encolarse y recuperarse, mientras que una ruta de estancamiento de época escala a backfill y los mensajes enviados sobreviven al trabajo de convergencia.

[El almacenamiento y las integraciones de host](https://github.com/marmot-protocol/mdk/pull/1201) reciben un refuerzo paralelo. MDK elimina de forma segura las proyecciones SQLite podadas, pone a cero las claves privadas importadas, los intermedios de exportación de claves cifradas NIP-49 y los búferes de serialización OpenMLS, y redacta las claves de imagen de grupo de la salida de depuración. La importación de cuentas puede reanudarse tras una interrupción, se reparan las rutas de almacenamiento privado en iOS y Android, y los hosts pueden cerrar explícitamente el almacenamiento antes de la suspensión. Nuevas proyecciones ligeras de roster y membresía local reducen lo que las aplicaciones deben leer, mientras que el conector Hermes puede entregar varias imágenes generadas por agentes como un álbum Marmot.

### Nostria 4.1.67 amplía la administración de comunidades cifradas

[Nostria 4.1.67](https://github.com/nostria-app/nostria/releases/tag/v4.1.67) es un cliente social web y de escritorio para Nostr. Se apoya en los grupos gestionados por relays experimentales de [NIP-29](/es/topics/nip-29/) (grupos gestionados por relays) y las comunidades cifradas Concord introducidas en 4.1.53, añadiendo disolución de comunidad, administración de icono y banner, subidas de fotos cifradas con vistas previas comprimidas, un selector completo de reacciones y un diseño de doble panel que mantiene una comunidad abierta mientras el usuario lee notas o artículos. La versión también añade mensajería en hilos y un hub combinado para chats públicos, de grupo y privados.

### Amber 6.4.0 hace explícita cada decisión de firma agrupada

[Amber 6.4.0](https://github.com/greenart7c3/Amber/releases/tag/v6.4.0) es un firmante Android que mantiene las claves privadas de Nostr separadas de las aplicaciones que solicitan firmas. Su pantalla rediseñada de solicitudes múltiples ofrece controles Aprobar y Denegar para cada petición y cada grupo, sustituyendo al flujo anterior de selección y confirmación. Las solicitudes denegadas enviadas a través de la interfaz bunker mediada por relay de Amber reciben ahora respuestas de error adecuadas, de modo que el cliente solicitante puede distinguir un rechazo de un firmante estancado.

[El código etiquetado de Amber](https://github.com/greenart7c3/Amber/tree/v6.4.0) también añade etiquetas localizadas y legibles para 113 kinds de evento más en cada locale publicado. Las adiciones incluyen eventos de grupo Concord, marcadores de repositorio Git de [NIP-51](/es/topics/nip-51/) (listas curadas de eventos) y eventos de presencia en sala de [NIP-53](/es/topics/nip-53/) (actividades en vivo), dando a los usuarios más contexto sobre datos desconocidos antes de aprobar una firma. Una guarda de mapa concurrente también corrige un fallo de suscripción a relay que podía producir un `NegativeArraySizeException`.


### Safebox Acorn separa un componente de recuperación portátil de la aplicación web

[Safebox Acorn](https://github.com/trbouma/safebox-acorn) es un componente Python independiente y una interfaz de línea de comandos para salvaguardar claves, fondos y registros controlados por el usuario con estado respaldado por Nostr. Extraer Acorn de la aplicación web Safebox más amplia permite a otro proyecto Python instalar el runtime y usar sus ayudantes de clave, perfil de Nostr, relay, registro, Cashu, Lightning y criptografía sin asumir la interfaz web. Sus primitivas actuales de protección de registros pueden generar una clave fresca de 256 bits, derivar una a partir de entropía suministrada por separado, y codificar la clave exacta como una frase de recuperación de 24 palabras con suma de comprobación.

La [guía de recuperación y continuidad](https://trbouma.github.io/safebox-acorn/recovery-and-continuity/) del proyecto enmarca Acorn como el componente de protocolo reemplazable dentro de un Safebox doméstico o comunitario. El diseño mantiene el estado cifrado disponible a través de un relay local y réplicas independientes para que la recuperación no dependa de un solo dispositivo, aplicación, relay, mint o proveedor de servicio. La documentación es cuidadosa con el límite actual: el cifrado de registros protegidos sigue en diseño, por lo que las aplicaciones no deberían hacer depender los registros de la nueva clave de protección de registros hasta que ese perfil se haya implementado y revisado.


## Versiones

### Mostro Core 0.14.2 cambia el sobre del chat cifrado

[Mostro Core](https://github.com/MostroP2P/mostro-core) es la biblioteca Rust de tipos compartidos y funciones entre pares usada por el daemon de intercambio Mostro y sus clientes. La [versión 0.14.2](https://github.com/MostroP2P/mostro-core/releases/tag/v0.14.2) sustituye los mensajes de chat gift-wrap por sobres de kind 14 que usan claves separadas de cifrado de conversación y de firma derivadas del secreto compartido de los pares. El nuevo lector valida el autor, la firma, el destinatario, la marca temporal y el tamaño del contenido, mientras que los ayudantes legacy de gift-wrap siguen disponibles para que los clientes puedan leer ambos formatos durante la migración.

### Mostro 0.18.1 inicia una ruta de escrow Cashu y refuerza el daemon

[Mostro](https://github.com/MostroP2P/mostro) es un daemon de intercambio Lightning entre pares que coordina órdenes a través de Nostr. La [versión 0.18.1](https://github.com/MostroP2P/mostro/releases/tag/v0.18.1) sienta las bases de un backend de escrow Cashu, incluyendo configuración, ayudantes de base de datos, integración con mint, cableado de arranque y la primera acción de bloqueo. También puede usar precios anunciados por un nodo de confianza sobre Nostr y anuncia requisitos de prueba de trabajo para el primer contacto en su evento de información reemplazable. La versión actualiza su dependencia de Nostr por una corrección de denegación de servicio de NIP-44, elimina claves privadas de los registros de sesión de restauración, rechaza mensajes de cancelación cooperativa no autorizados, refuerza las obtenciones LNURL contra falsificación de peticiones del lado del servidor y bloqueos, valida facturas de pago y restaura las suscripciones a facturas retenidas tras un reinicio.

### LaWallet NWC 2.3.0 añade notificaciones de Nostr y recibos de zap

[LaWallet NWC](https://github.com/lawalletio/lawallet-nwc) es una plataforma Lightning Address de código abierto que conecta monederos a través de [Nostr Wallet Connect](/es/topics/nip-47/) (conexión de monedero por Nostr). La [versión 2.3.0](https://github.com/lawalletio/lawallet-nwc/releases/tag/v2.3.0) permite a cada monedero enviar notificaciones de recibidos y reenviados como eventos de Nostr configurables, incluyendo una tag `p` del destinatario, relays seleccionados, contenido con plantilla y cifrado opcional de [NIP-44](/es/topics/nip-44/) (cifrado de mensajes); los reintentos reutilizan el mismo ID de evento firmado. También acepta solicitudes de zap y publica recibos firmados de kind 9735 de [NIP-57](/es/topics/nip-57/) (zaps) tras la liquidación, mientras que una nueva vista de capacidades de dirección muestra si la dirección resuelta admite NIP-05, NIP-57 y protocolos Lightning Address relacionados.

### nostr-double-ratchet TypeScript 0.0.166 vincula invitaciones públicas a claves de sesión

[nostr-double-ratchet](https://github.com/irislib/nostr-double-ratchet) proporciona primitivas TypeScript y Rust para mensajería directa y de grupo cifrada de extremo a extremo sobre relays de Nostr. [TypeScript 0.0.166](https://github.com/irislib/nostr-double-ratchet/releases/tag/nostr-double-ratchet-ts-v0.0.166) exige que una respuesta a invitación demuestre la propiedad de su clave de sesión, evitando que una invitación pública reutilizable vincule una identidad de Nostr a la sesión de otra parte. La versión también rechaza campos rumor malformados y refuerza la validación de cargas; las sesiones existentes siguen funcionando, pero un invitador actualizado rechaza respuestas sin prueba de invitados antiguos.

### cln-nip47 0.2.0 amplía y aísla las peticiones NWC

[cln-nip47](https://github.com/daywalker90/cln-nip47) es un plugin de Core Lightning que expone un nodo a monederos a través de [Nostr Wallet Connect](/es/topics/nip-47/) (conexión de monedero por Nostr). La [versión 0.2.0](https://github.com/daywalker90/cln-nip47/releases/tag/v0.2.0) añade métodos NWC para crear, cancelar y liquidar facturas retenidas más una notificación `hold_invoice_accepted`, y anuncia el conjunto de métodos que el nodo conectado admite realmente. Las respuestas de lista de transacciones se detienen ahora en 500 entradas y unos 128 kB, los eventos de petición se desduplican por ID de evento, y la notificación fallida de un cliente ya no impide la entrega a otros clientes. La versión también elimina los dos métodos de multipago que ya no forman parte de la especificación NWC.

### ClipRelay 0.1.3 restaura las conexiones de relay y firmante tras periodos de inactividad

[ClipRelay](https://github.com/tajava2006/cliprelay) sincroniza el portapapeles de un usuario entre dispositivos a través de relays de Nostr, cifrando el contenido hacia la misma identidad con [NIP-44](/es/topics/nip-44/) (cifrado de mensajes). Las versiones [de escritorio](https://github.com/tajava2006/cliprelay/releases/tag/desktop/v0.1.3) y [Android](https://github.com/tajava2006/cliprelay/releases/tag/android/v0.1.3) 0.1.3 correspondientes añaden un cuadro de texto para enviar texto escrito directamente al portapapeles de otro dispositivo. También prueban la actividad con idas y vueltas reales al relay tras periodos de inactividad, escalando desde la resuscripción hasta la sustitución del socket y un pool de conexiones reconstruido, mientras que las llamadas estancadas al firmante [NIP-46](/es/topics/nip-46/) (firma remota mediada por relays) agotan ahora el tiempo de espera y se reconstruyen automáticamente.

### NoorNote 1.3.2 traslada el descubrimiento de artículos al grafo social

[NoorNote](https://github.com/77elements/noornote) es un cliente de Nostr para publicaciones sociales, mensajes cifrados, artículos de formato largo y otros tipos de evento en web, escritorio y Android. La [versión 1.3.2](https://github.com/77elements/noornote/releases/tag/v1.3.2) sustituye su feed global plano de artículos por descubrimiento extraído de contactos de primer, segundo y tercer grado, ofreciendo a los lectores una línea temporal de artículos arraigada en su grafo de seguimiento. También colapsa ráfagas de mensajes directos reproducidos de remitentes desconocidos en una sola notificación continua en lugar de producir una pila de avisos a medida que llega el historial del relay.

### Bray 2.4.0 añade un dialecto compacto de firma remota

[Bray](https://github.com/forgesworn/bray) es un servidor MCP de Nostr que ofrece a agentes de software y personas herramientas para acceso a relays, identidad, publicación y firma remota. La [versión 2.4.0](https://github.com/forgesworn/bray/releases/tag/v2.4.0) acepta una solicitud de firma cuyo evento es un objeto además de la forma serializada en cadena usada por [NIP-46](/es/topics/nip-46/) (firma remota mediada por relays), y añade `sign_event_compact`, que devuelve solo el ID del evento, la firma, la pubkey y la marca temporal. Ese formato de petición y respuesta más pequeño reduce el uso de memoria para firmantes de hardware restringidos, mientras que el flujo estándar `sign_event` permanece sin cambios y ambos dialectos producen una firma sobre el ID del evento recibido.


## Recién descubiertos

### Pact aporta vínculos de agentes con consentimiento mutuo a Nostr

[Pact](https://github.com/bobodread876/pact), descubierto esta semana, es una capa de relaciones en fase temprana para agentes de software construida sobre MATE.md y un transporte borrador NIP-BD. Sus vínculos firmados con consentimiento mutuo los retienen las propias claves de los agentes y pueden publicarse sobre Nostr, mientras que los vínculos privados usan gift-wrap de [NIP-59](/es/topics/nip-59/) (envolturas que ocultan metadatos). El monorepo incluye un servidor MCP, SDK TypeScript, cliente de línea de comandos, daemon autoalojable e interfaz web. Su actividad más reciente en el repositorio es anterior a la ventana semanal de este número, por lo que esto es una nota de descubrimiento y no una afirmación de nueva versión.


## Cambios sin publicar

### nostrord mantiene sincronizado el silenciamiento de grupos entre dispositivos

[nostrord](https://github.com/nostrord/nostrord) es un cliente multiplataforma para comunidades gestionadas por relays. El [PR #250](https://github.com/nostrord/nostrord/pull/250) almacena las elecciones de silenciamiento por grupo de cada cuenta en un evento autocifrado de kind `30078` de [NIP-78](/es/topics/nip-78/) (datos específicos de aplicación), de modo que un ajuste hecho en un dispositivo puede seguir al usuario a otro sin revelar la lista de grupos al relay. El registro reemplazable usa ordenación por evento más reciente, escucha cambios en vivo y revierte la interfaz cuando falla la firma o la publicación en lugar de dejar el estado local desincronizado. Los grupos silenciados también dejan de contribuir totales de no leídos visibles mientras conservan su posición de no leído para la próxima visita.

### Amethyst completa el ciclo de vida de invitaciones de Concord

[Amethyst](https://github.com/vitorpamplona/amethyst) es un cliente Android de Nostr cuyo soporte de comunidades cifradas implementa el protocolo Concord. El [PR #3888](https://github.com/vitorpamplona/amethyst/pull/3888) permite que los enlaces de invitación sobrevivan a un refounding de comunidad reemitiendo sus paquetes en las mismas coordenadas direccionables, mientras que una comprobación de expulsión impide que un miembro eliminado use esa ruta de recuperación. También implementa la lista de invitaciones cifrada CORD-05 tanto en la aplicación como en el cliente de línea de comandos `amy`, añade lápidas de revocación por enlace, y exige confirmación del relay antes de eliminar la única clave de firma almacenada que puede retirar un enlace. El mismo trabajo dota a `amy` de las rutas de entrega de clave de control, refounding, rekeying y recuperación de miembros aislados necesarias para seguir épocas comunitarias posteriores.

### Buzz lleva la apariencia de cada comunidad entre escritorio y móvil

[Buzz](https://github.com/block/buzz) es un espacio de trabajo comunitario basado en Nostr con clientes de escritorio y móvil. Los PR fusionados de escritorio [#3653](https://github.com/block/buzz/pull/3653) y móvil [#3767](https://github.com/block/buzz/pull/3767) almacenan el tema, el acento y la elección de modo del sistema de cada comunidad como un registro cifrado NIP-78 en el relay de esa comunidad. Ambos clientes comparten la misma carga versionada y mantienen cachés locales con alcance de identidad, de modo que cambiar de comunidad o de cuenta no puede aplicar la apariencia equivocada mientras el relay no esté disponible. El orden de reemplazo, las escrituras protegidas y la resuscripción tras una conexión cerrada permiten que los dos clientes converjan de nuevo tras reconectar.

[Buzz Desktop 0.5.10](https://github.com/block/buzz/releases/tag/desktop-v0.5.10) llegó antes del corte del número con un pase de rendimiento y fiabilidad. Elimina regresiones introducidas tras 0.5.9, acelera la carga de canales, acota la retención inicial de la línea temporal, coalesce la persistencia del estado de lectura, preserva líneas temporales de canal frescas y evita que el worker de ingestión del relay falle con reacciones a eventos de proyecto. También añade el envío de un mensaje de hilo a un canal y restringe la búsqueda de escritorio al alcance previsto.


## Actualizaciones de NIPs y trabajo de especificación del protocolo

### NIPs

[El PR de NIPs #2435](https://github.com/nostr-protocol/nips/pull/2435) es una enmienda abierta a NIP-34 (colaboración en repositorios git mediante eventos de Nostr). Añade una tag `b` opcional a un evento de pull request para que el autor pueda nombrar una rama destino distinta de la predeterminada del repositorio. La propuesta coincide con soporte ya implementado en ngit y GitWorkshop, pero aún no ha entrado en la especificación.

[El PR de NIPs #2434](https://github.com/nostr-protocol/nips/pull/2434) es una propuesta abierta de claves de identidad poscuánticas. Deriva claves poscuánticas de cifrado y firma junto a la clave secp256k1 existente a partir de una semilla de derivación de claves mnemónicas de NIP-06, y vincula las pubkeys a la identidad de Nostr con una atestación de kind `10203`. El borrador limita su reclamo a proteger la confidencialidad de mensajes anteriores si secp256k1 se rompe más adelante; no sustituye las firmas de eventos actuales.

[El PR de NIPs #2431](https://github.com/nostr-protocol/nips/pull/2431) es una enmienda abierta de NIP-07 (firmantes de navegador). Un cliente podría adjuntar la pubkey que espera a las peticiones de firma o cifrado, exigiendo al firmante usar esa cuenta o rechazar la llamada. Esto evitaría que una página continuara silenciosamente bajo una identidad distinta después de que el usuario cambie de cuenta en el firmante.

[El PR de NIPs #1813](https://github.com/nostr-protocol/nips/pull/1813) sigue siendo una propuesta abierta de double-ratchet tras trabajo sustantivo durante la ventana. Especifica conversaciones cifradas con secreto hacia adelante cuyas claves avanzan con los mensajes, con una implementación ya disponible en la biblioteca nostr-double-ratchet e Iris. Sigue siendo un borrador, no un NIP fusionado.

[El PR de NIPs #2433](https://github.com/nostr-protocol/nips/pull/2433) se abrió y cerró sin fusionar durante la ventana. Proponía aclarar los errores de relay de NIP-42 para que `auth-required` significara que otra autenticación podría cambiar el resultado, mientras que `restricted` significaría que no podría. La distinción abordaba conexiones autenticadas para una clave pero aún sin autorización para otra; el estado cerrado significa que la redacción no entró en la especificación.

[El PR de NIPs #2378](https://github.com/nostr-protocol/nips/pull/2378), cubierto previamente mientras aún estaba propuesto, se ha cerrado ahora sin fusionar. Sus eventos propuestos de pasaportes de agente, descubrimiento, tareas, marketplace, facturas y conexiones permanecen por tanto fuera del conjunto de NIPs.

[El commit de NIPs 656cecc](https://github.com/nostr-protocol/nips/commit/656cecc7c0a815b6a2b218d3b5d6f078b3f4dbab) fusionó una corrección solo documental de NIP-29. Añade una tag `previous` al ejemplo de metadatos de grupo, mostrando cómo un evento de reemplazo puede identificar el evento que sustituye. Esto aclara un ejemplo y no introduce una nueva característica de protocolo.

### Concord y CORDs

[El PR de CORD #18](https://github.com/concord-protocol/concord/pull/18) fragmentaría las listas comunitarias cifradas en eventos de kind `33302`, eliminaría el límite de 50 membresías y podaría entradas retiradas para mantenerse dentro de los límites del relay. Otras dos propuestas abiertas añaden [localizadores de mención privada](https://github.com/concord-protocol/concord/pull/16) y una [señal de pausa](https://github.com/concord-protocol/concord/pull/17) que suspende el chat sin descartar mensajes.

[El PR de CORD-02 #15](https://github.com/concord-protocol/concord/pull/15) se fusionó el 6 de agosto y restringe las escrituras al plano de control de una comunidad. Propietarios y personal retienen un nuevo secreto de firma `control_root`, mientras que todos los miembros conservan la pubkey derivada y la clave de lectura necesarias para verificar y descifrar el estado de moderación. La clave de escritura es una barrera antispam, no un sustituto de las firmas internas de actor y las comprobaciones de roster que establecen la autoridad.

[El PR de CORD #12](https://github.com/concord-protocol/concord/pull/12), cubierto previamente como borrador abierto, se ha cerrado ahora sin fusionar. Su porción de plano de control fue reemplazada por la enmienda CORD-02 fusionada más estrecha arriba, mientras que los canales de escritura restringida y el resto del material borrador no entraron en la especificación.

## Análisis en profundidad de NIPs

### Solicitudes de borrado de eventos (NIP-09)

[NIP-09](/es/topics/nip-09/) (solicitudes de borrado de eventos), definido por la [especificación principal](https://github.com/nostr-protocol/nips/blob/master/09.md), ofrece al autor de un evento una forma firmada de pedir a relays y clientes que dejen de servir uno o más de los eventos de ese autor. No borra cada copia. Transporta la intención del autor a través de la misma red de relays que distribuyó el evento original.

La solicitud es un evento firmado ordinario de kind `5`. Sus tags contienen una o más referencias `e` a IDs de evento concretos o referencias `a` a coordenadas de eventos direccionables, y las [reglas de tags de NIP-09](https://github.com/nostr-protocol/nips/blob/master/09.md#event-deletion-request) indican que debería incluir una tag `k` por cada kind de evento referenciado. El `content` opcional puede explicar el motivo. Para una referencia `a`, un relay debería eliminar toda versión en esa coordenada cuya marca temporal no sea posterior al `created_at` de la solicitud, lo que evita que una solicitud de borrado antigua suprima un reemplazo posterior.

[La autoría es el límite de seguridad](https://github.com/nostr-protocol/nips/blob/master/09.md#relay-behavior). Un relay debería dejar de publicar un evento referenciado solo cuando su `pubkey` coincide con la `pubkey` de la solicitud de borrado, y un cliente debe realizar esa comprobación antes de ocultar un evento. Un relay puede no poseer el evento referenciado y por tanto ser incapaz de validar la relación al aceptar la solicitud, de modo que los clientes no pueden tratar la aceptación del relay como prueba de que el borrado fue autorizado. La especificación también pide a los relays conservar la solicitud de kind `5` porque otro cliente puede ya tener el evento original y encontrar la solicitud más tarde.

Aquí hay un [evento firmado de kind `5`](https://primal.net/e/6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943):

```json
{
  "id": "6f39fd3d0d593d97dd093f21fabe8f78895579d6979a6ecf14e169bd85bb0943",
  "pubkey": "5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743",
  "created_at": 1786465675,
  "kind": 5,
  "tags": [
    ["e", "f3d47f8b813928c5baf7ac993846be0220dc37a2e7c7b128fb49a4b92711f131"],
    ["k", "30091"],
    ["a", "30091:5877220aaae6e54a6f974602d5995c0fe24a3ea7ddabd8644bec795b9da00743:survey:0ad5cebc-608b-47d7-97fd-9e6c47787199"],
    ["t", "nostr-survey"]
  ],
  "content": "Public survey summary deleted during privacy refresh",
  "sig": "846be83b038dc5f91af0c9d03a4ac81aff9bc4cfde7d85c849fa2fdae890f75cc444a4072f45aa18883b0b3871e15381b220182d6e366892f0c9c6f9c0557244"
}
```

El borrado sigue siendo una política cooperativa, no revocación de un objeto firmado. Un relay, caché, captura de pantalla o cliente sin conexión puede conservar los bytes originales, y borrar la solicitud de kind `5` no la deshace. Los clientes pueden ocultar el objetivo, marcarlo como desautorizado o mostrar el motivo de la solicitud, pero deberían decir a los usuarios que no puede garantizarse un borrado universal. Esto difiere de [NIP-40](https://github.com/nostr-protocol/nips/blob/master/40.md) (expiración de eventos), donde una tag `expiration` pide a los relays dejar de almacenar un evento tras un momento elegido al publicarlo. NIP-09 maneja una decisión posterior del autor y puede apuntar a eventos ya distribuidos.

Las implementaciones actuales aplican esa política en distintas capas. [Divine PR #6623](https://github.com/divinevideo/divine-mobile/pull/6623) elimina vídeos borrados del almacén de eventos del cliente, [strfry PR #251](https://github.com/hoytech/strfry/pull/251) extiende las solicitudes de borrado válidas a destinatarios gift-wrap, y [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md) declara soporte de NIP-09 en su cliente. [El cliente de grupo de nostrord](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/network/NostrGroupClient.kt) ofrece otra ruta de implementación actual.

### Denuncias (NIP-56)

[NIP-56](/es/topics/nip-56/) (eventos de denuncia), definido por la [especificación principal](https://github.com/nostr-protocol/nips/blob/master/56.md), estandariza una denuncia firmada sobre una cuenta, un evento o un blob referenciado. Separa la señal de denuncia de la decisión de moderación, permitiendo a cada cliente o relay elegir qué denunciantes confía y qué respuesta encaja con su política.

Una denuncia usa kind `1984` y debe identificar la cuenta denunciada en una tag `p`. Denunciar una nota también requiere una tag `e` para el ID del evento. El tercer valor de la tag lleva una de las categorías especificadas: `nudity`, `malware`, `profanity`, `illegal`, `spam`, `impersonation` o `other`. Una denuncia sobre un blob puede usar su hash en una tag `x`, una tag `e` para el evento que referenció el blob, y una tag `server` opcional para una ubicación. Las tags opcionales `L` y `l` de [NIP-32](https://github.com/nostr-protocol/nips/blob/master/32.md) (etiquetado) pueden añadir una etiqueta con espacio de nombres cuando la lista fija de categorías no es lo bastante precisa.

[El evento prueba solo que una clave hizo una alegación](https://github.com/nostr-protocol/nips/blob/master/56.md#reporting). El contenido denunciado no se vuelve falso, ilegal o eliminable meramente porque exista un kind `1984` válido, y un relay abierto no puede contar con seguridad denuncias anónimas como votos. La especificación desaconseja la moderación automática del relay porque las denuncias son fáciles de manipular, a la vez que permite a los administradores de relay actuar sobre denuncias de moderadores en los que ya confían. Un cliente puede en cambio ponderar denuncias a través del grafo social de un usuario, por ejemplo difuminando contenido tras varios contactos de confianza que marquen la misma cuenta.

Aquí hay un [evento firmado de kind `1984`](https://primal.net/e/17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2):

```json
{
  "id": "17301ea66066d34af9ba0b6957ed9d9d8854b9436939e682e21e7a5a8768e4b2",
  "pubkey": "1ff02fb5cdc633c1be55368ab655490ec25d2f5dc2e364d4703bc3196d99eab1",
  "created_at": 1786465319,
  "kind": 1984,
  "tags": [
    ["p", "3a72b02cc05ee07310dc580874b6a9ca8271c6518b90655bd2e98003c9601e68", "impersonation"]
  ],
  "content": "",
  "sig": "6362e415410feb19e0505654a4660e8456b6b2aec5ae39173a0429a6a8e5fa1381c9488198ca2982db43ee8198af056f2a25537705c763784062056d0ab2eb1a"
}
```

[NIP-56 y NIP-09 resuelven problemas distintos](https://github.com/nostr-protocol/nips/tree/master). Una denuncia de kind `1984` puede apuntar a la cuenta o evento de otra persona, pero no confiere autoridad de borrado. Una solicitud de kind `5` expresa la intención del autor original y solo es válida contra los propios eventos de ese autor. Ninguno garantiza eliminación: NIP-56 delega deliberadamente la acción a la política de moderación local, mientras que NIP-09 depende de que relays y clientes honren una solicitud autenticada.

Las implementaciones exponen esas elecciones en productos distintos. [Divine PR #6591](https://github.com/divinevideo/divine-mobile/pull/6591) corrige la entrega de denuncias en un cliente de vídeo corto, [Conduit PR #250](https://github.com/Conduit-BTC/conduit-mono/pull/250) lee denuncias como contexto acotado para participantes de marketplace, y [el módulo NIP-56 de nostrord](https://github.com/nostrord/nostrord/blob/862855e8e7130f509c458c6b4d36a3bd660f16d8/composeApp/src/commonMain/kotlin/org/nostr/nostrord/nostr/Nip56.kt) publica y procesa eventos de denuncia. [Amethyst](https://github.com/vitorpamplona/amethyst/blob/278ddd27904dc721e54ffaca8803307d154f2e1d/README.md#nip-support) también lista soporte actual de NIP-56.


---

Envía un DM por NIP-17 para compartir un proyecto o noticia a través del [proyecto Nostr Compass](https://github.com/andotherstuff/nostr-compass).
