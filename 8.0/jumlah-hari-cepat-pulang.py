# Mencari jumlah hari karyawan cepat pulang
# Cepat pulang adalah attendance schedule dimana karyawan masuk namun Finish Early lebih besar dari 0
# Jumlah jam cepat pulang max dapat diatur pada konstanta JAM_MAX_CEPAT_PULANG
# JAM_MAX_CEPAT_PULANG diexpresikan dalam bilangan float (1 jam 30 meni == 1.5 jam)

# DEFINISI

JAM_MAX_CEPAT_PULANG = 0.0

# PERHITUNGAN (JANGAN DIUBAH)

obj_schedule = env["hr.timesheet_attendance_schedule"]


def _cari_jumlah_hari():
    criteria = [
        ("sheet_id", "=", sheet.id),
        ("state", "!=", "absence"),
        ("late_start_hour", ">", JAM_MAX_CEPAT_PULANG)
    ]
    return obj_schedule.search_count(criteria)


result = _cari_jumlah_hari()
