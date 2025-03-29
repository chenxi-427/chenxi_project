# -*- coding: utf-8 -*-
"""
@Author: diablo
@Date: 3/28/25
@Description:
"""
import mysql.connector
import pandas as pd

def connect_to_mysql(host, user, password, database):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None
def main():
    mydb = connect_to_mysql("localhost", "root", "396200", "test_dev")
    if not mydb:
        print("Failed to establish connection")
        return

    cursor = mydb.cursor()
    try:
        query = f"SELECT * FROM test"
        cursor.execute(query)
        results=cursor.fetchall()
        print(results)
        # 假设data是你的数据结构
        df = pd.DataFrame(results)
        # 将DataFrame保存为Excel文件
        df.to_excel('output.xlsx', sheet_name='Sheet1')

    except Exception as err:
        print(f"Error reading from MySQL: {err}")


if __name__ == "__main__":
    main()
