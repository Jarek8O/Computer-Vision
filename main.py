import cv2
from deepface import DeepFace
import os

# Carpeta donde están las fotos registradas
RUTA_FOTOS = "fotos"

def capturar_imagen():
    cam = cv2.VideoCapture(0)
    print("Presiona SPACE para capturar la imagen")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Camara", frame)

        key = cv2.waitKey(1)

        # SPACE para capturar
        if key % 256 == 32:
            img_path = "captura.jpg"
            cv2.imwrite(img_path, frame)
            print("Imagen capturada")
            break

    cam.release()
    cv2.destroyAllWindows()
    return img_path


def verificar_persona(imagen_capturada):
    for archivo in os.listdir(RUTA_FOTOS):
        ruta_foto = os.path.join(RUTA_FOTOS, archivo)

        try:
            resultado = DeepFace.verify(
                img1_path=ruta_foto,
                img2_path=imagen_capturada,
                enforce_detection=False
            )

            if resultado["verified"]:
                print(f"Asistencia registrada: {archivo}")
                return

        except:
            pass

    print("Persona no reconocida")


def main():
    imagen = capturar_imagen()
    verificar_persona(imagen)


if __name__ == "__main__":
    main()
