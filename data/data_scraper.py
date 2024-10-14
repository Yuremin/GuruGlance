import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
import sys
sys.path.append('.')
from config import db_config

def get_cs_rankings():
    url = 'http://csrankings.org/#/index?all'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    researchers = []

    # 假设我们从表格中提取信息
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) > 1:
            name = cols[0].text.strip()
            homepage_link = cols[0].find('a')['href']
            domain = cols[1].text.strip()  # 假设领域信息在第二列
            researchers.append({
                'name': name,
                'homepage': homepage_link,
                'domain': domain
            })

    return researchers

def insert_researchers_to_db(researchers):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO researchers (name, domain, homepage) 
        VALUES (%s, %s, %s)
        """

        for researcher in researchers:
            cursor.execute(insert_query, (researcher['name'], researcher['domain'], researcher['homepage']))

        connection.commit()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    researchers_data = get_cs_rankings()
    insert_researchers_to_db(researchers_data)
