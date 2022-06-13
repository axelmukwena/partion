import unittest
from app.entities.suggestions_entities import SuggestionsEntities
from app.models.company import Company
from app.models.suggestion import Suggestion

entities = SuggestionsEntities()


class SuggestionsEntitiesTests(unittest.TestCase):
    def test_cast_company(self: "SuggestionsEntitiesTests"):
        """ Should return object of type Company model """
        company = Company(pk=898, name="microsoft", country="us", industry="technology")
        self.assertEqual(entities.cast_company(company), company)
    
    def test_cast_suggestion(self: "SuggestionsEntitiesTests"):
        """ Should return object of type Suggestion model """
        suggestion = Suggestion(pk=89, company_pk=898, suggestions={"us": -1, "fr": 1})
        self.assertEqual(entities.cast_suggestion(suggestion), suggestion)


if __name__ == "__main__":
    unittest.main()
