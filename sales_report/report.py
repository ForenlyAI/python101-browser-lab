import csv
from pathlib import Path

AYLAR = {"ocak": "Ocak", "subat": "Şubat"}
toplam = 0
for dosya in sorted(Path("data").glob("*.csv"), key=lambda f: list(AYLAR).index(f.stem)):
    with dosya.open(encoding="utf-8") as f:
        ay_toplami = sum(float(satir["tutar"]) for satir in csv.DictReader(f))
    print(f"{AYLAR[dosya.stem]}: {ay_toplami}")
    toplam += ay_toplami
print(f"Toplam: {toplam}")
