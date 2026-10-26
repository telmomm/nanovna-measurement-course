<img src="mark.svg" width="72" alt="Símbolo de Hands-on VNA">

# Identidad visual

[English](README.md) · **Español**

La identidad visual de *Hands-on VNA*, aplicada al README, al libro web, al
libro en PDF y a las figuras de los cuadernos. Procede de un lienzo de diseño
que conserva el autor y que contiene también el material de lanzamiento
(publicaciones para redes, cartel A4, banner de LinkedIn, textos de
lanzamiento).

## El símbolo

La carta de Smith reducida a lo esencial: la circunferencia unidad, el eje
real y los tres estándares de la calibración SOL en su sitio real.
**Short** en Γ = −1 (azul), **Load** en Γ = 0 (verde), **Open** en Γ = +1
(naranja). Los tres colores son los tres primeros de las series de las
figuras de los cuadernos, así que la marca y el material hablan el mismo
idioma.

| Fichero | Uso |
|---|---|
| [`mark.svg`](mark.svg) | sobre fondos claros (logotipo del libro web en modo claro, PDF) |
| [`mark-dark.svg`](mark-dark.svg) | sobre fondos oscuros (logotipo del libro web en modo oscuro) |
| [`favicon.svg`](favicon.svg) | pestaña del navegador: el símbolo sobre una pieza de papel |
| `banner-{en,es}-{light,dark}.png` | cabecera del README, uno por idioma y esquema de color |
| `social-preview.png` | GitHub *Settings › Social preview*, 1280×640 |

## Color

| Nombre | Hex | Función |
|---|---|---|
| Pantalla | `#0E1116` | tinta; fondos oscuros (portada, barra de aviso, modo oscuro) |
| Papel | `#FCFCFB` | fondo claro; texto sobre Pantalla |
| Short · calibrado | `#2A78D6` | enlaces, acento principal, el resultado calibrado |
| Open · en bruto | `#EB6834` | lo que lee el instrumento antes de calibrar; avisos. Para texto naranja sobre Papel usa `#C4501F` (contraste) |
| Load | `#1BAF7A` | solo el tercer estándar |
| Retícula | `#E4E3DF` | filetes, bordes, retícula de las cartas |
| Secundario | `#52514E` | texto secundario sobre Papel; `#9AA3AE` sobre Pantalla |

Naranja es lo que lee el instrumento; azul, lo que queda tras calibrar. El
verde, solo para el tercer estándar.

## Tipografía

- **IBM Plex Sans** para todo: titulares en peso 700, texto en 400/500.
- **IBM Plex Mono** para datos, etiquetas, nombres de fichero y fórmulas en el
  texto. No tiene letras griegas: Γ y Ω se toman de Plex Sans.
- **IBM Plex Math** para las ecuaciones del PDF.

Las tres son abiertas (SIL Open Font License). El libro web las carga de
Google Fonts; el PDF usa las copias de TeX Live (paquete `plex`); las figuras
usan Plex Sans cuando está instalada.

## El motivo gráfico

Una resistencia de 75 Ω vista por un instrumento sin calibrar da vueltas en
torno al centro de la carta de Smith (naranja); tras la calibración SOL es un
único punto en Γ = 0.2 (azul). Cuenta el módulo de un vistazo. En este
repositorio se calcula, no se dibuja: [`make_brand.py`](make_brand.py) usa el
instrumento sintético de los cuadernos 02 y 03.

## Voz

- **Precisa, no grandilocuente.** Cifras reales del repositorio; nada de
  «revolucionario».
- **Invita a predecir.** Una pregunta antes que una promesa: «¿qué verás antes
  de ejecutar?».
- **Honesta con el estado.** Versión 0.1.0, aún sin usar en el aula: se dice, y
  se convierte en invitación.

## Dónde se aplica

| Lugar | Fichero |
|---|---|
| README (los dos idiomas) | `README.md`, `README.es.md` |
| Libro web: fuentes, colores, logotipo, barra de aviso | [`book/_static/brand.css`](../../book/_static/brand.css), `book/*/_config.yml` |
| Libro PDF: portada, fuentes, cabeceras de capítulo, colores | [`book/latex/handsonvna.sty`](../../book/latex/handsonvna.sty) |
| Figuras de los cuadernos | `vnacourse.plotting.use_course_style` |

## Regenerar las imágenes

```bash
python assets/brand/make_brand.py
```

Necesita los ficheros OpenType de IBM Plex (el paquete `plex` de TeX Live, o
la variable `PLEX_FONT_DIR`). Escribe los banners, la imagen social y
`book/latex/cover-motif.pdf`.
