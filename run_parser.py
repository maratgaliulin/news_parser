from methods.parser.rbc_news_parser import rbc_news_parser
import time
import asyncio

time_sleep = 3600

def timeless_loop():
    while True:
        rbc_news_parser()
        time.sleep(time_sleep)

if (__name__ == '__main__'):
    asyncio.run(timeless_loop())