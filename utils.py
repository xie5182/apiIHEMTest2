# 编写断言代码函数
import json

import pymysql

import app


def assert_common(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success的值
    self.assertEqual(code, response.json().get("code"))  # 断言code的值
    self.assertIn(message, response.json().get("message"))  # 断言message的值


def read_login_data():
    data_path = app.BASE_DIR + "/data/login_data.json"

    with open(data_path, mode='r', encoding='utf-8') as f:
        # 加载文件为 json 格式的数据
        jsonData = json.load(f)
        # 遍历文件取出其中数据并保存在列表中
        p_list = []

        for data in jsonData:
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            p_list.append((mobile, password, http_code, success, code, message))
        print(p_list)
        return p_list


def read_add_emp_data():
    """读取 添加员工"""

    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载文件为 json 格式的数据
        jsonData = json.load(f)
        # 由于 employee.json 是一个字典数据，那么我们可以使用字典的get方法获取其中

        add_emp_data = jsonData.get("add_emp")
        result_list = []
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        http_code = add_emp_data.get("http_code")
        result_list.append((username, mobile, success, code, message, http_code))

    print("读取 添加员工的数据", result_list)
    return result_list


def read_query_emp_data():
    """读取 查询员工"""

    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载文件为 json 格式的数据
        jsonData = json.load(f)
        # 由于 employee.json 是一个字典数据，那么我们可以使用字典的get方法获取其中

        result_list = []
        query_emp_data = jsonData.get("query_emp")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        http_code = query_emp_data.get("http_code")
        result_list.append((success, code, message, http_code))

    print("读取 查询 员工的数据", result_list)
    return result_list


def read_modify_emp_data():
    """读取 修改员工"""

    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载文件为 json 格式的数据
        jsonData = json.load(f)
        # 由于 employee.json 是一个字典数据，那么我们可以使用字典的get方法获取其中

        result_list = []

        modify_emp_data = jsonData.get("modify_emp")
        username = modify_emp_data.get("username")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        http_code = modify_emp_data.get("http_code")
        result_list.append((username, success, code, message, http_code))

    print("读取 修改 员工的数据", result_list)
    return result_list


def read_delete_emp_data():
    """读取 删除员工"""

    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载文件为 json 格式的数据
        jsonData = json.load(f)
        # 由于 employee.json 是一个字典数据，那么我们可以使用字典的get方法获取其中

        result_list = []

        delete_emp_data = jsonData.get("delete_emp")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        http_code = delete_emp_data.get("http_code")
        result_list.append((success, code, message, http_code))

    print("读取 删除 员工的数据", result_list)
    return result_list


class DBUtils:
    def __init__(self, host="182.92.81.159",
                 user="readuser",
                 password="iHRM_user_2019",
                 database="ihrm"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # __enter__ 和  __exit__ 是一对魔法方法，主要是和 with 结合使用
    # 如 with DBUtils as db:
    # 我们就可以在 with 的代码块中使用 db 来执行 sql 语句，这个 db 就相当于 cu
    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    # 自定义 建立 连接数据的函数    ------用不到---
    # def connect(self, host, user, password, database):
    #     conn = pymysql.connect(host, user, password, database)
    #     return conn


if __name__ == '__main__':
    # main 函数的作用？
    # 防止调用这个模块或者类时，自动执行代码
    read_login_data()
    print("hello")

