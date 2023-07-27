from flask import Flask, jsonify, request, render_template
import pymysql
app = Flask(__name__)
# MySQL数据库连接配置
db_config = {
    'host': '113.31.147.148',
    'user': 'drink',
    'password': 'Fatb6X6fNFXsY6MM',
    'database': 'drink',
    'port':3306
}
def query_data():
    goods={}
    # 建立MySQL数据库连接
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()
    query = f"SELECT * FROM drink"
    # 执行查询并获取结果
    cursor.execute(query)
    result = cursor.fetchall()
    data=[]
    if len(result) > 0:
        columns = [desc[0] for desc in cursor.description]
        table_data = [{columns[i]: row[i] for i in range(len(columns))} for row in result]
        data.extend(table_data)

    # 提交事务并关闭连接
    conn.commit()
    cursor.close()
    conn.close()
    for i in data:
        goods[i['name']]=i['price']
    return goods
# 将数据库取出来的数据赋值给goods
goods=query_data()

@app.route('/')
def index():
    return render_template('index.html',goods=goods)

@app.route('/goods', methods=['GET'])
def get_goods():
    return jsonify(goods)

@app.route('/checkout', methods=['POST'])
def checkout():
    cart = request.json.get('cart')
    total_price = calculate_total_price(cart)
    # 处理其他相关逻辑...
    return jsonify({'message': '结算成功', 'total_price': total_price})

def calculate_total_price(cart):
    total_price = 0
    # print(cart)
    for drink, count in cart.items():
        if drink in goods:
            total_price += goods[drink] * count
    return total_price

if __name__ == '__main__':
    app.run()
