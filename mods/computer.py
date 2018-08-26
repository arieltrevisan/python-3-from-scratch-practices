"""
    See: basic_syntax/modules.py
"""

__computers = {
    "Apple": {"model": "iPad", "year": 2015},
    "HP": {"model": "Pavilion", "year": 2018}
}


def info(brand: str):
    if brand in __computers:
        return __computers[brand]
