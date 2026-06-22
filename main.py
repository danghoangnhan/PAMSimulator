from controller import Navigator
import logging


def main():
    try:
        navigator = Navigator()
        navigator.start()
    except Exception as e:
        logging.error("An error occurred: %s", str(e))


if __name__ == "__main__":
    main()
