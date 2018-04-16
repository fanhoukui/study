#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from logging import handlers


def blog(name, data):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = handlers.TimedRotatingFileHandler("../logs/action.log", when="D", interval=1, backupCount=30, encoding="utf-8")
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.addHandler(fh)
    fh.setFormatter(file_formatter)
    logger.info(data)


def log(name, level, data):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    fh = handlers.TimedRotatingFileHandler("../logs/bank.log", when="D", interval=1, backupCount=30, encoding="utf-8")
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.addHandler(fh)
    fh.setFormatter(file_formatter)
    if level == "info":
        logger.info(data)
    elif level == "error":
        logger.error(data)


def write_account(name, account):
    with open("%s.log" % name, 'w', encoding="utf-8") as f:
        f.write(str(account))