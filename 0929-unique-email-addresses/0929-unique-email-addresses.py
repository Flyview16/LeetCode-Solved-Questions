class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.replace('.', '')   # Remove all dots
            local_name = local_name.split('+')[0]      #  Select first item and ignore all text after +
            email = f"{local_name}@{domain_name}"
            unique_emails.add(email)

        return len(unique_emails)
