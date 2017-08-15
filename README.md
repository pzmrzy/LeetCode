### 1.[Two Sum](https://leetcode.com/problems/two-sum) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/two_sum.py) 

在dictionary里找有没有

### 2.[Add Two Numbers](https://leetcode.com/problems/add-two-numbers) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/add_two_number.py) 

对好位置加，注意最后一个进位

### 3.[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/longest_substring_without_repearing_characters.py) 

用两个指针，记录前后位置，用字典存现在已经有的字符，重了就删，更新结果

### 4.[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/median_of_two_sorted_arrays.py) 

把问题转换成找两个数组的第几个数，找的时候二分删一个数组的一半

### 5.[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) (https://leetcode.com/problems/longest-palindromic-substring/)[|python|] 

选一个位置为中点向两边拓展，可以跳掉连续重复的字符

### 6.[ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/zigzag_conversion.py)  

用字典存每个字符应该出现在第几行，然后顺着输出

### 7.[Reverse Integer](https://leetcode.com/problems/reverse-integer) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/reverse_integer.py) 

先判断正负，然后取mod加到list里输出，主要和2**32比

### 8.[String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/string_to_integer.py) 

先判断正负，不是0-9的break，用ord转成数

### 9.[Palindrome Number](https://leetcode.com/problems/palindrome-number)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/palindrome_number.py) 

转成字符串，到n/2长度头尾比

### 11.[Container With Most Water](https://leetcode.com/problems/container-with-most-water) [|cpp|](https://leetcode.com/problems/container-with-most-water/) 

头尾两个指针扫，两个的距离乘矮的是当前能装的最多的，下一次矮的往里移

### 12.[Integer to Roman](https://leetcode.com/problems/integer-to-roman) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/integer_to_roman.py) 

先对应好，从大到小，然后用公式

### 13.[Roman to Integer](https://leetcode.com/problems/roman-to-integer)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/roman_to_integer.py) 

先对应好，从左到右，小的减，大的加

### 14.[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/longest_common_prefix.py) 

先两个找，找好了跟第三个比

### 15.[3Sum](https://leetcode.com/problems/3sum)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/2Sum.py) 

先排序，确定一个，然后两个指针扫

### 16.[3Sum Closest](https://leetcode.com/problems/3sum-closest) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/3Sum_closest.py) 

先排序，确定一个，然后两个指针扫，再维护一个dif存最小的差

### 17.[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/letter_combinations_of_a_phone_number.py) 

对应好之后BFS

### 18.[4Sum](https://leetcode.com/problems/4sum)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/4sum.py) 

先排序，确定两个，两个指针扫后两个

### 19.[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/remove_nth_node_from_end_of_list.py) 

两个指针先让一个走n个，然后一起走，第一个到结尾第二个就是第倒数第n个

### 20.[Valid Parentheses](https://leetcode.com/problems/valid-parentheses)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/valid_parentheses.py) 

用栈，左括号进，又括号弹，然后看对称不对称

### 21.[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/merge_two_sorted_lists.py) 

用优先队列，key就是每个链表的第一个元素，pop完，删一个再放回去

### 22.[Generate Parentheses](https://leetcode.com/problems/generate-parentheses) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/generate_parentheses.py) 

用队列存当前状态第几个左括号和第几个右括号，bfs

### 23.[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/merge_k_sorted_lists.py) 

所有链表的头存在优先队列里，每次合并pop出来一个，并更新这个头位它的next

### 24.[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/swap_nodes_in_pairs.py) 

三个指针，第一个第二个换，第三个迭代

### 26.[Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/remove_duplicates_from_sorted_array.py) 

两个指针，前一个指向不重复的，如果有新的不重复的就拷贝的前面

### 27.[Remove Element](https://leetcode.com/problems/remove-element) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/remove_element.py) 

头尾两个指针，如果要删就换

### 28.[Implement strStr()](https://leetcode.com/problems/implement-strstr) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/implement_strstr.py) 

暴力求，或者kmp

### 29.[Divide Two Integers](https://leetcode.com/problems/divide-two-integers) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/divide_two_integers.py) 

减除数，结果和除数<<1，直到被除数小，注意0，无穷和正负的处理

### 31.[Next Permutation](https://leetcode.com/problems/next-permutation) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/next_permulation.py) 

找到第一个第一个比右边小的，先交换然后后面排序，注意最大的直接排序

### 32.[Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses)  

用栈存左括号位置，遇到右括号pop，存额外右括号的位置，最后遍历一遍栈，找相邻元素距离最大的位结果

### 33.[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array) 

二分，找有序的一边

### 34.[Search for a Range](https://leetcode.com/problems/search-for-a-range)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/search_for_a_range.py) 

二分查找开始和结束位置

### 35.[Search Insert Position](https://leetcode.com/problems/search-insert-position) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/search_insert_positon.py) 

二分

### 36.[Valid Sudoku ](https://leetcode.com/problems/valid-sudoku)[|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/valid_sudoku.py) 

直接按要求检查

### 37.[Sudoku Solver](https://leetcode.com/problems/sudoku-solver)  

先存所有空格位置，暴力递归

### 38.[Count and Say](https://leetcode.com/problems/count-and-say)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/count_and_say.py) 

按照规定读自己

### 39.[Combination Sum](https://leetcode.com/problems/combination-sum) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/combination_sum.py) 

BFS

### 40.[Combination Sum II](https://leetcode.com/problems/combination-sum-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/combination_sum_II.py) 

BFS且记录位置

### 41.[First Missing Positive](https://leetcode.com/problems/first-missing-positive) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/first_missing_positive.py) 

删掉0和大于n的，建图。。

### 42.[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/trapping_rain_water.py) 

正反扫两边，记录最左最右的最大值，每个位置是左边最高右边最高中小的减去高度

### 43.[Multiply Strings](https://leetcode.com/problems/multiply-strings)  

对每两位的乘积存到对应位置上，再做一遍进位

### 44.[Wildcard Matching](https://leetcode.com/problems/wildcard-matching) 

dp，根据每一位进行状态转移

### 46.[Permutations](https://leetcode.com/problems/permutations)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/permutations.py) 

BFS DFS

