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

    def del_linked(self, phone, env="uat"):

        # 传入phone
        # 查询idpusers, 获取idp

        tables = {}
        _users = set()
        _usersdriver = set()
        _apply = set()
        _apply_info = set()
        _client_info = set()
        _account = set()

        client = pymongo.MongoClient(host)
        aos = pymongo.MongoClient(aoshost)

        if env == "test"
            idp = "eddidclientpool"
            crm = "test"
        elif env == "uat":
            idp = "eddidclientpooluat"
            crm = "uat"

        for result in client[idp]['users'].find({"phone_number":{"$regex":".+{}".format(phone)}}):
            # print("idp : ", result)
            # print(result['subject'])
            _users.add(result['_id'])
            for usersdriver in client[idp]['userdevices'].find({"subject" : result['subject']}):
                # print(usersdriver)
                _usersdriver.add(usersdriver['_id'])

        for result in client[crm]['apply_info'].find({"phone":phone}):
            # print("apply_info : ", result)
            # print(result['applyId'])
            _apply_info.add(result['_id'])
            for applyd in client[crm]['apply'].find({'_id':"result['_id"}):
                _apply.add(applyd['_id'])
                _apply_info.add(applyd['applyInfoIds'])
                for acc in client[crm]["account"].find({"accountNumber": applyd["accountNumber"]}):
                    _account.add(acc["_id"])


        for result in client[crm]["client_info"].find({"phone":phone}):
            _client_info.add(result["_id"])

            for acc in client[crm]["account"].find({"_id": result['accountId']}):
                _account.add(acc["_id"])



if __name__ == '__main__':
    host = 'mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net'
    # host = 'localhost:27017'
    database = 'aos'  # 查询的数据库
    # Database(host, database).del_linked("apply_debug", {"phone":"13709691525"})	# 传入需要查询的表和查询条件
    # Database(host, database).del_linked("apply_debug", {'email':{"$regex" : ".*onedi.*"}})

    d = mongoTool(host)
    result = d.findData(database, "accounts", {'phone': '15089514626'})
    print(result)
