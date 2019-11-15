#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commons.CommonsTool import query_initialData
from Commons.Logging import Logs


class ParentBase:
    log = Logs()

    def __init__(self):
        self.log.debug("父类调用query_initialData方法")
        query_initialData()