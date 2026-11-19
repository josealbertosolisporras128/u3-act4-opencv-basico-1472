# ==============================================================================
# 0. IMPORTACIÓN DE LIBRERÍAS Y FUNCIÓN DE VISUALIZACIÓN
# ==============================================================================
import cv2  # Importa la librería OpenCV para procesamiento de imágenes y visión artificial.
import numpy as np  # Importa NumPy para manejar las imágenes como arreglos/matrices matemáticas.
import sys  # Importa Sys para poder detener el programa de forma segura si ocurre un error.
import win32con
import win32api
import win32gui

print("------jose solis NC 1472-------")

def mostrar_imagen(titulo, imagen, escala=0.45):
    """Muestra la imagen escalada para que quepa en pantalla sin modificar la matriz original."""
    alto, ancho = imagen.shape[:2]
    nuevo_tamano = (int(ancho * escala), int(alto * escala))
    img_vista = cv2.resize(imagen, nuevo_tamano, interpolation=cv2.INTER_AREA)
    cv2.imshow(titulo, img_vista)

# ==============================================================================
# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES 1472")  # Imprime el título de la sección en la consola.
imgkenia_os = cv2.imread('keniaos.jpg')  # Lee la imagen 'keniaos.jpg' y la guarda como matriz.

if imgkenia_os is None:  # Verifica si la variable está vacía (es decir, si no encontró el archivo).
    print("Error: No se pudo leer 'keniaos.jpg'. Revisa el nombre y ubicación.")  # Muestra mensaje de error.
    sys.exit()  # Detiene inmediatamente la ejecución del programa para evitar fallos posteriores.
else:  # Si la imagen sí se cargó correctamente...
    print("Imagen cargada exitosamente.")  # Confirma en consola que la imagen está lista.

# ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN")  # Imprime el título de la segunda sección.
height, width, channels = imgkenia_os.shape  # Extrae el alto (filas), ancho (columnas) y canales de color.
print(f"Dimensiones de la imagen: {width}x{height} píxeles")  # Muestra el ancho por el alto en consola.
print(f"Número de canales de color: {channels}")  # Muestra cuántos canales tiene (3 para BGR).
print(f"Tipo de dato de la imagen: {imgkenia_os.dtype}")  # Muestra el tipo de dato (uint8 = enteros de 0 a 255).
print(f"Total de datos/píxeles: {imgkenia_os.size}")  # Muestra la cantidad total de valores numéricos en la matriz.

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL de kenia os")  # Imprime el título de la tercera sección.
print("Presiona cualquier tecla sobre la ventana de la imagen para continuar...")  # Instrucción para el usuario.
mostrar_imagen('gpo 3H kenia os jose solis 1472', imgkenia_os)  # Muestra la imagen reducida al 45%.
cv2.waitKey(0)  # Pausa el programa infinitamente hasta que el usuario presione una tecla.
cv2.destroyAllWindows()  # Cierra todas las ventanas de imágenes.

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")  # Imprime el título de la cuarta sección.
pixel_img = imgkenia_os.copy()  # Crea una copia exacta de la imagen original para no dañar la original.

y, x = 100, 150  # Define las coordenadas a analizar: fila (Y) = 100, columna (X) = 150.
pixel = pixel_img[y, x]  # Obtiene los 3 valores de color [Azul, Verde, Rojo] del píxel en esa posición.
print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")  # Imprime los valores BGR del píxel en consola.

pixel_img[y, x] = [0, 0, 255]  # Cambia el color de ese único píxel a Rojo puro (0 Azul, 0 Verde, 255 Rojo).
cv2.circle(pixel_img, (x, y), 15, (0, 255, 255), 2)  # Dibuja un círculo amarillo alrededor para verlo a simple vista.

mostrar_imagen('Pixel Modificado jose solis 1472', pixel_img)  # Muestra la imagen con el píxel alterado y señalado.
cv2.waitKey(0)  # Espera a que se presione una tecla para continuar.
cv2.destroyAllWindows()

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI - REGION OF INTEREST)
# ==============================================================================
print("\n5. REGIÓN DE INTERÉS (ROI)")  # Imprime el título de la quinta sección.
roi_img = imgkenia_os.copy()  # Crea una nueva copia limpia de la imagen original.

roi = roi_img[50:200, 100:300]  # Recorta una sub-matriz desde la fila 50 a 200 y columna 100 a 300.
cv2.rectangle(roi_img, (100, 50), (300, 200), (0, 255, 0), 2)  # Dibuja un rectángulo verde marcando la zona recortada.

mostrar_imagen('Imagen con ROI marcada jose solis 1472', roi_img)  # Muestra la imagen completa con el recuadro verde.
cv2.waitKey(0)  # Espera a que se presione una tecla.

cv2.imshow('ROI Extraida (Recorte) jose solis 1472', roi)  # Muestra el pedazo recortado (ya es pequeño de por sí).
cv2.waitKey(0)  # Espera a que se presione una tecla.
cv2.destroyAllWindows()

# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES DE COLOR (BGR)
# ==============================================================================
print("\n6. SEPARANDO Y FUSIONANDO CANALES")  # Imprime el título de la sexta sección.
b, g, r = cv2.split(imgkenia_os)  # Divide la imagen a color en 3 matrices independientes: Azul, Verde y Rojo.

