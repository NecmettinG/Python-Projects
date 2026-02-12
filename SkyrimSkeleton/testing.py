import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # 1. Görüntü İşleme Ön Hazırlığı
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  # Ayna etkisi için flip
    image.flags.writeable = False
    results = face_mesh.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    img_h, img_w, img_c = image.shape
    face_3d = []
    face_2d = []

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for idx, lm in enumerate(face_landmarks.landmark):
                # Bizim için önemli olan kilit noktalar (Burun ucu, çene, göz kenarları vb.)
                # Bu noktalar evrensel MediaPipe indeksleridir.
                if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                    if idx == 1:  # Burun ucu
                        nose_2d = (lm.x * img_w, lm.y * img_h)
                        nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)

                    x, y = int(lm.x * img_w), int(lm.y * img_h)

                    # 2D ve 3D koordinat listelerini doldur
                    face_2d.append([x, y])
                    face_3d.append([x, y, lm.z])

            face_2d = np.array(face_2d, dtype=np.float64)
            face_3d = np.array(face_3d, dtype=np.float64)

            # Kamera Matrisi (Kameranın odak uzaklığı vb. simüle ediyoruz)
            focal_length = 1 * img_w
            cam_matrix = np.array([[focal_length, 0, img_h / 2],
                                   [0, focal_length, img_w / 2],
                                   [0, 0, 1]])

            # Distortion (Bozulma) katsayıları (0 varsayıyoruz)
            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            # --- MATH MAGIC: Solve PnP ---
            # 2D görüntüden 3D rotasyonu buluyoruz
            success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

            # Rotasyon vektörünü Rotasyon Matrisine çevir
            rmat, jac = cv2.Rodrigues(rot_vec)

            # Euler Açılarını (Pitch, Yaw, Roll) hesapla
            angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

            # Açılar (Derece cinsinden)
            x = angles[0] * 360  # Pitch (Aşağı/Yukarı)
            y = angles[1] * 360  # Yaw (Sağa/Sola)

            # --- EKRANA YAZDIRMA ---
            # Bakış yönünü tespit et
            text = "Duz Bakiyor"

            # NOT: Bu eşik değerleri (threshold) senin testine göre değişecek!
            if x < -10:
                text = "ASAGI BAKIYOR (TELEFON?)"
                color = (0, 0, 255)  # Kırmızı
            elif x > 10:
                text = "Yukari Bakiyor"
                color = (255, 0, 0)
            else:
                color = (0, 255, 0)  # Yeşil

            # Burun ucundan çıkan bir çizgi çizelim (Görselleştirmek için)
            nose_3d_projection, jacobian = cv2.projectPoints(nose_3d, rot_vec, trans_vec, cam_matrix, dist_matrix)
            p1 = (int(nose_2d[0]), int(nose_2d[1]))
            p2 = (int(nose_2d[0] + y * 10), int(nose_2d[1] - x * 10))

            cv2.line(image, p1, p2, color, 3)
            cv2.putText(image, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
            cv2.putText(image, "x (Pitch): " + str(np.round(x, 2)), (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (255, 255, 255), 2)

    cv2.imshow('Head Pose Estimation', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()