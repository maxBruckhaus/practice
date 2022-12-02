import unittest
from remove_nth_node import ListNode


class TestRemoveNthNode(unittest.TestCase):
    def test_remove_nth_node1(self):
        input_list = [1, 2, 3, 4, 5]
        input_ll = ListNode().list_to_LL(input_list)
        print(input_ll)
        result = ListNode().remove_nth_node(input_ll, 2)

        ans = [1, 2, 3, 5]
        ans_list = ListNode().list_to_LL(ans)
        self.assertEqual(str(result), str(ans_list))

    def test_remove_nth_node2(self):
        input_list = [1, 2]
        input_ll = ListNode().list_to_LL(input_list)
        print(input_ll)
        result = ListNode().remove_nth_node(input_ll, 2)

        ans = [2]
        ans_list = ListNode().list_to_LL(ans)
        self.assertEqual(str(result), str(ans_list))

    def test_remove_nth_node3(self):
        input_list = [1, 2, 3]
        input_ll = ListNode().list_to_LL(input_list)
        print(input_ll)
        result = ListNode().remove_nth_node(input_ll, 1)

        ans = [1, 2]
        ans_list = ListNode().list_to_LL(ans)
        self.assertEqual(str(result), str(ans_list))

    def test_remove_nth_node4(self):
        input_list = [1, 2]
        input_ll = ListNode().list_to_LL(input_list)
        print(input_ll)
        result = ListNode().remove_nth_node(input_ll, 1)

        ans = [1]
        ans_list = ListNode().list_to_LL(ans)
        self.assertEqual(str(result), str(ans_list))


if __name__ == '__main__':
    unittest.main()
