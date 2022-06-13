import unittest
from app.entities.suggestions_entities import SuggestionsEntities
from app.models.company import Company
from app.models.suggestion import Suggestion

entities = SuggestionsEntities()


class SuggestionsEntitiesTests(unittest.TestCase):
    """
    Before running Suggestion Entity tests, you're expected to
    toggle the comment between raise and return statements
    in all the entity files

    raise NotImplemented | as per hiring test requirements
    return | as per testing requirements
    """
    
    def test_cast_company(self: "SuggestionsEntitiesTests"):
        """ Should return object of type Company model """
        company = Company(pk=898, name="microsoft", country="us", industry="technology")
        self.assertEqual(entities.cast_company(company), company)
    
    def test_cast_suggestion(self: "SuggestionsEntitiesTests"):
        """ Should return object of type Suggestion model """
        suggestion = Suggestion(pk=89, company_pk=898, suggestions={"us": -1, "fr": 1})
        self.assertEqual(entities.cast_suggestion(suggestion), suggestion)


"""
Running these tests will execute temporary print functions in specific methods
demonstrating the process and logic flow of the Suggestions Services
"""
if __name__ == "__main__":
    unittest.main()
