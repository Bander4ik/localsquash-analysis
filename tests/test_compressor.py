"""Unit-тести для модуля compressor. ЗАГЛУШКА — буде розширено у ЛР03."""
import pytest
from localsquash.compressor import compression_ratio


def test_compression_ratio_basic():
    assert compression_ratio(100, 25) == 0.75


def test_compression_ratio_zero_original_raises():
    with pytest.raises(ValueError):
        compression_ratio(0, 50)
