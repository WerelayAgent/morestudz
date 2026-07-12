import requests, re, os

BASE_URL = "https://morebrix.com"
DIR = r"c:\Tools\project crypto\morestudz\public\static\images"

r = requests.get(BASE_URL + "/")
html = r.text

# Find all image paths in the original HTML
images = set(re.findall(r'/(?:static|assets|media)/[a-zA-Z0-9_\.-]+\.(?:png|jpg|jpeg|svg|webp|gif)', html))

for path in images:
    if 'brix' in path.lower() or 'brick' in path.lower():
        url = BASE_URL + path
        print(f"Downloading {url}")
        res = requests.get(url)
        if res.status_code == 200:
            # Rebrand filename
            new_path = path.replace('brix', 'studz').replace('Brix', 'Studz').replace('brick', 'stud').replace('Brick', 'Stud')
            filename = os.path.basename(new_path)
            full_path = os.path.join(DIR, filename)
            with open(full_path, 'wb') as f:
                f.write(res.content)
            print(f"Saved to {filename}")

