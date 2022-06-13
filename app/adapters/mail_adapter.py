from typing import Set


class MailAdapter:
    """
    For Outbound Adapters you need to define classes/methods/interfaces and specify their signature
    but the body should remain empty (cf following example)
    """
    
    def send_mail(self: "MailAdapter", recipients: Set[str], title: str, content: str) -> None:
        
        # Toggle [raise : return] statements for testing
        # raise NotImplemented

        print("\nTEST ========= send_mail")
        print("title:", title, "| content:", content, "| recipients:", recipients)
        return None
