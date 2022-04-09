# Mencari jumlah hari karyawan cuti/izin
# Izin yang dicari dapat didefinisikan dengan LIST_ID_JENIS_CUTI
# LIST_ID_JENIS_CUTI adalah list dari ID jenis cuti yang ingin dicari

# DEFINISI

OVERTIME_TYPE_ID = False


# PERHITUNGAN (JANGAN DIUBAH)

obj_ovt = env["hr.overtime_request"]


def _cari_hari_lembur():
    jumlah_hari = 0.0
    criteria = [
        ("sheet_id", "=", sheet.id),
        ("state", "=", "valid"),
    ]
    if OVERTIME_TYPE_ID:
        criteria.append(("type_id", "=", OVERTIME_TYPE_ID))
    else:
        criteria.append(("type_id", "=", False))
    for ovt in obj_ovt.search(criteria):
        jumalh_hari += 1

    return jumalh_hari

result = _cari_hari_lembur()
