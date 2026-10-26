# Guía docente

Cómo enseñar con *nanovna-measurement-course*: qué cubre, cuánto dura, cómo
llevar una sesión, dónde es probable que el alumnado tenga dificultades y cómo
evaluarlo. La rúbrica de corrección está en [rubrica.md](rubrica.md).

> **Este módulo todavía no se ha usado en un aula.** Los tiempos de las
> sesiones son estimaciones a partir de la extensión del material, y las
> «dificultades probables» son lo que esperamos, no lo que hemos observado.
> Ambos se sustituirán por valores medidos tras el primer pilotaje. Si lo usas
> en clase, por favor [cuéntanos cómo ha ido](#12-cuéntanos-cómo-ha-ido).

## 1. De un vistazo

| | |
|---|---|
| Materia | Medida de parámetros S de un puerto con un analizador vectorial de redes de bajo coste: modelo de error, calibración SOL, validación |
| Nivel | Grado, tras una primera asignatura de circuitos; también adecuado para máster y TFG/TFM |
| Titulaciones | Ingeniería Biomédica, Ingeniería Electrónica, Ingeniería de Telecomunicación |
| Requisitos previos | Fasores e impedancia compleja; Python básico con NumPy y Matplotlib |
| No se necesita | Ninguna asignatura previa de RF ni de líneas de transmisión; ningún hardware |
| Formato | Cinco cuadernos Jupyter, cada uno con código guiado, preguntas y ejercicios; soluciones resueltas |
| Duración | 10–14 horas (estimación): unas 7.5 h guiadas, más de 2.5 h a 4.5 h de ejercicios según cuántos se planteen. La práctica evaluable añade 2–3 h. |
| Evaluación | Una práctica con datos reales, corregida con la [rúbrica](rubrica.md) |
| Se ejecuta en | Un navegador (Binder o Google Colab) o una instalación local de Python 3.10+ |
| Idiomas | Inglés (raíz del repositorio) y español (carpeta `es/`), con el mismo contenido y la misma numeración |

## 2. Qué aprende el alumnado

Al terminar el módulo, un estudiante es capaz de:

1. explicar una medida de reflexión en términos de ondas incidente y reflejada, y convertir entre coeficiente de reflexión e impedancia;
2. leer una carta de Smith y reconocer circuitos sencillos por sus trazas;
3. describir los tres términos de error sistemático de una medida de un puerto y predecir qué distorsiona cada uno;
4. deducir, implementar y aplicar una calibración cortocircuito–abierto–carga;
5. juzgar un resultado calibrado: probarlo con datos independientes, contrastarlo con límites físicos y declarar su repetibilidad;
6. comunicar un resultado con su incertidumbre, sus limitaciones y contexto suficiente para reproducirlo.

| Resultado | Cuaderno | Objetivos de aprendizaje declarados en el cuaderno |
|---|---|---|
| 1 | 00 · ¿Qué mide un VNA? | ondas incidente y reflejada; parámetros S; potencia reflejada y pérdidas de retorno; VNA frente a multímetro y osciloscopio |
| 1, 2 | 01 · Coeficiente de reflexión y carta de Smith | Γ ↔ Z; qué son las circunferencias y arcos de la carta; comportamiento inductivo, capacitivo y resonante; identificar un circuito por su traza |
| 3 | 02 · Errores sistemáticos | nombrar los tres términos de error; escribir el modelo de error; predecir qué dispositivos distorsiona cada término; reconocer una medida en bruto no fiable |
| 4, 5 | 03 · Calibración SOL | linealizar y resolver el modelo; corregir una medida; probar con datos reservados; plano de referencia y estándares imperfectos |
| 5, 6 | 05 · Validación y calidad de la medida | repetibilidad e incertidumbre típica; pasividad como prueba física; integridad, física y calidad; contexto y trazabilidad |

El cuaderno 04 (adquirir tus propios datos con un NanoVNA) está previsto, es
opcional y todavía no está disponible. Nada de los demás cuadernos depende de
él.

## 3. Cómo dependen los cuadernos entre sí

```
00 ──► 01 ──► 02 ──► 03 ──► 05
```

Cada cuaderno usa los anteriores. Tres maneras de recortar el módulo:

| Itinerario | Cuadernos | Tiempo (estimación) | Para |
|---|---|---|---|
| Completo | 00, 01, 02, 03, 05 | 10–14 h | Alumnado sin experiencia en RF. El itinerario por defecto. |
| Sin validación | 00, 01, 02, 03 | 8–11 h | Cuando hay poco tiempo. El cuaderno 05 está marcado como «avanzado» y puede eliminarse sin romper nada. |
| Solo calibración | 02, 03 | 4–5 h | Alumnado que ya conoce los parámetros S y la carta de Smith, por ejemplo tras una asignatura de RF o microondas. |

El cuaderno 05 necesita el 03. El cuaderno 01 puede acortarse (omitiendo la
sección 3.2, circuitos paralelo), pero no puede saltárselo quien nunca haya
visto una carta de Smith: los cuadernos 02 y 03 muestran resultados en ella.

## 4. Plan de sesiones

Para sesiones de dos horas. «Guiado» es el tiempo para recorrer el cuaderno
con sus predicciones y preguntas; «ejercicios» es el tiempo para los ejercicios
finales, en clase o como tarea.

| Sesión | Contenido | Guiado | Ejercicios |
|---|---|---|---|
| 1 | Cuaderno 00, completo. Cuaderno 01, secciones 1–2 (Γ ↔ Z, construir la carta). | 60 min + 35 min | 00: 30–45 min, tarea |
| 2 | Cuaderno 01, secciones 3–4 (trazas, adivina el circuito). | 40 min + 30 min para los circuitos misteriosos | 01: 45 min |
| 3 | Cuaderno 02, completo. | 75 min | 02: 45 min |
| 4 | Cuaderno 03, secciones 1–4.1 (el resolvedor, datos sintéticos, primer resultado real). | 60 min | 03, ejercicios 1–2: 30 min |
| 5 | Cuaderno 03, secciones 4.2–6 (plano de referencia, prueba con datos reservados, scikit-rf, estándares imperfectos). | 60 min | 03, ejercicios 3–5: 45 min |
| 6 | Cuaderno 05, completo. | 90 min | 05: 60 min, tarea |
| 7 (opcional) | Taller de la práctica evaluable, o una sesión práctica con el instrumento. | | Práctica: 2–3 h |

Las sesiones 4 y 5 son el corazón del módulo. Si hay que comprimir, quita
tiempo a la sesión 1 (asigna el cuaderno 00 como preparación) y no a estas.

## 5. Cómo llevar una sesión

Los cuadernos se construyen en torno a un hábito: **predecir, ejecutar,
explicar.**

1. **Predecir.** Antes de cada celda clave hay una indicación «Predice antes de
   ejecutar» (17 en total). Pide al alumnado que se comprometa antes con una
   respuesta: escrita en una línea o acordada con quien tenga al lado. Bastan
   treinta segundos. La predicción no tiene que ser correcta; tiene que
   existir.
2. **Ejecutar.** Ejecutan la celda y comparan.
3. **Explicar.** El texto que sigue a la celda explica el resultado. Donde la
   predicción y el resultado difieren, esa diferencia es la lección: dedica ahí
   el tiempo de clase.

El segundo recurso es el orden **primero sintético, después real**. Cada idea
se prueba primero en un instrumento inventado en el que la respuesta correcta
se conoce exactamente, y después en datos reales de un NanoVNA en los que no.
Hazlo notar: con datos sintéticos el método puede *verificarse*; con datos
reales solo puede *comprobarse su coherencia*.

Sugerencias prácticas:

- **El trabajo por parejas funciona bien** para las predicciones y para los
  circuitos misteriosos.
- **No proyectes el cuaderno resuelto.** El alumnado debe ejecutar las celdas;
  las salidas no se guardan en el repositorio a propósito.
- **El código es un medio.** No hace falta saber escribir el código de las
  gráficas. Sí hace falta saber escribir `apply_error_model`,
  `solve_error_terms` y `correct` (unas diez líneas en total), y cada cuaderno
  lo pide.
- **Las preguntas «Comprueba lo que has entendido»** tienen la respuesta a un
  clic. Úsalas como pausas de dos minutos en clase o como autoevaluación antes
  de los ejercicios.

## 6. Preparación

Tres maneras de ejecutar los cuadernos, de menos a más cosas que pueden fallar:

| Opción | El alumnado necesita | Notas |
|---|---|---|
| **Binder** | Un navegador | Pulsa la insignia de la parte superior de un cuaderno. El primer arranque tras un cambio en el repositorio tarda varios minutos mientras se construye el entorno; los siguientes son más rápidos. Las sesiones son temporales: el trabajo se pierde al cerrar la pestaña salvo que se descargue. |
| **Google Colab** | Un navegador y una cuenta de Google | Pulsa la insignia de Colab. La primera celda de código de cada cuaderno instala el paquete del curso. El trabajo puede guardarse en el Drive del estudiante. |
| **Local** | Python 3.10+ | Instrucciones en [Ejecutar las lecciones](../../book/es/setup.md). Es lo mejor para una asignatura que dura varias semanas. |

Antes de la primera sesión:

- [ ] Abre un cuaderno en la plataforma que vaya a usar el alumnado y
      ejecútalo hasta el final. Hazlo el día anterior: así además «calientas»
      Binder.
- [ ] Si usas Binder, ten Colab preparado como alternativa (o al revés). Ambos
      son servicios gratuitos sin garantía de disponibilidad.
- [ ] Comprueba que el cuaderno 05 se ejecuta. Es el único que necesita la
      biblioteca adicional `rfmeasurement`, que se instala automáticamente en
      Binder y Colab.
- [ ] Decide qué entrega el alumnado y explícale cómo guardar su trabajo.
- [ ] Decide cómo vas a usar las soluciones, que son públicas (sección 9).

No se necesita hardware en ningún momento. Si tienes NanoVNA, mira la
sección 10.

## 7. Notas sobre cada cuaderno

Las «dificultades probables» son previstas, todavía no observadas.

### 00 · ¿Qué mide un VNA?

- **La idea central:** en radiofrecuencia, un dispositivo se caracteriza por
  cómo refleja una onda, y eso requiere un módulo *y* una fase.
- **Dificultades probables:** tratar la onda reflejada como una pérdida o un
  defecto cuando es simplemente la consecuencia de una desadaptación; el signo
  de Γ (una carga por debajo de 50 Ω tiene Γ negativo); que las pérdidas de
  retorno sean un número positivo de decibelios que es *mejor* cuanto mayor;
  creer que la fase es un detalle.
- **Merece la pena discutir:** la sección 4 muestra que un |S11| plano con una
  fase que gira parece, para un instrumento que solo ve la tensión total, un
  dispositivo que cambia con la frecuencia. Pregunta: «¿qué concluirías solo
  con la segunda gráfica?».
- **Ejercicios:** el 3 (de pérdidas de retorno a impedancia) es el más útil si
  solo puedes plantear uno. El 4 prepara la discusión del plano de referencia
  del cuaderno 03.

### 01 · Coeficiente de reflexión y carta de Smith

- **La idea central:** la carta de Smith es el plano Γ con líneas de
  impedancia dibujadas encima, nada más.
- **Dificultades probables:** ver la carta como un tipo de gráfica aparte y
  misterioso; leer la resistencia solo por la posición horizontal (el punto
  justo encima del centro no tiene 50 Ω de resistencia); los circuitos
  paralelo y las circunferencias de conductancia; por qué las trazas giran en
  sentido horario.
- **Merece la pena discutir:** en la sección 2 el alumnado dibuja las
  circunferencias. Dale tiempo: es lo que quita el misterio. La sección 3.4
  (una circunferencia en torno al centro es un retardo) vuelve como sorpresa
  en datos reales en el cuaderno 03.
- **Adivina el circuito (sección 4):** funciona bien por parejas, con una
  breve puesta en común sobre *cómo* decidió cada pareja. Los tres circuitos
  son un RC serie, un RL paralelo y un RLC serie. Insiste en elegir la
  topología por la forma antes de calcular nada.
- **Si hay poco tiempo:** omite la sección 3.2 y el circuito misterioso B.

### 02 · Errores sistemáticos

- **La idea central:** un instrumento sin calibrar no es impreciso, es
  sistemáticamente erróneo, y ese error tiene exactamente tres parámetros.
- **Dificultades probables:** confundir el error sistemático con el ruido (la
  concepción errónea más fuerte del módulo: «mídelo otra vez y promedia»); el
  rizado, que exige pensar en Γm como una suma de vectores complejos que giran;
  recordar qué término es cuál.
- **Merece la pena discutir:** las tres gráficas «un defecto cada vez» de la
  sección 2. La predicción «¿qué dispositivo no se mueve?» tiene una respuesta
  limpia en cada caso y construye la tabla que cierra la sección. En la
  sección 4, la lectura en bruto del abierto, |Γ| = 2.1, es un buen momento
  para preguntar «¿está roto el fichero?» (no lo está), algo que el cuaderno 05
  responde con detalle.
- **Dile al alumnado:** los errores del instrumento sintético son inventados y
  exagerados para que se vea cada efecto. Los instrumentos reales son mejores.
- **Ejercicios:** el 1 (qué término tiene la culpa) consolida el cuaderno. El
  3 (el peor caso en decibelios) es rápido y conecta con cómo se leen las
  hojas de datos.

### 03 · Calibración SOL

- **La idea central:** tres dispositivos conocidos dan tres ecuaciones para
  los tres términos de error; se resuelven y después se invierte el modelo.
- **Dificultades probables:** el paso de linealización (multiplicar por el
  denominador y renombrar un producto de incógnitas como una sola incógnita,
  Δe); por qué corregir las propias medidas de calibración no demuestra nada;
  y el plano de referencia, que el alumnado encuentra aquí como un aparente
  fallo de la calibración.
- **Merece la pena discutir:** la sección 4.2 es el momento más importante del
  módulo. Tras la calibración, las dos resistencias oscilan entre 33 Ω y 75 Ω
  a lo largo de la banda. Deja que el alumnado crea durante un minuto que la
  calibración está mal antes de mostrar la carta de Smith. La solución
  (alrededor de 1 ns de línea entre el plano de calibración y las
  resistencias) se infiere de los propios datos.
- **La sección 6** (estándares imperfectos) puede asignarse como lectura si
  hay poco tiempo, pero no la elimines: es lo que impide que el alumnado crea
  que un resultado calibrado es exacto.
- **Ejercicios:** el 1 (forma cerrada) para quien disfrute del álgebra; el 2
  (menos repeticiones) para todos; el 4 (un cuarto estándar) es el más difícil
  y conviene a estudiantes avanzados o a un proyecto.

### 05 · Validación y calidad de la medida

- **La idea central:** un número se convierte en un resultado cuando viene
  con su repetibilidad, sus comprobaciones físicas y su historia.
- **Dificultades probables:** la desviación típica de una magnitud compleja;
  la diferencia entre la dispersión de las lecturas individuales y la
  incertidumbre de su media; leer «incertidumbre» como «error»; y querer
  «arreglar» una violación de la pasividad recortando.
- **Merece la pena discutir:** la sección 3 termina con un resultado de
  74.0 Ω ± 0.2 Ω para una resistencia nominal de 75 Ω. Pregunta qué podría
  explicar la diferencia. Todos los candidatos son algo que la incertidumbre no
  incluye, que es justo la idea. La tabla de la sección 4 (tres significados de
  |Γ| > 1) merece leerse en voz alta.
- **Sobre `rfmeasurement`:** las secciones 5 y 6 usan más maquinaria de la
  biblioteca que el resto del módulo. No hace falta memorizar la API. Lo que
  importa es la estructura: una medida con su contexto, reglas que devuelven un
  estado *con evidencia* y un historial de procesado. Los mensajes e informes
  de la biblioteca están en inglés.
- **Ejercicios:** el 1 (media o mediana) es corto y convincente. El 3 (escribe
  una regla) es el más abierto; su solución muestra a propósito una regla que
  da falsas alarmas y discute por qué.

## 8. Evaluación formativa

Tres fuentes de evidencia que no requieren esfuerzo de corrección:

- **Predicciones.** Recógelas de vez en cuando (una línea en papel, a mano
  alzada, una encuesta). Valora la participación, nunca el acierto: el método
  solo funciona si el alumnado se siente libre para equivocarse.
- **Preguntas «Comprueba lo que has entendido».** Usa dos o tres como billete
  de salida.
- **Ejercicios.** Basta una escala de tres niveles; véase la
  [rúbrica](rubrica.md#ejercicios-semanales).

## 9. Evaluación sumativa

### La práctica: caracterizar una resistencia a partir de datos en bruto

El alumnado no recibe nada nuevo: la tarea usa las medidas que ya están en el
repositorio, pero con una calibración propia.

> **Enunciado para el alumnado.** Dispones de medidas en bruto de un NanoVNA de
> tres estándares de calibración (diez repeticiones de cada uno, en
> `data/standards/`) y de una resistencia (tres repeticiones, en
> `data/dut/load_33ohm/`). Usando solo las tres repeticiones de los estándares
> que se te asignen:
>
> 1. Calcula los términos de error del instrumento y describe cómo se
>    comportan a lo largo de la banda.
> 2. Calibra la medida de la resistencia. Indica su resistencia por debajo de
>    10 MHz.
> 3. Muestra el resultado calibrado en toda la banda, explica lo que ves y
>    estima el retardo entre el plano de calibración y la resistencia.
> 4. Prueba tu calibración con las repeticiones de los estándares que no
>    usaste.
> 5. Comprueba la pasividad de la resistencia calibrada y de un estándar
>    calibrado, e interpreta el resultado.
> 6. Da una incertidumbre típica para la resistencia del paso 2. Indica qué
>    incluye y qué no.
> 7. Registra lo que otra persona necesitaría para reproducir tu resultado.
>
> Entrega un cuaderno que se ejecute de principio a fin y una conclusión de
> una página como máximo.

**Personalizarla.** Asigna a cada estudiante o pareja un conjunto distinto de
tres números de repetición de entre diez (hay 120 combinaciones). Los números
que obtienen difieren ligeramente, así que los resultados no pueden copiarse
sin más, mientras que los valores esperados se mantienen en un intervalo
estrecho que puedes comprobar.

**Lo que encuentra una entrega correcta** (verificado en las 120
combinaciones):

| Magnitud | Valor esperado |
|---|---|
| Resistencia por debajo de 10 MHz | de 32.3 Ω a 32.5 Ω |
| Retardo en un sentido hasta la resistencia | unos 1.05 ns (aproximadamente 22 cm de línea a 0.7 c) |
| Resistencia tras eliminar el retardo | unos 34 Ω de media, variando entre unos 30 Ω y 40 Ω a lo largo de la banda |
| Abierto reservado, distancia mediana a Γ = 1 | de 0.0015 a 0.0018 |
| Incertidumbre por las tres repeticiones de la resistencia | unos 0.09 Ω |
| Pasividad | La resistencia está muy dentro del límite (\|Γ\| por debajo de 0.25). Un abierto o un cortocircuito calibrados quedan ligeramente por encima de 1 en una gran fracción de los puntos, por cantidades comparables a la repetibilidad. |

Un estudiante que incluya además la dispersión de la calibración en la
incertidumbre, como hace el cuaderno 05, dará un valor algo mayor. Ambos son
aceptables si el estudiante dice qué fuentes ha incluido.

**Qué buscar** más allá de los números: si el estudiante *explica* la
oscilación de la resistencia a lo largo de la banda en lugar de presentarla
como un error, y si la incertidumbre declarada viene con sus limitaciones.
Estos dos aspectos separan la comprensión de la ejecución. La
[rúbrica](rubrica.md) los pondera en consecuencia.

### Sobre las soluciones públicas

Las soluciones resueltas de los ejercicios están en el repositorio, y los
cuadernos 03 y 05 ya resuelven por completo la resistencia de 75 Ω. Es
deliberado: el módulo está pensado también para el estudio autónomo. Para
trabajo calificado:

- usa la práctica anterior con repeticiones personalizadas, que no está
  resuelta en ningún sitio;
- o cambia los números de un ejercicio (valores de componentes, longitud del
  cable, capacidad del abierto);
- o califica las partes abiertas: una explicación, una decisión de diseño, una
  regla de validación y sus falsas alarmas.

Esta guía también es pública, incluidos los valores esperados anteriores. Le
dicen a un estudiante cómo es una respuesta correcta, no cómo obtenerla ni
explicarla.

## 10. Adaptar el módulo

**Tus propias medidas.** `load_repetitions("standards", "open")` lee todos los
ficheros `.s1p` de `data/standards/open/`. Para usar tus datos, sustituye los
ficheros manteniendo una carpeta por dispositivo y un fichero Touchstone por
repetición, todos con la misma rejilla de frecuencias. Actualiza
`data/README.md` con tu instrumento y tus condiciones. El texto explicativo de
los cuadernos 02, 03 y 05 cita números de los datos suministrados, así que
contrástalo con los tuyos.

**Con NanoVNA en el laboratorio.** Una sesión práctica natural tras el
cuaderno 03: el alumnado mide un cortocircuito, un abierto, una carga y un
componente de su elección, guarda ficheros Touchstone y pasa sus propios datos
por el cuaderno. Haz que calibren al final del cable que van a usar y que
después añadan un adaptador para ver cómo se mueve el plano de referencia.

**Nuevos circuitos misteriosos.** Para el cuaderno 01, genera tus propias
trazas:

```python
import numpy as np
from vnacourse.reflection import z_to_gamma

f_hz = np.linspace(10e6, 1.45e9, 600)
omega = 2 * np.pi * f_hz
z = 40 + 1j * omega * 12e-9  # por ejemplo: 40 Ω en serie con 12 nH
gamma = z_to_gamma(z)  # da al alumnado este vector, no la línea anterior
```

**Otro público.** Para estudiantes de Ingeniería Biomédica, conecta el
cuaderno 01 con la impedancia de electrodos y tejidos, y el cuaderno 05 con las
normas de presentación de resultados que encontrarán en instrumentación. Para
estudiantes de Telecomunicación, conecta el cuaderno 00 con la adaptación de
antenas y el cuaderno 03 con la calibración de dos puertos, que extiende la
misma idea a doce términos de error.

**Idiomas.** El material está en inglés y en español, con el mismo contenido.
El código (nombres de variables y funciones del paquete `vnacourse`) es el
mismo en ambas versiones; en la española se traducen el texto, los
comentarios, las etiquetas de las figuras y los mensajes. Se usa el punto
decimal, como en Python, para que el texto y las salidas del código coincidan.

## 11. Limitaciones conocidas del material

Tenlas presentes y plantéate contárselas al alumnado:

- **A los datos suministrados les falta parte del registro.** El kit de
  calibración y sus definiciones, el utillaje usado para las resistencias y la
  configuración de adquisición no se registraron con los datos (véase
  [`data/README.md`](../data/README.md)). Los cuadernos tratan los estándares
  como ideales e infieren el resto a partir de los datos. El cuaderno 05
  convierte esto en una lección sobre trazabilidad, pero limita hasta dónde
  pueden interpretarse los resultados.
- **Solo un puerto.** No se tratan las medidas de transmisión ni la
  calibración de dos puertos.
- **La incertidumbre se introduce, no se trata por completo.** El cuaderno 05
  cubre la repetibilidad (tipo A) y explica lo que deja fuera. No construye un
  presupuesto de incertidumbre completo.
- **El cuaderno 05 depende de una biblioteca en fase temprana.**
  `rfmeasurement` está en la versión 0.3 y su interfaz puede cambiar. Su regla
  de pasividad integrada no trata datos de un puerto en esa versión, así que el
  cuaderno pide al alumnado que escriba la suya.
- **Todavía no hay cuaderno con hardware.** El cuaderno 04 está previsto.

## 12. Cuéntanos cómo ha ido

Si usas el módulo, completo o en parte, por favor abre una incidencia
[«Classroom experience»](https://github.com/telmomm/nanovna-measurement-course/issues/new?template=classroom_report.yml)
(puedes escribirla en español). Bastan unas líneas: la asignatura, cuántos
estudiantes, qué cuadernos, cuánto tardaron y qué no funcionó. Así es como las
estimaciones de esta guía se convierten en medidas y como mejora la siguiente
versión.

Las correcciones y aportaciones a esta guía son bienvenidas a través del mismo
repositorio; véase
[CONTRIBUTING.es.md](https://github.com/telmomm/nanovna-measurement-course/blob/main/CONTRIBUTING.es.md).
