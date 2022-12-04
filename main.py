from peewee import *
from jwdb import *
# 根据已有数据库创建model.py命令：python -m pwiz -H localhost -p 3307 -u root -P  -e mysql jwdb > jwdb.py
# 建立数据库连接
#database.atomic() #上下文管理器，主要是事务
''' 
注意使用peewee在复制数据库生成model.py时候有bug，可以删除用不到的model表也就是class
也就是说有循环外键依赖，如本例子中的用peewee添加循环外键有点困难，因为在定义其中一个外键时，它指向的模型还没有定义，导致 NameError
(1) 第一种方式是：使用IntegerField储存原始ID ---目前使用这个模式这也是peewee缺点
class User(Model):
    username = CharField()
    favorite_tweet_id = IntegerField(null=True)
(2) 第二种方式是：使用DeferredForeignKey绕过该问题可以使用外键字段
    class User(Model):
        username = CharField()
        # Tweet表没有被定义但是可以延迟连接外键.
        favorite_tweet = DeferredForeignKey('Tweet', null=True)
    class Tweet(Model):
        message = TextField()
        user = ForeignKeyField(User, backref='tweets')
    # 既然Tweet已经定义，“favorite_Tweet”已经转换了
    print(User.favorite_tweet)
    # <ForeignKeyField: "user"."favorite_tweet">
'''
if __name__ == '__main__':
    # 判断是否连接数据库
    print(database.is_closed())
    # get()函数，获取单个记录-注意可以使用get()函数简写，不简写需要些==以及table.field
    grandma = AppFdDutCategory.select().where(AppFdDutCategory.c_name == '设计需求文档').get()
    oneselect = AppFdDutCategory.get(c_name='设计需求文档')
    print('查AppFdDutCategory表中第一个数据：',oneselect.c_name)
    print('查AppFdDutCategory表中第一个数据：', grandma)

    # 获取记录清单
    category = AppFdDutCategory.select() #这是个所有记录，是一个query_set类型
    for category_item in category:
        print(category_item.c_name)

    # 关闭数据库，下面确认是否关闭
    database.close()
    print(database.is_closed())


