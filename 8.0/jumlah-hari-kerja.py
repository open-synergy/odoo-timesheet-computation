# Mencari jumlah hari kerja pada satu timesheet


obj_schedule = env["hr.timesheet_attendance_schedule"]


def _cari_hari_kerja():
    criteria = [
        ("sheet_id", "=", sheet.id),
    ]
    return obj_schedule.search_count(criteria)


result = _cari_hari_kerja()