### 47.[Permutations II](https://leetcode.com/problems/permutations-ii)  

初始为空，每次插入一个数，如果要查的数和这个位置的数相同则break来去重

### 48.[Rotate Image](https://leetcode.com/problems/rotate-image)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/rotate_image.py) 

对应的四个点转，注意奇数时中间那列

### 49.[Group Anagrams](https://leetcode.com/problems/group-anagrams)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/group_anagrams.py) 

对每个字符串排序

### 50.[Pow(x, n)](https://leetcode.com/problems/powx-n)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/pow_x_n.py) 

算开方的，递归

### 51.[N-Queens](https://leetcode.com/problems/n-queens)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/NQueen.py) 

DFS，用一维数组存位置就够了

### 52.[N-Queens II](https://leetcode.com/problems/n-queens-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/NQueen_II.py) 

DFS，同上

### 53.[Maximum Subarray](https://leetcode.com/problems/maximum-subarray) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/maximum_subarray.py) 

求部分和，顺着找到目前位置最大的和最小的，差是结果，min-1

### 54.[Spiral Matrix](https://leetcode.com/problems/spiral-matrix)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/spiral_matrix.py) 

盲人探路

### 55.[Jump Game](https://leetcode.com/problems/jump-game)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/jump_game.py) 

如果能跳到n一定能到n-1倒着跳

### 56.[Merge Intervals](https://leetcode.com/problems/merge-intervals)  

按开始从小到大排序，如果有重合则更新当前区间结束点，否则在结果中增加当前区间

### 58.[Length of Last Word](https://leetcode.com/problems/length-of-last-word) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/length_of_last_word.py) 

split之后返回最后一个长度

### 59.[Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii)  [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/spiral_matrix_II.py) 

盲人探路

### 60.[Permutation Sequence](https://leetcode.com/problems/permutation-sequence) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/permutation_sequence.py) 

先求出来阶乘，然后挨个除，把对应的加进去

### 61.[Rotate List](https://leetcode.com/problems/rotate-list)  

找到尾以及链表长度，找到要转的位置，尾指向头成环，新的头为尾的下一个，尾下一个为空，切断环

### 62.[Unique Paths](https://leetcode.com/problems/unique-paths) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/unique_paths.py) 

dp，第一行1，每个格等于上面加左边

### 63.[Unique Paths II](https://leetcode.com/problems/unique-paths-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/unique_path_II.py) 

dp，先初始化第一行第一列，只要出现1后面都是0，中间的个如果是1是0，不然是左、上的和

### 64.[Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/minimum_path_sum.py) 

dp，初始化第一行，每个上面等于或左边最小的加自己

### 65.[Valid Number](https://leetcode.com/problems/valid-number) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/valid_number.py) 

慢慢写正则

### 66.[Plus One](https://leetcode.com/problems/plus-one) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/plus_one.py) 

先翻转顺着加一，再翻转

### 67.[Add Binary](https://leetcode.com/problems/add-binary) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/add_binary.py) 

先补齐，对位加，注意最后的进位

### 68.[Text Justification](https://leetcode.com/problems/text-justification) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/text_justification.py) 

好麻烦，各种情况想清楚

### 69.[Sqrt(x)](https://leetcode.com/problems/sqrtx) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/sqrt.py) 

二分

### 70.[Climbing Stairs](https://leetcode.com/problems/climbing-stairs) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/climging_stairs.cpp) 

dp，递推

### 71.[Simplify Path](https://leetcode.com/problems/simplify-path) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/simplify_path.py) 

栈，..弹栈，注意弹之前先判断size

### 72.[Edit Distance](https://leetcode.com/problems/edit-distance) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/edit_distance.py) 

dp，两个字符相等，直接等于前一个，否则是（前一个，删第一个，删第二个）中最小的+1

### 73.[Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/set_matrix_zeroes.py) 

每行的第一个做标记，然后再弄两个记第一行，最后都扫一遍

### 74.[Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/search_a_2D_matrix.py) 

相当于变成一维二分

### 75.[Sort Colors](https://leetcode.com/problems/sort-colors) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/sort_colors.py) 

三个指针，0和2换，0前面加一，2后面减一

### 76.[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/minimum_window_subtring.py) 

先统计，然后两个指针扫

### 77.[Combinations](https://leetcode.com/problems/combinations) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/combinations.py) 

dfs记录位置和个数

### 78.[Subsets](https://leetcode.com/problems/subsets) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/subsets.py) 

bfs

### 79.[Word Search](https://leetcode.com/problems/word-search) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/word_search.py) 

dfs回朔

### 80.[Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii)  

和I类似，如果比当前前两个数大，就拷贝过来

### 81.[Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii) 

。。。on比log的快

### 82.[Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii) 

dummy头指针，当前指针走到重复的最后一个，如果前一个指针的下个为当前指针则证明没重复，否则更新前一个指针跳掉当前指针

### 83.[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/remove_duplicates_from_sorted_list.py) 

等于next就删

### 84.[Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram)  

用栈存当前高度，如果比下一个高就pop，并算新的面积

### 86.[Partition List](https://leetcode.com/problems/partition-list) 

遍历一遍分成两个链表，最后再合并起来

### 87.[Scramble String](https://leetcode.com/problems/scramble-string) 

拿每个位置当根节点，递归

### 88.[Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/merge_sorted_array.py) 

一个数组一个指针，都从尾部开始，再一个指针放最后面，每次比大的放最后，最后把剩下的加进去

### 89.[Gray Code](https://leetcode.com/problems/gray-code) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/gray_code.py) 

弄了0和1，剩下的就reverse再在前面加

### 90.[Subsets II](https://leetcode.com/problems/subsets-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/subsets_II.py) 

相当于1，然后去重。。。正常应该是记录位置

### 91.[Decode Ways](https://leetcode.com/problems/decode-ways) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/decode_ways.py) 

dp注意整10 的情况，以及多个0

### 93.[Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/resore_ip_address.py) 

记录位置dfs

### 94.[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_inorder_traversal.py) 

dfs左根右

### 95.[Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii)  

枚举位置为根节点，递归求所有左右子树，再组合起来

### 96.[Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees) [|python|](unique_binary_search_trees.py) 

