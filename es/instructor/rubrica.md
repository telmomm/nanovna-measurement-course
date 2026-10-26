# Rúbrica de evaluación

Rúbrica para la práctica evaluable descrita en la
[guía docente](guia_docente.md#9-evaluación-sumativa), *Caracterizar una
resistencia a partir de datos en bruto*, seguida de una escala breve para los
ejercicios semanales.

> Como el resto del material docente, esta rúbrica todavía no se ha usado para
> corregir entregas reales. Toma los pesos como punto de partida.

## Cómo usarla

- Seis criterios, cada uno valorado en cuatro niveles. Para cada criterio
  calcula peso × nivel ÷ 4 y súmalos: el total es 100 cuando todos los
  criterios están en el nivel 4, y 25 cuando todos están en el nivel 1.
- Los niveles describen **lo que hay en la entrega**, no cuánto esfuerzo
  muestra. Asigna el nivel más alto cuya descripción se cumpla por completo.
- Los criterios B y D recogen la comprensión; A y C, la ejecución. Una entrega
  puede tener todos los números bien y quedarse en el nivel 2 en B y D.
- Comparte la rúbrica con el alumnado al plantear la práctica.

| | Criterio | Peso | Pasos de la práctica | Resultados del módulo |
|---|---|---|---|---|
| A | Procedimiento de calibración | 25 | 1, 2 | 3, 4 |
| B | Interpretación del resultado calibrado | 20 | 1, 3 | 1, 2, 4 |
| C | Validación | 20 | 4, 5 | 5 |
| D | Incertidumbre y limitaciones | 15 | 6 | 5, 6 |
| E | Reproducibilidad y trazabilidad | 10 | 7 | 6 |
| F | Comunicación | 10 | todos | |

Los resultados del módulo están numerados como en la sección 2 de la
[guía](guia_docente.md#2-qué-aprende-el-alumnado).

## La rúbrica

### A. Procedimiento de calibración (peso 25)

| Nivel | Descripción |
|---|---|
| **4 Excelente** | Términos de error calculados solo con las repeticiones asignadas, con un resolvedor que el estudiante sabe explicar. Corrección aplicada correctamente. Resistencia por debajo de 10 MHz dentro del intervalo esperado. El resultado se contrasta, por ejemplo con `skrf.calibration.OnePort` o con la forma cerrada. |
| **3 Competente** | Los términos de error y la corrección son correctos y la resistencia está dentro del intervalo esperado. Sin contraste independiente. |
| **2 En desarrollo** | El procedimiento es reconocible pero tiene un error que cambia el resultado: repeticiones equivocadas, estándares en el orden equivocado, la fórmula de corrección mal aplicada, o datos en bruto y calibrados confundidos. |
| **1 Inicial** | No hay una calibración que funcione, o se copian llamadas a la biblioteca sin evidencia de entender qué calculan. |

### B. Interpretación del resultado calibrado (peso 20)

| Nivel | Descripción |
|---|---|
| **4 Excelente** | Describe cómo se comportan los tres términos de error a lo largo de la banda y los relaciona con las lecturas en bruto. Reconoce que la oscilación de la resistencia con la frecuencia es un giro de Γ con módulo casi constante, la atribuye a un tramo de línea más allá del plano de calibración, estima el retardo, lo elimina y comenta lo que queda. |
| **3 Competente** | Identifica el efecto del plano de referencia y estima correctamente el retardo, con pocos comentarios sobre los términos de error o sobre la variación residual tras eliminar el retardo. |
| **2 En desarrollo** | Muestra la oscilación en la banda y señala que algo va mal, pero la atribuye a un error de calibración, al ruido o a la resistencia, o la presenta sin explicación. |
| **1 Inicial** | Solo da el valor a baja frecuencia, o presenta el resultado en toda la banda sin notar que no es una resistencia constante. |

### C. Validación (peso 20)

| Nivel | Descripción |
|---|---|
| **4 Excelente** | Prueba la calibración con repeticiones no usadas para calcularla y resume el residuo con un estadístico robusto. Comprueba la pasividad de la resistencia y de un estándar calibrado, e interpreta las excursiones por encima de 1 comparando su tamaño con la repetibilidad. Señala lo que la prueba con datos reservados no puede detectar. |
| **3 Competente** | La prueba con datos reservados y la comprobación de pasividad están hechas y bien presentadas, con una interpretación razonable pero breve. |
| **2 En desarrollo** | Solo una de las dos comprobaciones, o la calibración se «valida» con los mismos datos con los que se calculó, o un valor por encima de 1 se trata como un error de los datos y se recorta o se descarta. |
| **1 Inicial** | Sin validación, o la afirmación de que el resultado es correcto porque está cerca del valor nominal. |

### D. Incertidumbre y limitaciones (peso 15)

| Nivel | Descripción |
|---|---|
| **4 Excelente** | Da una incertidumbre típica con su deducción, distinguiendo la dispersión de las lecturas individuales de la incertidumbre de una media. Indica qué fuentes incluye y nombra las principales que no incluye: la definición de los estándares, el plano de referencia, la tolerancia del componente. Compara el resultado con el valor nominal en unidades de esa incertidumbre y extrae una conclusión justificada. |
| **3 Competente** | Una incertidumbre típica bien calculada, con al menos una limitación nombrada. |
| **2 En desarrollo** | Se da un número como «el error» sin deducción, o se presenta la desviación típica de las lecturas como incertidumbre de la media, o se presenta la incertidumbre como si lo cubriera todo. |
| **1 Inicial** | Sin incertidumbre, o el resultado se da con cifras sin significado. |

### E. Reproducibilidad y trazabilidad (peso 10)

| Nivel | Descripción |
|---|---|
| **4 Excelente** | El cuaderno se ejecuta de principio a fin sin cambios. Registra qué datos y repeticiones se usaron, el instrumento, la calibración y sus hipótesis, los pasos de procesado y las versiones del software, y distingue lo medido de lo supuesto. |
| **3 Competente** | El cuaderno se ejecuta de principio a fin e indica los datos, las repeticiones y la calibración usados. |
| **2 En desarrollo** | El cuaderno solo se ejecuta tras arreglos (celdas desordenadas, definiciones que faltan), o el lector tiene que adivinar qué datos produjeron cada resultado. |
| **1 Inicial** | El cuaderno no se ejecuta, o los resultados de la conclusión no pueden relacionarse con ninguna celda. |

### F. Comunicación (peso 10)

| Nivel | Descripción |
|---|---|
| **4 Excelente** | Todas las figuras tienen ejes rotulados con unidades, una leyenda cuando hay más de una traza y una frase que dice qué muestran. Los resultados se dan con unidades y un número razonable de cifras. La conclusión responde al enunciado en una página como máximo y se entiende sin leer el código. |
| **3 Competente** | Las figuras están rotuladas y los resultados tienen unidades. La conclusión es completa, pero obliga al lector a revisar el cuaderno. |
| **2 En desarrollo** | A algunas figuras les faltan rótulos o unidades, o la conclusión enumera lo que se hizo sin decir lo que se encontró. |
| **1 Inicial** | Figuras sin rotular o ausentes; sin conclusión. |

## Hoja de corrección

| Criterio | Peso | Nivel (1–4) | Peso × nivel ÷ 4 |
|---|---|---|---|
| A. Procedimiento de calibración | 25 | | |
| B. Interpretación | 20 | | |
| C. Validación | 20 | | |
| D. Incertidumbre y limitaciones | 15 | | |
| E. Reproducibilidad y trazabilidad | 10 | | |
| F. Comunicación | 10 | | |
| **Total** | **100** | | |

Una lectura orientativa del total: 85 o más, sobresaliente; de 70 a 84,
notable; de 50 a 69, aprobado; por debajo de 50, todavía no suficiente. Ajusta
los umbrales a la escala de tu institución.

**Comprobaciones rápidas al corregir.** Los valores esperados están en la
[guía](guia_docente.md#9-evaluación-sumativa). En la práctica:

- resistencia por debajo de 10 MHz fuera de 32.3–32.5 Ω: busca un error en A;
- ninguna mención a un retardo o a una línea: B está en el nivel 2 o por
  debajo;
- residuos exactamente nulos en los estándares: la calibración se probó con
  sus propios datos (C, nivel 2);
- una incertidumbre muy por debajo de 0.05 Ω o por encima de 1 Ω: revisa qué
  se calculó (D).

## Ejercicios semanales

Para los ejercicios del final de cada cuaderno basta una escala de tres
niveles. Su objetivo es mantener al alumnado trabajando entre sesiones, no
clasificarlo.

| Nivel | Descripción |
|---|---|
| **Completo** | El ejercicio se intenta por completo, el código se ejecuta y el resultado viene con una frase de interpretación: qué muestra o por qué sale así. |
| **Parcial** | El ejercicio se intenta y el código se ejecuta, pero no hay interpretación o falta una parte. |
| **No hecho** | No se intenta, o se copia sin cambios de la solución publicada. |

Las soluciones resueltas son públicas. Una interpretación escrita con las
propias palabras del estudiante es lo que distingue el trabajo de la copia, y
es la parte que merece la pena leer.

## Predicciones

No califiques el acierto de las respuestas a «Predice antes de ejecutar». Si
las registras, registra solo que se hizo una predicción. Una predicción
equivocada seguida de una buena explicación de la diferencia es el mejor
resultado que puede producir el módulo.
