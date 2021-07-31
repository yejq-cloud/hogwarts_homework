"""
hogwarts 
yejq
"""
import logging


class Calculator:

    def log_info(self, message):
        logging.info(message)

    def add(self, a, b):
        self.log_info("add")
        self.log_info(a)
        self.log_info(b)
        return a + b

    def minus(self, a, b):
        self.log_info("minus")
        self.log_info(a)
        self.log_info(b)
        return a - b

    def mcl(self, a, b):
        self.log_info("mcl")
        self.log_info(a)
        self.log_info(b)
        return a * b

    def div(self, a, b):
        self.log_info("div")
        self.log_info(a)
        self.log_info(b)
        return a / b