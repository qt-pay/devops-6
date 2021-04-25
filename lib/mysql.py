import time
import pymysql


def get_time():
    time_str = time.strftime("%Y{}%m{}%d{} %X")
    return time_str.format("年", "月", "日")


def get_connection():
    conn = pymysql.connect, db="django", charset='utf8')
    return conn
