import json

import frappe


WORKSPACE_NAME = "Biometric Integration"


def _workspace_content():
    return json.dumps(
        [
            {
                "id": "biometric-header-1",
                "type": "header",
                "data": {
                    "text": "<span class=\"h4\"><b>Biometric Integration</b></span>",
                    "col": 12,
                },
            },
            {
                "id": "biometric-shortcut-settings",
                "type": "shortcut",
                "data": {"shortcut_name": "Biometric Settings", "col": 3},
            },
            {
                "id": "biometric-shortcut-log",
                "type": "shortcut",
                "data": {"shortcut_name": "Attendance Logs", "col": 3},
            },
            {
                "id": "biometric-shortcut-manual",
                "type": "shortcut",
                "data": {"shortcut_name": "Manual Punch", "col": 3},
            },
            {
                "id": "biometric-shortcut-checkin",
                "type": "shortcut",
                "data": {"shortcut_name": "Employee Checkin", "col": 3},
            },
            {"id": "biometric-spacer-1", "type": "spacer", "data": {"col": 12}},
            {
                "id": "biometric-header-2",
                "type": "header",
                "data": {
                    "text": "<span class=\"h4\"><b>Reports and Setup</b></span>",
                    "col": 12,
                },
            },
            {
                "id": "biometric-card-masters",
                "type": "card",
                "data": {"card_name": "Masters", "col": 4},
            },
            {
                "id": "biometric-card-reports",
                "type": "card",
                "data": {"card_name": "Reports", "col": 4},
            },
            {
                "id": "biometric-card-tools",
                "type": "card",
                "data": {"card_name": "Tools", "col": 4},
            },
        ]
    )


def create_or_update_biometric_workspace():
    """Create/update app Workspace so it can be exported as fixture."""
    if frappe.db.exists("Workspace", WORKSPACE_NAME):
        ws = frappe.get_doc("Workspace", WORKSPACE_NAME)
    else:
        ws = frappe.new_doc("Workspace")
        ws.name = WORKSPACE_NAME

    ws.label = WORKSPACE_NAME
    ws.title = WORKSPACE_NAME
    ws.icon = "setting-gear"
    ws.module = "Biometric Integration"
    ws.public = 1
    ws.is_hidden = 0
    ws.content = _workspace_content()

    ws.set("shortcuts", [])
    ws.append(
        "shortcuts",
        {
            "type": "DocType",
            "label": "Biometric Settings",
            "link_to": "Biometric Integration Settings",
            "doc_view": "List",
            "color": "Blue",
        },
    )
    ws.append(
        "shortcuts",
        {
            "type": "DocType",
            "label": "Attendance Logs",
            "link_to": "Biometric Attendance Log",
            "doc_view": "List",
            "color": "Green",
        },
    )
    ws.append(
        "shortcuts",
        {
            "type": "DocType",
            "label": "Manual Punch",
            "link_to": "Biometric Manual Punch",
            "doc_view": "List",
            "color": "Orange",
        },
    )
    ws.append(
        "shortcuts",
        {
            "type": "DocType",
            "label": "Employee Checkin",
            "link_to": "Employee Checkin",
            "doc_view": "List",
            "color": "Grey",
        },
    )

    ws.set("links", [])

    ws.append("links", {"type": "Card Break", "label": "Masters"})
    ws.append(
        "links",
        {
            "type": "Link",
            "label": "Biometric Integration Settings",
            "link_type": "DocType",
            "link_to": "Biometric Integration Settings",
        },
    )
    ws.append(
        "links",
        {
            "type": "Link",
            "label": "Biometric Attendance Log",
            "link_type": "DocType",
            "link_to": "Biometric Attendance Log",
        },
    )
    ws.append(
        "links",
        {
            "type": "Link",
            "label": "Biometric Manual Punch",
            "link_type": "DocType",
            "link_to": "Biometric Manual Punch",
        },
    )
    ws.append(
        "links",
        {
            "type": "Link",
            "label": "Biometric Attendance Punch Table",
            "link_type": "DocType",
            "link_to": "Biometric Attendance Punch Table",
        },
    )
    ws.append(
        "links",
        {
            "type": "Link",
            "label": "Biometric Device",
            "link_type": "DocType",
            "link_to": "Biometric Device",
        },
    )

    ws.append("links", {"type": "Card Break", "label": "Reports"})
    ws.append(
        "links",
        {
            "type": "Link",
            "label": "Biometric Daily Report",
            "link_type": "Report",
            "link_to": "Biometric Daily Report",
            "report_ref_doctype": "Biometric Attendance Log",
            "is_query_report": 0,
        },
    )
    ws.append(
        "links",
        {
            "type": "Link",
            "label": "Biometric Monthly Report",
            "link_type": "Report",
            "link_to": "Biometric Monthly Report",
            "report_ref_doctype": "Biometric Attendance Log",
            "is_query_report": 0,
        },
    )

    ws.append("links", {"type": "Card Break", "label": "Tools"})
    ws.append(
        "links",
        {
            "type": "Link",
            "label": "Employee Checkin",
            "link_type": "DocType",
            "link_to": "Employee Checkin",
        },
    )

    ws.set("roles", [])
    ws.append("roles", {"role": "System Manager"})
    ws.append("roles", {"role": "CE HR"})

    ws.save(ignore_permissions=True)
    frappe.db.commit()
    return ws.name
