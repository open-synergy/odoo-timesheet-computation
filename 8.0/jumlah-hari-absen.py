# Mencari jumlah hari karyawan tidak melakukan absensi


obj_schedule = env["hr.timesheet_attendance_schedule"]


def _cari_hari_absen():
    criteria = [
        ("sheet_id", "=", sheet.id),
        ("state", "=", "absence")
    ]
    return obj_schedule.search_count(criteria)


result = _cari_hari_absen()
