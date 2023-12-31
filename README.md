# 项目来源
本项目来源于[《腾讯云 Cloud Studio 实战训练营》](https://marketing.csdn.net/p/06a21ca7f4a1843512fa8f8c40a16635)的参赛作品，该作品在腾讯云 [Cloud Studio](https://www.cloudstudio.net/?utm=csdn) 中运行无误。

# 饮料自动售卖机应用程序

这是一个基于Flask和MySQL的饮料自动售卖机应用程序，用户可以浏览饮料列表并将饮料添加到购物车中进行结算。

## 功能

- 显示饮料列表：从数据库中获取饮料名称和价格，并在前端页面上显示出来。
- 添加到购物车：用户可以点击“加入购物车”按钮将饮料添加到购物车，同时更新购物车的数量。
- 结算：用户点击“结算”按钮，将购物车的内容发送到后端进行处理，并返回总消费金额。

## 技术栈

- 后端：Python、Flask、MySQL
- 前端：HTML、CSS、JavaScript、Axios

## 部署步骤

1. 安装依赖：运行`pip install Flask pymysql`安装Flask和pymysql模块。
2. 配置数据库：在`db_config`中填入正确的MySQL数据库连接配置。
3. 创建数据库表：运行相应的SQL语句，创建名为"drink"的数据表，并添加必要的字段。
4. 运行后端：在终端中进入项目目录，运行`python app.py`启动后端服务器。
5. 部署前端：将前端代码保存为`index.html`文件，并将其放置在Flask应用程序的`templates`文件夹中。
6. 打开浏览器：在浏览器中输入`http://localhost:5000`即可打开购物车应用程序。

## 数据库结构

购物车应用程序使用一个名为"drink"的数据表来存储饮料的名称和价格。数据表的结构如下：

```
CREATE TABLE drink (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price FLOAT NOT NULL
);
```

## API 接口

- GET `/goods`：获取饮料列表的接口，返回所有饮料及其价格的JSON数据。
- POST `/checkout`：结算购物车的接口，接收前端发送的购物车内容并返回总消费金额的JSON数据。

## 注意事项

- 请确保正确配置数据库连接信息，并且已经创建了正确的数据表。
- 本应用程序仅为示例，未实现真正的支付功能，请勿将其用于生产环境。
- 如需自定义饮料列表，请修改后端代码中的`query_data`函数，并按照相应的数据格式返回饮料数据。
