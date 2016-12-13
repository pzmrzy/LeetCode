### Two Sum

在dictionary里找有没有

### Add Two Numbers

对好位置加，注意最后一个进位

### Longest Substring Without Repeating Characters

用两个指针，记录前后位置，用字典存现在已经有的字符，重了就删，更新结果

### Median of Two Sorted Arrays

把问题转换成找两个数组的第几个数，找的时候二分删一个数组的一半

### ZigZag Conversion

用字典存每个字符应该出现在第几行，然后顺着输出

### Reverse Integer

先判断正负，然后取mod加到list里输出，主要和2**32比

### String to Integer (atoi)

先判断正负，不是0-9的break，用ord转成数

### Palindrome Number

转成字符串，到n/2长度头尾比

### Container With Most Water

头尾两个指针扫，两个的距离乘矮的是当前能装的最多的，下一次矮的往里移

### Integer to Roman

先对应好，从大到小，然后用公式

### Roman to Integer

先对应好，从左到右，小的减，大的加

### Longest Common Prefix

先两个找，找好了跟第三个比

### 3Sum

先排序，确定一个，然后两个指针扫

### 3Sum Closest

先排序，确定一个，然后两个指针扫，再维护一个dif存最小的差

### Letter Combinations of a Phone Number

对应好之后BFS

### 4Sum

先排序，确定两个，两个指针扫后两个

### Remove Nth Node From End of List

两个指针先让一个走n个，然后一起走，第一个到结尾第二个就是第倒数第n个

### Valid Parentheses

用栈，左括号进，又括号弹，然后看对称不对称

### Merge k Sorted Lists

用优先队列，key就是每个链表的第一个元素，pop完，删一个再放回去

### Swap Nodes in Pairs

三个指针，第一个第二个换，第三个迭代

### Remove Duplicates from Sorted Array

### Remove Element

头尾两个指针，如果要删就换

### Next Permutation

找到第一个第一个比右边小的，先交换然后后面排序，注意最大的直接排序

### Search in Rotated Sorted Array

二分，找有序的一边

### Search Insert Position

二分

### Valid Sudoku

直接按要求检查

### Count and Say

按照规定读自己

### Combination Sum |python|

BFS

### Combination Sum II |python|

BFS且记录位置

### First Missing Positive |python|

删掉0和大于n的，建图。。

### Trapping Rain Water |python|

正反扫两边，记录最左最右的最大值，每个位置是左边最高右边最高中小的减去高度

### Permutations |python|

BFS DFS

### Rotate Image |python|

对应的四个点转，注意奇数时中间那列

### Group Anagrams |python|

对每个字符串排序

### Pow(x, n) |python|

算开方的，递归

### N-Queens |python|

DFS，用一维数组存位置就够了

### N-Queens II |python|

DFS，同上

### Maximum Subarray |python|

求部分和，顺着找到目前位置最大的和最小的，差是结果，min-1

### Spiral Matrix |python|

盲人探路

### Jump Game |python|

如果能跳到n一定能到n-1倒着跳

### Length of Last Word |python|

split之后返回最后一个长度

### Spiral Matrix II |python|

盲人探路

### Permutation Sequence |python|

先求出来阶乘，然后挨个除，把对应的加进去

### Unique Paths |python|

dp，第一行1，每个格等于上面加左边

### Unique Paths II |python|

dp，先初始化第一行第一列，只要出现1后面都是0，中间的个如果是1是0，不然是左、上的和

### Minimum Path Sum |python|

dp，初始化第一行，每个上面等于或左边最小的加自己

### Valid Number |python|

慢慢写正则

### Plus One |python|

先翻转顺着加一，再翻转

### Add Binary |python|

先补齐，对位加，注意最后的进位

### Text Justification |python|

好麻烦，各种情况想清楚

### Sqrt(x) |python|

二分

### Climbing Stairs |python|

dp，递推

### Simplify Path |python|

栈，..弹栈，注意弹之前先判断size

### Edit Distance |python|

