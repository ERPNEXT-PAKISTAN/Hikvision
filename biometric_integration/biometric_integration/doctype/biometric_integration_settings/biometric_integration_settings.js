// Copyright (c) 2025, NDV and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Biometric Integration Settings", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Biometric Integration Settings", {
    refresh: function(frm) {

        // 0) Test Connection
        frm.add_custom_button(__('Test Connection'), function() {
            frappe.call({
                method: "biometric_integration.biometric_integration.doctype.biometric_integration_settings.biometric_integration_settings.test_connection",
                freeze: true,
                freeze_message: __("Testing device connection(s)..."),
                callback: function(r) {
                    if (!r.message) return;
                    let rows = r.message.map(function(d) {
                        let icon = d.status === "success"
                            ? '<span style="color:green">&#10003; Connected</span>'
                            : '<span style="color:red">&#10007; Failed</span>';
                        return `<tr>
                            <td style="padding:4px 8px"><b>${d.label}</b></td>
                            <td style="padding:4px 8px">${d.ip}</td>
                            <td style="padding:4px 8px">${icon}</td>
                            <td style="padding:4px 8px">${d.message}</td>
                        </tr>`;
                    }).join("");
                    frappe.msgprint({
                        title: __("Device Connection Test Results"),
                        message: `<table style="width:100%;border-collapse:collapse">
                            <thead><tr>
                                <th style="padding:4px 8px;text-align:left">Device</th>
                                <th style="padding:4px 8px;text-align:left">IP</th>
                                <th style="padding:4px 8px;text-align:left">Status</th>
                                <th style="padding:4px 8px;text-align:left">Details</th>
                            </tr></thead>
                            <tbody>${rows}</tbody>
                        </table>`,
                        wide: true
                    });
                },
                error: function(r) {
                    frappe.msgprint({
                        title: __("Connection Test Error"),
                        message: r.message || __("Could not reach device. Check IP, username and password."),
                        indicator: "red"
                    });
                }
            });
        });

        // 1) Existing: full pipeline - Device -> Logs -> Punch Table -> Employee Checkin
        frm.add_custom_button(__('Sync Attendance (Device + Checkin)'), function() {
            frappe.call({
                method: "biometric_integration.biometric_integration.doctype.biometric_integration_settings.biometric_integration_settings.sync_attendance",
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(r.message);
                        frm.reload_doc();
                    }
                }
            });
        });

        // 2) NEW: only Punch Table -> Employee Checkin (no device call)
        frm.add_custom_button(__('Sync to Employee Checkin'), function() {
            frappe.call({
                method: "biometric_integration.biometric_integration.doctype.biometric_integration_settings.biometric_integration_settings.sync_to_employee_checkin_only",
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(r.message);
                        frm.reload_doc();
                    }
                }
            });
        });

    }
});

