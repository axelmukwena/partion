from typing import Dict


class PersistenceAdapter:
    """
    Handle outbound requests to the Database
    """
    
    # Save new, target company and list of suggested potential partners
    # of shape key: company_pk, value: status
    def create_suggestions(self: "PersistenceAdapter", company_pk: int,
                           suggestions: Dict[str, int]) -> None:
        
        # Toggle [raise : return] statements for testing
        # raise NotImplemented
        
        # ======== tests =========
        print("\nTEST ========= create_suggestions")
        print("company_pk:", company_pk, "| suggestions:", suggestions)
        return None
    
    # Find company_pk in suggestions and update
    # pk for the suggestion could also work
    def update_suggestions(self: "PersistenceAdapter", company_pk: int,
                           suggestions: Dict[str, int]) -> None:
        
        # Toggle [raise : return] statements for testing
        # raise NotImplemented

        # ======== tests =========
        print("\nTEST ========= update_suggestions")
        print("company_pk:", company_pk, "| suggestions:", suggestions)
        return None
    
    # Get suggestions given the company_pk
    def get_suggestions(self: "PersistenceAdapter", company_pk: int) -> Dict[str, int]:
        
        # Toggle [raise : return] statements for testing
        # raise NotImplemented

        # ======== tests =========
        suggestions = {"microsoft": -1, "netflix": 1}
        print("\nTEST ========= get_suggestions")
        print("company_pk:", company_pk, "| suggestions:", suggestions)
        return suggestions
