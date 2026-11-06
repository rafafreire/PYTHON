
## Outlook 365

Correo electrónico. Outlook 365

4 artículos

Esta leyTodo el tema

EscucharConfigurar

🔊 Aprovecha el transporte, conducción, gimnasio, paseos, deporte y rutinas diarias para escuchar las leyes — todo suma

[Hacer test de Outlook 365 →](https://www.vence.es/leyes/correo-electronico?selected_articles=1,2,3,4&source=temario)[🔧 Elegir qué artículos entran](https://www.vence.es/leyes/correo-electronico?abrir_filtro=1&source=temario_filtro)

Art. 1

### Conceptos y funcionamiento

## Qué es el correo electrónico

> **El correo electrónico** es un servicio de red que permite enviar y recibir mensajes digitales a través de redes de comunicación electrónica. Funciona de forma análoga al correo postal tradicional, pero se realiza íntegramente por Internet, con entrega prácticamente instantánea.

El correo electrónico es un **sistema de comunicación asíncrona**: el emisor envía el mensaje cuando lo desea y el receptor lo lee cuando le conviene, sin necesidad de que ambos estén conectados simultáneamente.

### Ventajas del correo electrónico

- **Rapidez**: entrega prácticamente inmediata.
    
- **Coste**: sin coste adicional más allá de la conexión a Internet.
    
- **Adjuntos**: permite enviar documentos, imágenes, vídeos, etc.
    
- **Registro**: queda constancia de todos los mensajes.
    
- **Accesibilidad**: desde cualquier dispositivo con Internet.
    
- **Masividad**: envío a múltiples destinatarios simultáneamente.
    

> **Importante**: El correo puede **dificultar la concentración** (interrumpe el flujo de trabajo); esto NO es una ventaja.

### Elementos mínimos para enviar un correo

Para que un correo electrónico pueda enviarse correctamente son necesarios **tres elementos mínimos**:

1. **Destinatario** (dirección de correo en el campo Para, CC o CCO)
    
2. **Remitente** (Sender / campo De) — la cuenta desde la que se envía
    
3. **Mensaje** (cuerpo del correo)
    

El asunto es **opcional** desde el punto de vista técnico, aunque se considera altamente recomendable porque ayuda al destinatario a identificar el contenido antes de abrir el mensaje. El único campo verdaderamente imprescindible para que Outlook permita el envío es la **dirección del destinatario**.

---

## Estructura de una dirección de correo electrónico

El formato estándar de una dirección de correo electrónico, definido por la norma **RFC 5322**, es:

|Parte|Nombre técnico|Ejemplo en `nombre.apellido@upm.es`|
|---|---|---|
|Parte izquierda del @|Nombre de usuario / buzón|`nombre.apellido`|
|Símbolo separador|Arroba (@)|`@`|
|Parte inmediatamente tras el @|Host / servidor de correo|`upm`|
|Dominio completo (host + extensión)|Dominio de correo|`upm.es`|
|Extensión final|Dominio de nivel superior (TLD)|`.es`|

Ejemplos de direcciones válidas: `mi_nombre@mihogar.com`, `lope.de.vega@inap.es`, `abcdef@gmail.es`

### Límites técnicos de las direcciones

Según el estándar **RFC 5321**, las partes de una dirección de correo electrónico tienen estos límites:

- Hasta **64 caracteres** para la parte local (nombre de usuario, antes de la @)
    
- Hasta **255 caracteres** para el dominio (parte tras la @)
    
- Hasta **254 caracteres** para la dirección completa: la ruta con la que SMTP la transmite admite 256, incluidos los signos < y > que la rodean
    

### Partes estructurales de un mensaje de correo

Un mensaje de correo electrónico se compone de **dos partes fundamentales**:

- **Cabecera (header)**: contiene los campos De, Para, CC, CCO, Asunto, fecha y demás metadatos del mensaje.
    
- **Cuerpo del mensaje**: la zona donde el remitente redacta el contenido principal, el texto o información que desea comunicar.
    

Los archivos adjuntos forman parte del contenido del mensaje y se envían junto con él a través de los servidores de correo.

---

## Protocolos de correo electrónico

Los protocolos regulan cómo se envían, reciben y almacenan los correos. Los principales son:

### SMTP — Protocolo de envío

> **SMTP** (Simple Mail Transfer Protocol) es el protocolo estándar para el **envío** de correos electrónicos entre servidores y desde clientes de correo hacia los servidores.

SMTP localiza al servidor destinatario mediante consultas al **DNS**. El servidor SMTP de destino deposita el mensaje en el buzón del usuario; **POP3 o IMAP** sirven después para que el cliente de correo acceda a ese buzón. Su función es exclusivamente el **envío** (no la recepción).

### POP3 — Protocolo de recepción clásico

> **POP3** (Post Office Protocol versión 3) es el protocolo que usan los clientes de correo para **recibir y descargar** los mensajes almacenados en un servidor remoto.

Características clave de POP3:

- **Descarga los mensajes** del servidor al dispositivo local.
    
- **Por defecto, elimina los mensajes del servidor** una vez descargados (configurable para conservar copias).
    
- Los mensajes quedan almacenados **localmente**; no sincroniza carpetas ni estado de lectura entre dispositivos.
    

### IMAP — Protocolo de recepción moderno

> **IMAP** (Internet Message Access Protocol) permite acceder y sincronizar los correos almacenados en el servidor desde cualquier dispositivo con conexión a Internet.

Características clave de IMAP:

- Los mensajes permanecen **sincronizados en el servidor** de forma permanente.
    
- Permite acceso desde **múltiples dispositivos** con estado sincronizado (leído/no leído, carpetas...).
    
- **Requiere conexión a Internet** continua, ya que trabaja en línea con el servidor.
    
- Los cambios realizados en un dispositivo se reflejan en todos los demás.
    

### Tabla comparativa: POP3 vs IMAP

|Característica|POP3|IMAP|
|---|---|---|
|Almacenamiento de mensajes|En el dispositivo local|En el servidor|
|Sincronización multidispositivo|No|Sí|
|Conexión permanente necesaria|No (solo para descargar)|Sí (trabaja en línea)|
|Elimina mensajes del servidor|Sí (por defecto)|No|
|Sincronización de carpetas|No|Sí|
|Adecuado para múltiples dispositivos|No|Sí|
|Uso sin conexión tras descarga|Sí|Limitado|

### Microsoft Exchange

> **Exchange** es el protocolo y servidor de mensajería de Microsoft, diseñado para entornos empresariales. Va mucho más allá de la simple gestión de correo electrónico.

A diferencia de IMAP y POP3, Exchange proporciona:

- Sincronización bidireccional en tiempo real entre todos los dispositivos.
    
- Gestión integrada de **correo, calendario, contactos y tareas**.
    
- Funciones colaborativas: carpetas compartidas, delegación de acceso, convocatorias de reunión.
    
- La posibilidad de recuperar mensajes enviados (si el destinatario no los ha abierto y ambos usan Exchange).
    

### MAPI

> **MAPI** (Messaging Application Programming Interface) es el protocolo de Microsoft que permite la integración profunda entre Outlook y los servidores Exchange, sincronizando funciones avanzadas como calendario, contactos y tareas en tiempo real.

### Otros protocolos relacionados

|Protocolo|Nombre completo|Función|
|---|---|---|
|DNS|Domain Name System|Resolución de nombres de dominio (necesario para SMTP)|
|SSL|Secure Sockets Layer|Cifrado de comunicaciones de correo|
|TLS|Transport Layer Security|Cifrado moderno de comunicaciones (sucesor de SSL)|
|FTP|File Transfer Protocol|Transferencia de archivos (NO es un protocolo de correo)|
|HTTP/HTTPS|HyperText Transfer Protocol (Secure)|Protocolo web (usado en webmail)|
|RTP|Real-time Transport Protocol|Transmisión de audio y vídeo en tiempo real (NO es de correo)|

> **FTP** y **DNS** no son protocolos de correo. DNS es necesario para SMTP (resuelve nombres) pero no es de correo. TLS y SSL son tecnologías de cifrado. Las tres formas habituales de acceder al correo son: **POP, IMAP y webmail**.

---

## Campos de un mensaje de correo electrónico

### Campo Para (destinatarios principales)

> El campo **"Para"** indica los **destinatarios principales** del mensaje. Se pueden incluir varias direcciones separadas por **punto y coma (;)**. El límite de destinatarios por mensaje no lo fija Outlook sino el servidor de correo: en Exchange Online es de **500 destinatarios** por defecto, personalizable hasta 1000.

### Campo CC (Copia Carbón)

> El campo **CC** (Con Copia / Copia Carbón) permite enviar una copia del mensaje a destinatarios adicionales. **Todos los receptores** (Para, CC y CCO) pueden ver las direcciones del campo CC.

Si un destinatario en CC usa "Responder a todos", todos los destinatarios de Para y CC verán la respuesta.

### Campo CCO (Copia Carbón Oculta)

> El campo **CCO** (Con Copia Oculta / Copia Carbón Oculta) permite incluir destinatarios que reciben el mensaje pero **cuya identidad permanece oculta** para todos los demás destinatarios (ni los del campo Para ni los de CC pueden ver a quienes están en CCO).

Los destinatarios en CCO **no pueden ver** a los demás destinatarios en CCO: quien recibe un mensaje no puede saber si el remitente añadió a otras personas en copia oculta. Solo el **remitente** sabe a quiénes se envió la copia oculta. Si un destinatario en CCO usa "Responder a todos", la respuesta va al remitente y a los destinatarios de Para y CC; nunca a los demás CCO, que no aparecen en el mensaje que recibe.

### Tabla comparativa: Para, CC y CCO

|Campo|Visibilidad para otros|Uso|
|---|---|---|
|**Para**|Visible para todos|Destinatarios principales|
|**CC**|Visible para todos|Destinatarios secundarios informados|
|**CCO**|Oculto para todos|Destinatarios privados, sin revelar su identidad|

### Campo Asunto

> El campo **Asunto** sirve para describir brevemente el tema o motivo del mensaje, facilitando al destinatario identificar de qué trata antes de abrirlo.

El asunto es **opcional** desde el punto de vista técnico, pero altamente recomendable. En Outlook, el asunto muestra prefijos automáticos según la acción realizada:

|Prefijo|Significado|
|---|---|
|**RE:**|Respuesta a un correo recibido previamente (del inglés _Reply_)|
|**RV:**|Reenvío de un mensaje anterior (en español, _Reenviado_)|

### Campo De, Cuerpo y Archivos adjuntos

El campo **De** identifica al remitente y se rellena automáticamente con la cuenta configurada.

> El **cuerpo del mensaje** es la zona donde el remitente redacta el contenido principal del correo.

Los archivos adjuntos se envían como parte del contenido del mensaje. El envío no está condicionado a que el receptor tenga el programa para abrirlos; se transmiten como datos binarios. El **tamaño máximo** depende del **servidor de correo** (Exchange, Outlook.com...) y la configuración. Por ejemplo, la aplicación de Outlook limita a **20 MB** los mensajes de las cuentas de correo de Internet y a **10 MB** por defecto los de Exchange, mientras que Outlook.com admite adjuntos de hasta **25 MB**. Por seguridad, Outlook bloquea por defecto los archivos ejecutables (`.exe`).

---

## Seguridad en el correo electrónico

### Spam (correo no deseado)

> El **spam** (también llamado correo basura) son mensajes no solicitados, no deseados o de remitente desconocido, enviados de forma masiva, generalmente con fines publicitarios o comerciales.

El spam se reconoce porque llega de forma periódica, en grandes cantidades, de remitentes desconocidos. El elemento más importante para evitarlo son los **filtros**. Outlook dispone del **Filtro de correo electrónico no deseado** que mueve el spam a la carpeta **Correo no deseado**.

### Phishing

> El **phishing** consiste en correos electrónicos fraudulentos que pretenden captar ilícitamente datos personales, especialmente información bancaria o credenciales de acceso, mediante la suplantación de identidad de entidades legítimas.

Los correos de phishing suelen suplantar a bancos, administraciones públicas u otras entidades conocidas para engañar al usuario y obtener sus datos.

### Hoax

> Un **hoax** es una cadena de correos que difunde información falsa (bulos, noticias falsas) de manera masiva a través del correo electrónico.

### Cifrado, 2FA y recomendaciones de seguridad

Los servidores de correo modernos usan **SSL** y **TLS** para cifrar las comunicaciones. **S/MIME** y **PGP** son estándares de cifrado de extremo a extremo para el contenido de los mensajes. DNS no es tecnología de cifrado.

No habilitar la **autenticación de dos factores (2FA)** aumenta el riesgo de accesos no autorizados. Algunos servicios requieren una **contraseña de aplicación** al configurar Outlook. Las buenas prácticas incluyen no abrir correos de remitentes desconocidos, no clicar en enlaces sospechosos y no descargar adjuntos inesperados.

---

## Webmail vs. cliente de correo de escritorio

|Característica|Webmail|Cliente de escritorio (ej. Outlook)|
|---|---|---|
|Acceso|Desde el navegador web|Mediante aplicación instalada|
|Instalación|No requiere|Sí requiere|
|Trabajo sin conexión|Limitado o ninguno|Sí (con modo caché)|
|Sincronización|Siempre actualizado|Depende de la sincronización|
|Almacenamiento|En el servidor|Puede ser local o en servidor|
|Ejemplos|Gmail (web), Outlook.com|Microsoft Outlook, Mozilla Thunderbird|

> **Mozilla Thunderbird** es un **cliente de correo de escritorio**, no un webmail. Se instala localmente y accede al correo mediante IMAP o POP3. Gmail y Outlook.com son ejemplos de webmail.

---

## Formatos de mensaje en Outlook

Outlook permite redactar correos en tres formatos de texto, accesibles desde la pestaña **Formato de texto**:

|Formato|Características|Uso recomendado|
|---|---|---|
|**HTML**|Texto enriquecido, imágenes, tablas, listas, estilos. Es el formato predeterminado.|Comunicaciones externas y generales|
|**Texto sin formato**|Sin formato alguno. **Máxima compatibilidad** con cualquier plataforma o dispositivo.|Compatibilidad universal|
|**Texto enriquecido (RTF)**|Admite algunas características de formato. Formato **propietario de Microsoft**, usado principalmente en mensajería interna Exchange.|Entornos internos Exchange|

> **El formato HTML es el predeterminado en Outlook 365** y el que ofrece mayores posibilidades de formato (imágenes, tablas, listas con viñetas, formatos avanzados). **PDF y XML no son formatos de redacción** de correos en Outlook.

---

## Microsoft Outlook 365

> **Outlook 365** es el programa de gestión de información personal de Microsoft, incluido en el paquete Microsoft 365. Integra correo electrónico, calendario, contactos, tareas y notas en una sola aplicación.

### Interfaz principal de Outlook

La interfaz de Outlook 365 se organiza en varias áreas:

- **Cinta de opciones**: contiene las pestañas **Archivo, Inicio, Enviar y Recibir, Carpeta y Vista**.
    
- **Panel de carpetas** (a la izquierda): muestra las carpetas del buzón. El número junto al nombre de cada carpeta indica sus **mensajes sin leer** o, si así se configura en las propiedades de la carpeta, el número total de elementos.
    
- **Panel de navegación** (inferior): accesos directos a Correo, Calendario, Contactos, Tareas. Muestra hasta **8 botones o iconos** como máximo. La opción "Vistas" no forma parte de esta barra.
    
- **Panel de lectura**: muestra el contenido del mensaje seleccionado.
    
- **Barra de estado** (inferior): muestra el número de elementos y el estado de conexión. NO muestra "Lista de contactos favoritos" ni "Mensajes en seguimiento".
    

### Configuración inicial y gestión de cuentas

La **primera acción** al usar Outlook 365 es configurar una cuenta de correo. La configuración automática requiere: nombre del usuario, dirección de correo y contraseña. **No se requiere** teléfono ni correo alternativo. Para enviar correos es imprescindible configurar la **dirección del servidor SMTP**.

Outlook 365 permite configurar **varias cuentas en un mismo perfil**, sin límite fijo. Para cada cuenta se configuran los protocolos correspondientes (SMTP para envío, IMAP/POP3 para recepción).

---

## Carpetas del buzón de Outlook

Las carpetas estándar que se encuentran en cualquier gestor de correo electrónico son:

|Carpeta|Contenido|
|---|---|
|**Bandeja de entrada**|Mensajes recibidos|
|**Bandeja de salida**|Mensajes pendientes de envío (cola temporal)|
|**Elementos enviados**|Copia de los mensajes enviados correctamente|
|**Borradores**|Mensajes en redacción guardados sin enviar|
|**Correo no deseado**|Mensajes identificados como spam|
|**Elementos eliminados**|Mensajes borrados (recuperables)|
|**Archivo**|Mensajes archivados sin borrar|

> **"Bandeja de importantes"** no es una carpeta universal estándar en todos los gestores de correo.

### Bandeja de salida

La **Bandeja de salida** actúa como cola de envío temporal. Cuando se pulsa "Enviar" en Outlook, el mensaje pasa primero por la bandeja de salida antes de ser transmitido al servidor. Si un mensaje permanece en la bandeja de salida, es señal de que **está pendiente de envío** (puede deberse a problemas de conexión o configuración).

### Borradores

Los correos en proceso de redacción guardados sin enviar se almacenan en la carpeta **Borradores**. Outlook guarda automáticamente los mensajes en redacción en Borradores cada **3 minutos** por defecto.

Si se cierra Outlook mientras se está redactando un mensaje y se guardan los cambios, el correo queda en **Borradores** disponible para continuar editándose.

### Archivado

La función **Archivar** mueve el mensaje a la carpeta de archivo, donde permanece accesible para consulta y búsqueda posterior sin ocupar espacio en la bandeja de entrada principal (no lo borra). La opción **Purgar** elimina definitivamente, en una cuenta IMAP, los mensajes marcados para su eliminación (que se muestran tachados en su carpeta), sin posibilidad de restaurarlos.

### Limpieza del buzón

La herramienta **Limpieza del buzón** (Archivo → Herramientas → Limpieza del buzón) ofrece:

- Buscar elementos por antigüedad y tamaño
    
- Autoarchivar
    
- Vaciar elementos eliminados
    

---

## Acciones sobre mensajes recibidos

### Responder vs. Responder a todos vs. Reenviar

|Acción|Destinatario de la respuesta|Adjuntos del original|
|---|---|---|
|**Responder**|Solo al remitente original|No se incluyen|
|**Responder a todos**|Al remitente y a todos los destinatarios visibles (Para y CC)|No se incluyen|
|**Reenviar (RV)**|A un nuevo destinatario elegido por el usuario|Sí se incluyen automáticamente|

> **Responder** (flecha curvada hacia la izquierda) **no** envía la respuesta a todos los destinatarios del mensaje original; solo al remitente. Para incluir a todos, se debe usar "Responder a todos".

### Iconos visuales en mensajes

|Icono|Significado|
|---|---|
|Flecha azul hacia abajo|Importancia baja|
|Exclamación roja (!)|Importancia alta / mensaje urgente|
|Clip (sujetapapeles)|El mensaje contiene archivos adjuntos|
|Flecha curvada hacia la izquierda|Mensaje al que se ha respondido|
|Bandera roja|Mensaje marcado para seguimiento|
|Sobre cerrado|Mensaje sin leer|

La **bandera** marca el mensaje **para seguimiento** (recordatorio de que queda algo por hacer con él); no indica importancia, que va con la exclamación roja, ni peligro, ni categoría (las categorías son etiquetas de color). Fuentes: Microsoft Support es-ES, «Métodos abreviados de teclado para Outlook», apartado Usar marcas: «Mostrar el cuadro de diálogo Marcar mensaje para seguimiento» ([https://support.microsoft.com/es-es/office/m%C3%A9todos-abreviados-de-teclado-para-outlook-3cdeb221-7ae5-4c1d-8c1d-9e63216c1efd](https://support.microsoft.com/es-es/office/m%C3%A9todos-abreviados-de-teclado-para-outlook-3cdeb221-7ae5-4c1d-8c1d-9e63216c1efd)) y en-US, «Keyboard shortcuts for Outlook»: «Display the Flag for follow up dialog box» ([https://support.microsoft.com/en-us/office/keyboard-shortcuts-for-outlook-3cdeb221-7ae5-4c1d-8c1d-9e63216c1efd](https://support.microsoft.com/en-us/office/keyboard-shortcuts-for-outlook-3cdeb221-7ae5-4c1d-8c1d-9e63216c1efd)).

### Importancia, lectura e ignorar conversación

Los mensajes pueden marcarse con tres niveles de importancia: **alta** (exclamación roja !), **normal** (sin icono) y **baja** (flecha azul hacia abajo).

**Marcar como leído** elimina el resaltado de mensaje nuevo. Si se marca como "No leído" tras haberlo abierto, Outlook muestra de nuevo el sobre cerrado.

La opción **Ignorar conversación** mueve los mensajes actuales y **futuros** de esa conversación a Elementos eliminados de forma automática.

---

## Reglas de correo en Outlook

> Una **regla de correo** en Outlook 365 es una instrucción que el programa ejecuta automáticamente sobre los mensajes según condiciones que el usuario define.

Las reglas permiten: clasificar mensajes, moverlos a carpetas, eliminarlos, marcarlos, cambiar su importancia, reenviarlos, etc.

### Tipos de reglas

Outlook 365 distingue **dos tipos de reglas**:

- **Reglas basadas en servidor**: se ejecutan en el servidor Exchange aunque Outlook esté cerrado.
    
- **Reglas solo de cliente**: se ejecutan únicamente cuando Outlook está abierto en el equipo.
    

### Crear una regla

Para crear una regla desde un mensaje existente: **clic con el botón derecho → Reglas → Crear regla**.

Las reglas se administran desde: **Inicio → Reglas → Administrar reglas y alertas**.

Una regla configurada para aplicarse "al recibir mensajes" se ejecuta en el **momento exacto de la recepción**, sin necesidad de ninguna acción manual.

### Limitaciones de las reglas

Las reglas automáticas de Outlook **no pueden modificar el contenido del cuerpo del mensaje**. Sí pueden mover, marcar, responder automáticamente y realizar otras acciones sobre el mensaje, pero el cuerpo del texto queda fuera de su alcance.

Si se desactiva una regla, esta **deja de ejecutarse automáticamente** sin ser eliminada, y puede reactivarse cuando se desee.

### Diferencia entre regla y filtro

||Regla|Filtro de búsqueda|
|---|---|---|
|Ejecución|Automática|Manual|
|Propósito|Automatizar acciones|Mostrar mensajes según criterio|
|Configuración|Condición + acción|Criterio de visualización|

---

## Búsqueda en Outlook

La **barra de búsqueda** de Outlook 365 (parte superior de la interfaz) permite localizar rápidamente correos, contactos, citas y otros elementos del buzón.

### Sintaxis de búsqueda avanzada

|Búsqueda|Descripción|
|---|---|
|`"frase exacta"`|Busca la frase entre comillas de forma literal|
|`Asunto:oferta NO primera`|Busca mensajes cuyo asunto contiene "oferta" pero no "primera"|
|Texto sin comillas (ej: `pone`)|Busca las palabras que EMPIEZAN por ese fragmento (ponencia, poner, ponente; no «componer»): Outlook usa concordancia de prefijos|

### Ámbito de búsqueda

Cuando se tiene más de una cuenta configurada y se selecciona "Buzón actual", la búsqueda se realiza sobre **todas las carpetas del buzón de la cuenta activa**, no sobre todas las cuentas.

### Filtrar correo electrónico

El comando **Filtrar correo electrónico** (disponible en la cinta de opciones) permite mostrar únicamente los mensajes que cumplan un determinado criterio: sin leer, con adjuntos, de hoy, de la última semana, etc.

---

## Categorías en Outlook

> Las **categorías** son una herramienta de organización visual que permite clasificar mensajes, citas, contactos y tareas mediante colores y etiquetas personalizadas.

Se pueden asignar **múltiples categorías a un mismo elemento**. Mejoran la organización de todos los elementos de la aplicación (correos, calendario, contactos, tareas) y permiten agruparlos y localizarlos con mayor facilidad mediante **colores**.

---

## Seguimiento de mensajes

> El **seguimiento de mensajes** en Outlook permite añadir avisos y recordatorios tanto a los correos recibidos como a los enviados, para no olvidar acciones pendientes relacionadas con ese mensaje.

Al marcar un correo con seguimiento, Outlook **crea automáticamente una tarea asociada** a ese mensaje en la lista de tareas.

### Marcas de seguimiento predeterminadas

Las marcas de seguimiento predeterminadas disponibles en Outlook son:

- **Hoy**
    
- **Mañana**
    
- **Esta semana**
    
- **La próxima semana**
    
- **Sin fecha**
    
- **Personalizar**
    

> **"La semana pasada"**, **"Ayer"** y **"Este mes"** NO son marcas de seguimiento predeterminadas. El seguimiento se orienta hacia el futuro, no hacia el pasado.

Un mensaje puede tener marcas de importancia (alta/normal/baja) y marcas de seguimiento **simultáneamente**; ambas configuraciones coexisten de forma independiente.

---

## Firmas, respuestas automáticas y envío programado

> La **firma** en Outlook 365 inserta automáticamente un bloque de texto personalizado al final de los mensajes. Se pueden crear **varias firmas** para distintos propósitos (nueva, respuesta, reenvío).

> Las **respuestas automáticas** (fuera de oficina) permiten enviar un mensaje predefinido automáticamente cuando el usuario no está disponible. Se configuran desde **Archivo → Respuestas automáticas**.

La opción **Retrasar entrega** (pestaña Opciones al redactar) permite programar el envío para una fecha y hora futuras. El mensaje permanece en la **Bandeja de salida** hasta la hora programada. Según Microsoft, para que esta característica funcione **Outlook debe estar en línea y conectado**: en el **modo de intercambio en caché** de Exchange (el predeterminado) el mensaje diferido espera en la Bandeja de salida local, así que si Outlook no está abierto a la hora programada **no se envía hasta que se vuelve a abrir**; solo en el modo en línea lo retiene el servidor.

El atajo de teclado para enviar un correo en Outlook 365 es **Ctrl + Enter**.

---

## Recuperar un mensaje enviado

En Outlook 365 es posible recuperar un mensaje enviado si: el destinatario **no lo ha abierto aún** y **ambos** (remitente y destinatario) están conectados a un servidor **Microsoft Exchange**. Si no se cumplen estas condiciones, no es posible recuperarlo.

---

## Modo sin conexión y sincronización

La opción **Trabajo sin conexión** (pestaña Enviar/Recibir) desconecta Outlook del servidor. Mientras está activa, **no se pueden enviar ni recibir mensajes nuevos**; los mensajes redactados quedan en la Bandeja de salida. En **modo caché**, los mensajes escritos también quedan retenidos hasta recuperar la conexión.

La sincronización automática es cada **30 minutos** por defecto. Para forzar la recepción manual: pestaña **"Enviar y recibir"** → **"Actualizar carpeta"**.

---

## Libreta de direcciones y contactos

> La **libreta de direcciones** en Outlook 365 integra los contactos propios del usuario con las listas de distribución y directorios disponibles según la cuenta configurada (p. ej. el directorio global de Exchange).

- Se puede tener **más de una libreta de direcciones** (corresponden a carpetas de Contactos distintas).
    
- Los contactos se almacenan en el **servidor de correo** cuando se usa Outlook con Exchange/Microsoft 365, y se sincronizan en cada equipo: por eso **no es correcto** decir que la libreta «se almacena en el dispositivo».
    
- Qué la forma, según Microsoft: «Los contactos de la carpeta Contactos constituyen el contenido de la Libreta de direcciones de Outlook» y «Si su compañía tiene una lista global de direcciones (LGD), también la verá en la lista Libreta de direcciones» (para verla hace falta una cuenta de Microsoft Exchange Server). Fuentes: Microsoft Support es-ES, «Cambiar la libreta de direcciones predeterminada» ([https://support.microsoft.com/es-es/office/change-the-default-address-book-84c7be39-282a-4096-aeb8-89a2661a5162](https://support.microsoft.com/es-es/office/change-the-default-address-book-84c7be39-282a-4096-aeb8-89a2661a5162)) y en-US, «Change the default Address Book» ([https://support.microsoft.com/en-us/office/change-the-default-address-book-84c7be39-282a-4096-aeb8-89a2661a5162](https://support.microsoft.com/en-us/office/change-the-default-address-book-84c7be39-282a-4096-aeb8-89a2661a5162)).
    

### Gestión de contactos

Un contacto en Outlook puede tener múltiples **direcciones de correo** (correo 1, 2, 3...), teléfonos, dirección postal, empresa, campo **Notas** y categorías de color. Un contacto **no puede tener** el campo "Cuenta bancaria del sistema" ni "Carpeta de búsqueda". Sí se le pueden **adjuntar archivos** (por ejemplo, una hoja de cálculo): en la ficha del contacto, pestaña **Insertar** → **Adjuntar archivo** (grupo **Incluir**).

- Para **compartir un contacto**: arrastrarlo a un correo como adjunto (genera un archivo VCard automáticamente).
    
- Para **crear un contacto desde un correo**: clic derecho sobre el remitente → "Agregar a contactos de Outlook".
    
- Los contactos eliminados van a **Elementos eliminados** y pueden recuperarse antes de vaciar esa carpeta.
    
- Si se cambia la dirección de un contacto, se **actualiza** su ficha sin afectar al historial de conversaciones.
    
- La **Vista Tarjeta** muestra cada contacto como una tarjeta individual.
    

### Formato VCard

> El formato **VCard** (.vcf) es el estándar para enviar información de contacto de forma interoperable entre distintos programas.

### Grupos de contactos (Listas de distribución)

> Un **grupo de contactos** contiene varias direcciones agrupadas bajo un nombre, permitiendo enviar a todos sus miembros con una sola entrada.

Para crearlo en Outlook 365: sección **"Personas"** → menú **"Inicio"** → **"Nuevo grupo de contactos"**. La dirección de un integrante **no puede modificarse directamente**; hay que eliminarlo y añadirlo de nuevo. Al crear un grupo de contactos **no** se elige si será **privado** o **público**: esa elección es propia de los **Grupos de Microsoft 365** (Inicio → **Nuevo grupo**, con cuenta profesional o educativa). Esos grupos se crean **privados** de forma predeterminada (solo los miembros ven su contenido); en uno **público**, cualquier persona de la organización puede ver su contenido y unirse.

---

## Delegación de acceso

La función **Delegar acceso** de Outlook 365 permite que otra persona:

- Envíe elementos en nombre del propietario de la cuenta.
    
- Cree y responda a convocatorias de reuniones.
    
- Acceda a la bandeja de entrada sin necesidad de compartir la contraseña.
    

El nivel de permiso **Editor** es el más completo de los niveles de delegación básica y permite enviar elementos en nombre del propietario y gestionar convocatorias de reunión.

---

## Archivos de datos de Outlook

Outlook utiliza archivos de datos para almacenar los mensajes y demás elementos localmente:

|Extensión|Nombre|Descripción|
|---|---|---|
|**.pst**|Personal Storage Table|Archivo de datos personal de Outlook. Almacena mensajes, calendarios, contactos, etc. localmente.|
|**.ost**|Offline Storage Table|Copia local de los datos del servidor Exchange para trabajo sin conexión.|
|**.eml**|Electronic Mail|Formato estándar para guardar mensajes individuales. No es un formato de Microsoft: es el formato de mensaje de Internet (MIME, RFC 5322) que usan muchos programas de correo; Outlook guarda los mensajes individuales en .msg.|

### Importar y exportar contactos

Para importar contactos desde otro programa, Outlook utiliza la función **Importar/Exportar** (accesible desde Archivo).

---

## Grupos de envío y recepción, formato condicional y encabezados

Los **Grupos de envío o recepción** permiten agrupar cuentas de correo para programar la sincronización. Es posible crear un grupo con una **sola cuenta** (la afirmación contraria es incorrecta).

El **formato condicional** permite configurar que los mensajes de un determinado contacto aparezcan con una fuente o estilo distinto en la Bandeja de entrada.

Los **encabezados** (headers) de un correo contienen la información técnica y de enrutamiento del mensaje: campos De, Para, CC, Asunto, fecha y hora, ruta de servidores y protocolos usados. Son útiles para rastrear el origen de un mensaje o detectar phishing.

---

## Funcionamiento técnico del correo electrónico

El proceso completo: (1) el remitente redacta el mensaje en su cliente de correo; (2) al pulsar Enviar, el mensaje va al **servidor SMTP** del remitente; (3) SMTP consulta el **DNS** para localizar el servidor destino; (4) el mensaje viaja entre **servidores intermedios** hasta el servidor del destinatario; (5) el mensaje se **almacena en el buzón** del destinatario; (6) el destinatario lo recupera con **IMAP, POP3 o webmail**.

> El servidor de correo actúa como intermediario: **recibe, almacena y pone a disposición** los mensajes hasta que el destinatario los lee.

Si la dirección del destinatario es incorrecta o inexistente, el servidor SMTP genera un **rebote** (bounced email) y el remitente recibe un aviso de error.

Elegir cuántas

[Hacer test Art. 1](https://www.vence.es/leyes/correo-electronico?selected_articles=1&source=temario)

Art. 2

### El entorno de trabajo

## El entorno de trabajo en Microsoft Outlook 365

Microsoft Outlook 365 integra en una única ventana principal todos los módulos de gestión de comunicación y productividad: correo, calendario, contactos, tareas y notas. Comprender su interfaz es imprescindible para trabajar con eficiencia.

---

## La ventana principal de Outlook

Al iniciar Outlook, la pantalla se divide en varias áreas funcionales que permanecen visibles en todo momento:

- **Cinta de opciones** (parte superior): contiene las pestañas con todos los comandos organizados por función.
    
- **Panel de navegación / Barra de navegación** (lateral izquierdo): acceso rápido a los distintos módulos.
    
- **Lista de elementos** (centro): muestra los mensajes, citas, contactos o tareas del módulo activo.
    
- **Panel de lectura** (derecha o inferior): previsualiza el elemento seleccionado sin necesidad de abrirlo.
    
- **Barra de tareas pendientes** (derecha): resumen de tareas y citas próximas.
    
- **Barra de estado** (parte inferior): información contextual sobre el estado de la aplicación.
    

---

## La cinta de opciones (Ribbon)

La cinta de opciones organiza los comandos en **pestañas** (tabs). Cada pestaña agrupa comandos relacionados en **grupos**. Las pestañas principales en la vista de Correo son:

### Pestaña Inicio

Es la pestaña activa por defecto en la vista de Correo. Contiene los comandos más utilizados:

|Grupo|Comandos principales|
|---|---|
|**Nuevo**|Nuevo correo electrónico, Nuevos elementos (mensaje, cita, reunión, contacto, tarea, nota)|
|**Eliminar**|Eliminar, Archivar, Limpiar conversación (eliminar mensajes redundantes), Correo no deseado|
|**Responder**|Responder, Responder a todos, Reenviar, Reunión de respuesta|
|**Mover**|Reglas, Mover a carpeta, Copiar en carpeta|
|**Etiquetas**|Seguimiento, Categorizar, Marcar/desmarcar como leído|
|**Buscar**|Filtrar correo electrónico, Buscar contacto|

### Pestaña Enviar y recibir

Permite sincronizar las cuentas de correo con el servidor:

|Grupo|Comandos principales|
|---|---|
|**Enviar y recibir**|Enviar/Recibir todas las carpetas (F9), Enviar todo|
|**Servidor**|Actualizar carpeta, Cancelar todo|
|**Descargar**|Descargar encabezados, Descargar el resto del mensaje|
|**Preferencias**|Definir grupos Enviar/Recibir, Trabajar sin conexión|

### Pestaña Carpeta

Gestiona las carpetas del buzón:

|Grupo|Comandos principales|
|---|---|
|**Nuevo**|Nueva carpeta, Nueva carpeta de búsqueda|
|**Acciones**|Cambiar nombre, Copiar, Mover, Eliminar carpeta, Marcar todo como leído|
|**Limpiar**|Limpiar carpeta (eliminar duplicados), Recuperar elementos eliminados|
|**Propiedades**|Directiva, Configuración de Autoarchivar, Permisos de carpeta, Mostrar recuento de todas las carpetas|

> **Importante para el examen:** La opción **Configuración de Autoarchivar** se encuentra en la pestaña **Carpeta**, no en Vista ni en Archivo.

### Pestaña Vista

Controla cómo se visualizan los elementos en Outlook:

|Grupo|Comandos principales|
|---|---|
|**Vista actual**|Cambiar vista (Compacto, Único, Vista previa), Configuración de vista, Restablecer vista|
|**Mensajes**|Mostrar como Conversaciones, Configuración de conversación|
|**Organización**|Panel de lectura, Panel de personas, Barra de tareas pendientes|
|**Diseño**|Panel de carpetas, Barra de acceso rápido|
|**Ventana**|Abrirla en nueva ventana|

### Pestaña Ayuda

Acceso a la ayuda en línea de Microsoft, formación y soporte técnico.

### Pestaña Archivo (Backstage)

Al hacer clic en **Archivo** (extremo izquierdo de la cinta), se abre la vista **Backstage**, que no es una pestaña de cinta al uso. Desde aquí se accede a:

- **Información:** estado de la cuenta, configuración de la cuenta, herramientas de limpieza de buzón.
    
- **Abrir y exportar:** abrir archivos .pst, importar/exportar contactos y datos.
    
- **Guardar como:** guardar mensajes en formatos externos.
    
- **Opciones:** configuración general de Outlook (correo, calendario, contactos, tareas, firmas, etc.).
    
- **Administrar reglas y alertas:** crear y editar reglas de mensajes.
    

---

## Panel de navegación y Barra de navegación

### Barra de navegación

La **barra de navegación** (lateral o inferior según la versión) permite cambiar entre los módulos principales de Outlook. De forma predeterminada muestra **4 iconos**:

1. **Correo** (sobre)
    
2. **Calendario**
    
3. **Contactos** (Personas)
    
4. **Tareas** (To Do)
    

El número máximo de botones o iconos visibles que se pueden configurar en la barra de navegación es **8**. Los iconos adicionales se pueden agregar desde las opciones de configuración de la barra.

> **Pregunta frecuente:** El número máximo de iconos visibles en la barra de navegación de Outlook 365 es **8**. Los predeterminados son **4**.

### Panel de carpetas

Dentro del módulo de Correo, el panel de carpetas muestra la jerarquía de carpetas del buzón. Las **carpetas predeterminadas** en Outlook son:

|Carpeta|Descripción|
|---|---|
|**Bandeja de entrada**|Recibe los mensajes entrantes|
|**Borradores**|Guarda automáticamente los mensajes sin enviar|
|**Elementos enviados**|Copia de cada mensaje enviado correctamente|
|**Elementos eliminados**|Mensajes borrados (permanecen en ella hasta que se vacía)|
|**Correo no deseado**|Mensajes filtrados como spam|
|**Archivo**|Carpeta de archivado de mensajes|
|**Bandeja de salida**|Mensajes pendientes de ser enviados|

> **Importante:** Los mensajes que no se terminan de redactar se guardan automáticamente en **Borradores**. Al eliminar un mensaje (tecla **Supr**), se mueve a **Elementos eliminados**. Si se vacía esa carpeta, los mensajes se **eliminan definitivamente** de ella; con una cuenta Exchange pasan a la carpeta oculta **Elementos recuperables**, desde donde aún pueden rescatarse durante un tiempo con **Inicio > Recuperar elementos eliminados del servidor**.

### Gestión de carpetas

Desde la pestaña **Carpeta** o haciendo clic derecho sobre una carpeta se puede:

- **Crear** nuevas carpetas (también con Ctrl+Mayús+E).
    
- **Renombrar** carpetas existentes.
    
- **Mover** carpetas a otras ubicaciones.
    
- **Eliminar** carpetas (y su contenido pasa a Elementos eliminados).
    
- **Configurar el Autoarchivar** para cada carpeta individualmente.
    

---

## Panel de lectura

El **panel de lectura** muestra una vista previa del mensaje seleccionado sin necesidad de abrirlo. Se puede configurar en tres posiciones:

- **A la derecha** (posición predeterminada): el panel aparece a la derecha de la lista de mensajes.
    
- **En la parte inferior**: el panel aparece debajo de la lista de mensajes.
    
- **Desactivado**: el panel queda oculto. Para ocultarlo completamente se usa la pestaña **Vista > Panel de lectura > Desactivado**.
    

---

## Panel de personas

El **panel de personas** (People Pane) aparece en la parte inferior del panel de lectura y muestra información sobre el remitente del mensaje seleccionado: nombre, foto de perfil, mensajes recientes y archivos compartidos.

---

## Barra de tareas pendientes

La **barra de tareas pendientes** (To-Do Bar) se muestra a la derecha de la ventana y ofrece un resumen accesible desde cualquier vista de Outlook. Muestra:

- Un **miniconsultario** (navegador de fechas).
    
- Las **citas próximas** de los días siguientes.
    
- Las **tareas pendientes** con fecha de vencimiento.
    

> Es accesible y visible desde cualquier módulo de Outlook (correo, calendario, contactos, tareas).

---

## Barra de estado

La **barra de estado** se sitúa en la parte inferior de la ventana de Outlook. Muestra información contextual sobre el módulo activo:

- **Número de elementos** en la carpeta seleccionada.
    
- **Número de mensajes no leídos**.
    
- **Estado de conexión** (conectado / trabajando sin conexión).
    
- **Progreso** de operaciones de envío y recepción.
    
- **Controles de zoom** del panel de lectura.
    

> **Lo que NO muestra la barra de estado:** el espacio disponible en la cuenta o la dirección de correo del remitente del mensaje seleccionado.

---

## Barra de herramientas de acceso rápido

La **barra de herramientas de acceso rápido** (Quick Access Toolbar, QAT) se encuentra en la parte **superior izquierda** de la ventana, sobre la cinta de opciones. Permite personalizar atajos de acceso rápido a los comandos más usados. Los accesos predeterminados incluyen: Enviar y recibir, Deshacer y Rehacer.

---

## Vistas de la lista de mensajes

En la vista de Correo, los mensajes se pueden visualizar de tres formas (Vista actual > Cambiar vista):

|Vista|Descripción|
|---|---|
|**Compacto**|Muestra el remitente, asunto y un fragmento del mensaje en líneas reducidas|
|**Único**|Muestra cada mensaje en una fila única con columnas separadas para remitente, asunto y fecha|
|**Vista previa**|Muestra varias líneas del mensaje bajo el asunto|

---

## Vista Conversación

La **vista de conversación** agrupa todos los mensajes que comparten el mismo **asunto** (y sus respuestas y reenvíos) en un único hilo expandible. Se activa desde **Vista > Mostrar como Conversaciones**.

Dentro de la **Configuración de conversación** (pestaña Vista, grupo Mensajes) están disponibles estas opciones:

- Mostrar mensajes de otras carpetas.
    
- Expandir siempre la conversación seleccionada.
    
- Usar vista con sangría clásica.
    
- Mostrar siempre los remitentes encima del asunto.
    

> **Lo que NO es una opción de Configuración de conversación:** "Ocultar remitentes duplicados" no existe como opción en este menú.

Al usar **"Responder a todos"** en un mensaje recibido, el nuevo mensaje tendrá como destinatarios al remitente original y a todos los que estaban en los campos **Para** y **CC** del mensaje recibido (nunca a los de CCO).

---

## Búsqueda de mensajes

La **barra de búsqueda** de Outlook 365 permite localizar mensajes, contactos, citas y tareas mediante texto libre u operadores de búsqueda:

- **Búsqueda simple:** escribir una palabra devuelve todos los elementos que la contienen (coincidencia por prefijo). Ejemplo: escribir "proyecto" devuelve mensajes que contienen "proyecto", "proyectos", etc.
    
- **Búsqueda de frase exacta:** poner la frase entre comillas. Ejemplo: "solicitud aprobada".
    
- **Operadores de campo:** restringen la búsqueda a un campo concreto. Ejemplo: Asunto:oferta busca solo en el campo Asunto.
    
- **Operador NO (NOT):** excluye términos. Ejemplo: Asunto:oferta NO primera busca mensajes con "oferta" en el asunto pero sin la palabra "primera".
    
- **Búsqueda avanzada:** Ctrl+Mayús+F.
    

Desde la pestaña **Inicio**, el grupo **Buscar** incluye el comando **Filtrar correo electrónico** con opciones para mostrar solo mensajes: No leídos, Con marca, Adjuntos, A mí, En copia, Categorizados, Urgentes, Próximos 7 días, etc.

En Microsoft Outlook, el criterio de disposición **"Para"** permite agrupar los mensajes de una carpeta según su destinatario.

---

## Gestión de mensajes

### Importancia y seguimiento

Los mensajes en Outlook pueden marcarse con tres niveles de **importancia**:

- **Alta** (exclamación roja `!`): indica que el mensaje requiere atención prioritaria.
    
- **Normal**: valor predeterminado.
    
- **Baja** (flecha hacia abajo azul).
    

> **Atención:** Un correo con **exclamación roja** tiene marcada importancia alta.

Las **marcas de seguimiento** permiten añadir un recordatorio a mensajes recibidos o enviados para gestionarlos posteriormente. Se pueden aplicar a cualquier mensaje de correo electrónico. Las opciones de seguimiento disponibles incluyen: Hoy, Mañana, Esta semana, La próxima semana, Sin fecha y Personalizada. El comando de **seguimiento personalizado** se abre con **Ctrl+Mayús+G**.

> **Lo que NO es una opción de Seguimiento:** "Mes siguiente" no aparece en el menú de seguimiento de Outlook.

**Bandera roja** junto a un correo: sirve para marcar el seguimiento de un correo, indicando que requiere atención o acción posterior.

### Categorías de color

Las **categorías de color** permiten asignar una etiqueta visual a cualquier elemento de Outlook (mensajes, citas, contactos, tareas). Hay varias categorías habilitadas por defecto que se pueden modificar, eliminar o renombrar. También es posible **crear nuevas categorías** y **asignar teclas de método abreviado** a cada una.

### Correo no deseado (spam)

Outlook incluye un **filtro antispam** que evalúa los mensajes entrantes y mueve automáticamente los sospechosos a la carpeta **Correo no deseado**. Se puede configurar el **nivel de protección**:

- Cuanto mayor sea el nivel de protección, mayor será el riesgo de que mensajes legítimos (falsos positivos) sean clasificados como no deseados.

Si un usuario marca un mensaje como **"No es correo no deseado"**, el mensaje vuelve a la Bandeja de entrada y el remitente puede añadirse a la lista de remitentes seguros.

Los **correos de phishing** son los que tratan de conseguir información confidencial (contraseñas, datos bancarios) de forma fraudulenta, haciéndose pasar por entidades legítimas. El **spam** es correo comercial no solicitado.

### Eliminar y purgar mensajes

- **Supr:** mueve el mensaje a Elementos eliminados. _(Ctrl+D en el módulo Correo responde al mensaje; en Tareas sí elimina el elemento)_
    
- **Mayús+Supr:** elimina permanentemente (no pasa por Elementos eliminados).
    
- **Vaciar Elementos eliminados:** elimina definitivamente todos los mensajes de esa carpeta (con una cuenta Exchange pasan a la carpeta oculta Elementos recuperables, desde donde aún pueden rescatarse un tiempo).
    
- **Limpiar conversación:** el comando **Limpiar** de Outlook elimina los mensajes repetidos o redundantes de la conversación o de la carpeta seleccionada enviándolos a Elementos eliminados.
    
- **Purgar:** en una cuenta IMAP, un mensaje eliminado puede quedar marcado para su eliminación (tachado, sin salir de su carpeta); **Purgar** elimina definitivamente esos mensajes marcados del servidor IMAP, sin posibilidad de restaurarlos.
    

---

## Redacción de mensajes

Al crear un nuevo mensaje, la ventana de redacción incluye sus propias pestañas:

|Pestaña|Contenido principal|
|---|---|
|**Mensaje**|Comandos de portapapeles, fuente, párrafo, responder, etiquetas y zoom|
|**Insertar**|Adjuntar archivo, firma, tablas, imágenes, hipervínculo, emoji, elementos rápidos|
|**Opciones**|CCO, De (remitente alternativo), Cifrado, Retrasar entrega, Confirmaciones (entrega, lectura), envío de las respuestas a otra dirección|
|**Formato de texto**|Negrita, cursiva, color de fuente, estilos, Cambiar estilos (conjunto de estilos, colores, fuentes)|
|**Revisar**|Ortografía y gramática, sinónimos, traducir|

> **Importante para el examen:** El botón **"Cambiar estilos"** (que modifica el conjunto de estilos, colores, fuentes y espacio entre párrafos) se encuentra en la pestaña **Formato de texto** de la ventana de redacción.

### Campos del mensaje

|Campo|Descripción|
|---|---|
|**Para**|Destinatario principal (obligatorio para enviar)|
|**CC** (Con Copia)|Destinatarios en copia (ven a los de Para y CC, pero no a los de CCO)|
|**CCO** (Con Copia Oculta)|Destinatarios en copia oculta (los demás no pueden verlos)|
|**Asunto**|Título breve que describe el contenido del mensaje|
|**Cuerpo**|Contenido del mensaje|

> Para enviar correo a varios destinatarios sin que se vean entre sí: usar el campo **CCO**.

Para enviar un correo solo es imprescindible indicar al menos un **destinatario** (en **Para**, **CC** o **CCO**). El **asunto** y el **cuerpo del mensaje** son opcionales: si el asunto está vacío, Outlook avisa antes de enviar, pero permite enviarlo igualmente. El remitente (**De**) lo rellena Outlook con la cuenta desde la que se envía.

### Adjuntos y opciones de envío

El tamaño máximo depende del tipo de cuenta: en la aplicación de Outlook, las cuentas de correo de Internet (Outlook.com, Gmail) tienen un límite de **20 MB** por mensaje, incluidos los adjuntos, y las cuentas de **Exchange** de **10 MB** por defecto; en **Outlook.com** (la web), el límite de un archivo adjunto es de **25 MB**, y de **2 GB** si se adjunta desde OneDrive.

> **Ojo con la pregunta:** si se pregunta por la **aplicación de Outlook** y una cuenta de Internet, la cifra es **20 MB**; si se pregunta por **Outlook.com**, es **25 MB**. Fuentes oficiales de Microsoft: «Para las cuentas de correo electrónico de Internet, como Outlook.com o Gmail, el límite de tamaño del correo electrónico es de 20 megabytes (MB)» ([https://support.microsoft.com/es-es/outlook/reduce-attachment-size-to-send-large-files-with-outlook](https://support.microsoft.com/es-es/outlook/reduce-attachment-size-to-send-large-files-with-outlook); en inglés, «For internet email accounts such as Outlook.com or Gmail, the email size limit is 20 megabytes (MB)», [https://support.microsoft.com/en-us/outlook/reduce-attachment-size-to-send-large-files-with-outlook](https://support.microsoft.com/en-us/outlook/reduce-attachment-size-to-send-large-files-with-outlook)) y «El tamaño límite de los datos adjuntos para archivos es de 25 MB» ([https://support.microsoft.com/es-es/outlook/sending-limits-in-outlook-com](https://support.microsoft.com/es-es/outlook/sending-limits-in-outlook-com); en inglés, «The attachment size limit for files is 25 MB», [https://support.microsoft.com/en-us/outlook/sending-limits-in-outlook-com](https://support.microsoft.com/en-us/outlook/sending-limits-in-outlook-com)).

La opción **Retrasar entrega** (pestaña Opciones del mensaje) permite programar una fecha y hora concretas para que el mensaje se envíe. Mientras no llega ese momento, el mensaje permanece en la **Bandeja de salida**. Si se pulsa "Enviar" accidentalmente y el mensaje está todavía en la Bandeja de salida, aún es posible abrirlo y borrarlo.

Desde la pestaña Opciones del mensaje se pueden solicitar:

- **Confirmación de entrega:** notifica cuando el mensaje llega al servidor del destinatario.
    
- **Confirmación de lectura:** notifica cuando el destinatario abre el mensaje (si este lo permite).
    

### Responder, Responder a todos, Reenviar

Estos tres comandos se encuentran en la pestaña **Inicio** de la cinta de opciones (grupo Responder):

|Acción|Resultado|
|---|---|
|**Responder**|Nuevo mensaje dirigido solo al remitente original|
|**Responder a todos**|Nuevo mensaje al remitente y a todos los de los campos Para y CC|
|**Reenviar**|Nuevo mensaje con el contenido original para enviarlo a un tercero|

> El prefijo **RE:** al inicio del asunto indica que el mensaje es una respuesta. El prefijo **RV:** indica que es un reenvío.

### Respuestas automáticas (fuera de la oficina)

Las respuestas automáticas se configuran desde **Archivo > Respuestas automáticas**. Permiten establecer un mensaje automático que se envía cuando se recibe un correo durante el período configurado (inicio y fin). Se pueden configurar mensajes distintos para personas de dentro y fuera de la organización.

> **Dónde se encuentran las Respuestas automáticas:** en **Archivo** (Archivo > Respuestas automáticas), no en la pestaña Inicio. Solo aparecen con cuentas que las admiten (Exchange); con Gmail, Yahoo u otras cuentas POP o IMAP se usa una regla.

### Identidades múltiples y dirección de respuesta

Desde un cliente Outlook, sí es posible enviar correos con **identidades diferentes** si se tienen varias cuentas configuradas o si se usa el campo **"De"** (pestaña Opciones). Desde la pestaña **Opciones** también se puede hacer que las respuestas al mensaje se dirijan a una dirección diferente de la que lo envía.

---

## Reglas de mensajes

Las **reglas** permiten automatizar la gestión del correo (mover, eliminar, reenviar, categorizar, marcar, etc.) según condiciones definidas por el usuario.

Existen dos tipos:

- **Reglas basadas en servidor:** se ejecutan en el servidor Exchange aunque Outlook no esté abierto.
    
- **Reglas solo de cliente:** se ejecutan únicamente cuando Outlook está en ejecución en el equipo local.
    

Para crear o gestionar reglas: **Inicio > Mover > Reglas > Administrar reglas y alertas** o desde **Archivo > Administrar reglas y alertas**.

Las reglas pueden basarse en condiciones como: remitente, asunto, tamaño, importancia, palabras clave, etc. Las acciones disponibles incluyen: mover a carpeta, eliminar, reenviar, responder con plantilla, marcar con seguimiento, cambiar importancia, etc.

---

## Grupos de envío y recepción

Los **grupos de envío y recepción** permiten configurar qué cuentas de correo se sincronizan, con qué frecuencia y qué carpetas se descargan. Se configuran desde **Enviar y recibir > Definir grupos Enviar/Recibir**.

---

## Limpieza del buzón

Outlook 365 incluye varias herramientas para administrar el tamaño del buzón, accesibles desde **Archivo > Herramientas de limpieza del buzón**:

- **Limpieza de buzón:** muestra estadísticas del tamaño del buzón y permite encontrar y eliminar elementos grandes o antiguos.
    
- **Autoarchivar:** mueve elementos antiguos a un archivo .pst automáticamente.
    
- **Vaciar carpeta Elementos eliminados.**
    
- **Limpiar carpeta Elementos eliminados.**
    

---

## Módulo Calendario

### Vistas del calendario

El calendario de Outlook ofrece las siguientes vistas:

|Vista|Descripción|Atajo|
|---|---|---|
|**Día**|Muestra las horas de un solo día|Ctrl+Alt+1|
|**Semana laboral**|Muestra los días laborables (lun-vie)|Ctrl+Alt+2|
|**Semana**|Muestra los 7 días de la semana|Ctrl+Alt+3|
|**Mes**|Vista mensual completa|Ctrl+Alt+4|
|**Programación**|Vista en franjas horizontales para comparar calendarios|—|

> **Al hacer doble clic sobre un día en la vista Mes:** se abre el formulario de una **cita nueva** para esa fecha. Como se pincha el día entero y no una franja horaria, Outlook la propone marcada como **Evento de todo el día**. Es el mismo comportamiento del doble clic en cualquier área en blanco del calendario, en todas las vistas.

> ⚠️ El doble clic **no cambia de vista**. Para pasar a la vista Día se usa la cinta (**Inicio > Organizar > Día**) o el atajo **Ctrl+Alt+1** de la tabla anterior.

### Tipos de elementos del calendario

|Tipo|Descripción|
|---|---|
|**Cita**|Evento personal sin invitados externos; solo afecta al propio calendario|
|**Reunión**|Evento con invitados; Outlook envía convocatoria por correo electrónico|
|**Evento**|Ocupa todo el día (o varios días) sin bloquear franjas horarias específicas|

- Las reuniones permiten usar el **Asistente para programación** (botón de la cinta del formulario de reunión) para ver la disponibilidad de todos los invitados y de las salas antes de confirmar la hora.
    
- Las citas recurrentes (diarias, semanales, mensuales, anuales) al eliminarse ofrecen la opción de borrar **solo esa ocurrencia** o **todas las recurrencias**.
    

---

## Módulo Contactos (Personas)

Outlook permite gestionar contactos individuales y **grupos de contactos** (antes llamados listas de distribución). Un grupo de contactos agrupa varias direcciones de correo para simplificar el envío masivo.

> En la página **Contactos**, para crear un grupo de contactos hay que seleccionar **Nuevo grupo de contactos** (no "Nueva lista de correo" ni "Nueva libreta de direcciones").

Desde la vista de contactos se puede:

- Ver, crear, editar y eliminar contactos.
    
- Enviar correo electrónico a un contacto.
    
- Programar una reunión con un contacto.
    
- Compartir contactos individuales (adjuntándolos como .vcf / vCard).
    
- Exportar contactos a CSV desde Archivo > Abrir y exportar > Importar/Exportar.
    

La **libreta de direcciones** centraliza todos los contactos y listas de distribución. Se abre con **Ctrl+Mayús+B**. Para verla, en la pestaña **Inicio**, grupo **Buscar**, se elige **Libreta de direcciones**; para **agregar** otra libreta de direcciones se va a **Archivo > Configuración de la cuenta > Configuración de la cuenta**, pestaña **Libretas de direcciones**, **Nuevo**.

> **Permisos al compartir una carpeta de contactos:** se usan los mismos niveles predefinidos de los permisos de carpeta (Propietario, Editor, Autor, Revisor…); «Solo lectura» corresponde a **Revisor**. No existe el nivel «Administrador del sistema».

---

## Módulo Tareas

Las tareas de Outlook permiten registrar compromisos con fecha de vencimiento, prioridad, estado y porcentaje de completado.

### Campos de una tarea

|Campo|Descripción|
|---|---|
|**Asunto**|Nombre de la tarea|
|**Fecha de inicio**|Cuándo empieza|
|**Fecha de vencimiento**|Fecha límite (se configura haciendo clic en "Fecha de vencimiento" en la ventana de la tarea)|
|**Estado**|Situación general de la tarea (por ejemplo, si no ha comenzado, si está en curso o si ya está terminada)|
|**Prioridad**|Importancia relativa de la tarea, en tres niveles|
|**% completado**|Porcentaje de avance|
|Aviso emergente|Se puede activar en la ventana de la tarea para que Outlook muestre un aviso emergente en la fecha y hora que se definan|

- Si la tarea se hace periódica (botón **Periodicidad**), se crea una nueva ocurrencia de la tarea automáticamente al completar la anterior.
    
- Al **arrastrar un correo electrónico a la sección de Tareas**, Outlook crea una nueva tarea usando el asunto y el cuerpo del mensaje (copia del correo como tarea).
    
- Para **eliminar varias tareas a la vez**: seleccionarlas con Ctrl+clic y pulsar Supr.
    

### Diferencia entre tarea, cita y reunión

La **tarea** solo tiene fecha de vencimiento y no bloquea la agenda ni tiene invitados. La **cita** tiene fecha/hora fija y bloquea la agenda pero no tiene invitados. La **reunión** tiene fecha/hora fija, bloquea la agenda y envía convocatoria a los invitados.

La **barra de tareas pendientes** (To-Do Bar) muestra un resumen de tareas y citas próximas accesible desde cualquier vista.

---

## Ejecución inicial, cuentas y seguridad

Si se ejecuta Outlook sin ninguna cuenta configurada, el asistente de configuración de cuentas se inicia automáticamente. Se puede añadir una nueva cuenta desde **Archivo > Agregar cuenta**.

Recomendaciones de seguridad básica: no abrir mensajes de remitentes desconocidos, no hacer clic en enlaces ni descargar adjuntos sospechosos, usar contraseñas seguras y activar la verificación en dos pasos. Responder correos desde dispositivos móviles no es una recomendación de seguridad específica.

Los **sistemas de acceso al correo que NO son webmail** (clientes de escritorio): Microsoft Outlook, Mozilla Thunderbird, Apple Mail. Los **webmail** son accesibles por navegador: Gmail, Outlook.com, Yahoo Mail.

---

<!-- ampliado claude_code_mislink_review_2026_07 (Microsoft Support: https://support.microsoft.com/es-es/office/agregar-gr%C3%A1ficos-a-mensajes-en-outlook-114bb251-861f-41cd-b20f-7e7289630c5b) -->

## Insertar gráficos de Excel en un mensaje

Outlook permite **crear** un gráfico de Excel directamente desde el editor de mensajes, sin tener que crearlo antes en Excel:

1. Haga clic en el cuerpo del mensaje.
    
2. En la pestaña **Insertar**, grupo **Ilustraciones**, elija **Gráfico**.
    
3. Elija el tipo de gráfico y pulse **Aceptar**.
    
4. En la hoja de cálculo de Excel que aparece, escriba los datos y ciérrela.
    

> **Fuente oficial:** Microsoft Support — «Agregar gráficos a mensajes en Outlook». La ruta correcta es **Insertar → Ilustraciones → Gráfico** (no «Opciones → grupo Excel»).

---

<!-- ampliado claude_code_mislink_review_2026_07 (Microsoft Support: https://support.microsoft.com/es-es/office/compartir-y-obtener-acceso-al-buz%C3%B3n-o-carpeta-de-otra-persona-en-outlook-a909ad30-e413-40b5-) -->

## Corrección — Niveles de permiso al compartir una carpeta (contactos, calendario, correo)

Al compartir una carpeta, Outlook ofrece niveles de permiso predefinidos que descienden de mayor a menor derecho: **Propietario**, **Editor de publicación**, **Editor**, **Autor de publicación**, **Autor**, **Autor no editor**, **Revisor** (solo lectura), **Colaborador** y **Ninguno**.

> **Fuente oficial:** Microsoft Support — «Compartir y obtener acceso al buzón o carpeta de otra persona en Outlook». **Propietario SÍ es un nivel de permiso válido** (el más alto). «Solo lectura» se corresponde con **Revisor**. NO existe el nivel «Administrador del sistema».

Elegir cuántas

[Hacer test Art. 2](https://www.vence.es/leyes/correo-electronico?selected_articles=2&source=temario)

Art. 3

### Atajos de teclado

## Atajos de teclado en Microsoft Outlook 365

El dominio de los métodos abreviados de teclado permite trabajar con Outlook de forma mucho más ágil. A continuación se recogen todos los atajos que aparecen en las preguntas de examen, organizados por categoría.

---

## Crear elementos nuevos

|Atajo|Acción|
|---|---|
|**Ctrl+N**|Nuevo mensaje (desde vista Correo) / Nueva cita (Calendario) / Nuevo contacto (Contactos) / Nueva tarea (Tareas)|
|**Ctrl+Mayús+M**|Nuevo mensaje de correo desde **cualquier** vista o módulo|
|**Ctrl+Mayús+A**|Nueva cita en el calendario desde **cualquier** vista|
|**Ctrl+Mayús+Q**|Nueva convocatoria de reunión desde **cualquier** vista|
|**Ctrl+Mayús+C**|Nuevo contacto desde **cualquier** vista|
|**Ctrl+Mayús+L**|Nuevo grupo de contactos (lista de distribución)|
|**Ctrl+Mayús+K**|Nueva tarea desde **cualquier** vista|

> **Nuevo mensaje de correo:** desde cualquier vista de Outlook es **Ctrl+Mayús+M**, y es el que recoge la documentación oficial de Microsoft (en español y en inglés). Desde la vista Correo, la documentación da **Ctrl+N**, que es el atajo internacional; en el **Outlook clásico instalado en español** ese atajo está localizado y es **Ctrl+U** (así lo muestra la información emergente del botón «Nuevo correo electrónico»), mientras que en el **Nuevo Outlook** es Ctrl+N. Como Ctrl+U no figura en la documentación oficial, en una pregunta de examen el atajo que se puede sostener sin discusión es Ctrl+Mayús+M. (No confundir con los atajos de leído/no leído: **Ctrl+Q** marca como **leído**; para **no leído** el atajo depende de la versión — ver la tabla de abajo.)

| **Ctrl+Mayús+E** | Nueva carpeta | | **Ctrl+Mayús+N** | Nueva nota |

> **Clave de examen:** Ctrl+Mayús+M crea un **nuevo mensaje**, no abre el calendario. Ctrl+Mayús+Q crea una **nueva solicitud de reunión**, no responde a todos (ese es Ctrl+Mayús+R).

---

## Gestión de mensajes

|Atajo|Acción|
|---|---|
|**Ctrl+R**|Responder al remitente|
|**Ctrl+Mayús+R**|Responder a todos (remitente y destinatarios de Para y CC)|
|**Ctrl+F**|Reenviar el mensaje seleccionado|
|**Ctrl+Alt+F**|Reenviar el mensaje como datos adjuntos|
|**Ctrl+Alt+R**|Responder al mensaje con una convocatoria de reunión|
|**Ctrl+Enter**|Enviar el mensaje (equivalente al botón Enviar)|
|**Alt+S**|Enviar el mensaje|
|**Ctrl+Q**|Marcar el mensaje como leído|
|**Ctrl+S** (Outlook de escritorio, clásico y nuevo) · **Ctrl+U** (Outlook en la Web)|Marcar el mensaje como no leído|
|**Ctrl+D**|En Correo **no elimina**: Microsoft es-ES lo da como «Responder a un mensaje» (ver el aviso de abajo). Para eliminar, **Supr**|
|**Supr**|Eliminar el mensaje seleccionado (mueve a Elementos eliminados)|
|**Mayús+Supr**|Eliminar permanentemente (sin pasar por Elementos eliminados)|
|**Ctrl+Mayús+V**|Mover el mensaje a una carpeta específica|
|**Ctrl+Mayús+G**|Abrir el cuadro de diálogo de seguimiento personalizado (asignar marca de seguimiento)|
|**Intro (Enter)**|Abrir el mensaje seleccionado|
|**Ctrl+A**|Abrir un mensaje recibido (así lo da la tabla de Microsoft para el Outlook clásico en español)|
|**Retroceso**|Archivar el elemento seleccionado|

> **Distinción clave:** Ctrl+Q marca como **leído**. Para **no leído**, Microsoft da **Ctrl+S** en el Outlook de escritorio (clásico y nuevo) y **Ctrl+U** en Outlook en la Web. Fuente: Microsoft Support es-ES, «Métodos abreviados de teclado de Outlook» (actualizada el 02/02/2026).

> **Distinción clave:** **Supr** elimina el mensaje (mueve a Elementos eliminados). Es el atajo de eliminar en las tres versiones de Outlook (clásico, nuevo y web). Para responder: **Ctrl+R** o **Ctrl+D** según la tabla de Microsoft (ver el aviso de abajo); a todos, **Ctrl+Mayús+R**.

> **⚠️ Ctrl+D — atajo multifuncional según el módulo activo:**

> Microsoft asigna distintas acciones a Ctrl+D dentro de Outlook clásico según el módulo en el que estés trabajando:

> | Módulo activo | Acción de Ctrl+D |

> |---|---|

> | **Correo** (mensaje seleccionado) | Responder al mensaje (tabla de correo del Outlook clásico y tablas del nuevo Outlook) |

> | **Calendario** (reunión seleccionada, Outlook clásico) | Responder a todos los convocados a una reunión con un mensaje |

> | **Tareas** | **Eliminar el elemento seleccionado** / Rechazar una solicitud de tarea |

> | **Contactos (Nuevo Outlook)** | Crear un contacto o lista de contactos (también con la tecla Eliminar) |

> | **Editor de texto** (al redactar un mensaje, nuevo Outlook) | Alinear un párrafo a la derecha |

> **Ctrl+D solo elimina en Tareas.** En Correo, Microsoft es-ES lo da como **Responder**: «Responder mensaje de correo» (nuevo Outlook) y «Responder a un mensaje» (tabla de correo del Outlook clásico). La misma página da también **Ctrl+R** para responder en la tabla de «más usados» del Outlook clásico y en Outlook en la Web, así que la fuente oficial asigna Responder a las dos teclas según la tabla. Lo que no da en ninguna versión es Ctrl+D para eliminar un mensaje: eliminar es **Supr**.

> **Además, el Nuevo Outlook para Windows** permite cambiar el conjunto de atajos en **Configuración → Accesibilidad → Métodos abreviados de teclado** entre cuatro perfiles: "Outlook" (el predeterminado, que es el que se evalúa), "Hotmail", "Gmail" y "Yahoo". En el modo "Hotmail" (heredado de Outlook.com) Ctrl+D pasa a eliminar el mensaje, lo que añade otra fuente de confusión.

> **Fuente oficial:** [Microsoft Support — Métodos abreviados de teclado para Outlook](https://support.microsoft.com/es-es/office/m%C3%A9todos-abreviados-de-teclado-para-outlook-3cdeb221-7ae5-4c1d-8c1d-9e63216c1efd)

---

## Enviar y recibir

|Atajo|Acción|
|---|---|
|**F9**|Enviar y recibir todos los correos de todas las cuentas|
|**Ctrl+M**|Enviar y recibir todos los correos (equivalente a F9)|

> **F9 y Ctrl+M son equivalentes** para sincronizar todas las cuentas configuradas en Outlook.

---

## Búsqueda

|Atajo|Acción|
|---|---|
|**Ctrl+E**|Ir al cuadro de búsqueda|
|**F3**|Ir al cuadro de búsqueda / buscar un contacto u otro elemento|
|**Ctrl+Mayús+F**|Abrir la búsqueda avanzada|
|**Ctrl+Mayús+P**|Crear una nueva carpeta de búsqueda|

> **F3 y Ctrl+E** llevan al cuadro de búsqueda. Ctrl+Mayús+P abre la ventana "Nueva carpeta de búsqueda".

---

## Navegación entre módulos

|Atajo|Módulo al que navega (Outlook de Microsoft 365, escritorio)|
|---|---|
|**Ctrl+1**|Correo|
|**Ctrl+2**|Calendario|
|**Ctrl+3**|Copilot|
|**Ctrl+4**|Personas (People: contactos y libreta de direcciones)|
|**Ctrl+5**|To Do|
|**Ctrl+6**|Panel del Explorador de la organización|
|**Ctrl+7**|Loop|
|**Ctrl+8**|Tareas|
|**Ctrl+Mayús+B**|Abrir la Libreta de direcciones|
|**Ctrl+Mayús+I**|Ir a la Bandeja de entrada|
|**Ctrl+Mayús+O**|Ir a la Bandeja de salida|
|**Ctrl+Y**|Ir a otra carpeta (abrir cuadro de diálogo)|

> **Así lo da Microsoft para el Outlook clásico para Windows** (el de escritorio de Microsoft 365), en español y en inglés, con la misma numeración: «Cambiar a la vista **Copilot**. Ctrl+3» · «Cambiar a la vista **People**. Ctrl+4» · «Abra **Tareas**. Ctrl+8» ([es-ES](https://support.microsoft.com/es-es/office/keyboard-shortcuts-for-outlook-3cdeb221-7ae5-4c1d-8c1d-9e63216c1efd)); «Switch to the **Copilot** view. Ctrl+3» · «Switch to the **People** view. Ctrl+4» · «Open **Tasks**. Ctrl+8» ([en-US](https://support.microsoft.com/en-us/office/keyboard-shortcuts-for-outlook-3cdeb221-7ae5-4c1d-8c1d-9e63216c1efd)). La propia página avisa de que estos números «pueden cambiar en función de la configuración de la aplicación».

> **Versiones anteriores (Outlook 2016, 2019 y 2021):** la numeración era otra: Ctrl+3 = Contactos, Ctrl+4 = Tareas, Ctrl+5 = Notas, Ctrl+6 = Lista de carpetas, Ctrl+7 = Accesos directos y Ctrl+8 = Diario. Es la que preguntó, por ejemplo, el examen de Auxiliar Administrativo del Estado de 2023. Si tu convocatoria fija Microsoft 365, la que vale es la de la tabla de arriba.

---

## Libreta de direcciones y contactos

|Atajo|Acción|
|---|---|
|**Ctrl+Mayús+B**|Abrir la Libreta de direcciones|
|**Ctrl+Mayús+C**|Nuevo contacto desde cualquier vista|
|**F3**|Buscar un contacto (también desde el cuadro de búsqueda general)|

---

## Vistas del Calendario

|Atajo|Vista del calendario|
|---|---|
|**Ctrl+Alt+1**|Vista Día|
|**Ctrl+Alt+2**|Vista Semana laboral (lunes a viernes)|
|**Ctrl+Alt+3**|Vista Semana (7 días)|
|**Ctrl+Alt+4**|Vista Mes|
|**Ctrl+G**|Ir a una fecha específica / configurar periodicidad de la cita|

> **Regla mnemotécnica:** Ctrl+Alt+1 = 1 día, Ctrl+Alt+2 = semana laboral (5 días), Ctrl+Alt+3 = semana completa (7 días), Ctrl+Alt+4 = mes.

---

## Preguntas de examen resueltas sobre atajos

A continuación se resumen las correspondencias que más veces han aparecido en preguntas de oposición:

|Atajo|Acción — descripción completa|
|---|---|
|**Ctrl+R**|Responder al remitente del mensaje|
|**Ctrl+Mayús+R**|Responder a todos (remitente y destinatarios de Para y CC). **No** crea una solicitud de reunión|
|**Ctrl+F**|Reenviar el mensaje. **No** es buscar (en Outlook la búsqueda es Ctrl+E o F3)|
|**Ctrl+N**|Nuevo elemento según la vista activa|
|**Ctrl+Mayús+M**|Nuevo mensaje desde **cualquier** módulo. Un opositor que pulse esto pensando que abre el calendario verá que se crea un nuevo mensaje|
|**Ctrl+Mayús+Q**|Nueva solicitud de reunión desde cualquier módulo. **No** confundir con Ctrl+Mayús+R (responder a todos)|
|**Ctrl+Mayús+A**|Nueva cita desde cualquier módulo|
|**Ctrl+Mayús+K**|Nueva tarea desde cualquier módulo|
|**Ctrl+Mayús+C**|Nuevo contacto desde cualquier módulo|
|**Ctrl+Mayús+E**|Nueva carpeta|
|**Ctrl+Mayús+G**|Asignar seguimiento personalizado (abre cuadro de diálogo de marca)|
|**Ctrl+Mayús+B**|Abrir la Libreta de direcciones|
|**Ctrl+Mayús+F**|Búsqueda avanzada|
|**Ctrl+Mayús+P**|Nueva carpeta de búsqueda|
|**Ctrl+Mayús+I**|Ir a Bandeja de entrada|
|**Ctrl+Mayús+O**|Ir a Bandeja de salida|
|**Ctrl+Mayús+N**|Nueva nota|
|**Ctrl+Enter**|Enviar el mensaje|
|**Alt+S**|Enviar el mensaje (alternativa a Ctrl+Enter)|
|**Ctrl+Q**|Marcar como leído|
|**Ctrl+S** (escritorio) · **Ctrl+U** (Outlook en la Web)|Marcar como no leído|
|**Ctrl+D**|En Correo, responder (tabla de correo del clásico y nuevo Outlook); en Tareas, eliminar el elemento seleccionado|
|**Supr**|Eliminar elemento (mueve a Elementos eliminados)|
|**Ctrl+P**|Imprimir el elemento seleccionado|
|**Ctrl+C**|Copiar|
|**Ctrl+X**|Cortar|
|**Ctrl+V**|Pegar|
|**Ctrl+Z**|Deshacer|
|**F9**|Enviar y recibir todos los mensajes|
|**F3**|Buscar contacto u otro elemento|
|**Ctrl+E**|Ir al cuadro de búsqueda|
|**Ctrl+Alt+1**|Vista Día (calendario)|
|**Ctrl+Alt+2**|Vista Semana laboral (calendario)|
|**Ctrl+Alt+3**|Vista Semana (calendario)|
|**Ctrl+Alt+4**|Vista Mes (calendario)|
|**Ctrl+G**|Ir a fecha / periodicidad (calendario)|
|**Ctrl+1**|Ir a Correo|
|**Ctrl+2**|Ir a Calendario|
|**Ctrl+3**|Ir a Copilot|
|**Ctrl+4**|Ir a Personas (contactos)|
|**Ctrl+5**|Ir a To Do|
|**Ctrl+8**|Ir a Tareas|
|**Intro**|Abrir el mensaje seleccionado|
|**Retroceso**|Archivar el elemento seleccionado|
|**Ctrl+Alt+R**|Responder con convocatoria de reunión|
|**Ctrl+Alt+F**|Reenviar como datos adjuntos|

---

## Errores frecuentes de confusión

|Error típico|Realidad|
|---|---|
|Creer que Ctrl+Mayús+R crea una solicitud de reunión|Ctrl+Mayús+R **responde a todos**; la reunión se crea con Ctrl+Mayús+Q|
|Creer que Ctrl+F busca (como en Word/Excel)|En Outlook, Ctrl+F **reenvía**; la búsqueda es Ctrl+E o F3|
|Creer que Ctrl+Mayús+M abre el calendario|Ctrl+Mayús+M crea un **nuevo mensaje**; el calendario es Ctrl+2|
|Creer que Ctrl+Q marca como no leído|Ctrl+Q marca como **leído**; no leído es **Ctrl+S** en el Outlook de escritorio y **Ctrl+U** en Outlook en la Web|
|Creer que Supr elimina definitivamente|Supr mueve a Elementos eliminados; para eliminar definitivamente hay que usar Mayús+Supr|
|Creer que Ctrl+D elimina mensajes|En Correo, Ctrl+D **no elimina**: Microsoft es-ES lo da como **Responder** (igual que Ctrl+R en otras tablas). El atajo de eliminación en Correo es **Supr**; Ctrl+D solo elimina en **Tareas**. Si en tu Nuevo Outlook Ctrl+D elimina, comprueba el conjunto de atajos en Configuración → Accesibilidad → Métodos abreviados de teclado (debería estar en "Outlook", no en "Hotmail")|

---

## ⚠️ Fuente oficial — verifica siempre Microsoft Support

Los atajos de teclado de Outlook **varían según el módulo activo** (Correo, Calendario, Tareas, Contactos, editor de texto) y **según la versión** (Outlook clásico, Nuevo Outlook para Windows, Outlook en la web). Para evitar confusiones — especialmente con **Ctrl+D**, que cambia de significado según el módulo — la fuente oficial y normativa es la documentación de Microsoft Support en español:

📖 **[Métodos abreviados de teclado para Outlook (Microsoft Support, es-es)](https://support.microsoft.com/es-es/office/m%C3%A9todos-abreviados-de-teclado-para-outlook-3cdeb221-7ae5-4c1d-8c1d-9e63216c1efd)**

Esta página detalla los atajos para cada versión y módulo. Es la única referencia que debe usarse para resolver dudas o discrepancias con materiales de estudio antiguos.

### Casos típicos de confusión documentados

|Atajo|Confusión habitual|Realidad oficial|
|---|---|---|
|**Ctrl+D**|"Elimina mensajes"|En Correo, Ctrl+D **responde** al mensaje (tablas de Microsoft es-ES del nuevo Outlook y de correo del clásico). Solo elimina en **Tareas**.|
|**Ctrl+R**|Responder al mensaje|Ctrl+R responde al remitente («más usados» del Outlook clásico y Outlook en la Web); Ctrl+Mayús+R responde a todos. Ctrl+D **también** responde según otras tablas de la misma página.|
|**Ctrl+Q vs Ctrl+S / Ctrl+U**|Confundir leído / no leído|**Ctrl+Q = leído**. No leído: **Ctrl+S** en el Outlook de escritorio (clásico y nuevo) y **Ctrl+U** en Outlook en la Web.|
|**Ctrl+F**|"Buscar (como en Word/Excel)"|En Outlook, Ctrl+F **reenvía** el mensaje. Buscar es **Ctrl+E** o **F3**.|
|**Supr vs Mayús+Supr**|"Ambos eliminan igual"|**Supr** mueve a Elementos eliminados; **Mayús+Supr** elimina permanentemente.|
|**Nuevo Outlook — perfil de atajos**|"Mi Ctrl+D elimina y la pregunta dice que responde"|El Nuevo Outlook permite cambiar el set de atajos en _Configuración → Accesibilidad → Métodos abreviados de teclado_ entre "Outlook" (predeterminado), "Hotmail", "Gmail" y "Yahoo". En modo "Hotmail" Ctrl+D elimina. Las preguntas evalúan siempre el set por defecto "Outlook".|

---

<!-- ampliado claude_code_mislink_review_2026_07 (Microsoft Support: https://support.microsoft.com/es-es/office/m%C3%A9todos-abreviados-de-teclado-para-outlook-3cdeb221-7ae5-4c1d-8c1d-9e63216c1efd) -->

## Dar formato al texto (editor de mensajes)

Estos atajos actúan sobre el párrafo del cuerpo de un mensaje al redactar (el editor usa el motor de Word):

|Atajo|Acción|
|---|---|
|**Ctrl+T**|Aumentar la sangría / crear una sangría francesa|
|**Ctrl+Mayús+T**|**Disminuir la sangría** del párrafo (reducir la sangría francesa)|

> **Fuente oficial:** Microsoft Support — «Métodos abreviados de teclado para Outlook», sección _Dar formato al texto_. **Ctrl+Mayús+T disminuye la sangría**; no crea correos (Ctrl+N / Ctrl+Mayús+M) ni abre la libreta de direcciones (Ctrl+Mayús+B).

Elegir cuántas

[Hacer test Art. 3](https://www.vence.es/leyes/correo-electronico?selected_articles=3&source=temario)

Art. 4

### Agenda electrónica

La agenda electrónica es la funcionalidad de gestión de calendario, citas, reuniones y tareas integrada habitualmente en los clientes de correo electrónico. Permite crear eventos, invitar participantes, enviar recordatorios, gestionar disponibilidad y compartir calendarios. Conceptos básicos: eventos, tareas, recordatorios, calendarios compartidos, invitaciones por iCalendar (.ics), sincronización con dispositivos móviles, integración con el correo electrónico y con el directorio corporativo.

### Alcance del módulo Calendario

Dentro del módulo Calendario, sin salir de él, se puede: crear, editar y eliminar citas (sin invitados) y reuniones (con invitados); enviar invitaciones y gestionar las respuestas (aceptado, rechazado, provisional); configurar recordatorios y periodicidad; y compartir o publicar calendarios. La gestión de contactos y de listas de distribución no forma parte del módulo Calendario: corresponde al módulo Personas (Contactos).

### Asistente para programación

Al organizar una reunión, el Asistente para programación muestra la disponibilidad de cada asistente (libre, ocupado, provisional o fuera de la oficina) en una cuadrícula de calendario, lo que permite localizar visualmente un intervalo horario en el que coincidan todos los participantes. También muestra la disponibilidad de salas y recursos añadidos a la convocatoria.

Elegir cuántas

[Hacer test Art. 4](https://www.vence.es/leyes/correo-electronico?selected_articles=4&source=temario)


## Microsoft Teams

Microsoft Teams: chat, canales, reuniones y videollamadas

2 de 4 artículos de tu programa

EscucharConfigurar

🔊 Aprovecha el transporte, conducción, gimnasio, paseos, deporte y rutinas diarias para escuchar las leyes — todo suma

[Hacer test de Microsoft Teams →](https://www.vence.es/leyes/microsoft-teams?selected_articles=1,2&source=temario)[🔧 Elegir qué artículos entran](https://www.vence.es/leyes/microsoft-teams?abrir_filtro=1&source=temario_filtro)

Art. 1

### Microsoft Teams: conceptos y canales

Microsoft Teams es la plataforma de comunicación y colaboración de Microsoft 365.

Conceptos fundamentales:

- Equipos: grupos de personas que trabajan juntas en un proyecto o departamento
    
- Canales: espacios de conversación dentro de un equipo, organizados por tema
    
- Canales estándar: visibles para todos los miembros del equipo
    
- Canales privados: solo accesibles para miembros seleccionados
    

Funcionalidades principales:

- Chat individual y grupal
    
- Compartir archivos (almacenados automáticamente en SharePoint)
    
- Integraciones con aplicaciones externas
    
- Notificaciones configurables por canal y tipo de actividad
    
- Los documentos descargados desde Teams se guardan por defecto en la carpeta Descargas
    

### Gestión de notificaciones

Las notificaciones se configuran desde Configuración > Notificaciones y actividad.

Por canal, se puede elegir entre tres niveles: todas las actividades (todos los mensajes y publicaciones nuevas), solo menciones y respuestas, o desactivadas.

En los chats individuales, grupales y de reunión se puede silenciar una conversación concreta sin desactivar el resto de notificaciones de Teams: al silenciarla, el usuario sigue formando parte de la conversación pero deja de recibir avisos de ella, salvo cuando le mencionan directamente (@mención).

El estado de presencia de concentración ("Focusing"; en la documentación oficial en español, «Enfocándose» o «Modo de concentración», y en muchos temarios «Enfocado») **no lo elige el usuario: lo pone Teams automáticamente** cuando empieza un bloque de tiempo de concentración reservado en el calendario de Outlook (con MyAnalytics/Viva Insights). Mientras dura, se silencian todas las notificaciones, hasta que termina ese tiempo de concentración.

Los estados que sí elige el usuario a mano son Disponible, Ocupado, No molestar, Vuelvo enseguida, Aparecer como ausente y Aparecer sin conexión; a cualquiera de ellos, salvo Disponible, se le puede poner una duración, y al terminar Teams restablece el estado.

Teams también puede integrarse con la configuración de notificaciones del sistema operativo (banners y sonidos): hay que tener las notificaciones habilitadas a nivel de sistema operativo para recibir avisos de Teams.

### Acceso a Teams sin instalar nada

Además de la aplicación de escritorio y la móvil, Teams se puede usar **en el navegador**, en **teams.microsoft.com**, sin instalar la aplicación (Teams para la web no está disponible en los navegadores de dispositivos móviles: ahí se usa la aplicación). Para unirse a una reunión también se puede elegir **«Continuar en este explorador»**, sin instalar nada.

### Dónde se guardan los archivos

- Al crear un equipo se crea automáticamente un **sitio de SharePoint** conectado a él: detrás de cada equipo de Teams hay un sitio de SharePoint.
    
- Los archivos de los **canales estándar** se guardan en ese sitio, en la biblioteca de documentos, con una carpeta para cada canal; es lo que se ve en la pestaña **Archivos** del canal.
    
- Cada **canal privado** y cada **canal compartido** tiene **su propio sitio de SharePoint**, al que solo acceden sus miembros.
    

### Grabación y seguridad de las reuniones

- La grabación de una reunión se guarda en el **OneDrive del organizador** (carpeta **Grabaciones**), aunque no haya asistido. La grabación de una **reunión de canal** se guarda en el **sitio de SharePoint** del equipo, en una carpeta **Grabaciones** dentro de Documentos.
    
- El **cifrado de un extremo a otro** de las reuniones **no está activado por defecto**: forma parte de **Teams Premium** (una licencia de complemento) y el organizador tiene que activarlo en las opciones de la reunión antes de que empiece. Solo cifra el audio, el vídeo y el uso compartido de pantalla basado en vídeo (no el chat ni las reacciones), y una reunión cifrada de un extremo a otro admite como máximo 200 participantes.
    

### Búsqueda

En la barra de búsqueda de la parte superior de Teams se escribe un nombre, una palabra clave o una frase, y los resultados se pueden filtrar para ver solo **mensajes**, **contactos** o **archivos**. Para buscar dentro de un chat o un canal concreto se pulsa **Ctrl+F** (cmd+F en macOS) estando en él.

Elegir cuántas

[Hacer test Art. 1](https://www.vence.es/leyes/microsoft-teams?selected_articles=1&source=temario)

Art. 2

### Microsoft Teams: reuniones y videollamadas

Reuniones y videollamadas en Microsoft Teams:

Tipos de reuniones:

- Reuniones programadas con invitación
    
- Reuniones instantáneas (Meet Now)
    
- Reuniones en vivo (Live Events) para grandes audiencias
    
- Webinars
    

Funcionalidades:

- Pantalla compartida
    
- Grabación de reuniones en la nube
    
- Fondos virtuales y desenfoque
    
- Salas de grupos (breakout rooms)
    
- Transcripción automática
    
- Chat durante la reunión
    

Métodos abreviados de teclado (aplicación de escritorio para Windows, según la tabla «Reuniones y llamadas» de Microsoft Support):

- Ctrl+Mayús+A: aceptar videollamada
    
- Ctrl+Mayús+S: aceptar llamada de audio
    
- Ctrl+Mayús+D: rechazar llamada
    
- Alt+Mayús+A: iniciar llamada de audio
    
- Alt+Mayús+V: iniciar videollamada
    
- Ctrl+Mayús+H: finalizar la llamada (de audio o de vídeo)
    
- Ctrl+Mayús+M: activar o desactivar el micrófono (alternar silencio)
    
- Ctrl+Mayús+O: activar o desactivar el vídeo (en la aplicación web no tiene acceso directo)
    
- Ctrl+Mayús+K: levantar o bajar la mano
    
- Ctrl+Mayús+Y: admitir personas desde la notificación de la sala de espera
    

En la aplicación web algunas combinaciones cambian: aceptar videollamada es Alt+Mayús+A y aceptar llamada de audio, Alt+Mayús+S.

### Roles y permisos en las reuniones

Además del organizador, en una reunión de Teams existen varios roles con distinto nivel de control:

- **Organizador:** quien crea la reunión. Tiene el control máximo sobre su configuración y sus participantes.
    
- **Coorganizador:** comparte casi todas las funciones del organizador (gestionar participantes, grabar, silenciar), con una diferencia: no puede cambiar la configuración de la reunión antes de que ésta comience. Los coorganizadores se asignan desde el propio calendario de la reunión.
    
- **Presentador:** puede compartir contenido (pantalla, documentos) durante la reunión.
    
- **Asistente:** es el rol con más restricciones. Puede hablar, compartir vídeo y participar en el chat, pero no tiene control sobre otros participantes ni sobre la configuración de la reunión.
    

**Los roles pueden cambiarse con la reunión ya en marcha**, sin necesidad de finalizarla ni volver a convocarla: desde el botón "Personas" de los controles de la reunión, se pasa el cursor sobre el nombre del participante y se elige "Hacer presentador" o "Hacer asistente".

**El organizador decide quién entra como presentador** mediante la opción "Quién puede presentar" de las opciones de la reunión, con tres valores posibles: solo el organizador y los coorganizadores; las personas de la organización (incluidos invitados); o todos los asistentes — que es el valor por defecto.

**El organizador también controla el acceso a la reunión** con la sala de espera (lobby): puede fijar quién entra directamente y quién queda a la espera de que se le admita.

**Y puede impedir que los asistentes se desmuteen a sí mismos**: es una opción de permisos de los asistentes disponible para el organizador, los coorganizadores y los presentadores; mientras está activada, solo ellos pueden reactivar el micrófono de un asistente.

Elegir cuántas

[Hacer test Art. 2](https://www.vence.es/leyes/microsoft-teams?selected_articles=2&source=temario)

## Microsoft 365

Microsoft 365: Trabajo Colaborativo

5 artículos

EscucharConfigurar

🔊 Aprovecha el transporte, conducción, gimnasio, paseos, deporte y rutinas diarias para escuchar las leyes — todo suma

[Hacer test de Microsoft 365 →](https://www.vence.es/leyes/microsoft-365?selected_articles=1,2,3,4,5&source=temario)[🔧 Elegir qué artículos entran](https://www.vence.es/leyes/microsoft-365?abrir_filtro=1&source=temario_filtro)

Art. 1

### OneDrive: conceptos y configuración

OneDrive es el servicio de almacenamiento en la nube de Microsoft, integrado de forma nativa en Windows.

Conceptos fundamentales:

- Almacenamiento en la nube: archivos accesibles desde cualquier dispositivo
    
- Sincronización: los cambios se reflejan automáticamente en todos los dispositivos
    
- Archivos bajo demanda (solo en línea): los archivos aparecen en el explorador pero no ocupan espacio hasta que se abren
    

Configuración y estado:

- Sincronización selectiva: elegir qué carpetas sincronizar en cada dispositivo
    
- Iconos de estado en el explorador: nube azul (solo en línea), marca verde (sincronizado), flechas circulares (sincronizando)
    
- Accesible desde web (office.com), aplicación de escritorio y dispositivos móviles (Android e iOS)
    
- Longitud máxima de ruta de acceso: 400 caracteres
    
- No requiere formato específico para guardar documentos
    

### Los tres estados de un archivo en el Explorador (Archivos a petición)

- **Solo en línea** (icono de **nube azul**): el archivo se ve en el Explorador pero **no ocupa espacio** en el equipo. **No se puede abrir cuando el dispositivo no está conectado a Internet.**
    
- **Disponible localmente** (**marca de verificación verde**): al abrir un archivo solo en línea, se descarga y pasa a este estado. Se puede abrir siempre, **incluso sin conexión**, y ocupa espacio.
    
- **Siempre disponible** (**círculo verde con la marca blanca**): es el archivo marcado con **«Mantener siempre en este dispositivo»** (clic derecho sobre el archivo o la carpeta). Se descarga, ocupa espacio y está siempre ahí, también sin conexión.
    

### Cargar archivos en OneDrive (web)

En onedrive.com, en la ubicación deseada, se pulsa **Cargar** y se eligen los archivos. En Microsoft Edge o Google Chrome el menú **Cargar** ofrece también **Carpeta**, y se pueden arrastrar carpetas a la web. O sea: se cargan **archivos o carpetas**.

### Cómo protege OneDrive los archivos

- Mientras viajan (del equipo al servicio y entre centros de datos), los datos van **cifrados con TLS**.
    
- Guardados en la nube, **cada archivo está cifrado** con su propia clave **AES256**.
    

Fuentes: [Microsoft Support — Ahorrar espacio en disco con Archivos a petición de OneDrive para Windows](https://support.microsoft.com/es-es/office/ahorrar-espacio-en-disco-con-archivos-a-petici%C3%B3n-de-onedrive-para-windows-0e6860d3-d9f3-4971-b321-7092438fb38e) · [Microsoft Support — Cargar fotografías y archivos en OneDrive](https://support.microsoft.com/es-es/office/cargue-y-guarde-archivos-y-carpetas-en-onedrive-a1397e56-61ec-4ed2-9dac-727bf8ac3357) · [Microsoft Support — Cómo protege OneDrive los datos en la nube](https://support.microsoft.com/es-es/office/c%C3%B3mo-protege-onedrive-los-datos-en-la-nube-23c6ea94-3608-48d7-8bf0-80e142edd1e1)

Elegir cuántas

[Hacer test Art. 1](https://www.vence.es/leyes/microsoft-365?selected_articles=1&source=temario)

Art. 2

### Microsoft Teams: conceptos y canales

Microsoft Teams es la plataforma de comunicación y colaboración de Microsoft 365.

Conceptos fundamentales:

- Equipos: grupos de personas que trabajan juntas en un proyecto o departamento
    
- Canales: espacios de conversación dentro de un equipo, organizados por tema
    
- Canales estándar: visibles para todos los miembros del equipo
    
- Canales privados: solo accesibles para miembros seleccionados
    

Funcionalidades principales:

- Chat individual y grupal
    
- Compartir archivos (almacenados automáticamente en SharePoint)
    
- Integraciones con aplicaciones externas
    
- Notificaciones configurables por canal y tipo de actividad
    
- Los documentos descargados desde Teams se guardan por defecto en la carpeta Descargas
    

Art. 3

### SharePoint y videoconferencias

SharePoint es la plataforma de gestión documental y colaboración empresarial de Microsoft 365.

Incluye todas las funcionalidades de OneDrive más:

- Sitios de equipo para departamentos o proyectos
    
- Bibliotecas de documentos compartidas
    
- Flujos de trabajo automatizados
    
- Listas y páginas web internas (intranet)
    

Trabajo colaborativo:

- Varias personas pueden editar simultáneamente documentos de Word, Excel o PowerPoint almacenados en OneDrive o SharePoint
    
- Los cambios se sincronizan en tiempo real
    
- Se puede ver quién está editando y dónde
    

Videoconferencias en Teams:

- Reuniones con cientos o miles de participantes
    
- Funciones de moderación y control de asistentes
    
- Salas de grupos (breakout rooms)
    
- Transcripción automática
    
- Grabación en la nube
    
- Fondos virtuales y desenfoque
    

### Niveles de permisos en SharePoint

A diferencia de OneDrive personal, SharePoint permite asignar permisos de forma granular en varios niveles jerárquicos, de más amplio a más estrecho:

- Colección de sitios
    
- Sitio y subsitio
    
- Biblioteca o lista
    
- Carpeta
    
- Elemento individual (documento o elemento de lista)
    

Por defecto, cada nivel hereda los permisos de su nivel superior (herencia de permisos): un sitio hereda del sitio raíz de su colección, las bibliotecas y listas heredan del sitio, y los elementos heredan de su biblioteca o lista. Un propietario puede romper esa herencia y asignar permisos exclusivos a un nivel concreto sin afectar al resto.

### Coautoría

Cuando varias personas trabajan **al mismo tiempo** en el mismo documento, se llama **coautoría**. Está disponible para los documentos guardados en **OneDrive** o en **SharePoint**: varias personas pueden trabajar juntas en un documento de Word, una hoja de cálculo de Excel o una presentación de PowerPoint.

### Microsoft To Do

**Microsoft To Do** es la aplicación de **listas de tareas** de Microsoft 365: organiza las tareas en listas personalizables (que se pueden agrupar). Se integra con Outlook (las tareas de Outlook y los correos marcados aparecen en To Do), y las listas se pueden **compartir** con un vínculo para coordinarse en equipos pequeños, asignando tareas a los miembros de la lista.

Fuentes: [Microsoft Support — Colaboración y coautoría de documentos](https://support.microsoft.com/es-es/sharepoint/get-started-with-sharepoint/document-collaboration-and-co-authoring) · [Microsoft Support — Novedades de Microsoft To Do](https://support.microsoft.com/es-es/office/novedades-de-microsoft-to-do-e4385509-13af-4a55-ae17-1c5a61cf2d41)

Elegir cuántas

[Hacer test Art. 3](https://www.vence.es/leyes/microsoft-365?selected_articles=3&source=temario)

Art. 4

### OneDrive: compartir archivos y versiones

Compartir archivos en OneDrive:

- Compartir mediante vínculos con permisos (ver o editar)
    
- Compartir de modo seguro a través de vínculos protegidos
    
- Colaboración en tiempo real: varias personas editando simultáneamente documentos de Word, Excel o PowerPoint
    

Historial de versiones:

- Recuperar versiones anteriores de archivos
    
- Ver quién hizo cambios y cuándo
    
- Restaurar una versión anterior
    
- No se puede cambiar el nombre del archivo desde el historial de versiones
    

Integración con SharePoint:

- En entornos empresariales, OneDrive se integra con SharePoint
    
- Los archivos de SharePoint se pueden sincronizar con OneDrive
    
- Permite la coautoría en documentos de Office
    

### Cómo se comparte un archivo en OneDrive

Se selecciona el archivo o la carpeta y se pulsa **Compartir** (en la parte superior de OneDrive, o en el menú de acciones del propio archivo). Desde ahí se puede **copiar el vínculo** o escribir los correos de las personas para enviárselo directamente.

**A quién da acceso el vínculo** (se elige en la configuración del vínculo):

- **Cualquier persona**: tiene acceso cualquiera que reciba el vínculo, se lo hayamos enviado nosotros o se lo haya reenviado otra persona.
    
- **Personas de la organización** (por ejemplo, «usuarios de la Universidad de Sevilla que tengan el vínculo»): solo acceden quienes pertenecen a la organización. Es la opción para compartir de modo seguro dentro de ella.
    
- **Personas con acceso existente**: no cambia ningún permiso; sirve para pasar el vínculo a quien ya tenía acceso.
    
- **Personas determinadas**: solo acceden las personas que se indiquen.
    

**Qué se puede controlar en el vínculo:**

- **Permitir la edición**: si está desactivada, los destinatarios solo pueden **ver** el archivo, no modificarlo.
    
- **Establecer la fecha de expiración**: a partir de esa fecha el vínculo deja de funcionar.
    
- **Establecer la contraseña**: hay que introducirla para abrir el vínculo.
    
- **Bloquear la descarga**: impide que los destinatarios descarguen el archivo.
    

### El historial de versiones

- Se abre desde el archivo (por ejemplo, con clic derecho en el Explorador de archivos si está instalada la aplicación de sincronización de OneDrive) con **Historial de versiones**.
    
- Junto a cada versión, en los puntos suspensivos (**…**), está **Restaurar**. Al restaurar, **la versión elegida se convierte en la versión actual** y sustituye a la que lo era, que queda en la lista como versión anterior.
    
- El historial **funciona con todos los tipos de archivo** (archivos de Microsoft 365, PDF, fotos, vídeos…) y las versiones anteriores se conservan **30 días**.
    
- El historial sirve para ver y restaurar versiones; para **compartir** un archivo se usa la opción **Compartir** del propio archivo.
    

Fuentes: [Microsoft Support — Compartir archivos y carpetas en Microsoft OneDrive](https://support.microsoft.com/es-es/office/compartir-archivos-y-carpetas-en-microsoft-onedrive-9fcc2f7d-de0c-4cec-93b0-a82024800c07) · [Microsoft Support — Restaurar una versión anterior de un archivo almacenado en OneDrive](https://support.microsoft.com/es-es/onedrive/restore-a-previous-version-of-a-file-stored-in-onedrive)

Elegir cuántas

[Hacer test Art. 4](https://www.vence.es/leyes/microsoft-365?selected_articles=4&source=temario)

Art. 5

### Microsoft Teams: reuniones y videollamadas

Reuniones y videollamadas en Microsoft Teams:

Tipos de reuniones:

- Reuniones programadas con invitación
    
- Reuniones instantáneas (Meet Now)
    
- Reuniones en vivo (Live Events) para grandes audiencias
    
- Webinars
    

Funcionalidades:

- Pantalla compartida
    
- Grabación de reuniones en la nube
    
- Fondos virtuales y desenfoque
    
- Salas de grupos (breakout rooms)
    
- Transcripción automática
    
- Chat durante la reunión
    

Métodos abreviados de teclado:

- Ctrl+Shift+M: silenciar/activar micrófono
    
- Ctrl+Shift+O: activar/desactivar cámara
    
- Ctrl+Shift+A: aceptar videollamada entrante
    
- Ctrl+Shift+C: iniciar videollamada
    
- Ctrl+Shift+D: rechazar videollamada



