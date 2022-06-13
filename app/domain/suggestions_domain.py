from app.entities.suggestions_entities import SuggestionsEntities

from ..adapters.companies_adapter import CompaniesAdapter
from ..adapters.persistence_adapter import PersistenceAdapter
from ..adapters.growth_adapter import GrowthAdapter
from ..adapters.timer_adapter import TimerAdapter
from ..adapters.mail_adapter import MailAdapter

companies_adapter = CompaniesAdapter()
persistence_adapter = PersistenceAdapter()
growth_adapter = GrowthAdapter()
timer_adapter = TimerAdapter()
mail_adapter = MailAdapter()
entities = SuggestionsEntities()


class SuggestionsDomain:
    """Main logic of the Suggestions Service."""
    
    def __init__(self):
        self.company = {}
    
    def handle_company_created(self: "SuggestionsDomain", company):
        """
        Get companies with same country and industry
        Returned list should be of type List(Company)
        """
        
        # Cast company to our Model Object
        self.company = entities.cast_company(company)
        
        # Get potential partners with matched country and industry
        potential_partners = companies_adapter.get_potential_partners(
            self.company.pk, self.company.country, self.company.industry)
        
        # Create a dict of suggestions initialized to status pending
        suggestions = {}
        for co in potential_partners:
            suggestions[co.name] = -1
        
        # Save the suggestions
        persistence_adapter.create_suggestions(self.company.pk, suggestions)
        
        # Get the email sequence to be sent
        sequence = growth_adapter.get_email_sequence(self.company.pk)
        
        # Set timer after we get sequences
        if len(sequence) > 0:
            [email_type, waiting_time] = sequence[0]
            timer_adapter.set_email_timer(waiting_time, email_type, self.company.pk)
    
    # Update suggestion based on new status of a potential company
    def handle_user_web_action(self: "SuggestionsDomain", company_pk: int, suggested_name: str, status: int):
        suggestions = persistence_adapter.get_suggestions(company_pk)
        suggestions[suggested_name] = status if status == 0 or status == 1 else -1
        persistence_adapter.update_suggestions(company_pk, suggestions)
    
    def handle_timer_expired(self, company_pk: int, email_type: int):
        suggestions = persistence_adapter.get_suggestions(company_pk)
        
        # If still have pending suggestions, get title, content and recipients to compose emails
        # Get all the names of pending suggested companies
        pending_suggestions = [key for (key, value) in suggestions.items() if value == -1]
        if len(pending_suggestions) > 0:
            title, content, recipients = growth_adapter.get_email_contents(
                company_pk, email_type, pending_suggestions)
            
            mail_adapter.send_mail(recipients, title, content)
            
            # Lets assume, given a sequence, the email type always starts at 1, in ascending order
            # If not, another variable could be used to track the position of send_email()
            # When tracking email type within sequence, we can decide when to terminate the scheduling
            if email_type == 1:
                self.__schedule_all_emails(company_pk)
    
    # ========== Private Methods ==========
    
    def __schedule_all_emails(self: "SuggestionsDomain", company_pk: int):
        sequence = growth_adapter.get_email_sequence(company_pk)
        
        for email_type, waiting_time in sequence[1:]:
            # Email is scheduled, but each time before sent, we check if
            # there are pending potential companies
            timer_adapter.set_email_timer(waiting_time, email_type, company_pk)
