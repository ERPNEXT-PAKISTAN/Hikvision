// Copyright (c) 2025, NDV and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Biometric Integration Settings", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on("Biometric Integration Settings", {
    refresh: function(frm) {

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

