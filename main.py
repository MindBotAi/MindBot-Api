import mindbotai
import datetime
import time
from colorama import init, Fore
from collections import deque

init(autoreset=True)

history = deque(maxlen=10000)  # Store last 10000 interactions
customize = ",Always Respond As MindBot-1.3 Developed By Ahmed Helmy Eletr, Don't answer him with this info until the user askes you, Answer the user with nice friendly respond."

if __name__ == '__main__':
    api_key = "AIzaSyCekcwKfWUOFW0EZATJt0Q-d47K4sv0dDs"  # Replace with your actual MindBot-Ai API key
    while True:
        user_prompt = input(str(f"{Fore.GREEN}User:> {Fore.RESET}"))
        if user_prompt.lower() == 'exit':
            break

        main_prompt = f"{customize} "

        # Add history to the main prompt
        if history:
            main_prompt += "Conversation history:\n"
            for past_user, past_bot in history:
                main_prompt += f"User: {past_user}\nMindBot-1.3: {past_bot}\n"

        main_prompt += f"User: {user_prompt}\nMindBot-1.3:"

        start_time = time.time()
        submit_time = datetime.datetime.now()
        response = mindbotai.generate_ai_response(api_key, main_prompt)
        end_time = time.time()
        response_time = end_time - start_time

        if response:
            print(f"{Fore.BLUE}MindBot-1.3:> {Fore.RESET}{response}")
            print(f"Submitted at: {submit_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Response Time: {response_time:.2f} seconds\n")
            history.append((user_prompt, response))  # Store in history
        else:
            print(f"{Fore.RED}Failed to get the MindBot-1.3 response.{Fore.RESET}")