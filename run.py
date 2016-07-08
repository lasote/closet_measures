MARGIN = 0.5


def margin_05(measure):
    return [mes - MARGIN for mes in measure]

DEEP = 56
WIDTH = 130
HEIGHT = 238

FLOOR_MEASURES = (0, 0)
GENERAL_DEEP = 50
TRUNK_HEIGHT = 50

WRAPPER_WOOD_WIDTH = 1
INTERIOR_WOOD_WIDTH = 1.6

LEFT_FRAME = 13
RIGHT_FRAME = 20

NEEDED_GAP_LEFT = 53

print("\n\nMELAMINA BLANCA 1 canto, 10mm")
print("---------------------------------\n")
print("Tablero techo: %s" % str(margin_05((WIDTH, DEEP))))
print("Tablero suelo: %s" % str(margin_05(FLOOR_MEASURES)))

print("Tapa trasera maletero: %s" % str((WIDTH - MARGIN, TRUNK_HEIGHT)))
print("Tapas laterales maletero 2x: %s" % str((DEEP - WRAPPER_WOOD_WIDTH - MARGIN, TRUNK_HEIGHT)))

ancho_izquierda_abajo = LEFT_FRAME + NEEDED_GAP_LEFT
ancho_derecha_abajo = WIDTH - ancho_izquierda_abajo

alto_abajo = HEIGHT - (2 * WRAPPER_WOOD_WIDTH) - TRUNK_HEIGHT - INTERIOR_WOOD_WIDTH

print("Tapa fondo abajo 1: %s" % str((ancho_izquierda_abajo, alto_abajo)))
print("Tapa fondo abajo 2: %s" % str((ancho_derecha_abajo, alto_abajo)))
print("Tapas lateral abajo 2x: %s" % str((GENERAL_DEEP - MARGIN - WRAPPER_WOOD_WIDTH, alto_abajo)))


print("\n\nMELAMINA BLANCA 1 canto, 20mm:")
print("---------------------------------\n")
print("Tablero maletero: %s" % str((WIDTH - MARGIN, GENERAL_DEEP)))
print("Separador vertical: %s" % str((GENERAL_DEEP, alto_abajo)))
print("Baldas izquierda 2x: %s" % str((ancho_izquierda_abajo, GENERAL_DEEP)))
print("Baldas derecha 1x: %s" % str((ancho_derecha_abajo, GENERAL_DEEP)))
print("\n")
