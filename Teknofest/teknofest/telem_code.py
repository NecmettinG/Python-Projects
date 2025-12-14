import threading
import queue
from pymavlink import mavutil
import json
import time
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2 import sql



# Semaphore ve Lock
lock = threading.Lock()
semaphore = threading.Semaphore(3)

# Kuyruklar
position_queue = queue.Queue()
attitude_queue = queue.Queue()
vfr_queue = queue.Queue()
battery_queue = queue.Queue()
mode_queue = queue.Queue()
gps_queue = queue.Queue()
output_queue = queue.Queue()
#cargo_queue = queue.Queue()
cargoMessage_queue = queue.Queue()


# Global değişkenler
lat = None
long = None
att = None
yaw = None
pitch = None
roll = None
heading = None
ground_speed = None
battery = None
mav_mode_auto = None
gps_saati = None
total_voltage = None
cargoData = None
mav_instance = None
tableExists = False
HomePositionVar = None


def get_cargo_data():
    """Function to safely get cargo data with lock"""
    with lock:
        return cargoData
    
def get_mav_instance():
    with lock:
        return mav_instance
    
def getDbMessage():
    try:
        return cargoMessage_queue.get_nowait()
    except queue.Empty:
        return None
    
def getHomePosition():
    with lock:
        return HomePositionVar

app = FastAPI()



# Bağlantıyı tek bir thread üzerinden sağla
def mavlink_listener():
    global mav_instance
    global HomePositionVar
    HomePositionState = 0
    try:
        mav = mavutil.mavlink_connection('COM6', baud=57600, autoreconnect=True, timeout=10)
        with lock:
            mav_instance = mav
        
        mav.wait_heartbeat()
        print("Bağlantı kuruldu")

        # Verilerin işlenmesi için thread'leri başlat
        threading.Thread(target=process_global_position, daemon=True).start()
        threading.Thread(target=process_attitude, daemon=True).start()
        threading.Thread(target=process_vfr_hud, daemon=True).start()
        threading.Thread(target=process_battery_status, daemon=True).start()
        threading.Thread(target=process_mode_control, daemon=True).start()
        threading.Thread(target=process_gps_time, daemon=True).start()
        threading.Thread(target=yazdirma, daemon=True).start()

        while True:
            try:
                # Bağlantıdan gelen veriyi al
                msg = mav.recv_match(blocking=True, timeout=5)
                if msg is None:
                    print("Uyarı: 5 saniyedir veri alınamıyor")
                    continue

                msg_type = msg.get_type()

                if msg_type == 'GLOBAL_POSITION_INT':
                    position_queue.put(msg)
                elif msg_type == 'ATTITUDE':
                    attitude_queue.put(msg)
                elif msg_type == 'VFR_HUD':
                    vfr_queue.put(msg)
                elif msg_type == 'BATTERY_STATUS':
                    battery_queue.put(msg)
                elif msg_type == 'HEARTBEAT':
                    mode_queue.put(msg)
                elif msg_type == 'GPS_RAW_INT':
                    gps_queue.put(msg)
                elif msg_type == 'HOME_POSITION' and HomePositionState < 5:
                    print(f"home position koordinat: {msg}")
                    with lock:
                        HomePositionVar = msg
                    HomePositionState+=1

            except Exception as e:
                print(f"Veri alırken hata: {e}")

    except Exception as e:
        print(f"Hata: {e}")

# İşlem fonksiyonları
def process_global_position():
    global lat, long, att
    while True:
        msg = position_queue.get()
        with semaphore:
            with lock:
                lat = msg.lat / 1e7
                long = msg.lon / 1e8
                att = msg.relative_alt / 1000

def process_attitude():
    global yaw, pitch, roll
    while True:
        msg = attitude_queue.get()
        with semaphore:
            with lock:
                yaw = msg.yaw
                pitch = msg.pitch
                roll = msg.roll

def process_vfr_hud():
    global heading, ground_speed
    while True:
        msg = vfr_queue.get()
        with semaphore:
            with lock:
                heading = msg.heading
                ground_speed = msg.groundspeed



def process_battery_status():
    global battery,total_voltage
    while True:
        msg = battery_queue.get()
        if msg.get_type() == 'BATTERY_STATUS':
            total_voltage_mv = msg.voltages[0]  # milivolt cinsinden
            total_voltage = total_voltage_mv / 1000.0  # volt cinsine çevir

