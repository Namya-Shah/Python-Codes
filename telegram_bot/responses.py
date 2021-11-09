from datetime import datetime
import requests
import bs4 as BeautifulSoup

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey! This is Nitin Shah from Namya International. How can I assist you?"
    if user_message in ("who are you?", "who are you"):
        return "I am BigSmoke"
    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    if user_message in ("stretch film"):
        return "What are your requirements?"

    return "I don't understand you."