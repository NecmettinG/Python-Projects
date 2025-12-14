import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Qt, QThread
from arayuz3 import Ui_QuanrumUAVArayz  # pyside6-uic ile çevrilen dosya
from telem_code import start_listener, output_queue, get_cargo_data, get_mav_instance, getDbMessage, lock, getHomePosition, threading   # Telemetri verilerini buradan alıyoruz
from mavlink_messages import start_udp_listener, get_log_message  # UDP message listener
import json
from PySide6.QtGui import QPixmap
from telem_threading import VideoThread  # RTSP video akışı için thread
import os
import time
from pymavlink import mavutil
import random
from send_test_messages_active import send_test_messages
import asyncio


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QuanrumUAVArayz()
        self.ui.setupUi(self)

        self.otokilitState = False
        self.otokenetState = False
        self.mobilbaglantiState = False
        self.failsafeState = False
        self.vakumState = False
        self.cargoPrintState = False
        self.dangerZoneState = False
        self.irtifa = 0

        os.chdir("C:/Users/Asus/Desktop")

        self.ui.pushButton_arm.clicked.connect(self.buttonARM)
        self.ui.pushButton_disarm.clicked.connect(self.buttonDISARM)
        self.ui.pushButton_rtl.clicked.connect(self.buttonRTL)
        self.ui.pushButton_emergency.clicked.connect(self.buttonEMERGENCY)

        #self.indicatorOtoKilit()
        #self.indicatorOtoKenet()
        #self.indicatorMobilBaglanti()
        #self.indicatorFailSafe()
        #self.indicatorVakum()

        # Initialize the status message display in textBrowser_2 (bottom-right box)
        self.ui.textBrowser_2.clear()
        self.ui.textBrowser_2.append("=== Status Messages ===")
        self.ui.textBrowser_2.append("UDP Listener started...")

        self.ui.textBrowserPhoto.setPixmap(QPixmap(u"C:/Users/Asus/Desktop/ihatablo.jpg"))
        self.ui.textBrowserPhoto.setScaledContents(True)

        start_listener()  # Telemetri bağlantısını başlat
        start_udp_listener()  # UDP log message listener'ı başlat

        self.timer = QTimer()
        self.timer.timeout.connect(self.dummyGuncelleGui) #Burada randomlu aktif su an!
        self.timer.start(1000)  # Her 1 saniyede bir GUI'yi güncelle

        # Timer for UDP log messages
        self.logTimer = QTimer()
        self.logTimer.timeout.connect(self.update_log_messages)
        self.logTimer.start(100)  # Check for new log messages every 100ms

        self.cargoInfoTimer = QTimer()
        self.cargoInfoTimer.timeout.connect(self.cargoInfoUpdater)
        self.cargoInfoTimer.start(1000)

        self.cargoTimer = QTimer()
        self.cargoTimer.timeout.connect(self.updateCargo)
        self.cargoTimer.start(5000) #120000

        self.dangerZoneTimer = QTimer()
        self.dangerZoneTimer.timeout.connect(self.updateForbiddenZone)
        self.dangerZoneTimer.start(5000)

        self.video_thread = None
        
        # Start the RTSP stream automatically
        self.start_rtsp_stream()
        
        threading.Thread(target=send_test_messages, daemon=True).start()

    def updateForbiddenZone(self):

        if os.path.exists("forbidden_zones.txt") and self.dangerZoneState == False:
            self.dangerZoneState = True
            with open("forbidden_zones.txt", "r") as f:
                dangerZoneData = f.read()
                self.ui.dangerZoneTextBrowser.append(dangerZoneData)
                f.close()
                cursor = self.ui.dangerZoneTextBrowser.textCursor()
                cursor.movePosition(cursor.MoveOperation.End)
                self.ui.dangerZoneTextBrowser.setTextCursor(cursor)

        else:
            if self.dangerZoneState == False:
                self.ui.dangerZoneTextBrowser.setText("yabanci nesne bulunamadi")

            elif self.dangerZoneState == True:
                return
            
    def cargoInfoUpdater(self):

        while True:
            message = getDbMessage()
            if message is None:
                break
            self.ui.textBrowserDB.append(message)
            cursor = self.ui.textBrowserDB.textCursor()
            cursor.movePosition(cursor.MoveOperation.End)
            self.ui.textBrowserDB.setTextCursor(cursor)

            document = self.ui.textBrowserDB.document()
            if document.blockCount() > 1000:
                cursor = self.ui.textBrowserDB.textCursor()
                cursor.movePosition(cursor.MoveOperation.Start)
                cursor.movePosition(cursor.MoveOperation.Down, cursor.MoveMode.KeepAnchor, 
                                  document.blockCount() - 1000)
                cursor.removeSelectedText()


    def update_log_messages(self):
        """Update the status text browser with new UDP log messages"""
        while True:
            message = get_log_message()
            if message is None:
                break
            if "otonom kilitlenme etkin." in message:
                self.ui.indicator_otokilit.setStyleSheet("background-color: green; border: 1px solid black;")
            if "otonom kilitlenme devre disi." in message:
                self.ui.indicator_otokilit.setStyleSheet("background-color: red; border: 1px solid black;")

            if "vakum etkin." in message:
                self.ui.indicator_vakum.setStyleSheet("background-color: green; border: 1px solid black;")
            if "vakum devre disi." in message:
                self.ui.indicator_vakum.setStyleSheet("background-color: red; border: 1px solid black;")

            if "otonom kenetlenme etkin." in message:
                self.ui.indicator_otokenet.setStyleSheet("background-color: green; border: 1px solid black;")
            if "otonom kenetlenme devre disi." in message:
                self.ui.indicator_otokenet.setStyleSheet("background-color: red; border: 1px solid black;")

            if "mobil baglanti etkin." in message:
                self.ui.indicator_mobilbaglanti.setStyleSheet("background-color: green; border: 1px solid black;")
            if "mobil baglanti devre disi." in message:
                self.ui.indicator_mobilbaglanti.setStyleSheet("background-color: red; border: 1px solid black;")

            if "fail safe etkin." in message:
                self.ui.indicator_failsafe.setStyleSheet("background-color: green; border: 1px solid black;")
            if "fail safe devre disi." in message:
                self.ui.indicator_failsafe.setStyleSheet("background-color: red; border: 1px solid black;")


            # Add message to text browser (using textBrowser_2 - bottom-right box)
            self.ui.textBrowser_2.append(message)
            # Auto-scroll to bottom to show latest messages
            cursor = self.ui.textBrowser_2.textCursor()
            cursor.movePosition(cursor.MoveOperation.End)
            self.ui.textBrowser_2.setTextCursor(cursor)
            
            # Optional: Limit the number of lines to prevent memory issues
            # Keep only the last 1000 lines
            document = self.ui.textBrowser_2.document()
            if document.blockCount() > 1000:
                cursor = self.ui.textBrowser_2.textCursor()
                cursor.movePosition(cursor.MoveOperation.Start)
                cursor.movePosition(cursor.MoveOperation.Down, cursor.MoveMode.KeepAnchor, 
                                  document.blockCount() - 1000)
                cursor.removeSelectedText()

    #Buraya txt dosya olusturma olacak
    def updateCargo(self):
        cargoData = get_cargo_data()  # Get cargo data using the function
        if cargoData is not None:
            if len(cargoData) == 0:
                self.ui.textBrowser_5.setText("No cargo data available.")
            
            elif len(cargoData) == 1:
                self.ui.textBrowser_5.setText(f"Cargo Data 1: {cargoData[0].get('coordinate', 'N/A')}")
                if self.cargoPrintState == False:
                    with open("cargo_data.txt", "w") as f:
                        f.write(f"Cargo Data 1: {cargoData[0].get('coordinate', 'N/A')}\n")
                    

            elif len(cargoData) == 2:
                self.ui.textBrowser_5.setText(f"Cargo Data 1: {cargoData[0].get('coordinate', 'N/A')}\nCargo Data 2: {cargoData[1].get('coordinate', 'N/A')}")
                if self.cargoPrintState == False:
                    self.cargoPrintState = True
                    with open("cargo_data.txt", "w") as f:
                        f.write(f"Cargo Data 1: {cargoData[0].get('coordinate', 'N/A')}\n")
                        f.write(f"Cargo Data 2: {cargoData[1].get('coordinate', 'N/A')}\n")
                    
                    
        else:
            self.ui.textBrowser_5.setText("No cargo data available. It is None.")

    def guncelle_gui(self):
        try:
            data = output_queue.get_nowait()
            print(json.dumps(data, indent=4), flush=True)
            self.ui.label_enlem_2.setText(str(data.get("iha_enlem", "N/A")))
            self.ui.label_boylam_2.setText(str(data.get("iha_boylam", "N/A")))
            self.ui.label_pitch_display.setText(str(round(data.get("iha_dikilme", "N/A"), 4)))
            self.ui.label_yaw_display.setText(str(round(data.get("iha_yonelme", "N/A"), 4)))
            self.ui.label_roll_display.setText(str(round(data.get("iha_yatis", "N/A"), 4)))
            self.ui.label_hiz_display.setText(f"{round(float(data.get('iha_hiz', 'N/A')), 4)} m/s")
            #self.ui.label_heading_text.setText(f"{data.get('iha_kuzey_yonelme', 'N/A')}°")
            self.ui.label_batarya_display.setText(f"%{data.get('iha_batarya', 'N/A')}")
            #self.ui.label_voltage.setText(f"{data.get('voltage', 'N/A')} V")
            self.ui.label_modelabel.setText("AUTO" if data.get("iha_mod") == 1 else "MANUAL")
            self.ui.textBrowser_4.setText(str(getHomePosition()))

            gps = data.get("gps_saati", {})
            if gps:
                saat = f"{gps.get('saat', 0):02d}:{gps.get('dakika', 0):02d}:{gps.get('saniye', 0):02d}.{gps.get('milisaniye', 0):03d}"
                self.ui.label_saat_display.setText(saat)

            self.ui.label_altitude_display.setText(f"{round(float(data.get('iha_irtifa', 'N/A')), 4)} m") #Buradaki irtifa!.
            
        except Exception as e:
            print(f"hata: {e}")
            return  # Veri yoksa pas geç
        
        
    def dummyGuncelleGui(self):
        self.ui.label_enlem_2.setText(str(41.1033292))
        self.ui.label_boylam_2.setText(str(28.9776504))
        self.ui.label_pitch_display.setText(str(round(random.uniform(-0.2, 0.2), 4)))
        self.ui.label_yaw_display.setText(str(round(random.uniform(-2.2, 0.999), 4)))
        self.ui.label_roll_display.setText(str(round(random.uniform(-0.99, 0.99), 4)))
        self.ui.label_hiz_display.setText(f"{0} m/s")
        #self.ui.label_heading_text.setText(f"{data.get('iha_kuzey_yonelme', 'N/A')}°")
        self.ui.label_batarya_display.setText(f"%{100}")
        #self.ui.label_voltage.setText(f"{data.get('voltage', 'N/A')} V")
        self.ui.label_modelabel.setText("AUTO")
        self.ui.textBrowser_4.setText("41.1033292, 28.9776504")

        
        saat = f"{00}:{00}:{00}.{000}"
        self.ui.label_saat_display.setText(saat)

        self.ui.label_altitude_display.setText(f"{self.irtifa} m")
        if self.irtifa < 15:
            self.irtifa += 2.5
    
    def start_rtsp_stream(self):
        if self.video_thread is None or not self.video_thread.isRunning():
            rtsp_url = "rtsp://192.168.154.252:8555/mystream"
            self.video_thread = VideoThread(0)
            self.video_thread.frame_ready.connect(self.update_video_frame)
            self.video_thread.connection_status.connect(self.update_video_status)
            self.video_thread.start()
            
    def stop_rtsp_stream(self):
        if self.video_thread and self.video_thread.isRunning():
            self.video_thread.stop()
            self.ui.video_label.setText("Stream Stopped")
            
    def update_video_frame(self, qt_image):
        # Convert QImage to QPixmap and scale to fit the label
        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(
            self.ui.video_label.size(), 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        )
        self.ui.video_label.setPixmap(scaled_pixmap)

    def update_video_status(self, status):
        # Update status when there are connection issues
        if not self.ui.video_label.pixmap():
            self.ui.video_label.setText(f"RTSP Stream: {status}")
        
    def closeEvent(self, event):
        # Clean up timers
        if hasattr(self, 'timer'):
            self.timer.stop()
        if hasattr(self, 'logTimer'):
            self.logTimer.stop()
        if hasattr(self, 'cargoTimer'):
            self.cargoTimer.stop()
        if hasattr(self, 'dangerZoneTimer'):
            self.dangerZoneTimer.stop()
        if hasattr(self, 'cargoInfoTimer'):
            self.cargoInfoTimer.stop()
            
        # Clean up video thread when closing the application
        if self.video_thread and self.video_thread.isRunning():
            print("Stopping video thread...")
            self.video_thread.stop()
            # Wait for thread to finish with timeout
            if not self.video_thread.wait(3000):  # 3 second timeout
                print("Force terminating video thread...")
                self.video_thread.terminate()
                self.video_thread.wait(1000)  # Wait 1 more second
                
        print("Application closing...")
        event.accept()

    def add_status_message(self, message):
        """Add a custom status message to the status terminal"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] STATUS → {message}"
        self.ui.textBrowser_2.append(formatted_message)
        # Auto-scroll to bottom
        cursor = self.ui.textBrowser_2.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.ui.textBrowser_2.setTextCursor(cursor)

    def buttonARM(self):
        print("arm button clicked")
        try:
            mavButton = get_mav_instance()
            with lock:
                
                if mavButton:
                    mavButton.mav.command_long_send(
                        mavButton.target_system,
                        mavButton.target_component,
                        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                        0, 
                        1, 0, 0, 0, 0, 0, 0
                    )
                    self.add_status_message("ARM command executed")
                else:
                    self.add_status_message("MAV instance not available(ARM)")
            

        except Exception as e:
            self.add_status_message(f"Error executing ARM command: {e}")

    def buttonDISARM(self):
        print("disarm button clicked")
        try:
            mavButton = get_mav_instance()
            with lock:
                
                if mavButton:
                    mavButton.mav.command_long_send(
                        mavButton.target_system,
                        mavButton.target_component,
                        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                        0, 
                        0, 0, 0, 0, 0, 0, 0
                    )
                    self.add_status_message("DISARM command executed")
                else:
                    self.add_status_message("MAV instance not available(DISARM)")

        except Exception as e:
            self.add_status_message(f"Error executing DISARM command: {e}")

            

    def buttonRTL(self):
        print("rtl button clicked")
        try:
            mavButton = get_mav_instance()
            with lock:
                
                if mavButton:
                    mavButton.mav.command_long_send(
                        mavButton.target_system,
                        mavButton.target_component,
                        mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,
                        0, 
                        0, 0, 0, 0, 0, 0, 0
                    )
                    self.add_status_message("RTL command executed")
                else:
                    self.add_status_message("MAV instance not available(RTL)")

        except Exception as e:
            self.add_status_message(f"Error executing RTL command: {e}")
    

    def buttonEMERGENCY(self):
        print("emergency button clicked")
        self.add_status_message("EMERGENCY landing command executed")

    def indicatorOtoKilit(self):

        self.otokilitState = True

        self.ui.indicator_otokilit.setStyleSheet("background-color: green; border: 1px solid black;")

    
    def indicatorOtoKenet(self):

        self.otokenetState = True

        self.ui.indicator_otokenet.setStyleSheet("background-color: green; border: 1px solid black;")

    
    def indicatorMobilBaglanti(self):

        self.mobilbaglantiState = True

        self.ui.indicator_mobilbaglanti.setStyleSheet("background-color: green; border: 1px solid black;")


    def indicatorFailSafe(self):

        self.failsafeState = True

        self.ui.indicator_failsafe.setStyleSheet("background-color: green; border: 1px solid black;")


    def indicatorVakum(self):

        self.vakumState = True

        self.ui.indicator_vakum.setStyleSheet("background-color: green; border: 1px solid black;")



        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = MyApp()
    pencere.show()
    sys.exit(app.exec())

