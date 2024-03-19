cv2.rectangle(imagen, (x, y), (x + ancho, y + alto), (0, 255, 0), 2)
# Definir las coordenadas de la región de interés (ROI)
x, y, ancho, alto = (
    100,
    100,
    200,
    200,
)  # Ejemplo: esquina superior izquierda (100, 100), ancho=200, alto=200


# Dibujar puntos de origen en la imagen original
for punto in puntos_origen:
    cv2.circle(imagen, (int(punto[0]), int(punto[1])), 5, (0, 255, 0), -1)

# Dibujar puntos de destino en la imagen del carril
for punto in puntos_destino:
    cv2.circle(carril, (int(punto[0]), int(punto[1])), 5, (0, 255, 0), -1)

# Definir los 4 puntos de interés en la imagen original (esquinas del carril)

puntos_origen = np.array(
    [
        [0, 0],
        [imagen.shape[1], 0],
        [0, imagen.shape[0]],
        [imagen.shape[1], imagen.shape[0]],
    ],
    dtype=np.float32,
)

# Definir las posiciones correspondientes de los puntos de interés en la imagen de salida (imagen transformada)
puntos_destino = np.array(
    [[100, 100], [500, 100], [100, 400], [500, 400]], dtype=np.float32
)

# Calcular la matriz de transformación
matriz_transformacion = cv2.getPerspectiveTransform(puntos_origen, puntos_destino)

# Aplicar la transformación de perspectiva a la imagen original
carril = cv2.warpPerspective(imagen, matriz_transformacion, (600, 600))
cv2.imshow("Carril", carril)
