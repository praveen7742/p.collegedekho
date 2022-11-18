import logging
import inspect

class LogGen:
    @staticmethod
    def loggen():
        # getLogger() method takes the test case name as input
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler('/home/collegedekho/p.collegedekho/CTA 2/Logs/automation1.log')

        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)

        # setting the logger level
        # logger.debug("Debug log")
        # logger.info("Information log ")
        # logger.warning("Warning log")
        # logger.error("Error log")
        # logger.critical("Critical log")
        return logger

