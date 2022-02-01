# Mencari jumlah hari karyawan cuti/izin
# Izin yang dicari dapat didefinisikan dengan LIST_ID_JENIS_CUTI
# LIST_ID_JENIS_CUTI adalah list dari ID jenis cuti yang ingin dicari

# DEFINISI

LIST_ID_JENIS_CUTI = []

# PERHITUNGAN (JANGAN DIUBAH)

obj_holiday = env["hr.holidays"]


def _cari_jumlah_hari():
    jumlah_hari_cuti = 0.0
    criteria = [
        ("sheet_id", "=", sheet.id),
        ("state", "=", "validate"),
        ("type", "=", "remove"),
        ("holiday_status_id.id", "in", LIST_ID_JENIS_CUTI),

    ]
    for leave in obj_holiday.search(criteria):
        jumlah_hari_cuti += leave.number_of_days_temp

    return jumlah_hari_cuti

result = _cari_jumlah_hari()
