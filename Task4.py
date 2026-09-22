from datetime import datetime

LOG_FILE = "keylog.txt"


def log_key(key):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {key}\n")


def main():
    print("===== Simple Keylogger =====")
    print("Type text below.")
    print("Type 'exit' to stop the program.\n")

    while True:
        text = input("Enter text: ")

        if text.lower() == "exit":
            print("Keylogger stopped.")
            break

        for key in text:
            log_key(key)

        log_key("ENTER")


if __name__ == "__main__":
    main()
