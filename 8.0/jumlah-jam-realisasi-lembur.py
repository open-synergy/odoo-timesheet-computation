# Mencari jumlah hari karyawan cuti/izin
# Izin yang dicari dapat didefinisikan dengan LIST_ID_JENIS_CUTI
# LIST_ID_JENIS_CUTI adalah list dari ID jenis cuti yang ingin dicari

# DEFINISI

USE_MAX_HOUR_PER_OVERTIME = False
MAX_HOUR_PER_OVERTIME = 0.0


# PERHITUNGAN (JANGAN DIUBAH)

obj_ovt = env["hr.overtime_request"]


def _cari_jumlah_jam():
    jumlah_jam = 0.0
    criteria = [
        ("sheet_id", "=", sheet.id),
        ("state", "=", "valid"),
    ]
    for ovt in obj_ovt.search(criteria):
        if NOT USE_MAX_HOUR_PER_OVERTIME:
            jumlah_jam += ovt.real_overtime_hour
        else:
            if ovt.real_overtime_hour > MAX_HOUR_PER_OVERTIME:
                jumlah_jam += MAX_HOUR_PER_OVERTIME

    return jumlah_jam

result = _cari_jumlah_jam()