dp，两个字符相等，直接等于前一个，否则是（前一个，删第一个，删第二个）中最小的+1

### Set Matrix Zeroes |python|

每行的第一个做标记，然后再弄两个记第一行，最后都扫一遍

### Search a 2D Matrix |python|

相当于变成一维二分

### Sort Colors |python|

三个指针，0和2换，0前面加一，2后面减一

### Minimum Window Substring |python|

先统计，然后两个指针扫

### Combinations |python|

dfs记录位置和个数

### Subsets |python|

bfs

### Word Search |python|

dfs回朔

### Search in Rotated Sorted Array II

。。。on比log的快

### Remove Duplicates from Sorted List |python|

等于next就删

### Merge Sorted Array |python|

一个数组一个指针，都从尾部开始，再一个指针放最后面，每次比大的放最后，最后把剩下的加进去

### Gray Code |python|

弄了0和1，剩下的就reverse再在前面加

### Subsets II |python|

相当于1，然后去重。。。正常应该是记录位置

### Decode Ways |python|

dp注意整10 的情况，以及多个0

### Restore IP Addresses |python|

记录位置dfs

### Binary Tree Inorder Traversal |python|

dfs左根右

### Unique Binary Search Trees |python|

dp，每多一个数，结果为前面所有分着乘

### Validate Binary Search Tree |python|

递归检查左右子树，要传最大最小界

### Same Tree |python|

递归左右子树

### Symmetric Tree |python|

递归比左右子树，注意none

### Binary Tree Level Order Traversal |python|

根为0，用字典存每层有哪个节点

### Maximum Depth of Binary Tree |python|

dfs左右子树

### Construct Binary Tree from Preorder and Inorder Traversal |python|

不能传数组，算下标

### Construct Binary Tree from Inorder and Postorder Traversal |python|

同上

### Binary Tree Level Order Traversal II |python|

和1一样，就输出的时候反着

### Convert Sorted Array to Binary Search Tree |python|

中间的当根，两边递归

### Balanced Binary Tree |python|

递归，左右高度相等或者差1，且左右子树平衡

### Minimum Depth of Binary Tree |python|

bfs，找到叶节点结束

### Path Sum |python|

bfs，搜到所有叶节点

### Path Sum II |python|

bfs时要记录路径

### Pascal's Triangle |python|

把上一行投影下来补0，从左到右等于自己加右边的

### Pascal's Triangle II |python|

一样，就返回一行

### Triangle |python|

dp倒着向上走，每次选小的加

### Best Time to Buy and Sell Stock |python|

贪心扫一遍

### Best Time to Buy and Sell Stock II |python|

贪心，相当于每天都能买卖，只要赚就卖

### Best Time to Buy and Sell Stock III |python|

dp，找到两次买卖的时间

### Binary Tree Maximum Path Sum |python|

左边最大，右边最大，和经过root+左边最大+右边最大，注意全负数的情况，返回只返回从自己出发最大的以及和0比

### Valid Palindrome |python|

正则把没用的删了，再判断

### Word Ladder |python|

神奇的建图方法，剩下就bfs

### Longest Consecutive Sequence |python|

并查集

### Sum Root to Leaf Numbers |python|

dfs，传当前的值

### Linked List Cycle |python|

一个slow一个fast，有环一定能重合

### Candy |python|

贪心，先正着给，再反着给

### Single Number |python|

xor一遍

### Word Break |python|

db拆不拆

### Binary Tree Preorder Traversal |python|

根左右

### Binary Tree Postorder Traversal |python|

左右根

### LRU Cache |python|

字典存值，list存位置，每次写的时候都放到最后，满了删最前

### Reverse Words in a String |python|

先split，reverse，再join回去

### Find Minimum in Rotated Sorted Array |python|

二分找最小的

### Find Minimum in Rotated Sorted Array II

直接min最快。。。

### Min Stack |python|

用list模拟

### Binary Tree Upside Down |python|

左子树位右子树，父节点位右孩子，

