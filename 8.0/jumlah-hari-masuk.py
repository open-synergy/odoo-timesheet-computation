# Mencari jumlah hari karyawan melakukan absensi tidak lengkap
# Absensi tidak lengkap terjadi dimana karyawan hanya sign in atau sign out

# DEFINISI

USE_MIN_WORK_HOUR = False
MIN_WORK_HOUR = 0.0


# PERHITUNGAN (JANGAN DIUBAH)

obj_schedule = env["hr.timesheet_attendance_schedule"]


def _cari_hari():
    criteria = [
        ("sheet_id", "=", sheet.id),
        ("state", "=", "present")
    ]
    if USE_MIN_WORK_HOUR:
        criteria += [
        ("real_work_hour", ">=", MIN_WORK_HOUR),
        ]
    return obj_schedule.search_count(criteria)


result = _cari_hari()
