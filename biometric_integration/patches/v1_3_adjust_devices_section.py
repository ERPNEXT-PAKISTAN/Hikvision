import frappe


def execute():
    """
    Adjust layout of 'Devices' child table on Biometric Integration Settings:

    - Add a Section Break after end_date_and_time
    - Move the Devices table field under that section
    - Set Devices table to full width (columns = 0)

    Does not change any logic, only the form layout.
    Safe to run multiple times.
    """

    dt = "Biometric Integration Settings"

    # 1) Ensure Section Break exists after end_date_and_time
    if not frappe.db.exists("Custom Field", {"dt": dt, "fieldname": "devices_section"}):
        sb = frappe.get_doc(
            {
                "doctype": "Custom Field",
                "dt": dt,
                "fieldname": "devices_section",
                "label": "Devices",
                "fieldtype": "Section Break",
                "insert_after": "end_date_and_time",
                # full-width section
                "columns": 0,
            }
        )
        sb.insert(ignore_permissions=True)

    # 2) Find the Devices child table field (Table → Biometric Device)
    table_fields = frappe.get_all(
        "Custom Field",
        filters={
            "dt": dt,
            "fieldtype": "Table",
            "options": "Biometric Device",
        },
        fields=["name"],
        limit=1,
    )

    if not table_fields:
        # Nothing to adjust (maybe field not created yet)
        frappe.clear_cache(doctype=dt)
        return

    devices_cf = frappe.get_doc("Custom Field", table_fields[0].name)

    # Move it under the new section and make it full-width
    devices_cf.insert_after = "devices_section"
    devices_cf.columns = 0
    devices_cf.save(ignore_permissions=True)

    frappe.clear_cache(doctype=dt)
