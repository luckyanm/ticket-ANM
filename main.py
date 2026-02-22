import qrcode
from datetime import datetime

# --- I TUOI DATI AGGIORNATI (22 Feb) ---
static_lines = [
    "7_GIORNI",
    "ANM",
    "2026-02-22T17:42",
    "2026-02-28T23:59",
    "E3GGJ2BYZE",
    "15",
    "2",
    "4",
    "050e9ecf31070627ed6a06783002899a3059e5749040e7f77aeb18f80c"
]

# --- CALCOLO ORARIO ATTUALE ---
now = datetime.now()
timestamp_line = now.strftime("%Y-%m-%dT%H:%M:%S") + "+01:00"

# Unisce i dati
full_data = "\n".join(static_lines) + "\n" + timestamp_line

print(f"Generato QR per le ore: {timestamp_line}")

# --- CREAZIONE QR (Piccolo e compatto) ---
qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,  # Dimensione ridotta per vederlo bene
    border=2,
)

qr.add_data(full_data)
qr.make(fit=True)

# Salva l'immagine
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
