# Mencari jumlah hari karyawan cuti/izin
# Izin yang dicari dapat didefinisikan dengan LIST_ID_JENIS_CUTI
# LIST_ID_JENIS_CUTI adalah list dari ID jenis cuti yang ingin dicari


# PERHITUNGAN (JANGAN DIUBAH)

obj_ovt = env["hr.overtime_request"]


def _cari_jumlah_jam():
    jumlah_jam = 0.0
    criteria = [
        ("sheet_id", "=", sheet.id),
        ("state", "=", "valid"),
    ]
    for ovt in obj_ovt.search(criteria):
        jumlah_jam += ovt.real_overtime_hour

    return jumlah_jam

result = _cari_jumlah_jam()
