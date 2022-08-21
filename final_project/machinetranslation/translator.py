"""
Final Project: Translator
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apiKey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(english_text):
    """
    Convert English to French Function
    """
    if english_text is None:
        return None

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text

def frenchToEnglish(french_text):
    """
    Convert French to English Function
    """
    if french_text is None:
        return None

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
