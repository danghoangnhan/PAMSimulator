"""Application entry point: launches the PAMSimulator GUI."""
from controller import Navigator
import logging


def main():
    """Construct the navigator and start the Qt event loop."""
    try:
        navigator = Navigator()
        navigator.start()
    except Exception as e:  # pylint: disable=broad-exception-caught
        logging.error("An error occurred: %s", str(e))


if __name__ == "__main__":
    main()
