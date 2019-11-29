#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-03 19:43:34
# @Author  : onedi (onedi@qq.com)
# @Link    : localhost
# @Version : $Id$


import pymongo

from Commons import Logging
from Commons.Logging import Logs


class mongoTool:
    log = Logging.Logs()
    # gm = GlobalMap()
    log = Logs()

    def __init__(self, host):
        self.log.debug("开始连接数据库: {}".format(host, ))
        self.client = pymongo.MongoClient(host)  # 连接数据库
        # self.client = pymongo.MongoClient(self.gm.get_value("mongohost"))		#连接数据库
        self.log.debug("数据库连接成功")

    #
    # def __del__(self):
    # 	self.log.debug("close Client")
    # 	self.client.close()		#关闭数据库

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
        for result in db[collection].find(query):
            self.log.debug("查询的数据为", result)
            return result

    def aggregate(self, database, collection, query):

        db = self.client[database]
        for result in db[collection].aggregate(query):
            self.log.debug("查询的数据为", result)
            return result

    def UpdataData(self, database=None, collection=None, query=None, setdata=None):
        db = self.client[database]
        # db["accounts"].update({"phone":"15089514626",  "forLogin":True} , { "$set" : { "currentRoute" : "/account"} })
        db[collection].update_one(query, setdata)

    def findData_All(self, database, collection, query):

    	delmap = {}

        db = self.client[database]
        applydata = db[collection].aggregate([{
            '$match': query
        }, {
            '$lookup': {
                'from': 'apply_info',
                'localField': 'applyInfoIds',
                'foreignField': '_id',
                'as': 'applyInfoTable'
            }
        }, {
            '$lookup': {
                'from': 'apply',
                'localField': 'applyId',
                'foreignField': '_id',
                'as': 'applyTable'
            }
        }, {
            '$lookup': {
                'from': 'lead',
                'localField': 'leadId',
                'foreignField': '_id',
                'as': 'leadTable'
            }
        }
        ])

        delmap['apply'] = applydata['_id']
        delmap['apply_info'] = applydata['applyInfoTable']['_id']
        delmap['lead'] = applydata['leadId']


        if applydata['idpUserId'] != "":
        	# 通过idp查询users表
        	pass

        # 判断数据是否成功, 成功则查询client_info
        if applydata['status'] == "success":

            clientdata = db['client_info'].aggregate([{
                '$match': {'phone': applydata['applyInfoTable']['phone'], 'email': applydata['applyInfoTable']['email']}
            }, {
                '$lookup': {
                    'from': 'account',
                    'localField': 'accountId',
                    'foreignField': '_id',
                    'as': 'accountTable'
                }
            }
            ])


if __name__ == '__main__':
    host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
    # host = 'localhost:27017'
    database = 'aos'  # 查询的数据库
    # Database(host, database).del_linked("apply_debug", {"phone":"13709691525"})	# 传入需要查询的表和查询条件
    # Database(host, database).del_linked("apply_debug", {'email':{"$regex" : ".*onedi.*"}})

    d = mongoTool(host)
    result = d.findData(database, "accounts", {'phone': '15089514626'})
    print(result)
