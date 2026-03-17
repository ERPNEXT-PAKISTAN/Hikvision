// Copyright (c) 2025, NDV and contributors
// For license information, please see license.txt

frappe.query_reports["Biometric Monthly Report"] = {
    filters: [
        {
            fieldname: "date_range",
            label: __("Enter Your Date Range"),
            fieldtype: "Date Range",
        },
    ],

    onload: function (report) {
        report.page.add_inner_button(__("Copy Link"), function () {
            var filters = report.get_filter_values();
            var params = new URLSearchParams();
            if (filters.date_range && Array.isArray(filters.date_range)) {
                params.set("from_date", filters.date_range[0]);
                params.set("to_date", filters.date_range[1]);
            }
            var base_url = window.location.origin + "/app/biometric-monthly-report";
            var url = params.toString() ? base_url + "?" + params.toString() : base_url;

            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(url).then(function () {
                    frappe.show_alert({ message: __("Link copied to clipboard!"), indicator: "green" });
                }).catch(function () {
                    frappe.show_alert({ message: __("Failed to copy link. Please copy it manually: ") + url, indicator: "red" });
                });
            } else {
                var textarea = document.createElement("textarea");
                textarea.value = url;
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand("copy");
                document.body.removeChild(textarea);
                frappe.show_alert({ message: __("Link copied to clipboard!"), indicator: "green" });
            }
        });
    }
};
