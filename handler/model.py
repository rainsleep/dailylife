#encoding:utf-8
__author__ = 'Administrator'
import pymongo

class DataBase(object):
	"""
	数据库的封装,这里采用MongoDB作为数据库。
	"""
	def __init__(self, host = "localhost", port = 27017):
		self.con = pymongo.Connection(host,port)
		self.db = self.con.daily_life #创建数据库

	def add(self, tb, record):
		"""
		describe:数据库的插入操作
		args:
			tb:数据库表名
			record:待插入的记录
		"""
		user_table = self.db[tb]#取得数据库表
		user_table.insert(record)
	def delete(self, tb, key):
		"""
		describe:数据库的删除
		args:
			tb:数据库表名
			key:删除条件，是一个键值对,如如{"username":"apple"}
				类似于SQL语句的 delete *from tb where username = apple
		"""
		#muser.remove({'id':1}) # delet records where id = 1
		user_table = self.db[tb]
		user_table.remove(key)
	def update(self, tb, key, update_data):
		"""
		describe:更新
		args:
			tb:数据库表
			key:更新条件
			update_data:新的数据,键值对
		"""
		user_table = self.db[tb]
		update_record = {}
		update_record["$set"] = update_data
		user_table.update(key,update_record )
	def find(self, tb, key):
		"""
		describe:查询一条记录
		args:
			tb:数据库表
			key:查询条件
		return:若找到，返回一个个键值对，斗则返回None
		"""
		user_table = self.db[tb]
		return user_table.find_one(key)
	def find_all(self, tb, key):
		"""
		describe:批量查询
		args:
			tb:数据库表
			key:查询条件
		return:返回一个列表
		"""
		records = []
		user_table = self.db[tb]
		for record in  user_table.find(key):
			records.append(record)
		return records