dp，每多一个数，结果为前面所有分着乘

### 98.[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/validate_binary_search_tree.py) 

递归检查左右子树，要传最大最小界

### 100.[Same Tree](https://leetcode.com/problems/same-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/same_tree.py)https://github.com/pzmrzy/LeetCode/blob/master/python/symmetric_tree.py 

递归左右子树

### 101.[Symmetric Tree](https://leetcode.com/problems/symmetric-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/symmetric_tree.py) 

递归比左右子树，注意none

### 102.[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_level_order_traversal.py) 

根为0，用字典存每层有哪个节点

### 103.[Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal)  

中序遍历树，字典存节点的层，根据奇偶正反序输出

### 104.[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/maximum_depth_of_binary_tree.cpp) 

dfs左右子树

### 105.[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/construct_binary_tree_from_inorder_preorder_traversal.py) 

不能传数组，算下标

### 106.[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/construct_binary_tree_from_inorder_postorder_traversal.py) 

同上

### 107.[Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/ 

和1一样，就输出的时候反着

### 108.[Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/covert_sorted_array_to_binary_search_tree.py) 

中间的当根，两边递归

### 109.[Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree)  

快慢指针找中点，中点为根，递归左右子树

### 110.[Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/balanced_binary_tree.py) 

递归，左右高度相等或者差1，且左右子树平衡

### 111.[Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/minimum_depth_of_binary_tree.py) 

bfs，找到叶节点结束

### 112.[Path Sum](https://leetcode.com/problems/path-sum) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/path_sum.py) 

bfs，搜到所有叶节点

### 113.[Path Sum II](https://leetcode.com/problems/path-sum-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/path_sum_II.py) 

bfs时要记录路径

### 118.[Pascal's Triangle](https://leetcode.com/problems/pascals-triangle) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/pascal_triangle.py) 

把上一行投影下来补0，从左到右等于自己加右边的

### 119.[Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/pascal_triangle_II.py) 

一样，就返回一行

### 120.[Triangle](https://leetcode.com/problems/triangle) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/triangle.py) 

dp倒着向上走，每次选小的加

### 121.[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/best_time_to_buy_and_sell_stoke.py) 

贪心扫一遍

### 122.[Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/best_time_to_buy_and_sell_stock_II.py) 

贪心，相当于每天都能买卖，只要赚就卖

### 123.[Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/best_time_to_buy_and_sell_stock_III.py) 

dp，找到两次买卖的时间

### 124.[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_maximum_path_sum.py) 

左边最大，右边最大，和经过root+左边最大+右边最大，注意全负数的情况，返回只返回从自己出发最大的以及和0比

### 125.[Valid Palindrome](https://leetcode.com/problems/valid-palindrome) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/valid_palindrome.py) 

正则把没用的删了，再判断

### 127.[Word Ladder](https://leetcode.com/problems/word-ladder) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/word_ladder.py) 

神奇的建图方法，剩下就bfs

### 128.[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/longest_consecutive_sequence.py) 

并查集

### 129.[Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/sum_root_to_leaf_numbers.py) 

dfs，传当前的值

### 134.[Gas Station](https://leetcode.com/problems/gas-station)  

如果总和大于cost一定有结果，从头模拟如果不行就从不行的节点当头

### 135.[Candy](https://leetcode.com/problems/candy) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/candy.py) 

贪心，先正着给，再反着给

### 136.[Single Number](https://leetcode.com/problems/single-number) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/single_numbers.py) 

xor一遍

### 139.[Word Break](https://leetcode.com/problems/word-break) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/word_break.py) 

db拆不拆

### 141.[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle)  

一个slow一个fast，有环一定能重合

### 144.[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_preorder_traversal.py) 

根左右

### 145.[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_postorder_traversal.py) 

左右根

### 146.[LRU Cache](https://leetcode.com/problems/lru-cache) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/lru_cache.py) 

字典存值，list存位置，每次写的时候都放到最后，满了删最前

### 151.[Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/reverse_words_in_a_string.py) 

先split，reverse，再join回去

### 153.[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/find_minimum_in_rotated_sorted_array.py) 

二分找最小的

### 154.[Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii)  

直接min最快。。。

### 155.[Min Stack](https://leetcode.com/problems/min-stack) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/min_stake.py) 

用list模拟

### 156.[Binary Tree Upside Down](https://leetcode.com/problems/binary-tree-upside-down) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_upside_down.py) 

左子树位右子树，父节点位右孩子，

### 157.[Read N Characters Given Read4](https://leetcode.com/problems/read-n-characters-given-read4) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/read_n_characters_given_read4.py) 

每次读，直到不够4个位置，为什么py不对

### 158.[Read N Characters Given Read4 II - Call multiple times](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/read_n_characters_given_read4_II.cpp) 

差不多py不行

### 159.[Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/longest_substring_with_at_most_two_distinct_characters.py) 

两个指针记录两个字符最前面的位置

### 160.[Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists)  

从两个指针的头开始，如果走到尾则换到另一个链表，直到两个指针相同，为交点

### 161.[One Edit Distance](https://leetcode.com/problems/one-edit-distance) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/one_edit_distance.py) 

相等是不是差一个字母，不相等长度差1，差一个字母

### 162.[Find Peak Element](https://leetcode.com/problems/find-peak-element) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/find_peak_element.py) 

扫一遍大于左右

### 163.[Missing Ranges](https://leetcode.com/problems/missing-ranges) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/missing_ranges.py) 

相等跳过，差一加一，否则输出，注意单个的

### 165.[Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/compare_version_numbers.py) 

split之后直接比

### 167.[Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/two_sum_II.py) 

确定一个二分第二个

### 168.[Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/excel_sheet_column_title.cpp) 

mod26

### 169.[Majority Element](https://leetcode.com/problems/majority-element) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/majority_element.py) 

count > n/2

### 170.[Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/two_sum_III.py) 

用字典存，查的时候on

### 171.[Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/excel_sheet_column_number.cpp) 

反过来

### 172.[Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/factorial_trailing_zeroes.cpp) 

删了。。。

### 173.[Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_search_tree_iterator.py) 

中序遍历放到数组里

### 179.[Largest Number](https://leetcode.com/problems/largest-number) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/largest_number.py) 

