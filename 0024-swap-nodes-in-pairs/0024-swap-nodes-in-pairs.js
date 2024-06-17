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
    let dummy = new ListNode(0);
    dummy.next = head;
    let prev = dummy;

    while(prev.next !== null && prev.next.next !== null){
        // Nodes to swap
        let first = prev.next;
        let second = prev.next.next;

        // Swapping nodes
        prev.next = second;
        first.next = second.next;
        second.next = first;

        prev = first;
    }
    return dummy.next;
};