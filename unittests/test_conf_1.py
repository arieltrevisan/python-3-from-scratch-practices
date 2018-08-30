import pytest


def test_conf_1_method_1(setup_only_once, setup_each_method):
    print("test_conf1_m1")


def test_conf_1_method_2(setup_only_once, setup_each_method):
    print("test_conf1_m2")
