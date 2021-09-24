import pytest
# 详细断言异常
class TestCase:

    def test_zero_division_long(self):
        with pytest.raises(ZeroDivisionError) as excinfo:
            var = 1 / 0

        # 断言异常类型 type
        assert excinfo.type == ZeroDivisionError
        # 断言异常 value 值
        assert "zero" in str(excinfo.value)

    def test_01(self):
        print("test")

print('chongtu')


