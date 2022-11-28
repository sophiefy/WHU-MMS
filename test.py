import pymysql

# 打开数据库连接
db = pymysql.connect(user="DB_USER08",
                     password="DB_USER08@123",
                     host="124.70.7.2",
                     port=3306,
                     database="user08db",
                     charset='utf8')
# 端口号3306，utf-8编码，否则中文有可能会出现乱码。
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 如果存在表则删除
cursor.execute("DROP TABLE IF EXISTS Employee")

# 使用 execute()  方法执行 SQL 查询
sql = '''CREATE TABLE Employee (
         Id  CHAR(20) NOT NULL,
         Name  CHAR(20),
         Age INT,  
         SEX CHAR(1),
         Salary FLOAT )'''
try:
    cursor.execute(sql)
except Exception as e:
    db.rollback()  # 如果出错就回滚并且抛出错误收集错误信息。
    print("Error!:{0}".format(e))
# finally:
#     db.close()
# # 关闭数据库连接
# cursor = db.cursor()
#SQL语句
sql="SELECT * FROM Employee"
try:
    cursor.execute(sql)
    results = cursor.fetchall() #获取全部结果集。  fetchone 查询第一条数据
    if not results: #判断是否为空。
        print("数据为空！")
    else:
        for row in results:
            Id = row[0]
            Name = row[1]
            Age = row[2]
            Sex = row[3]
            Salary = row[4]
            # 打印结果
            print("id:{0}姓名:{1}年龄:{2}性别:{3}工资:{4}".format(Id,Name,Age,Sex,Salary))
except Exception as e:
    db.rollback()  #如果出错就会滚数据库并且输出错误信息。
    print("Error:{0}".format(e))
finally:
    db.close()#关闭数据库。