import allure
import pytest


class TestUn:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是test_001测试第一步")  # 标记测试步骤
    def test_001_1(self):
        print("------>test_001_1")
        allure.attach("标题", "具体测试内容")  # 添加步骤描述信息
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是test_001测试第二步")
    def test_001_2(self):
        print("------>test_001_2")
        allure.attach("用户名：", "李白")
        allure.attach("密码：", "李白白")
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是test_001测试第步")  # 标记测试步骤
    def test_001_3(self):
        print("------>test_001_1")
        allure.attach("标题", "具体测试内容")  # 添加描述信息
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是test_001测试第一步")  # 标记测试步骤
    def test_001_4(self):
        print("------>test_001_1")
        allure.attach("标题", "具体测试内容")  # 添加描述信息
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是test_001测试第一步")  # 标记测试步骤
    def test_001_5(self):
        print("------>test_001_1")
        allure.attach("标题", "具体测试内容")  # 添加描述信息
        assert True
