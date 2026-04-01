from pathlib import Path
import sys

import pytest

# Ensure the project root is in the system path for imports
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from api import app


@pytest.fixture
def test_client():
    with app.test_client() as client:
        with app.app_context():
            yield client
