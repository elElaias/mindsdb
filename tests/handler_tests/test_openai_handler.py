import os
import pytest

from mindsdb.api.mysql.mysql_proxy.libs.constants.response_type import RESPONSE_TYPE
from integration_tests.flows.http_test_helpers import HTTPHelperMixin
from integration_tests.flows.conftest import *  # noqa: F403,F401

# used by (required for) mindsdb_app fixture in conftest
API_LIST = [
    "http",
]

OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY")


@pytest.mark.usefixtures("mindsdb_app")
class TestOpenAIHandler(HTTPHelperMixin):
    def test_missing_required_keys(self):
        query = f"""
            CREATE MODEL sentiment_classifier_gpt3
            PREDICT sentiment
            USING
            engine = 'openai',
            api_key = '{OPEN_AI_API_KEY}';
        """
        self.sql_via_http(query, RESPONSE_TYPE.ERROR)
