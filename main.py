from ui.console_ui import play_console


def main():
    while True:
        play_console()
        again = input("\nPlay again? (yes/no): ").lower().strip()
        if again != "yes":
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()