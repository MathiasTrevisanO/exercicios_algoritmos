import unittest
from exercicio_endereçamento_direto import add_name, table_age, get_name_by_age 

class TestName(unittest.TestCase):
    def test_add_name(self):
        # Arrange
        age = 25
        name = "name1"

        # Act
        add_name(name, age)

        # Assert
        self.assertEqual(table_age[age], name)

    def test_get_name_by_age(self):
        # Arrange
        age = 25
        name = "name1"
        table_age[age] = name

        # Act
        result = get_name_by_age(age)

        # Assert
        self.assertEqual(result, name)

if __name__ == '__main__':
    unittest.main()