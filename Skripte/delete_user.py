import requests
import sys

def delete_user(sid, username):
    """
    Löscht einen bestehenden Benutzer.
    
    :param sid: Gültige Session-ID (SID)
    :param username: Benutzername des zu löschenden Nutzers
    """
    # URL für das Löschen eines Benutzers
    url = f"http://192.168.178.32:8080/cgi-bin/priv/privRequest.cgi"
    
    # Parameter der Anfrage
    params = {
        "sid": sid,
        "subfunc": "user",
        "apply": "1",
        "del_cnt": "1",  # Anzahl der zu löschenden Benutzer
        "delete_userhome": "false",  # Benutzerordner behalten
        "user_list": username  # Benutzername des zu löschenden Nutzers
    }
    
    try:
        # Senden der Anfrage
        response = requests.get(url, params=params)
        
        # Status auswerten
        if response.status_code == 200:
            print("[*] Benutzer erfolgreich gelöscht!")
            print("Antwort des Servers:")
            print(response.text)
        else:
            print(f"[!] Fehler: Server antwortete mit Status-Code {response.status_code}")
            print("Antwort des Servers:")
            print(response.text)
    except Exception as e:
        print(f"[!] Fehler beim Senden der Anfrage: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Fehler: SID und Benutzername müssen angegeben werden.")
        print("Verwendung: python3 delete_user.py <SID> <Benutzername>")
        sys.exit(1)
    
    # SID und Benutzername aus den Argumenten übernehmen
    sid = sys.argv[1]
    username = sys.argv[2]
    
    # Benutzer löschen
    delete_user(sid, username)