### Read N Characters Given Read4 |python|

每次读，直到不够4个位置，为什么py不对

### Read N Characters Given Read4 II - Call multiple times |python|

差不多py不行

### Longest Substring with At Most Two Distinct Characters |python|

两个指针记录两个字符最前面的位置

### One Edit Distance |python|

相等是不是差一个字母，不相等长度差1，差一个字母

### Find Peak Element |python|

扫一遍大于左右

### Missing Ranges |python|

相等跳过，差一加一，否则输出，注意单个的

### Compare Version Numbers |python|

split之后直接比

### Two Sum II - Input array is sorted |python|

确定一个二分第二个

### Excel Sheet Column Title |python|

mod26

### Majority Element |python|

count > n/2

### Two Sum III - Data structure design |python|

用字典存，查的时候on

### Excel Sheet Column Number |python|

反过来

### Factorial Trailing Zeroes |python|

删了。。。

### Binary Search Tree Iterator |python|

中序遍历放到数组里

### Largest Number |python|

贪心，写一个比较函数

### Reverse Words in a String II |python|

如果是空格翻转，最后一起再翻转

### Rotate Array |python|

切片

### Reverse Bits |python|

转二进制，zfill，翻转，再转回去

### Number of 1 Bits |python|

转二进制数

### House Robber |python|

dp每个房间偷不偷

### Binary Tree Right Side View |python|

中序遍历，加一个level

### Number of Islands |python|

dfs/bfs/并查集

### Happy Number |python|

死循环到1或者重复

### Remove Linked List Elements |python|

dummy，等于就跳

### Count Primes |python|

筛法，或者后面好多hint

### Isomorphic Strings |python|

用dict，换线换一次看看是不是都行

### Reverse Linked List |python|

每次tail向后一个

### Course Schedule |python|

拓扑排序

### Implement Trie (Prefix Tree) |python|

字典树

### Course Schedule II |python|

拓扑排序

### House Robber II |python|

环可以变成两次dp，偷不偷最后一个

### Kth Largest Element in an Array |python|

每次找一个，大于小于的分治，注意shuffle

### Combination Sum III |python|

bfs，放位置和剩余的

### Contains Duplicate |python|

用set，一个新数in set就true

### Contains Duplicate II |python|

字典存每个数都出现在哪，每个数判断一下距离

### Rectangle Area |python|

求交集然后减

### Basic Calculator |python|

后缀表达式，栈空进栈，优先级高进展，否则弹出到比自己低的，自己再进栈

### Implement Stack using Queues |python|

数组模拟

### Invert Binary Tree |python|

先转子树，再交换孩子节点

### Basic Calculator II |python|

比1简单 没括号

### Summary Ranges |python|

先加个-1，两个指针，有空了输出

### Majority Element II |python|

count。。

### Kth Smallest Element in a BST |python|

中序遍历

### Power of Two |python|

除log之后是不是整数

### Implement Queue using Stacks |python|

数组模拟

### Number of Digit One |python|

考虑1出现在哪位，公式

### Palindrome Linked List |python|

快慢指针先走到中点，然后翻转一半比

### Lowest Common Ancestor of a Binary Search Tree |python|

先看会不会是根，不是往子树里找

### Delete Node in a Linked List |python|

遍历，等于就删

### !!!Product of Array Except Self |python|

先正着扫，乘左边的，再反着扫乘右边的

### Sliding Window Maximum |python|

双向队列，删除超出的，且保持第一个永远最大

### Search a 2D Matrix II |python|

右上角开始，向左下找

### Valid Anagram |python|

先排序，看看等不等

### Shortest Word Distance |python|

两个指针扫两个单词，每次更新结果，开始给-1

### Shortest Word Distance II |python|

用字典存每个单词的位置，然后遍历

### Shortest Word Distance III |python|

和一一样，注意只有两个指针不等才更新

### Strobogrammatic Number |python|

找好对应的，扫一半+1

### Group Shifted Strings |python|

