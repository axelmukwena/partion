from app.models.company import Company


class CompaniesAdapter:
    """
    Handle outbound requests to the Companies Service
    
    company_pk: get all rows except current company or
    maybe filter out current company in the results
    """
    
    # Get companies matching [company] and [industry]
    def get_potential_partners(self: "CompaniesAdapter", company_pk: int,
                               country: str, industry: str) -> list[Company]:
        
        # Toggle [raise : return] statements for testing
        # raise NotImplemented
        
        print("\nTEST ========= get_potential_partners")
        print("company_pk:", company_pk, "| country:", country, "| industry:", industry)
        companies = [Company(pk=893, name="microsoft", country="us", industry="technology"),
                     Company(pk=893, name="netflix", country="us", industry="technology")]
        return companies