贪心，写一个比较函数

### 186.[Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/reverse_words_in_a_string_II.py) 

如果是空格翻转，最后一起再翻转

### 189.[Rotate Array](https://leetcode.com/problems/rotate-array) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/rotate_array.py) 

切片

### 190.[Reverse Bits](https://leetcode.com/problems/reverse-bits) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/reverse_bits.py) 

转二进制，zfill，翻转，再转回去

### 191.[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/number_of_1_bits.cpp) 

转二进制数

### 198.[House Robber](https://leetcode.com/problems/house-robber) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/house_robber.py) 

dp每个房间偷不偷

### 199.[Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_right_side_view.py) 

中序遍历，加一个level

### 200.[Number of Islands](https://leetcode.com/problems/number-of-islands) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/number_of_islands.py) 

dfs/bfs/并查集

### 202.[Happy Number](https://leetcode.com/problems/happy-number) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/happy_number.py) 

死循环到1或者重复

### 203.[Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/remove_linked_list_elements.py) 

dummy，等于就跳

### 204.[Count Primes](https://leetcode.com/problems/count-primes) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/count_primes.py) 

筛法，或者后面好多hint

### 205.[Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/isomorphic_strings) 

用dict，换线换一次看看是不是都行

### 206.[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/reverse_linked_list.py) 

每次tail向后一个

### 207.[Course Schedule](https://leetcode.com/problems/course-schedule) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/207.course_schedule.py) 

拓扑排序

### 208.[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/implement_Trie.py) 

字典树

### 210.[Course Schedule II](https://leetcode.com/problems/course-schedule-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/course_schedule_II.py) 

拓扑排序

### 213.[House Robber II](https://leetcode.com/problems/house-robber-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/house_robber_II.py) 

环可以变成两次dp，偷不偷最后一个

### 215.[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/kth_largest_element_in_an_array.py) 

每次找一个，大于小于的分治，注意shuffle

### 216.[Combination Sum III](https://leetcode.com/problems/combination-sum-iii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/combination_sum_III.py) 

bfs，放位置和剩余的

### 217.[Contains Duplicate](https://leetcode.com/problems/contains-duplicate) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/contains_duplicate.cpp) 

用set，一个新数in set就true

### 219.[Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/contains_duplicate_II.py) 

字典存每个数都出现在哪，每个数判断一下距离

### 223.[Rectangle Area](https://leetcode.com/problems/rectangle-area) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/rectangle_area.py) 

求交集然后减

### 224.[Basic Calculator](https://leetcode.com/problems/basic-calculator) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/basic_calculator.py) 

后缀表达式，栈空进栈，优先级高进展，否则弹出到比自己低的，自己再进栈

### 225.[Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/implement_stack_using_queue.py) 

数组模拟

### 226.[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/invert_binary_tree.py) 

先转子树，再交换孩子节点

### 227.[Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/basic_calculator_II.py) 

比1简单 没括号

### 228.[Summary Ranges](https://leetcode.com/problems/summary-ranges) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/summary_ranges.py) 

先加个-1，两个指针，有空了输出

### 229.[Majority Element II](https://leetcode.com/problems/majority-element-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/majority_element_II.py) 

count。。

### 230.[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/Kth_smallest_element_in_a_BST.py) 

中序遍历

### 231.[Power of Two](https://leetcode.com/problems/power-of-two) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/power_of_two.cpp) 

除log之后是不是整数

### 232.[Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/232.implement_queue_using_stack.py) 

数组模拟

### 233.[Number of Digit One](https://leetcode.com/problems/number-of-digit-one) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/number_of_digit_ones.py) 

考虑1出现在哪位，公式

### 234.[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/palindorome_linked_list.py) 

快慢指针先走到中点，然后翻转一半比

### 235.[Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/lowest_common_ancestor_of_a_binary_search_tree.py) 

先看会不会是根，不是往子树里找

### 236.[Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)  

如果根是其中一个子树或者空则返回，否则递归两个子树找lca，如果两边都不是空则为当前点，否则为非空子树的结果

### 237.[Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/delete_node_in_linked_list.py) 

遍历，等于就删

### 238.[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/product_of_array_except_selp.py) 

先正着扫，乘左边的，再反着扫乘右边的

### 239.[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/sliding_window_maximum.py) 

双向队列，删除超出的，且保持第一个永远最大

### 240.[Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/search_a_2d_matrix_II.py) 

右上角开始，向左下找

### 241.[Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses)  

遍历字符串如果是运算符则拆成两边递归，将两边的结果组合，如果不包含运算符则返回数字

### 242.[Valid Anagram](https://leetcode.com/problems/valid-anagram) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/valid_anagram.cpp) 

先排序，看看等不等

### 243.[Shortest Word Distance](https://leetcode.com/problems/shortest-word-distance) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/shortest_word_distance.py) 

两个指针扫两个单词，每次更新结果，开始给-1

### 244.[Shortest Word Distance II](https://leetcode.com/problems/shortest-word-distance-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/shortest_word_distance_II.py) 

用字典存每个单词的位置，然后遍历

### 245.[Shortest Word Distance III](https://leetcode.com/problems/shortest-word-distance-iii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/shortest_word_distance_III.py) 

和一一样，注意只有两个指针不等才更新

### 246.[Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/strobogrammatic_number.py) 

找好对应的，扫一半+1

### 249.[Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/group_shifted_strings.py) 

用两个字母的差当key，然后分组

### 250.[Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/count_univalue_subtrees.py) 

遍历的时候返回三个值，真：左边个数加右边个数+1，假：左右最大，以及自己的值

### 251.[Flatten 2D Vector](https://leetcode.com/problems/flatten-2d-vector) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/flatten_2D_vector.py) 

for一遍，虽然肯定要求不是这样的

### 252.[Meeting Rooms](https://leetcode.com/problems/meeting-rooms) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/meeting_rooms.py) 

排序完比

### 253.[Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/meeting_rooms_II.py) 

排序完用优先队列，新的进来如果比最小的有冲突就都加进去，max qsize是结果

### 254.[Factor Combinations](https://leetcode.com/problems/factor-combinations) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/factor_combinations.py) 

dfs，存结果，当前的，和从几开始

