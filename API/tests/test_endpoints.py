"""
This file holds the tests for endpoints.py
"""

from unittest import TestCase, skip
from flask_restx import Resource, Api
import random

import API.endpoints as ep
import db.db as db

HUGE_NUM = 10000000000000


def new_entity_name(entity_type):
    int_name = random.randint(0, HUGE_NUM)
    return f"new {entity_type}" + str(int_name)

class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.HELLO, ret)    # uses new HELLO constant

    def test_create_user(self):
        """
        See if we can successully create a new user.
        Post-condition: user is in DB.
        """
        cu = ep.CreateUser(Resource)
        new_user = new_entity_name("user")
        ret = cu.post(new_user)
        rooms = db.get_users()
        self.assertIn(new_user, rooms)

    def test_create_room(self):
        """
        See if we can successully create a new room.
        Post-condition: room is in DB.
        """
        cr = ep.CreateRoom(Resource)
        new_room = new_entity_name("room")
        ret = cr.post(new_room)
        rooms = db.get_rooms()
        self.assertIn(new_room, rooms)
    
    def test_list_rooms1(self):
        """
        Post-condition 1: return is a dictionary
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        self.assertIsInstance(ret, dict)

    def test_list_rooms2(self):
        """
        Post-condition 2: keys to the dict are strings
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        for key in ret:
            self.assertIsInstance(key, str)

    def test_list_rooms3(self):
        """
        Post-condition 3: the values in the dict are themselves dicts
        """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        for val in ret.values():
            self.assertIsInstance(val, dict)