"""
Specify object parameters for the Company resource
Obvious parameters such as created and updated_at are skipped

pk => primary_key
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Company:
    pk: int
    name: str
    country: str  # ISO code https://www.ncbi.nlm.nih.gov/books/NBK7249/
    industry: str