### 256.[Paint House](https://leetcode.com/problems/paint-house) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/paint_house.py) 

dp，rgb三个变量，每次取和自己不一样颜色里小的加自己的费用

### 257.[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_path.py) 

遍历的时候返回path

### 258.[Add Digits](https://leetcode.com/problems/add-digits) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/add_digits.cpp) 

mod 9的余数

### 259.[3Sum Smaller](https://leetcode.com/problems/3sum-smaller) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/three_sum_smaller.py) 

排序，确定一个扫另外两个

### 260.[Single Number III](https://leetcode.com/problems/single-number-iii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/single_number_III.py) 

xor之后找最后一个1，然后分成两组xor，两组的结果就是

### 261.[Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/graph_valid_tree.py) 

是不是n-1边，判断是不是连通的

### 263.[Ugly Number](https://leetcode.com/problems/ugly-number) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/ugly_num.py) 

不停除235之后看是不是1

### 266.[Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/palindrome_permutation.py) 

统计一遍个数，是不是只有最多一个奇数

### 268.[Missing Number](https://leetcode.com/problems/missing-number) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/missing_number.py) 

求和减一下

### 269.[Alien Dictionary](https://leetcode.com/problems/alien-dictionary) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/alien_dictionary.py) 

拓扑排序

### 270.[Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/closet_binary_search_tree_value.py) 

遍历时候和全局结果比

### 271.[Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/encode_and_decode_string.py) 

放每个字符串的长度，用#分开

### 272.[Closest Binary Search Tree Value II](https://leetcode.com/problems/closest-binary-search-tree-value-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/closest_binary_search_tree_value_II.py) 

中序遍历，然后两边往里加

### 273.[Integer to English Words](https://leetcode.com/problems/integer-to-english-words) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/integer_to_english_words.py) 

1到19先写好，写一个转1k以下的，然后多少b多少m多少k

### 274.[H-Index](https://leetcode.com/problems/h-index) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/H-index.py) 

记录每个citation有几篇文件，然后倒着扫

### 276.[Paint Fence](https://leetcode.com/problems/paint-fence) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/paint_fence.py) 

dp，same和dif两个变量

### 277.[Find the Celebrity](https://leetcode.com/problems/find-the-celebrity) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/find_the_celebrity.py) 

因为就一个找到可能的那个人，在判断一遍是不是符合条件

### 278.[First Bad Version](https://leetcode.com/problems/first-bad-version) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/first_bad_version.py) 

二分调api

### 279.[Perfect Squares](https://leetcode.com/problems/perfect-squares) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/perfect_squares.py) 

how to prove 4^k(8*m+7)????

### 280.[Wiggle Sort](https://leetcode.com/problems/wiggle-sort) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/wiggle_sort.cpp) 

on找中位数算法，k largerst ，cpp好省事

### 281.[Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/zigzag_iterator.py) 

先遍历了

### 283.[Move Zeroes](https://leetcode.com/problems/move-zeroes) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/move_zeroes.cpp) 

找到0删了，最后再加，或者直接换到后面

### 284.[Peeking Iterator](https://leetcode.com/problems/peeking-iterator)  

记录peek num

### 285.[Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/inorder_successor_in_BST.py) 

先中序遍历

### 286.[Walls and Gates](https://leetcode.com/problems/walls-and-gates) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/walls_and_gates.py) 

从门开始bfs

### 287.[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/find_the_duplicate_number.py) 

slow fast建图

### 288.[Unique Word Abbreviatio](https://leetcode.com/problems/unique-word-abbreviation) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/unique_word_abbreviation.py) 

建好判断是不是unique的

### 289.[Game of Life](https://leetcode.com/problems/game-of-life) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/game_of_life.py) 

模拟

### 290.[Word Pattern](https://leetcode.com/problems/word-pattern) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/word_pattern.py) 

对应pattern和单词，判断是不是冲突

### 292.[Nim Game](https://leetcode.com/problems/nim-game) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/nim_game.cpp) 

mod4

### 293.[Flip Game](https://leetcode.com/problems/flip-game) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/flip_game.py) 

顺着扫一遍所有可能的

### 294.[Flip Game II](https://leetcode.com/problems/flip-game-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/filp_game_II.py) 

借助前一个，用递归看看第一步是不是有一个能赢，

### 295.[Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream)  

两个优先队列，记录大数和小数，每加一个新数根据当前长度向其中一个放

### 296.[Best Meeting Point](https://leetcode.com/problems/best-meeting-point) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/best_meeting_point.cpp) 

每一个维度的中间点，还用找中位数算法

###297.[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree)  

前序遍历，#为None，空格分开

### 298.[Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_longest_consecutive_sequence.py) 



### 299.[Bulls and Cows](https://leetcode.com/problems/bulls-and-cows) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/bulls_and_cows.py) 

模拟

### 300.[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/longest_increasing_subsequence.py) 

最长递升子序列，log的dp

### 302.[Smallest Rectangle Enclosing Black Pixels](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/smallest_rectangle_enclosing_black_pixels.py) 

遍历每个点更新四个角，最后求面积

### 303.[Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/range_sum_query_immutable.cpp) 

部分和

### 305.[Number of Islands II](https://leetcode.com/problems/number-of-islands-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/number_of_islands_II.py) 

并查集

### 307.[Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/range_sum_query_mutable.py) 

树状数组

### 308.[Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/range_sum_query_2d_mutable.py) 

二维树状数组或者用部分和也能过

### 309.[Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown)  

dp，存前两天买或者卖的状态

### 310.[Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/minimum_height_tree.py) 

做两次bfs，根在第一次bfs最深的那个店

### 312.[Burst Balloons](https://leetcode.com/problems/burst-balloons) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/burst_balloons.py) 

dp，取一个扎，为乘积+左右两侧的

### 314.[Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_tree_vertical_order_traversal.py) 

bfs，根为0，左减又加，输出key最小到最大

### 318.[Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/maximum_product_of_word_lengths.py) 

26位mask，二维for一遍 然后and是0就算，注意加一个0，没有符合条件的情况

### 319.[Bulb Switcher](https://leetcode.com/problems/bulb-switcher) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/bulb_switcher.py) 

