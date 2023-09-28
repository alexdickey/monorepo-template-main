class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        cls.messages = []
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.add_message("Logger created exactly once")
        else:
            cls._instance.add_message("logger already created")
        return cls._instance

    def add_message(self, message):
        self.messages.append(message)


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class.
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")
        print(logger.messages)


if __name__ == "__main__":
    main()