用两个字母的差当key，然后分组

### Count Univalue Subtrees |python|

遍历的时候返回三个值，真：左边个数加右边个数+1，假：左右最大，以及自己的值

### Flatten 2D Vector |python|

for一遍，虽然肯定要求不是这样的

### Meeting Rooms |python|

排序完比

### Meeting Rooms II |python|

排序完用优先队列，新的进来如果比最小的有冲突就都加进去，max qsize是结果

### Factor Combinations |python|

dfs，存结果，当前的，和从几开始

### Paint House |python|

dp，rgb三个变量，每次取和自己不一样颜色里小的加自己的费用

### Binary Tree Paths |python|

遍历的时候返回path

### Add Digits |python|

mod 9的余数

### 3Sum Smaller |python|

排序，确定一个扫另外两个

### Single Number III |python|

xor之后找最后一个1，然后分成两组xor，两组的结果就是

### Graph Valid Tree |python|

是不是n-1边，判断是不是连通的

### Ugly Number |python|

不停除235之后看是不是1

### Palindrome Permutation |python|

统计一遍个数，是不是只有最多一个奇数

### Missing Number |python|

求和减一下

### Alien Dictionary |python|

拓扑排序

### Closest Binary Search Tree Value |python|

遍历时候和全局结果比

### Encode and Decode Strings |python|

放每个字符串的长度，用#分开

### Closest Binary Search Tree Value II |python|

中序遍历，然后两边往里加

### Integer to English Words |python|

1到19先写好，写一个转1k以下的，然后多少b多少m多少k

### H-Index |python|

记录每个citation有几篇文件，然后倒着扫

### Paint Fence |python|

dp，same和dif两个变量

### Find the Celebrity |python|

因为就一个找到可能的那个人，在判断一遍是不是符合条件

### First Bad Version |python|

二分调api

### how to prove 4^k(8*m+7)????Perfect Squares |python|

rt

### Wiggle Sort |python|

on找中位数算法，k largerst ，cpp好省事

### Zigzag Iterator |python|

先遍历了

### Move Zeores |python|

找到0删了，最后再加，或者直接换到后面

### Inorder Successor in BST |python|

先中序遍历

### Walls and Gates |python|

从门开始bfs

### Find the Duplicate Number |python|

slow fast建图

### Unique Word Abbreviation |python|

建好判断是不是unique的

### Game of Life |python|

模拟

### Word Pattern |python|

对应pattern和单词，判断是不是冲突

### Nim Game |python|

mod4

### Flip Game |python|

顺着扫一遍所有可能的

### Flip Game II |python|

借助前一个，用递归看看第一步是不是有一个能赢，

### Best Meeting Point |python|

每一个维度的中间点，还用找中位数算法

### Binary Tree Longest Consecutive Sequence |python|



### Bulls and Cows |python|

模拟

### Longest Increasing Subsequence |python|

最长递升子序列，log的dp

### Smallest Rectangle Enclosing Black Pixels |python|



### Range Sum Query - Immutable |python|

部分和

### Number of Islands II |python|

并查集

### Range Sum Query - Mutable |python|

树状数组

### Range Sum Query 2D - Mutable |python|

二维树状数组或者用部分和也能过

### Minimum Height Trees |python|

做两次bfs，根在第一次bfs最深的那个店

### Burst Balloons |python|

dp，取一个扎，为乘积+左右两侧的

### Binary Tree Vertical Order Traversal |python|

bfs，根为0，左减又加，输出key最小到最大

### Maximum Product of Word Lengths |python|

26位mask，二维for一遍 然后and是0就算，注意加一个0，没有符合条件的情况

### Bulb Switcher |python|

sqrt

### Generalized Abbreviation |python|

dfs，记录位置

### Number of Connected Components in an Undirected Graph |python|

bfs

### Power of Three |python|

和2一样

### Odd Even Linked List |python|

奇偶两个dummy，扫完了连起来

### Increasing Triplet Subsequence |python|

