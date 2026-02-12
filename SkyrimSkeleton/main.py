import cv2
import mediapipe as mp
import time

# 1. MediaPipe Kurulumu
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# 2. Kamera Erişimi (0 genelde laptop kamerasıdır)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Kameradan görüntü alınamadı.")
        continue

    # MediaPipe RGB sever, OpenCV BGR kullanır. Dönüşüm yapıyoruz.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Performans için görüntüyü yazmaya kapatalım (Process ederken)
    image.flags.writeable = False

    # --- MODELİN ÇALIŞTIĞI AN ---
    results = face_mesh.process(image)
    # ---------------------------

    # Görüntüyü tekrar BGR'a çevir (Ekrana basmak için)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Eğer yüz bulduysa çizim yap
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Yüzdeki o ağı (mesh) çizelim
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec)

    # Ekrana bas
    cv2.imshow('Doom Scrolling Police', image)

    # 'q' tuşuna basarsan çık
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()