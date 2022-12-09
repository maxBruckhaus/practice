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
        if head.next:
            return self.get_list_length(head.next, iterations+1)
        return iterations

    def create_new_list(self, head, iterations, ignored_element):
        print("iterations:" + str(iterations))
        print("head:" + str(head))

        # check if we reached past the last element
        if head is None:
            return

        # check if ignored element is last element
        if iterations == ignored_element and head.next is None:
            return

        if head.next:
            if iterations == ignored_element:
                return ListNode(head.next.val, self.create_new_list(head.next.next, iterations+1, ignored_element))
            else:
                return ListNode(head.val, self.create_new_list(head.next, iterations+1, ignored_element))
        return ListNode(head.val)

    def remove_nth_node(self, head, n):
        listnode_size = self.get_list_length(head, 1)
        ignored_element = listnode_size - n
        print("size:" + str(listnode_size))
        print("IGNORED: " + str(ignored_element))

        counter = 0
        # check if only one element in input
        if listnode_size == 1:
            return None

        # check if removing 1st element
        if ignored_element == 0:
            return ListNode(head.next.val, head.next.next)

        new_ll = self.create_new_list(head, 0, ignored_element)
        return new_ll


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    ll1 = ListNode().list_to_LL(list1)
    print(ll1)
    result = ListNode().remove_nth_node(ll1, 2)
    print("result" + str(result))