first second两个，小更新，找到第三个

### House Robber III |python|

如果抢，就dp下两层的，不抢就一层的，用负数表是是不是求过

### Counting Bits |python|

2的n次方拓展

### Nested List Weight Sum |python|

求深度的的和函数互相调

### Power of Four |python|

log

### Integer Break |python|

拆3

### Reverse String |python|

直接reverse

### Reverse Vowels of a String |python|

两个指针前后找元音，然后交换

### Moving Average from Data Stream |python|

每次重算了。。

### Top K Frequent Elements |python|

字典然后排序

### Design Tic-Tac-Toe |python|

模拟

### Intersection of Two Arrays |python|

取set求交

### Intersection of Two Arrays II |python|

用字典统计个数，取小的

### Android Unlock Patterns |python|

写好每个数能去哪个数 然后dfs

### Design Twitter |python|

各种字典

### Line Reflection |python|

去重，排序，找到中点，用一半对应另一半

### Count Numbers with Unique Digits |python|

0，10，81是两位的，最后一个*t-1是下一个的

### Logger Rate Limiter |python|

用字典存时间

### Sort Transformed Array |python|

判断二次项正负，两个指针，找绝对值大的加

### Design Hit Counter |python|

用字典存序列

### Nested List Weight Sum II |python|

dfs

### Water and Jug Problem |python|

互质就可以

### Find Leaves of Binary Tree |python|

dfs记录层数

### Valid Perfect Square |python|

二分

### Largest Divisible Subset |python|

dp，只用判断最大的能不能整除

### Plus One Linked List |python|

找到一个不是9的加，后面变0，全是9直接变0

### Range Addition |python|

左端点加，右断点减，最后统计

### Super Pow |python|

先把0到9次方求了，然后每位算

### Guess Number Higher or Lower |python|

二分猜

### Wiggle Subsequence |python|

贪心扫

### Combination Sum IV |python|

dfs

### Kth Smallest Element in a Sorted Matrix |python|

优先队列

### Design Phone Directory |python|

用字典

### Linked List Random Node |python|

xx sampling随机算法

### Ransom Note |python|

字典统计一次

### Shuffle an Array |python|

随机交换两个数

### First Unique Character in a String |python|

用字典扫一遍

### Find the Difference |python|

两个字典比一下

### Elimination Game |python|

每次找头在哪里

### Is Subsequence |python|

两个指针扫，相等下一个，不等找到相等的位置，如果不全 false

### UTF-8 Validation |python|

分类判断

### Rotate Function |python|

推和上一项的关系

### Integer Replacement |python|

往四的倍数走，注意最后3直接减除

### Random Pick Index |python|

xx采样

### Evaluate Division |python|

能除的建图 bfs

### Binary Watch |python|

确定小时 遍历分钟

### Remove K Digits |python|

贪心，注意0

### Sum of Left Leaves |python|

dfs

### Convert a Number to Hexadecimal |python|

负数+2**32

### Queue Reconstruction by Height |python|

### Valid Word Abbreviation |python|

判断是不是

### Longest Palindrome |python|

统计多少个是偶数次

### Minimum Unique Word Abbreviation |python|

去掉长度不一样的，然后利用前面的生成，然后从最短的开始找

### Fizz Buzz |python|

先mod15在mod5和3

### Arithmetic Slices |python|

确定两个扫

### Third Maximum Number |python|

冒泡三次

### Add Strings |python|

按位加

### Pacific Atlantic Water Flow |python|

两边bfs，求交集

### Battleships in a Board |python|

一个x上面或者左边是点

### Valid Word Square |python|

两层for判断

### Reconstruct Original Digits from English |python|

找到每个数唯一的字母

### Word Squares |python|

trie,dfs

### Path Sum III |python|

dfs是不是从自己开始

### Find All Anagrams in a String |python|

用一个字典存，遇到没用的字符跳

### Ternary Expression Parser |python|

从后面开始，用栈

### Sequence Reconstruction |python|

建图，拓扑排序