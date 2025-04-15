'''
from survey import AnonymousSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Italian', 'Binandere']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
'''

# the above code has two tests that both pass
# however, they are a bit repetitive.
# to streamline this, we can use a fixture that inserts the repeated lines of code into each test function.

import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Italian', 'Binandere']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses