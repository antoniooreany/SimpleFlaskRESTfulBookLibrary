# conftest.py

import warnings
from sqlalchemy.exc import SAWarning

def pytest_configure(config):
    warnings.filterwarnings("ignore", category=SAWarning, message=".*Query.get.*")
    warnings.filterwarnings("ignore", category=DeprecationWarning, message=".*LegacyAPIWarning.*")