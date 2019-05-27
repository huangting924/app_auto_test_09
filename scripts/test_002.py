import allure


class Test002:

    def test_002_1(self):
        """将截图上报到测试报告中"""
        with open("/Users/test/Documents/python_project/AppAutoTest/day08/scripts/aa.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
