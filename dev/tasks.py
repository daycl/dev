from __future__ import unicode_literals
import frappe
from frappe.utils import datediff, nowdate, format_date, add_days

def all():
    recipient = "wcl_orange@163.com"
    frappe.sendmail(recipients=[recipient],
        sender="test@example.com",
        subject="Library Articles Overdue", content="123", bulk=True)
