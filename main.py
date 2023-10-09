import openai
import random
import logging
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from bit import Key
from PIL import Image
import os

logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

class UserInterface:
    def __init__(self, chatbot):
        self.console = Console()
        self.chatbot = chatbot

    def display_welcome_message(self):
        try:
            self.console.print(Panel.fit(Text("Welcome to Krakow Guide on AI", style="bold")))
            self.console.print("This application will help you explore Krakow's historical, architectural, and legendary facets.")
            user_experience = Prompt.ask("What experience do you want in Krakow?")
            self.chat_with_ai(user_experience)
        except Exception as e:
            logging.error(f"Exception in display_welcome_message: {e}")

    def chat_with_ai(self, user_experience):
        try:
            response = self.chatbot.answer_questions(user_experience)
            self.console.print(f"AI: [bold cyan]{response}[/bold cyan]")
        except Exception as e:
            logging.error(f"Exception in chat_with_ai: {e}")

    def display_menu(self):
        try:
            self.console.print("1. Ask a question")
            self.console.print("2. Get recommendations")
            self.console.print("3. View advertisements")
            self.console.print("4. View sponsored content")
            self.console.print("5. Continue chatting")
            self.console.print("6. Exit")
        except Exception as e:
            logging.error(f"Exception in display_menu: {e}")

    def get_menu_option(self):
        try:
            option = Prompt.ask("Please select an option (1-6)")
            if option not in ['1', '2', '3', '4', '5', '6']:
                self.console.print("Invalid option! Please try again.", style="bold red")
                return self.get_menu_option()
            return option
        except Exception as e:
            logging.error(f"Exception in get_menu_option: {e}")

    def display_recommendations(self, recommendations):
        try:
            for i, recommendation in enumerate(recommendations, start=1):
                self.console.print(f"{i}. {recommendation}")
            choice = Prompt.ask("Choose an attraction for more information", choices=[str(i) for i in range(1, len(recommendations)+1)])
            return choice
        except Exception as e:
            logging.error(f"Exception in display_recommendations: {e}")

# Initialize logging
logging.basicConfig(filename='krakowguideonai.log', level=logging.ERROR)



class Chatbot:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key

    def answer_questions(self, user_prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a guide on krakow's historical, architectural, and legendary facets. Like from book Putiwnik po Architektursze Krakowa. Your goal is to achieve a user satisfaction rate of at least 90% via responses to user messages.",
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
                temperature=0.5,
            )
            user_message = response['choices'][0]['message']['content']
            return user_message
        except Exception as e:
            logging.error("Exception: %s", e)
            logging.error("Response: %s", response)
            return "An error occurred. Please check the error log for more details."

class RecommendationEngine:
    def generate_recommendations(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"I am a travel guide bot. A user is asking for recommendations in Krakow. The user said: '{user_input}'. What should I recommend?",
                max_tokens=50,
            )
            recommendations = response.choices[0].text.strip().split(', ')
            return recommendations
        except Exception as e:
            logging.error("Exception: %s", e)
            return ["Wawel Castle", "Main Square", "St. Mary's Basilica"]


class AffiliateMarketing:
    def select_advertisement(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"I am a travel guide bot. A user is asking for recommendations in Krakow. The user said: '{user_input}'. What advertisement should I show?",
                max_tokens=50,
            )
            advertisement = response.choices[0].text.strip()
            return advertisement
        except Exception as e:
            logging.error("Exception: %s", e)
            return "Visit the Wieliczka Salt Mine, a UNESCO World Heritage Site!"


class SponsoredContent:
    def select_content(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"I am a travel guide bot. A user is asking for recommendations in Krakow. The user said: '{user_input}'. What sponsored content should I show?",
                max_tokens=50,
            )
            content = response.choices[0].text.strip()
            return content
        except Exception as e:
            logging.error("Exception: %s", e)
            return "Did you know that Krakow is home to Europe's largest market square?"


