import frappe


def execute():
    """
    Add device_id field (Data) where needed:

    - Biometric Attendance Log           -> device_id (Data)
    - Biometric Attendance Punch Table   -> device_id (Data)
    - Employee Checkin                   -> device_id (Data)  [only if not already present]

    Safe to run multiple times (checks if field / column already exists).
    """

    targets = [
        ("Biometric Attendance Log", "event_date"),
        ("Biometric Attendance Punch Table", "punch_type"),
        ("Employee Checkin", "log_type"),
    ]

    for dt, insert_after in targets:
        # If the column already exists (standard or custom), skip
        if frappe.db.has_column(dt, "device_id"):
            continue

        # If a Custom Field already exists (but column somehow missing), also skip
        if frappe.db.exists(
            "Custom Field",
            {"dt": dt, "fieldname": "device_id"},
        ):
            continue

        cf = frappe.get_doc(
            {
                "doctype": "Custom Field",
                "dt": dt,
                "fieldname": "device_id",
                "label": "Device ID",
                "fieldtype": "Data",
                "insert_after": insert_after,
            }
        )
        cf.insert(ignore_permissions=True)
        frappe.clear_cache(doctype=dt)
