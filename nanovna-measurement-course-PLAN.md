# nanovna-measurement-course — Documento de planificación

> Documento de trabajo para crear el repositorio `nanovna-measurement-course` y preparar su envío a **The Journal of Open Source Education (JOSE)** como *learning module*.
> Autor: Telmo Miguel-Medina · Estado: borrador v0.1 · Fecha: octubre 2026

---

## 1. Objetivo

Crear un **módulo de aprendizaje computacional abierto** sobre medida de parámetros S con un analizador vectorial de redes de bajo coste (NanoVNA). El módulo cubre el modelo de error y la calibración SOL y llega hasta una aplicación introductoria en ingeniería biomédica (caracterización dieléctrica de phantoms o tejidos).

El módulo **deriva** del repositorio de investigación [`telmomm/nanovna-calibration`](https://github.com/telmomm/nanovna-calibration), pero **no lo sustituye**:

| Repositorio | Función | Público | Publicación prevista |
|---|---|---|---|
| `nanovna-calibration` | Registro reproducible de la investigación (preprint de calibración) | Investigadores | Preprint / revista RF |
| `rfmeasurement` | Framework de validación y trazabilidad de medidas RF | Investigadores, desarrolladores | JOSS (cuando madure) |
| **`nanovna-measurement-course`** | Módulo docente: aprender midiendo y programando | Estudiantes y docentes | **JOSE** |

**Principio rector (JOSE):** *coding to learn*, no *learning to code*. El código es el medio para entender la medida, no el fin.

---

## 2. Requisitos de JOSE y estado

| Requisito JOSE | Estado en `nanovna-calibration` | Acción en el nuevo repo |
|---|---|---|
| Material totalmente abierto (Open Definition) | ✅ Público | Mantener |
| `LICENSE` en texto plano: OSI para código, Creative Commons para contenido | ⚠️ Solo BSD-3-Clause | **Doble licencia**: BSD-3-Clause (código) + CC BY 4.0 (texto, cuadernos, figuras, datos) |
| Módulo completo y usable para autoaprendizaje o adopción por otros docentes | ❌ Flujo de investigación | Rediseñar como secuencia didáctica |
| Objetivos de aprendizaje evidentes | ❌ | Objetivos por cuaderno (sección 5) |
| Contenido sustancial | ✅ Base suficiente | Ampliar con teoría y ejercicios |
| Guía de contribución | ✅ `CONTRIBUTING.md` | Adaptar a contribuciones docentes |
| Release versionada que coincida con el paper | ⚠️ Zenodo v0.1.0 | Release `v1.0.0` + archivo en Zenodo |
| Paper de ~1000 palabras (`paper.md` + `paper.bib`) | ❌ | Borrador en sección 9 |
| Experiencia de uso docente | ❌ | **Pilotar antes del envío** (sección 8) |
| Ejecutable sin barreras | ❌ Requiere NanoVNA conectado | Modo sin hardware + Binder/Colab |

---

## 3. Público destinatario y prerrequisitos

**Destinatarios:**
- Grado en Ingeniería Biomédica (asignaturas de instrumentación y electrónica).
- Grado en Ingeniería Electrónica / Telecomunicación (introducción a RF y medida).
- Autoaprendizaje: estudiantes de máster, TFG/TFM y profesionales que empiezan con un NanoVNA.

**Prerrequisitos:**
- Circuitos en régimen sinusoidal (fasores, impedancia compleja). Se puede remitir al Volumen I de *Electrónica en Ingeniería Biomédica* (Miguel-Medina, s.f.).
- Python básico (NumPy, Matplotlib). No se requiere experiencia previa en RF.

**Duración estimada:** 10–14 h (aprox. 5–7 sesiones de 2 h), o un bloque de prácticas de una asignatura cuatrimestral.

---

## 4. Estructura del repositorio

```
nanovna-measurement-course/
├── README.md                 # Presentación, objetivos, cómo empezar (EN, con versión ES)
├── LICENSE                   # BSD-3-Clause (código)
├── LICENSE-CONTENT           # CC BY 4.0 (texto, cuadernos, figuras, datos)
├── CITATION.cff
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── environment.yml           # Para Binder / conda
├── pyproject.toml
├── paper/
│   ├── paper.md              # Paper JOSE
│   └── paper.bib
├── book/                     # Jupyter Book o MkDocs (reutilizar config existente)
│   ├── _config.yml
│   └── _toc.yml
├── notebooks/
│   ├── 00_introduccion_vna.ipynb
│   ├── 01_reflexion_smith.ipynb
│   ├── 02_errores_sistematicos.ipynb
│   ├── 03_calibracion_sol.ipynb
│   ├── 04_adquisicion_nanovna.ipynb      # Opcional (requiere hardware)
│   ├── 05_validacion_calidad.ipynb
│   └── 06_aplicacion_biomedica.ipynb     # v1.1 / v2
├── data/
│   ├── standards/            # Medidas reales O/S/L repetidas (Touchstone)
│   ├── dut/                  # DUT de ejemplo (resistencias, RC, línea)
│   └── phantoms/             # (v2) Phantoms o tejidos
├── src/vnacourse/            # Utilidades mínimas (simulación, ploteo, carga de datos)
├── exercises/
│   └── solutions/            # Soluciones (opcionalmente en rama aparte)
├── instructor/
│   ├── guia_docente.md       # Planificación, tiempos, evaluación
│   └── rubrica.md
└── tests/                    # Ejecución automática de cuadernos (nbmake / nbval)
```

**Decisiones de diseño:**
- **Todo ejecutable sin hardware.** Cada cuaderno funciona con datos simulados (scikit-rf) o con las medidas reales de `data/`. Solo el cuaderno 04 necesita un NanoVNA.
- **Botón Binder/Colab** en cada cuaderno.
- **Dependencia mínima de `rfmeasurement`:** solo aparece en el cuaderno 05 como contenido avanzado. El resto del módulo usa NumPy y scikit-rf.
- **CI** que ejecute todos los cuadernos (salvo el 04) en cada push.
- **Idioma:** contenido en inglés para la revisión, con versión en español (carpeta `es/` o rama). Se puede presentar como valor añadido para contextos hispanohablantes.

---

## 5. Secuencia didáctica y objetivos de aprendizaje

### 00 · ¿Qué mide un VNA?
- **Objetivos:** explicar onda incidente y reflejada; definir los parámetros S; distinguir un VNA de un multímetro o un osciloscopio.
- **Actividades:** simular una línea con carga; visualizar *a₁*, *b₁* y S₁₁ frente a la frecuencia.
- **Sin hardware.**

### 01 · Coeficiente de reflexión y carta de Smith
- **Objetivos:** relacionar Γ y Z (Z = Z₀(1+Γ)/(1−Γ)); interpretar trayectorias en la carta de Smith; reconocer el comportamiento capacitivo e inductivo.
- **Actividades:** cargas ideales (R, RC, RL, RLC serie y paralelo); ejercicio de "adivina el circuito" a partir de una traza.
- **Sin hardware.**

### 02 · Errores sistemáticos: el modelo de tres términos
- **Objetivos:** identificar directividad, *source match* y *reflection tracking*; entender por qué una medida sin calibrar engaña.
- **Actividades:** el alumno "fabrica" un instrumento imperfecto con términos de error sintéticos y observa cómo se distorsiona un DUT conocido.
- **Sin hardware.** (Base: Miguel-Medina, 2026a.)

### 03 · Calibración SOL
- **Objetivos:** plantear y resolver el sistema de tres ecuaciones; aplicar la corrección; valorar el efecto de estándares no ideales.
- **Actividades:** (a) calibrar los datos sintéticos del cuaderno 02 y recuperar el DUT; (b) calibrar **medidas reales** del NanoVNA-F V2 (`data/standards/`); (c) comparar con la implementación de scikit-rf.
- **Sin hardware** (datos reales incluidos). (Base: Miguel-Medina, 2026a, 2026b.)

### 04 · Adquisición con NanoVNA (opcional)
- **Objetivos:** configurar barrido y puntos; adquirir repeticiones O/S/L; exportar a Touchstone.
- **Actividades:** práctica guiada con el instrumento; buenas prácticas (par de apriete, plano de referencia, calentamiento).
- **Requiere NanoVNA.** Incluye una alternativa sin hardware: "adquisición" desde ficheros grabados.

### 05 · Validación y calidad de la medida (avanzado)
- **Objetivos:** cuantificar la repetibilidad; comprobar la pasividad (|S₁₁| ≤ 1) como test físico; registrar el contexto de la medida (trazabilidad).
- **Actividades:** generar un informe de validación con `rfmeasurement`; discutir por qué una violación de pasividad es evidencia experimental y no un error de datos.
- **Sin hardware.** (Base: Miguel-Medina, 2026c.)

### 06 · Aplicación biomédica: hacia la espectroscopía dieléctrica (v1.1 / v2)
- **Objetivos:** relacionar la impedancia medida con la permitividad compleja; conocer los límites del NanoVNA en este uso.
- **Actividades:** medida de phantoms (soluciones salinas de distinta concentración); modelo Cole-Cole introductorio.
- **Referencia externa:** espectrómetro dieléctrico basado en NanoVNA V2 (arXiv:2402.00498).
- **Nota:** se puede dejar fuera de la v1.0 para no retrasar el envío, y citarlo en el paper como extensión prevista.

**Formato común de cada cuaderno:**
1. Objetivos (3–4 viñetas).
2. Teoría breve, con ecuaciones y figura.
3. Código guiado.
4. Preguntas de comprobación ("¿qué esperas ver antes de ejecutar?").
5. Ejercicios abiertos.
6. Resumen y enlace al siguiente cuaderno.

---

## 6. Datos

- Reutilizar las medidas Touchstone de `nanovna-calibration/data/`, citando su DOI.
- Añadir un `data/README.md` con instrumento (NanoVNA-F V2), rango de frecuencia, número de puntos, estándares usados y condiciones.
- Licencia de datos: CC BY 4.0.
- (v2) Dataset de phantoms con su propio DOI en Zenodo.

---

## 7. Plan de trabajo

| Fase | Tareas | Entregable |
|---|---|---|
| 1. Andamiaje | Crear repo, licencias, `environment.yml`, CI con nbmake, Binder | Repo vacío funcional |
| 2. Migración | Portar la lógica SOL de `nanovna-calibration` a los cuadernos 02–03 | Cuadernos 02–03 ejecutables |
| 3. Contenido nuevo | Cuadernos 00, 01 y 05; ejercicios; soluciones | Módulo v0.9 |
| 4. Material docente | `guia_docente.md`, rúbrica, tiempos | Carpeta `instructor/` |
| 5. Piloto | Uso en clase o TFG; encuesta breve; recogida de feedback | Datos de experiencia de uso |
| 6. Ajustes | Incorporar feedback; traducción EN/ES | v1.0.0-rc |
| 7. Envío | Release v1.0.0, Zenodo, `paper.md`, envío a JOSE | Submission |
| 8. (v2) | Cuaderno 06 y dataset de phantoms | v1.1 / v2.0 |

---

## 8. Experiencia de uso (necesaria para el paper)

JOSE pide describir la **experiencia de uso en situaciones reales de enseñanza**. Antes del envío conviene recoger como mínimo:
- Contexto: asignatura, curso, titulación y número de estudiantes.
- Modalidad: presencial, remota o autoaprendizaje.
- Qué cuadernos se usaron y cuánto tiempo llevaron.
- Feedback cualitativo (encuesta anónima corta) y dificultades detectadas.
- Cambios introducidos a raíz del piloto.

> No hace falta un estudio de investigación educativa; basta una descripción honesta del uso.

---

## 9. Borrador de `paper/paper.md`

```markdown
---
title: 'Hands-on vector network analysis with a low-cost NanoVNA: an open computational learning module on S-parameter measurement and calibration'
tags:
  - Python
  - Jupyter
  - RF measurement
  - vector network analyzer
  - calibration
  - biomedical engineering education
authors:
  - name: Telmo Miguel-Medina
    orcid: 0000-0000-0000-0000   # TODO
    affiliation: 1
affiliations:
  - name: TODO
    index: 1
date: TODO 2026
bibliography: paper.bib
---

# Summary

<!-- ~150 words: what the module is, who it is for, what students do. -->

# Statement of need

<!-- ~250 words:
- Low-cost VNAs (NanoVNA) make RF measurement accessible for teaching, but the
  calibration step is usually a black box ("press CAL").
- Biomedical engineering students increasingly need RF/impedance concepts
  (dielectric spectroscopy, wearables, sensing) with little RF background.
- Existing materials: hobbyist guides or advanced RF textbooks; few open,
  executable, curriculum-ready modules.
- This module turns calibration into something students derive, simulate,
  and verify with real data, without requiring hardware.
-->

# Learning objectives

<!-- Bulleted list, one per notebook. -->

# Content and instructional design

<!-- ~250 words: notebook sequence, "predict-run-explain" pattern,
synthetic-then-real data progression, optional hardware notebook,
advanced validation notebook. Mention reuse of real NanoVNA-F V2 data
[@miguelmedina2026nanovnacal] and the error-modeling notebook
[@miguelmedina2026errormodel]; validation via rfmeasurement
[@miguelmedina2026rfmeasurement]; built on scikit-rf [@arsenovic2022skrf]. -->

# Experience of use

<!-- ~200 words: pilot context, number of students, time, feedback, changes. -->

# Acknowledgements

# References
```

---

## 10. Borrador de `paper/paper.bib`

> Se incluyen las obras propias donde aportan algo al módulo. Las entradas marcadas `TODO` deben completarse o comprobarse antes del envío.

```bibtex
@software{miguelmedina2026rfmeasurement,
  author    = {Miguel-Medina, Telmo},
  title     = {rfmeasurement: an open-source framework for uncertainty-aware
               validation and reproducible analysis of RF measurements},
  year      = {2026},
  version   = {0.1.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22058515}
}

@software{miguelmedina2026nanovnacal,
  author    = {Miguel-Medina, Telmo},
  title     = {NanoVNA Calibration: reproducible calibration and analysis of
               RF measurements},
  year      = {2026},
  version   = {v0.1.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.22722704},
  url       = {https://github.com/telmomm/nanovna-calibration}
}

@misc{miguelmedina2026errormodel,
  author    = {Miguel-Medina, Telmo},
  title     = {NanoVNA Error Modeling and Calibration Method},
  year      = {2026},
  publisher = {Zenodo},
  note      = {Computational notebook},
  doi       = {10.5281/zenodo.20142349}
}

@misc{miguelmedina2026preprint,
  author    = {Miguel-Medina, Telmo},
  title     = {TODO: título del preprint de calibración del NanoVNA},
  year      = {2026},
  howpublished = {Research Square preprint},
  doi       = {TODO}
}

@book{miguelmedina_ebm_vol1,
  author    = {Miguel-Medina, Telmo},
  title     = {Electrónica en Ingeniería Biomédica. Volumen I},
  year      = {TODO},
  publisher = {Zenodo},
  doi       = {TODO},
  url       = {https://github.com/telmomm/electronica-ingenieria-biomedica-vol-I}
}

@article{arsenovic2022skrf,
  author  = {Arsenovic, Alexander and Hillairet, Julien and Anderson, Jackson
             and Forst{\'e}n, Henrik and Rie{\ss}, Vinc{\'e}nt and Eller, Michael
             and Sauber, Noah and Weikle, Robert and Barnhart, William and
             Forstmayr, Franz},
  title   = {scikit-rf: An Open Source Python Package for Microwave Network
             Creation, Analysis, and Calibration},
  journal = {IEEE Microwave Magazine},
  year    = {2022},
  volume  = {23},
  number  = {1},
  pages   = {98--105},
  doi     = {10.1109/MMM.2021.3117139}
}

@misc{nanovna_dielectric_arxiv,
  author  = {TODO},
  title   = {Development of a high-frequency dielectric spectrometer using a
             portable vector network analyzer},
  year    = {2024},
  eprint  = {2402.00498},
  archivePrefix = {arXiv}
}
```

**Dónde citar cada obra propia:**

| Obra | Dónde y por qué |
|---|---|
| `rfmeasurement` | Cuaderno 05 y paper (diseño instruccional: validación y trazabilidad) |
| `nanovna-calibration` | Procedencia de los datos reales y de la lógica SOL (cuadernos 03–04) |
| Cuaderno *Error Modeling* (Zenodo) | Origen del cuaderno 02 |
| Preprint de calibración | Statement of need / contenido, si ya es público con DOI |
| Libro *Electrónica en Ingeniería Biomédica* Vol. I | Prerrequisitos (fasores, impedancia) en README y paper |

> Recomendación: citar las obras propias solo donde son la fuente real del material (datos, método, prerrequisitos). Los revisores de JOSE valoran la coherencia, y la autocita gratuita resta.

---

## 11. `CITATION.cff` (plantilla)

```yaml
cff-version: 1.2.0
message: "If you use this learning module, please cite it as below."
title: "nanovna-measurement-course: Hands-on vector network analysis with a low-cost NanoVNA"
authors:
  - family-names: Miguel-Medina
    given-names: Telmo
    orcid: "https://orcid.org/0000-0000-0000-0000"   # TODO
version: 1.0.0
license: [BSD-3-Clause, CC-BY-4.0]
repository-code: "https://github.com/telmomm/nanovna-measurement-course"
references:
  - type: software
    title: "rfmeasurement"
    doi: 10.5281/zenodo.22058515
  - type: software
    title: "NanoVNA Calibration"
    doi: 10.5281/zenodo.22722704
```

---

## 12. Checklist previo al envío a JOSE

- [ ] Repo público con `LICENSE` (BSD-3) y `LICENSE-CONTENT` (CC BY 4.0)
- [ ] Todos los cuadernos (salvo el 04) se ejecutan en CI y en Binder
- [ ] Objetivos de aprendizaje visibles en el README y en cada cuaderno
- [ ] Ejercicios y soluciones
- [ ] Guía docente en `instructor/`
- [ ] `CONTRIBUTING.md` y `CODE_OF_CONDUCT.md`
- [ ] Piloto docente realizado y documentado
- [ ] Contenido en inglés (y versión ES si es posible)
- [ ] Release `v1.0.0` en GitHub, archivada en Zenodo con DOI
- [ ] Título y autores de Zenodo idénticos a los del paper
- [ ] `paper.md` de ~1000 palabras y `paper.bib` completos (sin `TODO`)
- [ ] Revisar los ejemplos publicados en JOSE para calibrar tono y extensión

---

## 13. Pendientes que debo completar yo

- [ ] ORCID y afiliación.
- [ ] Título exacto y DOI del preprint de calibración en Research Square.
- [ ] DOI de Zenodo del Volumen I.
- [ ] Autores del arXiv:2402.00498.
- [ ] Asignatura y grupo donde pilotar el módulo.
- [ ] Decidir si el cuaderno 06 entra en la v1.0 o en la v2.
