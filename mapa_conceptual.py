#si no funciona poner en terminal: pip install matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


fig, ax = plt.subplots(figsize=(14, 9))
ax.set_xlim(0, 14)
ax.set_ylim(0, 9)
ax.axis('off')
ax.set_title("Mapa Conceptual: Circuitería Alternativa de E/S",
             fontsize=16, fontweight='bold', color='#1a237e', pad=15)


def concepto(x, y, texto, color='#AED6F1', ancho=2.4, alto=0.9, tam=11):
    caja = FancyBboxPatch(
        (x - ancho/2, y - alto/2), ancho, alto,
        boxstyle="round,pad=0.08,rounding_size=0.2",
        linewidth=1.5, edgecolor='#1a237e', facecolor=color, zorder=3
    )
    ax.add_patch(caja)
    ax.text(x, y, texto, ha='center', va='center',
            fontsize=tam, fontweight='bold', color='#0d1b2a', zorder=4)


def enlace(x1, y1, x2, y2, etiqueta='', color='#37474F',
           estilo='-', dashed=False):
    flecha = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='-|>', mutation_scale=15,
        linewidth=1.5, color=color, zorder=2,
        linestyle='--' if dashed else '-'
    )
    ax.add_patch(flecha)
    if etiqueta:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mx, my + 0.08, etiqueta, ha='center', va='bottom',
                fontsize=9, style='italic', color='#455A64',
                bbox=dict(boxstyle='round,pad=0.15',
                          fc='white', ec='none', alpha=0.85),
                zorder=5)


concepto(7, 8.2, "Circuitería Alternativa\nde E/S", color='#F7DC6F',
         ancho=3.2, alto=1.0, tam=13)


concepto(2.5, 6.2, "E/S Programada", color='#A9DFBF', ancho=2.6)
concepto(7.0, 6.2, "E/S por\nInterrupciones", color='#A9DFBF', ancho=2.6)
concepto(11.5, 6.2, "DMA", color='#A9DFBF', ancho=2.0)


concepto(1.2, 4.2, "Polling", color='#F5B7B1', ancho=2.0)
concepto(3.8, 4.2, "CPU en\nespera activa", color='#F5B7B1', ancho=2.2)
concepto(6.2, 4.2, "IRQ", color='#F5B7B1', ancho=1.6)
concepto(8.2, 4.2, "Manejador de\ninterrupción", color='#F5B7B1', ancho=2.6)
concepto(10.8, 4.2, "Controlador\nDMA", color='#F5B7B1', ancho=2.2)
concepto(12.8, 4.2, "Transf. directa\na RAM", color='#F5B7B1', ancho=2.2)


concepto(1.2, 2.2, "Teclado", color='#D7BDE2', ancho=1.8, tam=10)
concepto(3.8, 2.2, "Impresora", color='#D7BDE2', ancho=1.8, tam=10)
concepto(10.8, 2.2, "Discos SSD", color='#D7BDE2', ancho=1.8, tam=10)
concepto(12.8, 2.2, "Tarjetas de red", color='#D7BDE2', ancho=2.2, tam=10)



enlace(7, 7.7, 2.5, 6.65, "se clasifica en")
enlace(7, 7.7, 7.0, 6.65, "se clasifica en")
enlace(7, 7.7, 11.5, 6.65, "se clasifica en")


enlace(2.0, 5.85, 1.2, 4.65, "usa")
enlace(3.0, 5.85, 3.8, 4.65, "provoca")
enlace(6.5, 5.75, 6.2, 4.65, "genera")
enlace(7.5, 5.75, 8.2, 4.65, "ejecuta")
enlace(10.9, 5.75, 10.8, 4.65, "requiere")
enlace(12.0, 5.75, 12.8, 4.65, "permite")


enlace(1.2, 3.75, 1.2, 2.65, "ejemplo")
enlace(3.8, 3.75, 3.8, 2.65, "ejemplo")
enlace(10.8, 3.75, 10.8, 2.65, "ejemplo")
enlace(12.8, 3.75, 12.8, 2.65, "ejemplo")


enlace(10.0, 4.6, 7.1, 4.6, "libera al CPU de",
       color='#C62828', dashed=True)
enlace(8.2, 3.9, 4.0, 3.9, "evita",
       color='#C62828', dashed=True)


leyenda = [
    mpatches.Patch(color='#F7DC6F', label='Concepto raíz'),
    mpatches.Patch(color='#A9DFBF', label='Nivel 1: Tipos de E/S'),
    mpatches.Patch(color='#F5B7B1', label='Nivel 2: Mecanismos'),
    mpatches.Patch(color='#D7BDE2', label='Nivel 3: Ejemplos'),
    mpatches.Patch(color='#C62828', label='Conexión cruzada'),
]
ax.legend(handles=leyenda, loc='lower left', fontsize=9,
          framealpha=0.9, ncol=2)

plt.tight_layout()
plt.show()   