class DataCollectionAndAnalysis:
    def collect_data(self, user_input, response, recommendations, advertisement, content, available_purchases):
        # Collect the data
        data = {
            'user_input': user_input,
            'response': response,
            'recommendations': recommendations,
            'advertisement': advertisement,
            'content': content,
            'available_purchases': available_purchases,
        }
        # Save the data to a database or a file
        # ...
        return data

    def analyze_data(self, data):
        # Load the collected data from the database or file
        # ...
        # Analyze the data to gain insights about the user's preferences and behavior
        # ...
        # Use the insights to improve the application, for example by personalizing recommendations or advertisements
        # ...
        insights = {
            'preferred_recommendations': ['Wawel Castle', 'Main Square'],
            'preferred_advertisements': ['Wieliczka Salt Mine'],
            'preferred_content': ['Europe\'s largest market square'],
        }
        return insights

    def improve_application(self, insights):
        # Use the insights gained from the analysis to improve the application
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"I have analyzed the user's preferences and behavior and found that they prefer the following recommendations: {insights['preferred_recommendations']}, advertisements: {insights['preferred_advertisements']}, and content: {insights['preferred_content']}. How can I improve the application to better suit the user's preferences?",
                max_tokens=50,
            )
            improvement_suggestions = response.choices[0].text.strip()
            return improvement_suggestions
        except Exception as e:
            logging.error("Exception: %s", e)
            return "An error occurred. Please check the error log for more details."

class MechanikaPutiwnika:
    def __init__(self, user_interface, chatbot, recommendation_engine, affiliate_marketing, sponsored_content, data_collection_and_analysis):
        self.user_interface = user_interface
        self.chatbot = chatbot
        self.recommendation_engine = recommendation_engine
        self.affiliate_marketing = affiliate_marketing
        self.sponsored_content = sponsored_content
        self.data_collection_and_analysis = data_collection_and_analysis

    def display_teatip_advertisement(self):
        if random.random() < 0.4:
            address = '174gHv4dgLDTfy3byUPUkpaai6hfFMYw8R'
            print("Maybe you want to send your Bitcoin tips to this address:", address)
            print("2% from all tips will be provided to charity.")
    # Open the QR code image
            img = Image.open("qr_code.png")
            img.show()


    def process_question(self, user_input):
        answer = self.chatbot.answer_questions(user_input)
        self.user_interface.console.print(f"Answer: {answer}")


    def start(self):
        # 1. Завязка
        self.user_interface.console.print("Welcome to Krakow Guide on AI!")
        user_experience = Prompt.ask("What experience do you want in Krakow?")
        
        # 2. Развітіе Сюжета
        self.display_teatip_advertisement()
        
        while True:
            self.user_interface.console.print("Menu:")
            self.user_interface.console.print("1. Ask a question")
            self.user_interface.console.print("2. Get recommendations")
            self.user_interface.console.print("3. View advertisements")
            self.user_interface.console.print("4. View sponsored content")
            self.user_interface.console.print("5. Exit")
            
            option = Prompt.ask("Please select an option (1-5)")
            
            if option == '1':
                user_input = Prompt.ask("What would you like to ask?")
                self.process_question(user_input)
            elif option == '2':
                recommendations = self.recommendation_engine.generate_recommendations(user_experience)
                self.user_interface.console.print(f"Recommendations: {recommendations}")
            elif option == '3':
                ad = self.affiliate_marketing.select_advertisement(user_experience)
                self.user_interface.console.print(f"Advertisement: {ad}")
            elif option == '4':
                content = self.sponsored_content.select_content(user_experience)
                self.user_interface.console.print(f"Sponsored Content: {content}")
            elif option == '5':
                break
            
            self.display_teatip_advertisement()
        
        # 3. Развязка
        self.user_interface.console.print("Goodbye!")

def main():
    try:
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            print("Please set your OpenAI API key as an environment variable.")
            return

        chatbot = Chatbot(openai_api_key)
        user_interface = UserInterface(chatbot)
        recommendation_engine = RecommendationEngine()
        affiliate_marketing = AffiliateMarketing()
        sponsored_content = SponsoredContent()
        data_collection_and_analysis = DataCollectionAndAnalysis()

        mechanika_putiwnika = MechanikaPutiwnika(user_interface, chatbot, recommendation_engine, affiliate_marketing, sponsored_content, data_collection_and_analysis)
        mechanika_putiwnika.start()
    except Exception as e:
        logging.error("Exception: %s", e)
        print("An error occurred. Please check the error log for more details.")


if __name__ == "__main__":
    main()

