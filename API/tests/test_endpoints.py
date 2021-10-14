"""
This file holds the tests for endpoints.py
"""

from unittest import TestCase, skip
from flask_restx import Resource, Api

import API.endpoints as ep

class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
        
        #self.assertIn('hello', ret) # bc 'h' is lowercase, cause test FAIL
        self.assertIn(ep.HELLO, ret)    # uses new HELLO constant

