import pytest
from testscripts.BaseTest import BaseTest

class Test_Dependent(BaseTest):

    @pytest.mark.dependency
    def test_1(self):
        print("This is test1")
        assert 11==11

    @pytest.mark.dependency(depends=["test_1"])
    def test_2(self):
        print("This is test2 dependent on test1")
        assert 11==11


    @pytest.mark.xfail
    def test_3(self):
        print("This is test3")
        assert 11==10