sqrt

### 320.[Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/generalized_abbreviation.py) 

dfs，记录位置

### 321.[Create Maximum Number](https://leetcode.com/problems/create-maximum-number)  

枚举每个里面取的个数，得到能取到的最大的，再merge

### 323.[Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/number_of_connected_components_in_an_undirected_graph.py) 

bfs

### 326.[Power of Three](https://leetcode.com/problems/power-of-three) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/power_of_three.cpp) 

和2一样

### 328.[Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/odd_even_linked_list.py) 

奇偶两个dummy，扫完了连起来

### 329.[Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix)  

first second两个，小更新，找到第三个

### 330.[Patching Array](https://leetcode.com/problems/patching-array) 

找出现miss的数，如果有比他小的，就加这个数，否则*2

### 334.[Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/increase_triplet_subsequence.py) 

存最小的两个，如果有新的比这两个大，则为真

### 337.[House Robber III](https://leetcode.com/problems/house-robber-iii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/house_robbrt_iii.py) 

如果抢，就dp下两层的，不抢就一层的，用负数表是是不是求过

### 338.[Counting Bits](https://leetcode.com/problems/counting-bits) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/counting_bits.py) 

2的n次方拓展

### 339.[Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/nested_list_wright_sum.cpp) 

求深度的的和函数互相调

### 341.[Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator)  

用栈存list和深度

### 342.[Power of Four](https://leetcode.com/problems/power-of-four) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/power_of_four.cpp) 

log

### 343.[Integer Break](https://leetcode.com/problems/integer-break) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/interger_break.py) 

拆3

### 344.[Reverse String](https://leetcode.com/problems/reverse-string) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/reverse_string.py) 

直接reverse

### 345.[Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/reverse_vowels_of_a_string.py) 

两个指针前后找元音，然后交换

### 346.[Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/moving_average_from_data_stream.py) 

每次重算了。。

### 347.[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/topk_frequent_element.py) 

字典然后排序

### 348.[Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/design_tic-tac-toe.py) 

模拟

### 349.[Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/intersection_of_two_arrays.py) 

取set求交

### 350.[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/intersection_of_two_array_ii.py) 

用字典统计个数，取小的

### 351.[Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/android_unlock_patterns.py) 

写好每个数能去哪个数 然后dfs

###354.[Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes)  

按x[0],-x[x]排序，二分

### 355.[Design Twitter](https://leetcode.com/problems/design-twitter) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/design_twitter.py) 

各种字典

### 356.[Line Reflection](https://leetcode.com/problems/line-reflection) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/line_reflection.py) 

去重，排序，找到中点，用一半对应另一半

### 357.[Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/count_numbers_with_unique_digits.py) 

0，10，81是两位的，最后一个*t-1是下一个的

### 359.[Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/logger_rate_limiter.py) 

用字典存时间

### 360.[Sort Transformed Array](https://leetcode.com/problems/sort-transformed-array) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/sort_transformed_array.py) 

判断二次项正负，两个指针，找绝对值大的加

### 362.[Design Hit Counter](https://leetcode.com/problems/design-hit-counter) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/design_hit_counter.py) 

用字典存序列

### 364.[Nested List Weight Sum II](https://leetcode.com/problems/nested-list-weight-sum-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/364.nested_list_weight_sum_II.py) 

dfs

### 365.[Water and Jug Problem](https://leetcode.com/problems/water-and-jug-problem) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/water_and_jug_problem.py) 

互质就可以

### 366.[Find Leaves of Binary Tree](https://leetcode.com/problems/find-leaves-of-binary-tree) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/find_leaves_of_binary_tree.py) 

dfs记录层数

### 367.[Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/valid_perfect_square.py) 

二分

### 368.[Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/largest_divisible_subset.py) 

dp，只用判断最大的能不能整除

### 369.[Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/plus_one_linked_list.py) 

找到一个不是9的加，后面变0，全是9直接变0

### 370.[Range Addition](https://leetcode.com/problems/range-addition) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/range_addition.py) 

左端点加，右断点减，最后统计

### 371.[Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers)  

位运算，mask，b的每一位给a

### 372.[Super Pow](https://leetcode.com/problems/super-pow) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/super_pow.py) 

先把0到9次方求了，然后每位算

### 373.[Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)  

优先队列存组合，找的时候j+1，到头再i+1

### 374.[Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/guess_number_higher_or_lower.py) 

二分猜

### 376.[Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/wiggle_subsequence.py) 

贪心扫

### 377.[Combination Sum IV](https://leetcode.com/problems/combination-sum-iv) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/combination_sum_IV.py) 

dfs

### 378.[Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/kth_smallest_element_in_sorted_matrix.py) 

优先队列

### 379.[Design Phone Directory](https://leetcode.com/problems/design-phone-directory) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/design_phone_dictionary.py) 

用字典

### 382.[Linked List Random Node](https://leetcode.com/problems/linked-list-random-node) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/linked_list_random_node.py) 

xx sampling随机算法

### 383.[Ransom Note](https://leetcode.com/problems/ransom-note) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/ransom_note.py) 

字典统计一次

### 384.[Shuffle an Array](https://leetcode.com/problems/shuffle-an-array) [|cpp|](https://github.com/pzmrzy/LeetCode/blob/master/cpp/384.shuffle_an_array.cpp) 

随机交换两个数

### 386.[Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers)  

存当前的数，根据情况对当前的数*10，+1，/10+1

### 387.[First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/first_unique_character_in_a_string.py) 

用字典扫一遍

### 388.[Longest Absolute File Path](https://leetcode.com/problems/longest-absolute-file-path)  

用字典存层数，如果是包含点则是文件，更新当前长度，否决存下一层

### 389.[Find the Difference](https://leetcode.com/problems/find-the-difference) 

两个字典比一下

### 390.[Elimination Game](https://leetcode.com/problems/elimination-game) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/elimination_game.py) 

每次找头在哪里

### 391.[Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle)  

存四个最外围的点，然后比总面积是不是为四个点包围的面积

### 392.[Is Subsequence](https://leetcode.com/problems/is-subsequence) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/is_subsequence.py) 

两个指针扫，相等下一个，不等找到相等的位置，如果不全 false

