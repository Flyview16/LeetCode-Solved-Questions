/**
 * @param {number[]} nums
 * @return {number}
 */
var duplicateNumbersXOR = function (nums) {
    seen = new Set();
    let xor_result = 0;

    for (let num of nums) {
        if (seen.has(num)) {
            xor_result ^= num;
        }
        else {
            seen.add(num);
        }
    }
    return xor_result;
};