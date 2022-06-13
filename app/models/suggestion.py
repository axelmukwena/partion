"""
Specify object parameters for the Suggestion resource
Obvious parameters such as created and updated_at are skipped

pk => primary_key
"""
from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Suggestion:
    """
    - Should we save each association of target_company and suggested_company as a distinct row?
        - Better manipulation, querying and storage of values
        - when was suggestion created, accepted, declined; did the target company change the status again
        - Any relationships between accepted, declined and pending suggestions
        - Rows could reach number_of_companies x (n - 1), is this bad?
        
    - Save as one row, with all associated, potential partners in a JSON column
        - Saves size and cheaper
        - Queries could become complex
        - Rows max count is equal number_of_companies
    
    
    company_pk | The company to receive / receiving suggestions
    
    suggestions | Dictionary
    key: unique_company_name, value: status
    status => -1: pending | 0: declined | 1: accepted
    """
    pk: int
    company_pk: int
    suggestions: Dict[str, int]
