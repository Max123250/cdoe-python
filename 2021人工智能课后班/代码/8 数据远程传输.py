from flask import Flask
app = Flask(__name__)#创建服务
@app.route('/')#配置路由 route n.路径 子路径用@app.route('/xxx')
def f():#网站会执行一次定义函数的代码，则不用
    return "ready"#返回值
app.run("127.0.0.1",5000)#启动服务,局域网内用“127.0.0.1”或本机ip 5000为开启的端口
