
import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Python AI Training")


def main():
    print("Application:", APP_NAME)

    try:
        user_input = input("Enter your message: ")

        if not user_input.strip():
            raise ValueError("Message cannot be empty!")

        processed_input = user_input.strip().lower()
        print("Processed message:", processed_input)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
