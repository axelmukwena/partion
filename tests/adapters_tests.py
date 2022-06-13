import unittest

from app.adapters.companies_adapter import CompaniesAdapter
from app.adapters.persistence_adapter import PersistenceAdapter
from app.adapters.growth_adapter import GrowthAdapter
from app.adapters.timer_adapter import TimerAdapter
from app.adapters.mail_adapter import MailAdapter
from app.models.company import Company

companies_adapter = CompaniesAdapter()
persistence_adapter = PersistenceAdapter()
growth_adapter = GrowthAdapter()
timer_adapter = TimerAdapter()
mail_adapter = MailAdapter()


class AdaptersTests(unittest.TestCase):
    """
    Before running Adapter tests, you're expected to
    toggle the comment between raise and return statements
    in all the adapter files

    raise NotImplemented | as per hiring test requirements
    return | as per testing requirements
    """
    
    """ Companies Adapters """
    def test_get_potential_partners(self: "AdaptersTests"):
        companies = [Company(pk=893, name="microsoft", country="us", industry="technology"),
                     Company(pk=893, name="netflix", country="us", industry="technology")]
        self.assertEqual(companies_adapter.get_potential_partners(898, "us", "technology"), companies)
    
    """ Growth Adapters """
    def test_get_email_sequence(self: "AdaptersTests"):
        sequence = [(1, 3600), (2, 86400), (4, 604800)]
        self.assertEqual(growth_adapter.get_email_sequence(898), sequence)
    
    def test_get_email_contents(self: "AdaptersTests"):
        returned = ("Look! Potential partners", "Hey there! ...", {"Axel", "Jason", "Thomas", "Londechamp"})
        self.assertEqual(growth_adapter.get_email_contents(898, 2, ["microsoft", "netflix"]), returned)
    
    """ Mail Adapters """
    def test_send_mail(self: "AdaptersTests"):
        self.assertEqual(mail_adapter.send_mail({"Axel", "Jason", "Thomas", "Londechamp"},
                                                "Look! Potential partners", "Hey there! ..."), None)
    
    """ Persistence Adapters """
    def test_create_suggestions(self: "AdaptersTests"):
        self.assertEqual(persistence_adapter.create_suggestions(898, {"microsoft": -1, "netflix": -1}), None)

    def test_update_suggestions(self: "AdaptersTests"):
        self.assertEqual(persistence_adapter.update_suggestions(898, {"microsoft": 1, "netflix": 0}), None)

    def test_get_suggestions(self: "AdaptersTests"):
        suggestions = {"microsoft": -1, "netflix": 1}
        self.assertEqual(persistence_adapter.get_suggestions(898), suggestions)
    
    """ Timer Adapters """
    def test_set_email_timer(self: "AdaptersTests"):
        self.assertEqual(timer_adapter.set_email_timer(3600, 1, 898), None)


"""
Running these tests will execute temporary print functions in specific methods
demonstrating the process and logic flow of the Suggestions Services
"""
if __name__ == "__main__":
    unittest.main()
