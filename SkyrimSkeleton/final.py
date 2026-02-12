import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import warnings
import os
import pygame
from moviepy import VideoFileClip
import urllib.request

# --- 1. UYARILARI SUSTURMA ---
# MediaPipe'ın eski protobuf versiyonlarından kaynaklanan o uzun uyarıyı engeller
warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# --- AYARLAR ---
DOOM_THRESHOLD = -10.5  # Eşik değerin
VIDEO_PATH = "skeleton.mp4"
AUDIO_PATH = "skeleton_audio.mp3"
MODEL_PATH = "face_landmarker.task"

# --- MODEL DOSYASINI İNDİR (Bir kez) ---
if not os.path.exists(MODEL_PATH):
    print("Face Landmarker modeli indiriliyor...")
    model_url = "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task"
    urllib.request.urlretrieve(model_url, MODEL_PATH)
    print("Model indirildi!")

# --- SES DOSYASINI ÇIKAR (Bir kez) ---
if not os.path.exists(AUDIO_PATH):
    print("Ses dosyası çıkarılıyor...")
    video_clip = VideoFileClip(VIDEO_PATH)
    if video_clip.audio is not None:
        video_clip.audio.write_audiofile(AUDIO_PATH, logger=None)
    video_clip.close()
    print("Ses dosyası hazır!")

# --- PYGAME SES KURULUMU ---
pygame.mixer.init()
pygame.mixer.music.load(AUDIO_PATH)

# --- MEDIAPIPE KURULUMU (New Tasks API) ---
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    output_face_blendshapes=False,
    output_facial_transformation_matrixes=False,
    num_faces=1,
    min_face_detection_confidence=0.5,
    min_face_presence_confidence=0.5,
    min_tracking_confidence=0.5
)
face_landmarker = vision.FaceLandmarker.create_from_options(options)

# --- KAMERA VE VIDEO YÜKLEME ---
cap = cv2.VideoCapture(0)
video_cap = cv2.VideoCapture(VIDEO_PATH)

if not video_cap.isOpened():
    print(f"Hata: {VIDEO_PATH} bulunamadı.")
    exit()

# State Management (Durum Yönetimi)
is_video_window_open = False
is_audio_playing = False

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Görüntü işleme hazırlığı
    image = cv2.flip(image, 1)
    h, w, c = image.shape
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process (Yüz Tespiti) - New Tasks API
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
    results = face_landmarker.detect(mp_image)

    pitch = 0  # Varsayılan

    if results.face_landmarks:
        for face_landmarks in results.face_landmarks:
            face_3d = []
            face_2d = []

            for idx, lm in enumerate(face_landmarks):
                if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                    x, y = int(lm.x * w), int(lm.y * h)
                    face_2d.append([x, y])
                    face_3d.append([x, y, lm.z])

            face_2d = np.array(face_2d, dtype=np.float64)
            face_3d = np.array(face_3d, dtype=np.float64)

            focal_length = 1 * w
            cam_matrix = np.array([[focal_length, 0, h / 2], [0, focal_length, w / 2], [0, 0, 1]])
            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)
            rmat, jac = cv2.Rodrigues(rot_vec)

            # --- SENİN DÜZELTTİĞİN KISIM ---
            # OpenCV sürümüne göre doğru unpack yöntemi:
            angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

            pitch = angles[0] * 360

            # Ekrana Debug bilgisi yazalım (Kendi kamera görüntüne)
            cv2.putText(image, f"Pitch: {int(pitch)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # --- LOGIC KISMI (POP-UP PENCERE YÖNETİMİ) ---

    if pitch < DOOM_THRESHOLD:
        # Kafa Aşağıda -> Video Oynat

        ret, video_frame = video_cap.read()

        # Video bittiyse başa sar
        if not ret:
            video_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
            ret, video_frame = video_cap.read()

        if ret:
            # İsteğe bağlı: Video boyutunu küçültmek istersen
            video_frame = cv2.resize(video_frame, (400, 400))

            # POP-UP PENCERE AÇ
            cv2.imshow('RAAAAAGGHH', video_frame)

            # Ses çalmaya başla (sadece ilk açılışta)
            if not is_audio_playing:
                pygame.mixer.music.play()
                is_audio_playing = True

            is_video_window_open = True

            # Ana ekrana uyarı
            cv2.putText(image, "TELEFONU KAPATIYORSUN KARDESIM!", (50, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

    else:
        # Kafa Yukarıda -> Pencereyi Kapat ve Videoyu Resetle
        if is_video_window_open:
            try:
                cv2.destroyWindow('RAAAAAGGHH')
            except:
                pass  # Pencere zaten kapalıysa hata vermesin

            # Sesi durdur
            pygame.mixer.music.stop()
            is_audio_playing = False

            # Videoyu başa sar (Rewind)
            video_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            is_video_window_open = False

    # Ana kamera görüntüsü (Her zaman açık)
    cv2.imshow('DoomScrolling Detector', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
video_cap.release()
cv2.destroyAllWindows()