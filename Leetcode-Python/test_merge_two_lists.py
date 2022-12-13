import unittest
from merge_two_lists import ListNode


class TestMergeTwoLists(unittest.TestCase):
    def test_merge_two_lists1(self):
        l1 = [1, 2, 4]
        l2 = [1, 3, 4]
        ll_l1 = ListNode().list_to_LL(l1)
        ll_l2 = ListNode().list_to_LL(l2)
        solution = [1, 1, 2, 3, 4, 4]
        result = ListNode().merge_two_lists(ll_l1, ll_l2)
        self.assertEqual(solution, result)

    def test_merge_two_lists2(self):
        l1 = [4, 9, 10]
        l2 = [9, 14, 100]
        ll_l1 = ListNode().list_to_LL(l1)
        ll_l2 = ListNode().list_to_LL(l2)
        solution = [4, 9, 9, 10, 14, 100]
        result = ListNode().merge_two_lists(ll_l1, ll_l2)
        self.assertEqual(solution, result)

    def test_merge_two_lists3(self):
        l1 = []
        l2 = [1]
        ll_l1 = ListNode().list_to_LL(l1)
        ll_l2 = ListNode().list_to_LL(l2)
        solution = [1]
        result = ListNode().merge_two_lists(ll_l1, ll_l2)
        self.assertEqual(solution, result)


if __name__ == '__main__':
    unittest.main()
