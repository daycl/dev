from __future__ import unicode_literals
import frappe

def all():
    recipient = "wcl_orange@163.com"
    frappe.sendmail(recipients=[recipient],
        sender="test@example.com",
        subject="Library Articles Overdue", content="123", bulk=True)
