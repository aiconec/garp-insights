import frappe

from insights.api.subscription import get_subscription_key


def execute():
    if get_subscription_key():
        notify_users()


def notify_users():
    # notify users about the support portal access
    note = frappe.new_doc("Note")
    note.title = "GARP Data Studio Support Portal"
    note.public = 1
    note.notify_on_login = 1
    note.content = """
    <div class="ql-editor read-mode"><h3>GARP Data Studio Support Portal</h3><br><p>You have an active subscription (or trial) for GARP Data Studio. You can now access the Support Portal to get help from the GARP team.</p><br><p>To access the portal go to <a href="/insights/settings" target="_blank">Settings</a> -> Send Login Link</p><img class="mt-2" src="https://user-images.githubusercontent.com/25369014/229565675-fb96d7f0-cd0d-472e-8c9f-d0e1b7a36439.png" alt="support_portal_1.png"><p><br></p></div>
    """
    note.insert(ignore_mandatory=True)
