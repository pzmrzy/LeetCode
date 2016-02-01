/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        if ((!root->left) && (!root->right)) return 1;
        int ml = root->left ? maxDepth(root->left):1;
        int mr = root->right ? maxDepth(root->right):1;
        return max(ml, mr) + 1;
    }
    int max(int x, int y){
        return x > y ? x: y;
    }
};
