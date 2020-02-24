import nose.tools as nt

from part_a import get_number_of_steps, get_number_of_steps_recursive


class Tests(object):

    def test_getting_number_of_steps(self):
        actual = get_number_of_steps(10)
        expected = 6
        nt.assert_equals(expected, actual)

        actual = get_number_of_steps(27)
        expected = 111
        nt.assert_equals(expected, actual)

        actual = get_number_of_steps(871)
        expected = 178
        nt.assert_equals(expected, actual)

        actual = get_number_of_steps(837799)
        expected = 524
        nt.assert_equals(expected, actual)

    def test_getting_number_of_steps_with_recursion(self):
        actual = get_number_of_steps_recursive(10)
        expected = 6
        nt.assert_equals(expected, actual)

        actual = get_number_of_steps_recursive(27)
        expected = 111
        nt.assert_equals(expected, actual)

        actual = get_number_of_steps_recursive(871)
        expected = 178
        nt.assert_equals(expected, actual)

        actual = get_number_of_steps_recursive(837799)
        expected = 524
        nt.assert_equals(expected, actual)