# 3S LiPo batarya voltajına göre yüzde hesapla
            if total_voltage >= 12.60:
                battery = 100
            elif total_voltage >= 12.45:
                battery = 95
            elif total_voltage >= 12.30:
                battery = 90
            elif total_voltage >= 12.15:
                battery = 85
            elif total_voltage >= 12.00:
                battery = 80
            elif total_voltage >= 11.85:
                battery = 75
            elif total_voltage >= 11.70:
                battery = 70
            elif total_voltage >= 11.55:
                battery = 65
            elif total_voltage >= 11.40:
                battery = 60
            elif total_voltage >= 11.25:
                battery = 50
            elif total_voltage >= 11.10:
                battery = 40
            elif total_voltage >= 10.95:
                battery = 30
            elif total_voltage >= 10.80:
                battery = 20
            elif total_voltage >= 10.60:
                battery = 10
            elif total_voltage >= 10.40:
                battery = 5
            else:
                battery = 0




def process_mode_control():
    global mav_mode_auto
    while True:
        msg = mode_queue.get()
        with semaphore:
            with lock:
                base_mode = msg.base_mode
                if base_mode & mavutil.mavlink.MAV_MODE_FLAG_AUTO_ENABLED:
                # Auto mode aktifse 1 yazdır
                    mav_mode_auto = 1
                else:
                    mav_mode_auto = 0

def process_gps_time():
    global gps_saati
    while True:
        msg = gps_queue.get()
        with semaphore:
            with lock:
                gps_time_usec = msg.time_usec
                gps_time = datetime.utcfromtimestamp(gps_time_usec // 1_000_000)
                milisaniye = (gps_time_usec % 1_000_000) // 1_000
                gps_saati = {
                    "saat": gps_time.hour,
                    "dakika": gps_time.minute,
                    "saniye": gps_time.second,
                    "milisaniye": milisaniye
                }


def yazdirma():
    
    while True:
        with lock:
            iha_data = {
                "iha_enlem": lat,
                "iha_boylam": long,
                "iha_irtifa": att,
                "iha_dikilme": pitch,
                "iha_yonelme": yaw,
                "iha_yatis": roll,
                "iha_hiz": ground_speed,
                "iha_kuzey_yonelme": heading,
                "iha_batarya": battery,
                "voltage" : total_voltage,
                "iha_mod": mav_mode_auto,
                "gps_saati": gps_saati
            }

        output_queue.put(iha_data)

        time.sleep(1)

def connectCargoDb():
    global cargoData
    global tableExists
    tableExistsLoopController = True
#Buraya telem_code2'nin MyApp classindan instance olusturulup gerektiginde updateCargo cagrilabilir.
#updateCargoyu zamanlamaya sokmak yerine, veritabanindan veri cekildiginde cagrilabilir.  
    try:
        print("Attempting to connect to PostgreSQL database...")
        cargoMessage_queue.put("Attempting to connect to PostgreSQL database...")
        db_connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="vdmuy3rg.",
        host="localhost",
        port="5432"
        )
        print("PostgreSQL connection successful!")
        cargoMessage_queue.put("PostgreSQL connection successful!")

        while True:
            if tableExists == True and tableExistsLoopController == True:
                cargoMessage_queue.put("SQL table is created successfully.")
                tableExistsLoopController = False
            
            try:
            
                cursor = db_connection.cursor()
                cursor.execute("SELECT * FROM cargo")
                tableExists = True
                rows = cursor.fetchall()
                column_names = [description[0] for description in cursor.description]
                result = [dict(zip(column_names, row)) for row in rows]
                cursor.close()
                
                # Use lock when updating global variable
                with lock:
                    cargoData = result
                    
                print("Cargo Data updated:", cargoData, flush=True)
                time.sleep(5)

            except psycopg2.Error as e:
                print(f"Database error: {e}")
                cargoMessage_queue.put("SQL table for cargo doesn't exist")
                # Rollback the transaction to clear the error state
                db_connection.rollback()
                # Use lock when updating global variable to None in case of error
                with lock:
                    cargoData = None
                print("Transaction rolled back, retrying in 5 seconds...")
                time.sleep(5)
            except Exception as e:
                print(f"Veri çekilirken hata: {e}")
                cargoMessage_queue.put(f"Veri çekilirken hata: {e}")
                # Use lock when updating global variable to None in case of error
                with lock:
                    cargoData = None
                time.sleep(5)


    except Exception as e:
        print(f"Veritabanı bağlantısı kurulamadı: {e}")
        cargoMessage_queue.put(f"Veritabanı bağlantısı kurulamadı: {e}")
        # Set cargoData to None if connection fails
        with lock:
            cargoData = None



# Ana program fonksiyonu
def start_listener():
    # Start database connection first
    print("Starting database connection thread...")
    db_thread = threading.Thread(target=connectCargoDb, daemon=True)
    db_thread.start()
    
    # Then start MAVLink listener
    print("Starting MAVLink listener thread...")
    listener_thread = threading.Thread(target=mavlink_listener, daemon=True)
    listener_thread.start()

if __name__ == "__main__":
    start_listener()
    while True:
        try:
            data = output_queue.get(timeout=2)
            print(json.dumps(data, indent=4), flush=True)
        except queue.Empty:
            print("Veri bekleniyor...", flush=True)
