from database import engine
import pandas as pd

data = {
    "lokasi": ["Lab A", "Lab B", "Lab C", "Lab A", "Lab B"],
    "suhu": [26.5, 27.1, 25.8, 26.9, 27.3],
    "kelembaban": [60, 62, 58, 61, 63],
    "waktu": ["2025-01-01"] * 5
}

df = pd.DataFrame(data)
df.to_sql("sensor_log", engine, if_exists="replace", index=False)

print("Database & tabel berhasil dibuat")
