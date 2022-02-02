# Mencari jumlah hari karyawan melakukan absensi tidak lengkap
# Absensi tidak lengkap terjadi dimana karyawan hanya sign in atau sign out


obj_schedule = env["hr.timesheet_attendance_schedule"]


def _cari_hari():
    criteria = [
        ("sheet_id", "=", sheet.id),
        ("state", "=", "present")
    ]
    return obj_schedule.search_count(criteria)


result = _cari_hari()
