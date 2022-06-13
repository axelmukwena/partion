import unittest
from app.domain.suggestions_domain import SuggestionsDomain
from app.models.company import Company

domain = SuggestionsDomain()


class SuggestionsDomainTests(unittest.TestCase):
    def test_domain(self: "SuggestionsDomainTests"):
        company = Company(pk=893, name="microsoft", country="us", industry="technology")
        domain.handle_company_created(company)
        
        domain.handle_user_web_action(898, "microsoft", 1)
        
        domain.handle_timer_expired(898, 1)


"""
Running these tests will execute temporary print functions in specific methods
demonstrating the process and logic flow of the Suggestions Services
"""
if __name__ == "__main__":
    unittest.main()
