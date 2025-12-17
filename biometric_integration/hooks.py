# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "biometric_integration"
app_title = "Biometric Integration"
app_publisher = "Taomoor"
app_description = "Hikvision biometric devices Integration with ERPNext"
app_icon = "octicon octicon-device-camera"
app_color = "grey"
app_email = "tymuur@outlook.com"
app_license = "MIT"

# Scheduled Tasks
# ---------------

scheduler_events = {
    # Simple options (uncomment if you want daily instead of cron)
    # "daily": [
    #     "biometric_integration.biometric_integration.doctype.biometric_integration_settings.biometric_integration_settings.scheduled_attendance_sync"
    # ],

    "cron": {
        # Run every 15 minutes (change to */5, 0 2 * * *, etc. as you like)
        "*/15 * * * *": [
            "biometric_integration.biometric_integration.doctype.biometric_integration_settings.biometric_integration_settings.scheduled_attendance_sync"
        ]
    }
}
