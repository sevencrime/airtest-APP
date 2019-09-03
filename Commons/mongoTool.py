#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-03 19:43:34
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import pymongo
from bson.objectid import ObjectId
from collections import Counter

from Commons import Logging


class mongoTool:
	log = Logging.Logs(logname= "mongodb")


	def __init__(self, host, database):
		self.log.debug("连接数据库%s" %database)
		self.client = pymongo.MongoClient(host)		#连接数据库
		self.db = self.client[database]		#指定数据库
		self.database = database	#用于切换数据库返回

	def __del__(self):
		self.log.debug("close Client")
		self.client.close()		#关闭数据库


	def findData(self, collection, query):
		result = self.db[collection].find(query)
		for r in result:
			print(r)

		# db.getCollection("apply_info").find({phone: "15089514626"})
		# .forEach(
		# 	function(item)
		# {
		# 	print(db.getCollection("apply").find({"_id": item.applyId}))
		# db.getCollection("apply").remove({"_id": item.applyId})
		# }
		# )

	def UpdataData(self):
		self.db["accounts"].update({"phone":"15089514626",  "forLogin":True} , { "$set" : { "currentRoute" : "/account"} })





if __name__ == '__main__':
	# host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
	host = 'localhost:27017'
	database = 'aos'	#查询的数据库
	# Database(host, database).del_linked("apply_debug", {"phone":"13709691525"})	# 传入需要查询的表和查询条件
	# Database(host, database).del_linked("apply_debug", {'email':{"$regex" : ".*onedi.*"}})

	d = mongoTool(host, database)
	d.findData()
	


	

	







