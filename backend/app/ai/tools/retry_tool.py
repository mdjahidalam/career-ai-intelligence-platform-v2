import time


class RetryTool:

    @staticmethod
    def execute(
        func,
        retries: int = 3,
        delay: int = 2
    ):

        last_exception = None

        for attempt in range(retries):

            try:

                return func()

            except Exception as e:

                last_exception = e

                if attempt < retries - 1:

                    time.sleep(delay)

        raise last_exception