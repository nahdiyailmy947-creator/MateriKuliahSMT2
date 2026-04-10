def pipeline_manajemen_log(logs, batch_baru, limit):
    return sorted(logs + batch_baru)[-limit:]


# Input
logs = ["WARN", "INFO"]
batch_baru = ["ERROR", "DEBUG"]
limit = 2

# Proses
hasil = pipeline_manajemen_log(logs, batch_baru, limit)

# Output
print("Hasil akhir:", hasil)