# peeweegeter
循环外键当前解决办法

(1) 第一种方式是：使用IntegerField储存原始ID ---目前使用这个模式这也是peewee缺点

```python
class User(Model):
    username = CharField()
    favorite_tweet_id = IntegerField(null=True) #使用简单方式
```

(2) 第二种方式是：使用DeferredForeignKey绕过该问题可以使用外键字段

```python
class User(Model):
	username = CharField()
#Tweet表没有被定义但是可以延迟连接外键.
	favorite_tweet = DeferredForeignKey('Tweet', null=True)
class Tweet(Model):
	message = TextField()
	user = ForeignKeyField(User, backref='tweets')

#既然Tweet已经定义，“favorite_Tweet”已经转换了
print(User.favorite_tweet)
#结果
<ForeignKeyField: "user"."favorite_tweet">
```