mostrar_imagen('Canal Azul (Escala de grises) jose solis 1472', b)  # Muestra la intensidad del canal azul en tonos de gris.
mostrar_imagen('Canal Verde (Escala de grises) jose solis 1472', g)  # Muestra la intensidad del canal verde en tonos de gris.
mostrar_imagen('Canal Rojo (Escala de grises) jose solis 1472', r)  # Muestra la intensidad del canal rojo en tonos de gris.
cv2.waitKey(0)  # Pausa el programa mientras observas las 3 ventanas en blanco y negro.
cv2.destroyAllWindows()

zeros = np.zeros_like(b)  # Crea una matriz llena de ceros (negro) del mismo tamaño que un canal.
blue_img = cv2.merge([b, zeros, zeros])  # Une el canal azul real con verde y rojo en cero (solo se ve azul).
green_img = cv2.merge([zeros, g, zeros])  # Une el canal verde real con azul y rojo en cero (solo se ve verde).
red_img = cv2.merge([zeros, zeros, r])  # Une el canal rojo real con azul y verde en cero (solo se ve rojo).

mostrar_imagen('Canal Azul (Coloreado) jose solis 1472', blue_img)  # Muestra la imagen filtrada únicamente en color azul.
mostrar_imagen('Canal Verde (Coloreado) jose solis 1472', green_img)  # Muestra la imagen filtrada únicamente en color verde.
mostrar_imagen('Canal Rojo (Coloreado) jose solis 1472', red_img)  # Muestra la imagen filtrada únicamente en color rojo.
cv2.waitKey(0)  # Espera a que se presione una tecla para avanzar.
cv2.destroyAllWindows()

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES (RESIZING)
# ==============================================================================
print("\n7. REDIMENSIONANDO IMÁGENES")  # Imprime el título de la séptima sección.
resized_img = cv2.resize(imgkenia_os, (400, 300))  # Cambia el tamaño exacto a 400px de ancho por 300px de alto.
cv2.imshow('Redimensionada a 400x300 jose solis 1472', resized_img)  # Muestra la imagen con sus nuevas dimensiones fijas.
cv2.waitKey(0)  # Espera a que se presione una tecla.

half_size = cv2.resize(imgkenia_os, None, fx=0.5, fy=0.5)  # Reduce la imagen a la mitad (50% ancho y 50% alto).
double_size = cv2.resize(imgkenia_os, None, fx=1.5, fy=1.5)  # Amplía la imagen un 50% extra (escala 1.5x).

cv2.imshow('Mitad de tamano (0.5x) jose solis 1472', half_size)  # Muestra la versión reducida.
cv2.waitKey(0)  # Espera a que se presione una tecla.
cv2.imshow('Ampliada (1.5x) jose solis 1472', double_size)  # Muestra la versión ampliada.
cv2.waitKey(0)  # Espera a que se presione una tecla.
cv2.destroyAllWindows()

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n8. ROTANDO IMÁGENES")  # Imprime el título de la octava sección.
height, width = imgkenia_os.shape[:2]  # Obtiene nuevamente el alto y ancho actual de la imagen original.
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)  # Calcula matriz para girar 45°.
rotated_img = cv2.warpAffine(imgkenia_os, rotation_matrix, (width, height))  # Aplica la rotación sobre la imagen.

mostrar_imagen('Imagen Rotada (45 grados) jose solis 1472', rotated_img)  # Muestra la imagen inclinada 45 grados.
cv2.waitKey(0)  # Espera a que se presione una tecla.
cv2.destroyAllWindows()

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES (FLIPPING)
# ==============================================================================
print("\n9. VOLTEANDO IMÁGENES")  # Imprime el título de la novena sección.
horizontal_flip = cv2.flip(imgkenia_os, 1)  # Voltea la imagen horizontalmente (código 1 = efecto espejo).
mostrar_imagen('Volteo Horizontal (Espejo) jose solis 1472', horizontal_flip)  # Muestra el volteo horizontal.
cv2.waitKey(0)  # Espera a que se presione una tecla.

vertical_flip = cv2.flip(imgkenia_os, 0)  # Voltea la imagen verticalmente (código 0 = de cabeza).
mostrar_imagen('Volteo Vertical (De cabeza) jose solis 1472', vertical_flip)  # Muestra el volteo vertical.
cv2.waitKey(0)  # Espera a que se presione una tecla.

both_flip = cv2.flip(imgkenia_os, -1)  # Voltea en ambos ejes al mismo tiempo (código -1 = horizontal + vertical).
mostrar_imagen('Volteo en Ambos Ejes jose solis 1472', both_flip)  # Muestra el volteo combinado.
cv2.waitKey(0)  # Espera a que se presione una tecla.
cv2.destroyAllWindows()

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n10. GUARDANDO IMAGEN RESULTANTE")  # Imprime el título de la décima sección.
result = cv2.imwrite('rotated_image.jpg', rotated_img)  # Guarda la imagen rotada en el disco duro.

if result:  # Comprueba si el guardado devolvió True (verdadero).
    print("Imagen rotada guardada exitosamente como 'rotated_image.jpg'")  # Confirma que el archivo se creó.
else:  # Si ocurrió algún problema de permisos o ruta...
    print("Error: No se pudo guardar la imagen rotada.")  # Notifica el fallo en consola.

cv2.destroyAllWindows()  # Cierra todas las ventanas gráficas abiertas por OpenCV para liberar memoria RAM.
print("\n¡Todas las operaciones se completaron con éxito!")  # Mensaje final de cierre en la terminal.
















