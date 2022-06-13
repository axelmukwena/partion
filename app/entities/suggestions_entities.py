from app.models.company import Company
from app.models.suggestion import Suggestion


class SuggestionsEntities:
    @staticmethod
    def cast_company(company):
        print("\nTEST ========= cast_company")
        print("company:", company)
        return Company(company.pk, company.name, company.country, company.industry)
    
    @staticmethod
    def cast_suggestion(suggestion):
        print("\nTEST ========= cast_suggestion")
        print("suggestion:", suggestion)
        return Suggestion(suggestion.pk, suggestion.company_pk, suggestion.suggestions)
