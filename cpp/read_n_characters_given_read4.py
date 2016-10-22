// Forward declaration of the read4 API.
int read4(char *buf);

class Solution {
public:
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int res = 0;
        while (res < n){
            int t = read4(buf);
            res += t;
            if (t < 4)
                break;
            buf += 4;
        }
        return min(res, n);
    }
};
