import requests
import sys

def change_admin_password(sid, old_password, new_password):
    """
    Ändert das Passwort des Administrators.
    
    :param sid: Gültige Session-ID (SID)
    :param old_password: Aktuelles Passwort des Admin-Benutzers
    :param new_password: Neues Passwort für den Admin-Benutzer
    """
    # URL für das Ändern des Admin-Passworts
    url = f"http://192.168.178.32:8080/cgi-bin/priv/privWizard.cgi"
    
    # Parameter der Anfrage
    params = {
        "sid": sid,
        "wiz_func": "user_password_edit",
        "action": "user_password_edit",
        "username": "admin",
        "old_password": old_password,
        "password": new_password,
        "need_check": "yes"
    }
    
    try:
        # Senden der Anfrage
        response = requests.get(url, params=params)
        
        # Status auswerten
        if response.status_code == 200:
            print("[*] Admin-Passwort erfolgreich geändert!")
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
        print("Fehler: SID, altes Passwort und neues Passwort müssen angegeben werden.")
        print("Verwendung: python3 change_admin_password.py <SID> <Altes Passwort> <Neues Passwort>")
        sys.exit(1)
    
    # SID, altes Passwort und neues Passwort aus den Argumenten übernehmen
    sid = sys.argv[1]
    old_password = sys.argv[2]
    new_password = sys.argv[3]
    
    # Admin-Passwort ändern
    change_admin_password(sid, old_password, new_password)
