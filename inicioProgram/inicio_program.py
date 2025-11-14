import tkinter as tk
from tkinter import messagebox

# === Importamos módulos del proyecto ===
from teorias.teoria import mostrar_teoria_en_frame
from preguntas.cuestionario import crear_cuestionario_en_frame, preguntas_nivel_1, preguntas_nivel_2
from preguntas.tutorial import tutorial_en_frame

# ============================================================
# FUNCIÓN PRINCIPAL - EQUIVALENTE A iniciar_programa()
# ============================================================
def iniciar_programa():
    app = tk.Tk()
    app.title("GH Programming - Curso Interactivo")
    app.geometry("1600x920")
    app.config(bg="#0d1117")

    # Frame principal que contendrá todo el contenido
    contenedor_principal = tk.Frame(app, bg="#0d1117")
    contenedor_principal.pack(expand=True, fill="both")

    # --------------------------------------------
    # FUNCIONES AUXILIARES
    # --------------------------------------------
    def limpiar_pantalla():
        for widget in contenedor_principal.winfo_children():
            widget.destroy()

    def menu_principal():
        limpiar_pantalla()

        lbl_titulo = tk.Label(
            contenedor_principal,
            text="💻 BIENVENIDO A GH PROGRAMMING 💻",
            font=("Arial", 36, "bold"),
            fg="#58a6ff",
            bg="#0d1117",
        )
        lbl_titulo.pack(pady=40)

        lbl_sub = tk.Label(
            contenedor_principal,
            text="Donde aprenderás lo básico de programación",
            font=("Arial", 22),
            fg="#3fb950",
            bg="#0d1117",
        )
        lbl_sub.pack(pady=20)

        botones = tk.Frame(contenedor_principal, bg="#0d1117")
        botones.pack(pady=100)

        tk.Button(
            botones,
            text="Soy nuevo 👶",
            font=("Arial", 20, "bold"),
            bg="#238636",
            fg="white",
            width=25,
            command=pantalla_nuevo,
        ).grid(row=0, column=0, pady=20)

        tk.Button(
            botones,
            text="Tengo experiencia 💪",
            font=("Arial", 20, "bold"),
            bg="#1f6feb",
            fg="white",
            width=25,
            command=pantalla_experiencia,
        ).grid(row=1, column=0, pady=20)

        tk.Button(
            botones,
            text="Salir 🚪",
            font=("Arial", 20, "bold"),
            bg="#d73a49",
            fg="white",
            width=25,
            command=app.destroy,
        ).grid(row=2, column=0, pady=20)

    # --------------------------------------------
    # MODO NUEVO APRENDIZ
    # --------------------------------------------
    def pantalla_nuevo():
        limpiar_pantalla()

        tk.Label(
            contenedor_principal,
            text="Bienvenido, nuevo aprendiz 👋",
            font=("Arial", 30, "bold"),
            fg="#58a6ff",
            bg="#0d1117",
        ).pack(pady=40)

        tk.Button(
            contenedor_principal,
            text="Comenzar teoría Nivel 1 📘",
            font=("Arial", 20, "bold"),
            bg="#238636",
            fg="white",
            width=30,
            command=lambda: mostrar_teoria_nivel_1(),
        ).pack(pady=20)

        tk.Button(
            contenedor_principal,
            text="Volver al menú principal",
            font=("Arial", 18),
            bg="#6e7681",
            fg="white",
            width=25,
            command=menu_principal,
        ).pack(pady=20)

    def mostrar_teoria_nivel_1():
        """Muestra la teoría de nivel 1 COMPLETA"""
        secciones = [
            """═══════════════════════════════════════════════════
    TEORÍA NIVEL 1 - FUNDAMENTOS DE PROGRAMACIÓN WEB
═══════════════════════════════════════════════════

Bienvenido al curso de programación web. En este nivel aprenderás los conceptos 
básicos de HTML, CSS y JavaScript que son la base de toda página web moderna.

HTML es el lenguaje de marcado que estructura el contenido.
CSS es el lenguaje de estilos que hace que todo se vea bonito.
JavaScript es el lenguaje de programación que hace que las páginas sean interactivas.

Presioná "Continuar" para avanzar a la siguiente sección.""",

            """═══════════════════════════════════════════════════
    SECCIÓN 1: HTML - ESTRUCTURA BÁSICA
═══════════════════════════════════════════════════

HTML (HyperText Markup Language) es el lenguaje estándar para crear páginas web.
Utiliza "etiquetas" que están encerradas entre < y >.

TÍTULOS Y ENCABEZADOS:
Los títulos se crean con las etiquetas <h1> hasta <h6>:

• <h1> - Es el título principal y más importante de la página
• <h2> - Subtítulo de segundo nivel
• <h3> hasta <h6> - Títulos de menor importancia

Ejemplo:
<h1>Mi primer sitio web</h1>
<h2>Sección de bienvenida</h2>

La etiqueta <h1> debe usarse solo UNA VEZ por página para el título principal.""",

            """═══════════════════════════════════════════════════
    SECCIÓN 2: HTML - COMENTARIOS Y ELEMENTOS BÁSICOS
═══════════════════════════════════════════════════

COMENTARIOS EN HTML:
Los comentarios son texto que NO se muestra en la página pero ayuda a documentar el código.
Se escriben así: <!-- Este es un comentario -->

SALTOS DE LÍNEA:
La etiqueta <br> crea un salto de línea (no necesita etiqueta de cierre).

Ejemplo:
<p>Primera línea<br>Segunda línea</p>

IMÁGENES:
La etiqueta <img> se usa para insertar imágenes:
<img src="imagen.jpg" alt="Descripción de la imagen">

• src: indica la ruta/URL de la imagen
• alt: texto alternativo si la imagen no carga (importante para accesibilidad)""",

            """═══════════════════════════════════════════════════
    SECCIÓN 3: HTML - ENLACES Y LISTAS
═══════════════════════════════════════════════════

ENLACES (LINKS):
La etiqueta <a> crea enlaces a otras páginas:
<a href="https://ejemplo.com">Ir a Ejemplo</a>

• href: es el atributo que indica la dirección web (URL) a la que lleva el enlace
• El texto entre <a> y </a> es lo que el usuario ve y puede hacer clic

LISTAS:
Hay dos tipos principales de listas:

• Listas NO ordenadas (con viñetas) - se crean con <ul>:
  <ul>
    <li>Elemento 1</li>
    <li>Elemento 2</li>
  </ul>

• Listas ORDENADAS (numeradas) - se crean con <ol>:
  <ol>
    <li>Primer paso</li>
    <li>Segundo paso</li>
  </ol>""",

            """═══════════════════════════════════════════════════
    SECCIÓN 4: HTML - TABLAS Y FORMULARIOS
═══════════════════════════════════════════════════

TABLAS:
Las tablas organizan información en filas y columnas:

<table>
  <tr>  <!-- Fila -->
    <th>Encabezado 1</th>  <!-- Celda de encabezado -->
    <th>Encabezado 2</th>
  </tr>
  <tr>
    <td>Dato 1</td>  <!-- Celda de datos -->
    <td>Dato 2</td>
  </tr>
</table>

INPUTS OBLIGATORIOS:
El atributo "required" hace que un campo de formulario sea obligatorio:
<input type="text" required>

Si el usuario intenta enviar el formulario sin completar campos con "required",
el navegador mostrará un mensaje de error.""",

            """═══════════════════════════════════════════════════
    SECCIÓN 5: CSS - FUNDAMENTOS DE ESTILOS
═══════════════════════════════════════════════════

CSS (Cascading Style Sheets) controla cómo se ven los elementos HTML.

PROPIEDAD COLOR:
La propiedad "color" cambia el color del TEXTO:

h1 {
  color: blue;  /* El texto del h1 será azul */
}

Puedes usar:
• Nombres: red, blue, green, yellow, etc.
• Hexadecimal: #FF0000, #00FF00, #0000FF
• RGB: rgb(255, 0, 0)

PROPIEDAD TEXT-ALIGN:
Controla la alineación del texto:

p {
  text-align: center;  /* Centra el texto */
}

Valores posibles:
• left - alinea a la izquierda (por defecto)
• center - centra el texto
• right - alinea a la derecha
• justify - justifica el texto""",

            """═══════════════════════════════════════════════════
    SECCIÓN 6: JAVASCRIPT - INTRODUCCIÓN
═══════════════════════════════════════════════════

JavaScript es el lenguaje de programación que hace las páginas web interactivas.

¿DÓNDE SE COLOCA JAVASCRIPT?
JavaScript se coloca dentro de la etiqueta <script>, que puede ir en:

1. Dentro del <head>:
   <head>
     <script>
       // código JavaScript aquí
     </script>
   </head>

2. Dentro del <body> (al final es mejor para rendimiento):
   <body>
     <h1>Mi página</h1>
     <script>
       // código JavaScript aquí
     </script>
   </body>

COMENTARIOS EN JAVASCRIPT:
Se usan dos barras diagonales: //

// Este es un comentario de una línea
let x = 5;  // También puede ir al final de una línea""",

            """═══════════════════════════════════════════════════
    SECCIÓN 7: JAVASCRIPT - TIPOS DE DATOS
═══════════════════════════════════════════════════

JavaScript tiene varios tipos de datos. Los más importantes son:

1. STRING (texto):
   let nombre = "Juan";
   let mensaje = 'Hola mundo';

2. NUMBER (números):
   let edad = 25;
   let precio = 19.99;

3. BOOLEAN (verdadero/falso):
   let activo = true;
   let apagado = false;
   
   Los booleanos solo pueden tener DOS valores: true o false
   Se usan para condiciones y decisiones en el código.

Ejemplo:
let esMayorDeEdad = true;
if (esMayorDeEdad) {
  console.log("Puede entrar");
}

═══════════════════════════════════════════════════
    ¡FIN DE LA TEORÍA NIVEL 1!
═══════════════════════════════════════════════════

Ahora estás listo para realizar el cuestionario de Nivel 1.
¡Mucha suerte! 🎉"""
        ]
        mostrar_teoria_en_frame(
            contenedor_principal,
            "📚 Teoría Nivel 1 – Nuevo Aprendiz",
            secciones,
            on_finish=despues_teoria1
        )

    # --- Después de leer teoría 1 ---
    def despues_teoria1():
        if messagebox.askyesno(
            "Evaluación Nivel 1",
            "¿Deseás realizar el cuestionario de evaluación de Nivel 1?"
        ):
            crear_cuestionario_en_frame(
                contenedor_principal,
                "Cuestionario Nivel 1",
                preguntas_nivel_1,
                on_releer=mostrar_teoria_nivel_1,
                on_menu=menu_principal,
                siguiente_nivel=mostrar_teoria_nivel_2
            )
        else:
            menu_principal()

    def mostrar_teoria_nivel_2():
        """Muestra la teoría de nivel 2 COMPLETA"""
        secciones = [
            """═══════════════════════════════════════════════════
    TEORÍA NIVEL 2 - CONCEPTOS INTERMEDIOS
═══════════════════════════════════════════════════

¡Felicitaciones por completar el Nivel 1!

En este nivel aprenderás conceptos más avanzados que te permitirán crear 
páginas web más profesionales e interactivas.

Veremos:
• HTML semántico y atributos avanzados
• CSS con Flexbox y posicionamiento
• JavaScript para manipular el DOM y manejar eventos

Presioná "Continuar" para comenzar.""",

            """═══════════════════════════════════════════════════
    SECCIÓN 1: HTML INTERMEDIO - ATRIBUTOS
═══════════════════════════════════════════════════

ATRIBUTO PLACEHOLDER:
Muestra un texto de ayuda dentro de un input que desaparece al escribir:

<input type="text" placeholder="Ingresá tu nombre">

El texto "Ingresá tu nombre" aparecerá en gris claro dentro del campo,
y desaparecerá cuando el usuario empiece a escribir.

ATRIBUTO REQUIRED:
Ya lo vimos en Nivel 1, pero es importante recordarlo:
<input type="email" required>
Hace que el campo sea OBLIGATORIO.

ATRIBUTO ACTION (en formularios):
Indica dónde se enviarán los datos del formulario:
<form action="/procesar" method="POST">
  <!-- campos del formulario -->
</form>""",

            """═══════════════════════════════════════════════════
    SECCIÓN 2: HTML SEMÁNTICO
═══════════════════════════════════════════════════

Las ETIQUETAS SEMÁNTICAS dan significado al contenido (no solo estilo).
Son importantes para accesibilidad y SEO (posicionamiento en buscadores).

Principales etiquetas semánticas:

• <section> - Define una sección temática del documento
  Agrupa contenido relacionado, como capítulos de un libro.
  
• <article> - Define contenido independiente y auto-contenido
  Puede ser un artículo de blog, noticia, comentario, etc.
  
• <aside> - Define contenido complementario o lateral
  Como una barra lateral con información adicional.

Ejemplo:
<section>
  <h2>Noticias deportivas</h2>
  <article>
    <h3>Gran partido de fútbol</h3>
    <p>Descripción del partido...</p>
  </article>
</section>

<aside>
  <p>Dato curioso relacionado...</p>
</aside>""",

            """═══════════════════════════════════════════════════
    SECCIÓN 3: CSS INTERMEDIO - FLEXBOX
═══════════════════════════════════════════════════

FLEXBOX es un sistema de diseño que facilita organizar elementos en filas o columnas.

Para activar Flexbox:
.contenedor {
  display: flex;
}

PROPIEDADES IMPORTANTES:

• justify-content: Alinea elementos en el eje principal (horizontal por defecto)
  - flex-start: al inicio
  - center: al centro
  - flex-end: al final
  - space-between: espacio entre elementos

• align-items: Alinea elementos en el eje cruzado (vertical por defecto)
  - flex-start: arriba
  - center: centro
  - flex-end: abajo
  - stretch: estira los elementos

Ejemplo:
.contenedor {
  display: flex;
  justify-content: center;  /* Centra horizontalmente */
  align-items: center;      /* Centra verticalmente */
}""",

            """═══════════════════════════════════════════════════
    SECCIÓN 4: CSS INTERMEDIO - DISPLAY Y POSITION
═══════════════════════════════════════════════════

PROPIEDAD DISPLAY:
Controla cómo se muestra un elemento.

• display: none; - OCULTA completamente el elemento
  El elemento no ocupa espacio en la página.
  
• display: block; - El elemento ocupa todo el ancho disponible
• display: inline; - El elemento ocupa solo el espacio necesario

PROPIEDAD POSITION:
Controla el posicionamiento de elementos.

• position: static; - Posición normal (por defecto)
• position: relative; - Se posiciona relativo a su posición original
• position: absolute; - Se posiciona relativo a su contenedor más cercano
  que tenga position: relative

Ejemplo importante:
.padre {
  position: relative;  /* Contenedor de referencia */
}

.hijo {
  position: absolute;  /* Se posiciona relativo al padre */
  top: 10px;
  left: 20px;
}""",

            """═══════════════════════════════════════════════════
    SECCIÓN 5: CSS - TEXT-ALIGN AVANZADO
═══════════════════════════════════════════════════

Ya conocés text-align: center; del Nivel 1.

Otros valores importantes:

• text-align: left; - Alinea a la IZQUIERDA (por defecto)
• text-align: right; - Alinea a la DERECHA
• text-align: justify; - JUSTIFICA el texto (como en libros)
• text-align: center; - CENTRA el texto

Ejemplo:
.titulo {
  text-align: center;  /* Título centrado */
}

.fecha {
  text-align: right;   /* Fecha a la derecha */
}

.parrafo {
  text-align: justify; /* Texto justificado */
}""",

            """═══════════════════════════════════════════════════
    SECCIÓN 6: JAVASCRIPT - EL DOM
═══════════════════════════════════════════════════

¿QUÉ ES EL DOM?
DOM significa "Document Object Model" (Modelo de Objetos del Documento).
Es la ESTRUCTURA que representa todo el HTML de una página.

El DOM convierte el HTML en un "árbol" de objetos que JavaScript puede manipular.

SELECCIONAR ELEMENTOS CON getElementById():
Es el método más común para seleccionar un elemento por su ID:

HTML:
<div id="miDiv">Contenido</div>

JavaScript:
let elemento = document.getElementById("miDiv");
elemento.style.color = "red";  // Cambia el color a rojo

IMPORTANTE: 
- getElementById busca UN elemento con ese ID específico
- Los IDs deben ser únicos en la página
- Devuelve el elemento o null si no existe""",

            """═══════════════════════════════════════════════════
    SECCIÓN 7: JAVASCRIPT - EVENTOS
═══════════════════════════════════════════════════

Los EVENTOS son acciones que ocurren en la página: clics, teclas, movimientos del mouse, etc.

MÉTODO addEventListener():
Es la forma moderna y recomendada de manejar eventos:

Sintaxis:
elemento.addEventListener('tipoDeEvento', función);

Ejemplo de evento 'click':
let boton = document.getElementById("miBoton");

boton.addEventListener('click', function() {
  alert("¡Hiciste clic!");
});

Eventos comunes:
• 'click' - cuando se hace clic
• 'mouseover' - cuando el mouse pasa por encima
• 'keypress' - cuando se presiona una tecla
• 'submit' - cuando se envía un formulario
• 'change' - cuando cambia el valor de un input""",

            """═══════════════════════════════════════════════════
    SECCIÓN 8: JAVASCRIPT - VARIABLES Y TIPOS DE INPUT
═══════════════════════════════════════════════════

VARIABLES: let y const
En JavaScript moderno usamos:

• let - para variables que PUEDEN cambiar:
  let edad = 25;
  edad = 26;  // Puedo cambiar el valor

• const - para variables que NO cambian (constantes):
  const PI = 3.14159;
  // PI = 3.14;  // ¡ERROR! No se puede cambiar

TIPOS DE INPUT:
HTML5 introdujo muchos tipos de input especializados:

• <input type="text"> - Texto normal
• <input type="email"> - Email (valida formato)
• <input type="date"> - Selector de FECHA (calendario)
• <input type="number"> - Solo números
• <input type="password"> - Oculta el texto
• <input type="checkbox"> - Casilla de verificación
• <input type="radio"> - Botón de opción

El type="date" es especialmente útil porque muestra un calendario
visual para que el usuario seleccione la fecha fácilmente.""",

            """═══════════════════════════════════════════════════
    SECCIÓN 9: JAVASCRIPT - API
═══════════════════════════════════════════════════

¿QUÉ ES UNA API?
API significa "Application Programming Interface" (Interfaz de Programación de Aplicaciones).

En el contexto web, una API permite que tu página se comunique con 
SERVICIOS EXTERNOS (otros servidores) para obtener o enviar datos.

Ejemplo: Obtener el clima actual
fetch('https://api.clima.com/ciudad/buenos-aires')
  .then(response => response.json())
  .then(data => {
    console.log("Temperatura: " + data.temperatura);
  });

Las APIs son fundamentales para:
• Obtener datos de bases de datos
• Conectarse a redes sociales
• Procesar pagos
• Obtener información en tiempo real

Por ahora solo necesitás saber que las APIs permiten que tu código
JavaScript se comunique con servicios externos.""",

            """═══════════════════════════════════════════════════
    SECCIÓN 10: LISTAS Y TABLAS AVANZADAS
═══════════════════════════════════════════════════

LISTAS (repaso con detalles):
• <ul> - Lista NO ordenada (viñetas)
• <ol> - Lista ORDENADA (números)
• <li> - Elemento de lista (list item)

TABLAS AVANZADAS:
Las tablas pueden tener secciones semánticas:

<table>
  <thead>  <!-- Encabezado de la tabla -->
    <tr>
      <th>Nombre</th>
      <th>Edad</th>
    </tr>
  </thead>
  
  <tbody>  <!-- Cuerpo de la tabla -->
    <tr>
      <td>Juan</td>
      <td>25</td>
    </tr>
  </tbody>
  
  <tfoot>  <!-- Pie de tabla (resumen, totales, etc.) -->
    <tr>
      <td>Total:</td>
      <td>1 persona</td>
    </tr>
  </tfoot>
</table>

Esto mejora la semántica y accesibilidad de las tablas.

═══════════════════════════════════════════════════
    ¡FIN DE LA TEORÍA NIVEL 2!
═══════════════════════════════════════════════════

¡Excelente trabajo! Ahora tenés conocimientos intermedios de:
• HTML semántico y formularios avanzados
• CSS con Flexbox y posicionamiento
• JavaScript para manipular el DOM y manejar eventos

Estás listo para el cuestionario de Nivel 2. ¡Adelante! 🚀"""
        ]
        mostrar_teoria_en_frame(
            contenedor_principal,
            "📚 Teoría Nivel 2 - Intermedio",
            secciones,
            on_finish=despues_teoria2
        )

    # --- Después de leer teoría 2 ---
    def despues_teoria2():
        if messagebox.askyesno(
            "Evaluación Nivel 2",
            "¿Deseás realizar el cuestionario de evaluación de Nivel 2?"
        ):
            crear_cuestionario_en_frame(
                contenedor_principal,
                "Cuestionario Nivel 2",
                preguntas_nivel_2,
                on_releer=mostrar_teoria_nivel_2,
                on_menu=menu_principal
            )
        else:
            menu_principal()

    # --------------------------------------------
    # MODO EXPERIENCIA (CON TUTORIAL)
    # --------------------------------------------
    def pantalla_experiencia():
        limpiar_pantalla()

        tk.Label(
            contenedor_principal,
            text="Modo con experiencia 💪",
            font=("Arial", 30, "bold"),
            fg="#58a6ff",
            bg="#0d1117",
        ).pack(pady=40)

        tk.Label(
            contenedor_principal,
            text="¿Querés realizar el tutorial para repasar conceptos?",
            font=("Arial", 20),
            fg="white",
            bg="#0d1117",
        ).pack(pady=20)

        tk.Button(
            contenedor_principal,
            text="Sí, comenzar tutorial 🧠",
            font=("Arial", 20, "bold"),
            bg="#238636",
            fg="white",
            width=30,
            command=lambda: tutorial_en_frame(contenedor_principal, on_finish=resultado_tutorial),
        ).pack(pady=20)

        tk.Button(
            contenedor_principal,
            text="Volver al menú principal",
            font=("Arial", 18),
            bg="#6e7681",
            fg="white",
            width=25,
            command=menu_principal,
        ).pack(pady=20)

    def resultado_tutorial(resultado):
        """Callback que maneja el resultado del tutorial"""
        # ====== MODIFICADO: Sin segundo cartel, va directo al siguiente nivel ======
        if resultado == "tutorial aprobado":
            mostrar_teoria_nivel_2()  # Va directo sin mostrar otro cartel
        elif resultado == "tutorial abandonado":
            # El usuario volvió al menú desde el tutorial
            menu_principal()
        else:
            # Tutorial no aprobado
            mostrar_teoria_nivel_1()  # Va directo a repasar sin cartel extra

    # --------------------------------------------
    # INICIO
    # --------------------------------------------
    menu_principal()
    app.mainloop()


# ============================================================
# PUNTO DE ENTRADA PRINCIPAL
# ============================================================
if __name__ == "__main__":
    iniciar_programa()