### 393.[UTF-8 Validation](https://leetcode.com/problems/utf-8-validation) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/UTF-8_validation.py) 

分类判断

### 394.[Decode String](https://leetcode.com/problems/decode-string)  

用栈存，设多个状态

### 396.[Rotate Function](https://leetcode.com/problems/rotate-function) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/rotate_function.py) 

推和上一项的关系

### 397.[Integer Replacement](https://leetcode.com/problems/integer-replacement) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/interger_replacement.py) 

往四的倍数走，注意最后3直接减除

### 398.[Random Pick Index](https://leetcode.com/problems/random-pick-index) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/random_pick_index.py) 

xx采样

### 399.[Evaluate Division](https://leetcode.com/problems/evaluate-division) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/evaluate_division.py) 

能除的建图 bfs

### 400.[Nth Digit](https://leetcode.com/problems/nth-digit)  

找到对应的数，在找到位置，对应的数每次减去 l（每次加一）*count（每次乘10）

### 401.[Binary Watch](https://leetcode.com/problems/binary-watch) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/binary_watch.py) 

确定小时 遍历分钟

### 402.[Remove K Digits](https://leetcode.com/problems/remove-k-digits) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/remove_K_digit.py) 

贪心，注意0

### 404.[Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/sum_of_left_leaves.py) 

dfs

### 405.[Convert a Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/convert_a_number_to_hexadecimal.py) 

负数+2**32

### 406.[Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/queue_reconstration_by_height.py) 

先按-x[0],x[1]排序，在p[1]插入p

### 408.[Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/valid_word_abbreviation.py) 

判断是不是

### 409.[Longest Palindrome](https://leetcode.com/problems/longest-palindrome) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/longest_palindrome.py) 

统计多少个是偶数次

### 411.[Minimum Unique Word Abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/minimum_unique_word_abbreviation.py) 

去掉长度不一样的，然后利用前面的生成，然后从最短的开始找

### 412.[Fizz Buzz](https://leetcode.com/problems/fizz-buzz) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/fizz_buzz.py) 

先mod15在mod5和3

### 413.[Arithmetic Slices](https://leetcode.com/problems/arithmetic-slices) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/arithmetic_slices.py) 

确定两个扫

### 414.[Third Maximum Number](https://leetcode.com/problems/third-maximum-number) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/third_maximim_number.py) 

冒泡三次

### 415.[Add Strings](https://leetcode.com/problems/add-strings) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/add_strings.py) 

按位加

### 416.[Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum)  

dp，能不能凑成一半，对每个数要或者不要

### 417.[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/pacific_atlantic_water_flow.py) 

两边bfs，求交集

### 419.[Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/battleships_in_a_board.py) 

一个x上面或者左边是点

### 421.[Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array)  

从最高位32位开始，每次结果左移一位，看对应位是1的，如果这些数有一个和1和当前结果xor是1，结果加1

### 422.[Valid Word Square](https://leetcode.com/problems/valid-word-square) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/valid_word_square.py) 

两层for判断

### 423.[Reconstruct Original Digits from English](https://leetcode.com/problems/reconstruct-original-digits-from-english) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/reconstruct_original_digits_from_english.py) 

找到每个数唯一的字母

### 424.[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement)  

用字典存每个字母出现的次数，对每个字符找到最左边的

### 425.[Word Squares](https://leetcode.com/problems/word-squares) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/word_squares.py) 

trie,dfs

### 434.[Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string)  

如果是空格状态为0字母为1，0的时候状态为1，结果+1

### 435.[Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals) 

按开始排序，扫一遍和前面比

### 437.[Path Sum III](https://leetcode.com/problems/path-sum-iii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/path_sum_III.py) 

dfs是不是从自己开始

### 438.[Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/find_all_anagrams_in_a_string.py) 

用一个字典存，遇到没用的字符跳

### 439.[Ternary Expression Parser](https://leetcode.com/problems/ternary-expression-parser) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/ternary_expression_parser.py) 

从后面开始，用栈

### 441.[Arranging Coins](https://leetcode.com/problems/arranging-coins)  

等差数列 [(sqrt(8n+1)-1)/2]

### 442.[Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array) 

用数组自己作为hash存哪个数之前出现过，第一次出现的数将对应位置变成负的

### 444.[Sequence Reconstruction](https://leetcode.com/problems/sequence-reconstruction) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/sequence_reconstruction.py) 

建图，拓扑排序

### 445.[Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/add_two_numbers_II.py) 

先存到数组里加

### 447.[Number of Boomerangs](https://leetcode.com/problems/number-of-boomerangs) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/number_of_boomeranges.py)

枚举中间的点，算距其他所有点的距离存到字典里，距离相同的点组成结果

### 448. [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/find_all_numbers_disappeared_in_an_array.py) 

用数组的index做hash，出现过则变成负数

### 449.[Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/serialize_and_deserialize_BST.py) 

序列化用前序遍历空格分开，恢复时用deque，递归建树

### 451.[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/sort_characters_by_frequency.py)

存到字典里按顺序输出

### 452.[Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/minimum_number_of_arrows_to_burst_balloons.py)

按横坐标排序，初始左右为正负无穷，对于不在范围里的气球，更新左右结果+1

### 453.[Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/minimum_moves_to_equal_array_elements.py)

数学，sum(num)-l*min(num)

### 454.[4Sum II](https://leetcode.com/problems/4sum-ii) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/4Sim_II.py)

把两个数组合并成一个，转换成2sum

### 455.[Assign Cookies](https://leetcode.com/problems/assign-cookies) [|python|](https://github.com/pzmrzy/LeetCode/blob/master/python/assign_cookie.py)

从小到大排序，从小的开始，如果能满足就给，不能就跳

### 456.[132 Pattern](https://leetcode.com/problems/132-pattern) [|python|]()



### 459.[Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern) [|python|]()



### 461. [Hamming Distance](https://leetcode.com/problems/hamming-distance) [|python|]()  



### 462.[Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii) [|python|]() 



### 463.[Island Perimeter](https://leetcode.com/problems/island-perimeter) [|python|]()



### 474.[Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes) [|python|]()



### 475.[Heaters](https://leetcode.com/problems/heaters) [|python|]()



