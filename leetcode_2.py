class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = []

    curr_node1 = l1
    curr_node2 = l2
    carry_over = 0

    # 2 <= digit_sum <= 18
    while curr_node1 is not None and curr_node2 is not None:
        digit_sum = curr_node1.val + curr_node2.val

        if carry_over != 0:
            digit_sum += carry_over
            carry_over = 0

        if digit_sum >= 10:
            carry_over = 1
            digit_sum = digit_sum - 10

        result.append(digit_sum)

        curr_node1 = curr_node1.next
        curr_node2 = curr_node2.next

    # Number 1 has more digits, so add them to results without adding
    if curr_node1 is not None and curr_node2 is None:

        while curr_node1 is not None:
            digit_sum = curr_node1.val

            if carry_over != 0:
                digit_sum += carry_over
                carry_over = 0

            if digit_sum >= 10:
                carry_over = 1
                digit_sum = digit_sum - 10

            result.append(digit_sum)
            curr_node1 = curr_node1.next

    # Number 2 has more digits, so add them to results without adding
    elif curr_node1 is None and curr_node2 is not None:

        while curr_node2 is not None:
            digit_sum = curr_node2.val

            if carry_over != 0:
                digit_sum += carry_over
                carry_over = 0

            if digit_sum >= 10:
                carry_over = 1
                digit_sum = digit_sum - 10

            result.append(digit_sum)
            curr_node2 = curr_node2.next

    if carry_over != 0:
        result.append(carry_over)
        carry_over = 0

    result_list = ListNode(result[0])
    curr_node_result = result_list

    for i in range(1, len(result)):
        curr_node_result.next = ListNode(result[i])
        curr_node_result = curr_node_result.next

    return result


if __name__ == "__main__":
    num1 = ListNode(9)
    num1.next = ListNode(9)
    num1.next.next = ListNode(9)
    num1.next.next.next = ListNode(9)
    num1.next.next.next.next = ListNode(9)
    num1.next.next.next.next.next = ListNode(9)
    num1.next.next.next.next.next.next = ListNode(9)

    num2 = ListNode(9)
    num2.next = ListNode(9)
    num2.next.next = ListNode(9)
    num2.next.next.next = ListNode(9)


    print(addTwoNumbers(num1, num2))




