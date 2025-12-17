import frappe


def execute():
    """
    Add required fields on Biometric Attendance Punch Table for Employee Checkin sync:
    - synced_to_employee_checkin (Check)
    - employee_checkin (Link to Employee Checkin)  [optional but useful]

    This patch is safe to run multiple times: it checks if fields already exist.
    """

    # 1) Synced to Employee Checkin (Check)
    if not frappe.db.exists(
        "Custom Field",
        {"dt": "Biometric Attendance Punch Table", "fieldname": "synced_to_employee_checkin"},
    ):
        cf = frappe.get_doc(
            {
                "doctype": "Custom Field",
                "dt": "Biometric Attendance Punch Table",
                "fieldname": "synced_to_employee_checkin",
                "label": "Synced to Employee Checkin",
                "fieldtype": "Check",
                "default": "0",
                # place after punch_type or any existing field
                "insert_after": "punch_type",
            }
        )
        cf.insert(ignore_permissions=True)
        frappe.clear_cache(doctype="Biometric Attendance Punch Table")

    # 2) Employee Checkin (Link)  - optional, only used if present
    if not frappe.db.exists(
        "Custom Field",
        {"dt": "Biometric Attendance Punch Table", "fieldname": "employee_checkin"},
    ):
        cf = frappe.get_doc(
            {
                "doctype": "Custom Field",
                "dt": "Biometric Attendance Punch Table",
                "fieldname": "employee_checkin",
                "label": "Employee Checkin",
                "fieldtype": "Link",
                "options": "Employee Checkin",
                "insert_after": "synced_to_employee_checkin",
            }
        )
        cf.insert(ignore_permissions=True)
        frappe.clear_cache(doctype="Biometric Attendance Punch Table")

