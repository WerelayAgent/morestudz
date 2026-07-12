import os
import re
import requests

html = open('public/index.html', 'r', encoding='utf-8').read()
img_tags = re.findall(r'<img[^>]*src="([^"]+)"[^>]*>', html)

for img in img_tags:
    print(img)
    if 'stud' in img.lower() and not os.path.exists(f"public{img}"):
        print(f"Missing: {img}")
        # The original was likely 'brix' or 'brick'
        orig = img.replace('studz', 'brix').replace('Studz', 'Brix').replace('stud', 'brick').replace('Stud', 'Brick')
        url = f"https://morebrix.com{orig}"
        print(f"Trying to fetch: {url}")
        res = requests.get(url)
        if res.status_code == 200:
            with open(f"public{img}", 'wb') as f:
                f.write(res.content)
            print("Downloaded!")
