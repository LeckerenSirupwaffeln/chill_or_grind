# Python imports

# 3rd party imports
from loguru import logger

# Relative imports


@logger.catch
def main():
    logger.info("Hello from chill-or-grind!")


if __name__ == "__main__":
    main()
