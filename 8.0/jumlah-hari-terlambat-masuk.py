# Mencari jumlah hari karyawan terlambat masuk
# Terlambat masuk adalah attendance schedule dimana karyawan masuk namun Late Start lebih besar dari 0
# Jumlah jam terlambat max dapat diatur pada konstanta JAM_MAX_TERLAMBAT
# JAM_MAX_TERLAMBAT diexpresikan dalam bilangan float (1 jam 30 meni == 1.5 jam)

# DEFINISI

JAM_MAX_TERLAMBAT = 1.0

# PERHITUNGAN (JANGAN DIUBAH)

obj_schedule = env["hr.timesheet_attendance_schedule"]


def _cari_jumlah_hari():
    criteria = [
        ("sheet_id", "=", sheet.id),
        ("state", "!=", "absence"),
        ("late_start_hour", ">", JAM_MAX_TERLAMBAT)
    ]
    return obj_schedule.search_count(criteria)


result = _cari_jumlah_hari()
