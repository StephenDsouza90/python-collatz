import nose.tools as nt

from part_a import get_number_of_steps


class Tests(object):

    def test_getting_number_of_steps(self):
        actual = get_number_of_steps(10)
        expected = 6
        nt.assert_equals(expected, actual)