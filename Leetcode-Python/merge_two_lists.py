class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

    def list_to_LL(self, arr):
        if len(arr) < 1:
            return None
        if len(arr) == 1:
            return ListNode(arr[0])
        return ListNode(arr[0], next=self.list_to_LL(arr[1:]))

    def get_list_length(self, head, iterations):
        if head is None:
            return 0
        if head.next:
            return self.get_list_length(head.next, iterations+1)
        return iterations

    def merge_two_lists(self, list1, list2):
        i = 0
        j = 0
        len_list1 = self.get_list_length(list1, 1)
        len_list2 = self.get_list_length(list2, 1)
        result = []
        while i < len_list1 or j < len_list2:
            if i == len_list1:
                while list2.next:
                    result.append(list2.val)
                    list2 = list2.next
                result.append(list2.val)
                break
            elif j == len_list2:
                while list1.next:
                    result.append(list1.val)
                    list1 = list1.next
                result.append(list1.val)
                break
            if list1.val <= list2.val:
                result.append(list1.val)
                list1 = list1.next
                i += 1
            else:
                result.append(list2.val)
                list2 = list2.next
                j += 1
        return result


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    ll_l1 = ListNode().list_to_LL(l1)
    ll_l2 = ListNode().list_to_LL(l2)
    ans = ListNode().merge_two_lists(ll_l1, ll_l2)
    ans_ll = ListNode().list_to_LL(ans)
    print(str(ans_ll))
