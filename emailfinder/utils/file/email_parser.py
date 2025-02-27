import re

def get_emails(target, text):
    regex = r"[a-zA-Z0-9_\.+-]+@" + re.escape(target)  # Escape target to prevent regex issues
    cleaned_text = text.replace("<em>", "").replace("</em>", "") \
                       .replace("<strong>", "").replace("</strong>", "") \
                       .replace("<b>", "").replace("</b>", "")
    emails = re.findall(regex, cleaned_text)
    return emails
