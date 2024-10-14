from flask import Blueprint, render_template, jsonify, request
import mysql.connector
from mysql.connector import Error
from config import db_config

main = Blueprint('main', __name__)

# 首页路由
@main.route('/')
def index():
    return render_template('index.html')

# 获取领域下的研究专家
@main.route('/researchers', methods=['GET'])
def get_researchers():
    domain = request.args.get('domain')
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        if domain and domain != "all":
            query = "SELECT * FROM researchers WHERE domain = %s"
            cursor.execute(query, (domain,))
        else:
            query = "SELECT * FROM researchers"
            cursor.execute(query)

        result = cursor.fetchall()
        return jsonify(result)

    except Error as e:
        return jsonify({"error": str(e)})

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
