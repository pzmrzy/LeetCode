#include <algorithm>
class Solution {
public:
    int minTotalDistance(vector<vector<int>>& grid) {
        vector<int> x;
        vector<int> y;
        int m = grid.size();
        int n = grid[0].size();
        int tot = 0;
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if (grid[i][j] == 1){
                    tot += 1;
                    x.push_back(i);
                    y.push_back(j);
                }
            }
        }
        int med = tot / 2;
        //nth_element(x.begin(), x.begin() + med, x.end());
        nth_element(y.begin(), y.begin() + med, y.end());
        int midx = x[med];
        int midy = y[med];
        int res = 0;
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if (grid[i][j] == 1){
                    res += abs(midx - i) + abs(midy - j);
                }
            }
        }
        return res;
    }
};
