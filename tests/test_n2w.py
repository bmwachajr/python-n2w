#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, skip
from app.n2w import N2w


class N2wTestCase(TestCase):

    def setUp(self):
        self.n2w = N2w()

    @skip
    def test_convert_numbers_successfully(self):
        result = self.n2w.convert(123)
        self.assertEqual("one hundred twenty three", result.lower())

    @skip
    def test_convert_numbers_less_than_ten_successfully(self):
        result = self.n2w.convert(2)
        self.assertEqual("two", result.lower())

    @skip
    def test_convert_numbers_less_than_100_successfully(self):
        result = self.n2w.convert(49)
        self.assertEqual("forty two", result.lower())

    @skip
    def test_convert_hundreds_successfully(self):
        result = self.n2w.convert(134)
        self.assertEqual("one hundred thirty four", result.lower())

    @skip
    def test_convert_thousands_successfully(self):
        result = self.n2w.convert(2222)
        self.assertEqual("two thousand two hundred twenty two", result.lower())

    @skip
    def test_convert_millions_succussfully(self):
        result = self.n2w.convert(2000001)
        self.assertEqual("two million one", result.lower())

    @skip
    def test_convert_billions_successfully(self):
        result = self.n2w.convert(1000000000)
        self.assertEqual("one billion", result.lower())

    @skip
    def test_convert_quadrillions_successfully(self):
        result = self.n2w.convert(3000000000000)
        self.assertEqual("three quandrillion", result.lower())

    @skip
    def test_convert_quintillions_successfully(self):
        result = self.n2w.convert(10000000000000000)
        self.assertEqual("ten quintillion", result.lower())