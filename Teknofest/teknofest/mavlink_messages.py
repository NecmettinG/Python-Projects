import socket
import threading
import base64
from datetime import datetime
import queue

# === Ayarlar ===
UDP_PORT = 5005
#TCP_PORT = 5050
#IMAGE_PATH = "received_tcp_image.png"

# Queue for GUI communication
log_message_queue = queue.Queue()

# === UDP: Log Mesajları Dinle ===
def udp_listener():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", UDP_PORT))
    print(f"🎧 UDP dinleniyor: {UDP_PORT}")

    while True:
        data, _ = sock.recvfrom(2048)
        if data.startswith(b"LOG:"):
            msg = data[4:].decode(errors="ignore")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_message = f"[{timestamp}] LOG → {msg}"
            print(formatted_message)
            # Put message in queue for GUI to read
            log_message_queue.put(formatted_message)

# === TCP: Görsel Alıcı ===
#def tcp_image_receiver():
#    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    server.bind(("0.0.0.0", TCP_PORT))
#    server.listen(1)
#    print(f"📡 TCP dinleniyor: {TCP_PORT}")

#    while True:
#        conn, addr = server.accept()
#        print(f"📥 Görsel bağlantısı: {addr}")
#        with open(IMAGE_PATH, 'wb') as f:
#            while True:
#                chunk = conn.recv(1024)
#                if not chunk:
#                    break
#                f.write(chunk)
#        print(f"✅ Görsel kaydedildi: {IMAGE_PATH}")

# === Thread'leri Başlat ===
def start_udp_listener():
    """Start UDP listener in a daemon thread"""
    udp_thread = threading.Thread(target=udp_listener, daemon=True)
    udp_thread.start()
    return udp_thread

def get_log_message():
    """Get log message from queue (non-blocking)"""
    try:
        return log_message_queue.get_nowait()
    except queue.Empty:
        return None

if __name__ == "__main__":
    start_udp_listener()
    #threading.Thread(target=tcp_image_receiver, daemon=True).start()

    try:
        while True:
            pass  # Ana thread açık kalmalı
    except KeyboardInterrupt:
        print("\n⛔ Kapatılıyor.")