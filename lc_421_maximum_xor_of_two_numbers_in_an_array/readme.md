# [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

<span style="color:orange">Medium</span>

Given an integer array `nums`, return _the maximum result of_ `nums[i] XOR nums[j]`, where `0 ≤ i ≤ j < n`.

**Follow up:** Could you do this in O(_n_) runtime?

**Example 1:**

<pre>
<b>Input:</b> [3, 10, 5, 25, 2, 8]
<b>Output:</b> 28
<b>Explanation:</b> The maximum result is <b>5</b> ^ <b>25</b> = 28.
</pre>

**Example 2:**

<pre>
<b>Input:</b> [0]
<b>Output:</b> 0
</pre>

**Example 3:**

<pre>
<b>Input:</b> [2, 4]
<b>Output:</b> 6
</pre>

**Example 4:**

<pre>
<b>Input:</b> [8, 10, 2]
<b>Output:</b> 10
</pre>

**Example 5:**

<pre>
<b>Input:</b> [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
<b>Output:</b> 127
</pre>

**Constraints:**

-   1 ≤ nums.length ≤ 2 \* 10<sup>4</sup>
-   0 ≤ nums[i] ≤ 2<sup>31</sup> - 1

---

**Related Topics:** `Bit Manipulation` `Trie`
