import socket
import time

def send_test_messages():
    """Send test UDP messages to verify the listener is working"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    messages = [
        
        #"vakum etkin.", 
        #"otonom kenetlenme etkin.",
        "mobil baglanti etkin.",
        "ARM edildi.",
        #"fail safe etkin.",
        "Şu anki irtifa: 8.73 m",
        "Hedef irtifaya ulaşıldı.",
        "Rota başarıyla belirlendi.",
        "Anlık irtifa: 15.00 m",
        "Drone zaten yeterli irtifada.",
        "2 adet waypoint yüklendi.",
        "Görev yükleniyor...",
        "Görev yüklendi!",
        "Görev başlatılıyor...",
        "otonom kilitlenme etkin.",

    ]
    
    print("Sending test UDP messages...")
    
    for i, message in enumerate(messages):
        full_message = f"LOG:{message}"
        sock.sendto(full_message.encode(), ("127.0.0.1", 5005))
        print(f"Sent {i+1}/{len(messages)}: {message}")
        time.sleep(2)  # Wait 2 seconds between messages
    
    sock.close()
    print("All test messages sent successfully!")

if __name__ == "__main__":
    send_test_messages()
