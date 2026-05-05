// Copyright (c) 2025, NDV and contributors
// For license information, please see license.txt

frappe.query_reports["Biometric Monthly Report"] = {
    filters: [
        {
            fieldname: "date_range",
            label: __("Enter Your Date Range"),
            fieldtype: "Date Range",
            default: [
                frappe.datetime.month_start(),
                frappe.datetime.month_end(),
            ],
        },
    ]
};
