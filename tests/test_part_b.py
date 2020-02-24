import nose.tools as nt

from part_b import get_number_of_steps_for_each_m


class Tests(object):

    def test_getting_number_of_steps(self):
        actual = get_number_of_steps_for_each_m(1, 10)
        expected = {1: 0, 2: 1, 3: 7, 4: 2, 5: 5, 6: 8, 7: 16, 8: 3, 9: 19, 10: 6}
        nt.assert_equals(expected, actual)