### 476.[Number Complement](https://leetcode.com/problems/number-complement) [|python|]()



### 477.[Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance) [|python|]()



### 479.[Largest Palindrome Product](https://leetcode.com/problems/largest-palindrome-product) [|python|]()



### 481.[Magical String](https://leetcode.com/problems/magical-string) [|python|]()



### 482.[License Key Formatting](https://leetcode.com/problems/license-key-formatting) [|python|]()



### 485.[Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones) [|python|]()



### 486. [Predict the Winner](https://leetcode.com/problems/predict-the-winner) [|python|]()



### 491.[Increasing Subsequences](https://leetcode.com/problems/increasing-subsequences) [|python|]()



### 492.[Construct the Rectangle](https://leetcode.com/problems/construct-the-rectangle) [|python|]()



### 495.[Teemo Attacking](https://leetcode.com/problems/teemo-attacking) [|python|]()



### 496.[Next Greater Element I](https://leetcode.com/problems/next-greater-element-i)[|python|]() 



### 498.[Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse)[|python|]() 



### 500.[Keyboard Row](https://leetcode.com/problems/keyboard-row)[|python|]() 



### 501.[Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree) [|python|]()



###503.[Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii) [|python|]()

###504.[Base 7](https://leetcode.com/problems/base-7) [|python|]()

###506.[Relative Ranks](https://leetcode.com/problems/relative-ranks) [|python|]()

###507.[Perfect Number](https://leetcode.com/problems/perfect-number) [|python|]()

###508.[Most Frequent Subtree Su](https://leetcode.com/problems/most-frequent-subtree-sum) [|python|]()

###513.[Find Bottom Left Tree Value](https://leetcode.com/problems/find-bottom-left-tree-value) [|python|]()

###515.[Find Largest Value in Each Tree Row](https://leetcode.com/problems/find-largest-value-in-each-tree-row) [|python|]()

###516.[Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence) [|python|]()

###520.[Detect Capital](https://leetcode.com/problems/detect-capital) [|python|]()

###521.[Longest Uncommon Subsequence I](https://leetcode.com/problems/longest-uncommon-subsequence-i) [|python|]()

###524.[Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting) [|python|]()

###525.[Contiguous Array](https://leetcode.com/problems/contiguous-array) [|python|]()

###526.[Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement) [|python|]()

###529.[Minesweeper](https://leetcode.com/problems/minesweeper) [|python|]()

###530.[Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst) [|python|]()

###531.[Lonely Pixel I](https://leetcode.com/problems/lonely-pixel-i) [|python|]()

###532.[K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array) [|python|]()

###533.[Lonely Pixel II](https://leetcode.com/problems/lonely-pixel-ii) [|python|]()

###535.[Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl) [|python|]()

###536.[Construct Binary Tree from String](https://leetcode.com/problems/construct-binary-tree-from-string) [|python|]()

###537.[Complex Number Multiplication](https://leetcode.com/problems/complex-number-multiplication) [|python|]()

###538.[Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree) [|python|]()

###539.[Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference) [|python|]()

###540.[Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array) [|python|]()

###541.[Reverse String II](https://leetcode.com/problems/reverse-string-ii) [|python|]()

###543.[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree) [|python|]()

###547.[Friend Circles](https://leetcode.com/problems/friend-circles) [|python|]()

###551.[Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i) [|python|]()

###553.[Optimal Division](https://leetcode.com/problems/optimal-division) [|python|]()

###554.[Brick Wall](https://leetcode.com/problems/brick-wall) [|python|]()

###557.[Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii) [|python|]()

###560.[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k) [|python|]()

###561.[Array Partition I](https://leetcode.com/problems/array-partition-i) [|python|]()

###563.[Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt) [|python|]()

###565.[Array Nesting](https://leetcode.com/problems/array-nesting) [|python|]()

###566.[Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix) [|python|]()

###572.[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree) [|python|]()

###575.[Distribute Candies](https://leetcode.com/problems/distribute-candies) [|python|]()

###581.[Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray) [|python|]()

###582.[Kill Process](https://leetcode.com/problems/kill-process) [|python|]()

###583.[Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings) [|python|]()

###592.[Fraction Addition and Subtraction](https://leetcode.com/problems/fraction-addition-and-subtraction) [|python|]()

###593.[Valid Square](https://leetcode.com/problems/valid-square) [|python|]()

###594.[Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence) [|python|]()

###598.[Range Addition II](https://leetcode.com/problems/range-addition-ii) [|python|]()

###599.[Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists) [|python|]()

###605.[Can Place Flowers](https://leetcode.com/problems/can-place-flowers) [|python|]()

###606. [Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree) [|python|]()

###609.[Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system) [|python|]()

###611.[Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number) [|python|]()

###617.[Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees) [|python|]()

###621.[Task Scheduler](https://leetcode.com/problems/task-scheduler) [|python|]()

###623.[Add One Row to Tree](https://leetcode.com/problems/add-one-row-to-tree) [|python|]()

###628.[Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers) [|python|]()

###630.[Course Schedule III](https://leetcode.com/problems/course-schedule-iii) [|python|]()

###633.[Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers) [|python|]()

###635.[Design Log Storage System](https://leetcode.com/problems/design-log-storage-system) [|python|]()

###636.[Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions) [|python|]()

###637.[Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree) [|python|]()

###640.[Solve the Equation](https://leetcode.com/problems/solve-the-equation) [|python|]()

###643.[Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i) [|python|]()

###645.[Set Mismatch](https://leetcode.com/problems/set-mismatch) [|python|]()

###646.[Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain) [|python|]()

###647.[Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings) [|python|]()

###648.[Replace Words](https://leetcode.com/problems/replace-words) [|python|]()

###650.[2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard) [|python|]()

###652.[Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees) [|python|]()

###653.[Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst) [|python|]()

###654.[Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree) [|python|]()

###655.[Print Binary Tree](https://leetcode.com/problems/print-binary-tree) [|python|]()

###657.[Judge Route Circle](https://leetcode.com/problems/judge-route-circle) [|python|]()

###658.[Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements) [|python|]()

###659.[Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences) [|python|]()

###660.[Remove 9](https://leetcode.com/problems/remove-9) [|python|]()





