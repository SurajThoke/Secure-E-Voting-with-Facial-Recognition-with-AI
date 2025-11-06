# download_static_files.py
import os
import requests

files = [
    ("https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css", "static/lib/animate/animate.min.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css", "static/lib/owlcarousel/assets/owl.carousel.min.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/css/lightbox.min.css", "static/lib/lightbox/css/lightbox.min.css"),
    ("https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js", "static/lib/easing/easing.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js", "static/lib/owlcarousel/owl.carousel.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/jquery.isotope/3.0.6/isotope.pkgd.min.js", "static/lib/isotope/isotope.pkgd.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.4/js/lightbox.min.js", "static/lib/lightbox/js/lightbox.min.js"),
]

for url, path in files:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(f"Downloading {url} to {path}...")
    r = requests.get(url)
    with open(path, "wb") as f:
        f.write(r.content)
print("All files downloaded.")