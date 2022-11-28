# Backend Description

1. 为了测试前端效果，暂时使用了`sqlite3`创建和管理一个测试用的数据库。它存放在`database/books.db`。
2. `CRUD.py`同样是基于`sqlite3`编写的测试用后端代码。实现了简单的增删查改图书功能。
3. 之后将使用`pymysql`连接并管理`GuassDB`。