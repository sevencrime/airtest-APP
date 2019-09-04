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


	def __init__(self, host):
		self.client = pymongo.MongoClient(host)		#连接数据库

	def __del__(self):
		self.log.debug("close Client")
		self.client.close()		#关闭数据库

	# 迭代判断是否最后一个值
	def lookahead(iterable):
		"""Pass through all values from the given iterable, augmented by the
        information if there are more values to come after the current one
        (True), or if it is the last value (False).
        """
		# Get an iterator and pull the first value.
		it = iter(iterable)
		last = next(it)
		# Run the iterator to exhaustion (starting from the second value).
		for val in it:
			# Report the *previous* value (more to come).
			yield last, True
			last = val
		# Report the last value.
		yield last, False


	def findData(self, database, collection, query):

		db = self.client[database]
		aosdb = self.client['aos']
		userdb = self.client['eddidclientpoolfeature']

		# 判断先查询哪个数据库的那个表
		# 记录查询的每个_id, 避免重复
		# aos.account.idp >> users.subject >> deivers.subjcet >> apply.idp >> apply_info._id >> account.idp >> client_info._id
		if database == "test" or database == "uat":
			if collection == "apply_info":
				findlist = ['apply_info', 'apply', 'account', 'client_info']

		elif database == "aos":
			pass

		elif database == "eddidclientpoolfeature":
			pass

		for applyinfo in db[collection].find(query):
			print("applyinfo >> ", applyinfo)

			for apply in db['apply'].find({'_id' : applyinfo['applyId']}):
				print("apply >> ", apply)

				for account in db['account'].find({'idpUserId' : apply['idpUserId']}):
					print("account >> ", account)

					if isinstance(account['clientId'], list):
						for n in range(len(account['clientId'])):

							for client in db['client_info'].find({'_id' : account['clientId'][n]}):
								print("client_info >> ", client)

					else:
						print("数据有问题")

				# users 表

				for users in userdb['users'].find({'subject' : apply['idpUserId']}):
					print("users >> ", users)

				for userdevices in userdb['userdevices'].find({'subject' : apply['idpUserId']}):
					print("userdevices >> ", userdevices)



				for aosaccount in aosdb['account'].find({'idpUserId' : apply['idpUserId']}):
					print("aosaccount >> ", aosaccount)


	def UpdataData(self):
		self.db["accounts"].update({"phone":"15089514626",  "forLogin":True} , { "$set" : { "currentRoute" : "/account"} })





if __name__ == '__main__':
	host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
	# host = 'localhost:27017'
	database = 'test'	#查询的数据库
	# Database(host, database).del_linked("apply_debug", {"phone":"13709691525"})	# 传入需要查询的表和查询条件
	# Database(host, database).del_linked("apply_debug", {'email':{"$regex" : ".*onedi.*"}})

	d = mongoTool(host)
	d.findData(database, "apply_info", {'email':'901onedi2s1067@qq.com'})
	


	

	








