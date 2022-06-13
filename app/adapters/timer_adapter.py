class TimerAdapter:
    """
    Handle outbound requests to the Timer Service
    """
    
    # waiting_time => seconds
    # company_pk => target company to receive suggestions
    def set_email_timer(self: "TimerAdapter", waiting_time: int,
                        email_type: int, company_pk: int) -> None:
        
        # Toggle [raise : return] statements for testing
        # raise NotImplemented

        print("\nTEST ========= set_email_timer")
        print("waiting_time:", waiting_time, "| email_type:", email_type, "| company_pk:", company_pk)
        return None
