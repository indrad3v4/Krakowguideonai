import openai
import os
from rich.console import Console
from rich.table import Table
from rich.prompt import IntPrompt, Prompt
from rich.panel import Panel
from rich.text import Text
from loguru import logger

logger.add("error_log.txt", level="ERROR")




class UserInterface:
    def __init__(self):
        self.console = Console()

    def display_menu(self):
        self.console.print(Panel.fit(Text("Krakow Guide on AI", style="bold")))
        self.console.print("1. Ask a question")
        self.console.print("2. Get recommendations")
        self.console.print("3. Manage affiliate marketing partnerships")
        self.console.print("4. Manage sponsored content")
        self.console.print("5. Manage in-app purchases")
        self.console.print("6. Collect and analyze data")
        self.console.print("7. Quit")

    def start(self, krakow_guide):
        try:
            self.console.print("Welcome to Krakow Guide on AI!", style="bold")
            while True:
                self.display_menu()
                # logger.debug("Displaying menu")
                choice = IntPrompt.ask("Please choose an option", choices=[str(i) for i in range(1, 8)])
                # logger.debug(f"User chose option {choice}")
                if choice == 7:
                    break
                elif choice == 6:
                    krakow_guide.DataCollectionAndAnalysis.collect_and_analyze_data()
                elif choice == 5:
                    krakow_guide.InAppPurchases.manage_transactions()
                elif choice == 4:
                    krakow_guide.SponsoredContent.manage_content()
                elif choice == 3:
                    krakow_guide.AffiliateMarketing.handle_partnerships()
                elif choice == 2:
                    self.display_recommendations(krakow_guide)
                elif choice == 1:
                    self.ask_question(krakow_guide)
        except Exception as e:
            print("An error occurred", exc_info=True)

    def display_recommendations(self, krakow_guide):
        recommendations = krakow_guide.RecommendationEngine.provide_recommendations()
        table = Table(title="Recommendations")
        table.add_column("Number")
        table.add_column("Attractions/Activities")
        for i, recommendation in enumerate(recommendations, start=1):
            table.add_row(str(i), recommendation)
        self.console.print(table)
        choice = IntPrompt.ask("Choose an attraction for more information", choices=range(1, len(recommendations)+1))
        # Logic to display more information about the chosen attraction
        # ...

    def ask_question(self, krakow_guide):
        question = self.console.input("Please enter your question: ")
        response = krakow_guide.Chatbot.answer_questions(question)
        self.console.print("Chatbot: " + response)

class Chatbot:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def answer_questions(self, question):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=50,
        )
        return response.choices[0].text.strip()

class RecommendationEngine:
    def provide_recommendations(self):
        # List of popular attractions or activities in Krakow
        recommendations = [
            "Wawel Castle",
            "Main Market Square",
            "St. Mary's Basilica",
            "Kazimierz",
            "Oskar Schindler's Factory",
        ]
        return recommendations

class AffiliateMarketing:
    def handle_partnerships(self):
        # Logic to handle partnerships
        print("Managing affiliate marketing partnerships...")

class SponsoredContent:
    def manage_content(self):
        # Logic to manage sponsored content
        print("Managing sponsored content...")

class InAppPurchases:
    def manage_transactions(self):
        # Logic to handle in-app purchases and transactions
        print("Managing in-app purchases and transactions...")

class DataCollectionAndAnalysis:
    def collect_and_analyze_data(self):
        # Logic to collect and analyze data
        print("Collecting and analyzing data...")

class KrakowGuideOnAi:
    def __init__(self, api_key):
        self.UI = UserInterface()
        self.Chatbot = Chatbot(api_key)
        self.RecommendationEngine = RecommendationEngine()
        self.AffiliateMarketing = AffiliateMarketing()
        self.SponsoredContent = SponsoredContent()
        self.InAppPurchases = InAppPurchases()
        self.DataCollectionAndAnalysis = DataCollectionAndAnalysis()

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")  # Get OpenAI API key from environment variables
    if not api_key:
        print("Please set your OpenAI API key as an environment variable.")
    else:
        krakow_guide = KrakowGuideOnAi(api_key)
        krakow_guide.UI.start(krakow_guide)
