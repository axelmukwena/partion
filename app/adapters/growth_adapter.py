from typing import List, Tuple


class GrowthAdapter:
    """
    Handle outbound requests to the Growth Policies Service
    """
    
    # Get companies matching [company] and [industry], except this, new company?
    def get_email_sequence(self: "GrowthAdapter", company_pk: int) -> List[Tuple[int, int]]:
        
        # Toggle [raise : return] statements for testing
        # raise NotImplemented

        print("\nTEST ========= get_email_sequence")
        print("company_pk:", company_pk)
        sequence = [(1, 3600), (2, 86400), (4, 604800)]
        return sequence
    
    # Get email contents for pending suggestions,
    # return title, contents and list of recipients
    def get_email_contents(self: "GrowthAdapter", company_pk: int, email_type: int,
                           suggestions: List[str]) -> (str, str, List[str]):
        
        # Toggle [raise : return] statements for testing
        # raise NotImplemented

        print("\nTEST ========= get_email_contents")
        print("company_pk:", company_pk, "| email_type:", email_type, "| suggestions:", suggestions)
        returned = ("Look! Potential partners", "Hey there! ...", {"Axel", "Jason", "Thomas", "Londechamp"})
        return returned
