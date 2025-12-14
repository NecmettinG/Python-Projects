import sys
import cv2
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QThread, Qt, QTimer, Signal
from PySide6.QtGui import QImage

class VideoThread(QThread):
    frame_ready = Signal(QImage)
    connection_status = Signal(str)  # Add connection status signal
    
    def __init__(self, rtsp_url):
        super().__init__()
        self.rtsp_url = rtsp_url
        self.running = False
        
    def run(self):
        self.running = True
        self.connection_status.emit("Bağlanıyor...")
        cap = cv2.VideoCapture(self.rtsp_url)
        
        # Set buffer size to reduce latency
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        cap.set(cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, 3000)  # 3 second timeout
        cap.set(cv2.CAP_PROP_READ_TIMEOUT_MSEC, 3000)   # 3 second read timeout

        if not cap.isOpened():
            self.connection_status.emit("Bağlantı Hatası!")
            return
            
        self.connection_status.emit("Bağlandı")
        
        while self.running and cap.isOpened():
            ret, frame = cap.read()
            if ret and self.running:
                try:
                    # Convert BGR to RGB
                    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgb_frame.shape
                    bytes_per_line = ch * w
                
                    # Create QImage
                    qt_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                    
                    if self.running:  # Check again before emitting
                        self.frame_ready.emit(qt_image)

                except Exception as e:
                    print(f"Frame processing error: {e}")
                    break

            elif not ret:
                self.connection_status.emit("Stream Kesildi")
                break
                
        try:
            if cap.isOpened():
                cap.release()
        except:
            pass
            
        self.connection_status.emit("Bağlantı Kapandı")
        print("Video thread finished")
        
    def stop(self):
        print("Stopping video thread...")
        self.running = False
