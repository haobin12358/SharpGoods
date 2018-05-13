# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from config.response import APIS_WRONG
from control.CLocations import CLocations

class ALocations(Resource):
    def __init__(self):
        self.clocations = CLocations()

    def get(self, locations):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是get".format(locations))
        print("=======================api===================")

        apis = {
            "get_all_location":"self.clocations.get_all_location()"
        }

        if locations not in apis:
            from config.response import APIS_WRONG
            return APIS_WRONG
        return eval(apis[locations])

    def post(self, locations):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是post".format(locations))
        print("=======================api===================")

        apis = {
            "new_location":"self.clocations.new_location()",
            "update_location": "self.clocations.update_location()"
        }

        if locations not in apis:
            from config.response import APIS_WRONG
            return APIS_WRONG
        return eval(apis[locations])