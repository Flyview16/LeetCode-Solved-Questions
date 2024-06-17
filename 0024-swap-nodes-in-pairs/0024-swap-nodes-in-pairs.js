/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
     if(!head || !head.next) return head;

    let left = head;
    let right = head.next;
    let prevRight = null;
    let nextLeft = null;

    while(left && right) {
        if(left === head) head = right;
        if(prevRight) prevRight.next = right;

        nextLeft = right.next;
        right.next = left;
        left.next = nextLeft;
        prevRight = left;
        left = nextLeft;
        right = left?.next;
    }
    return head;
};