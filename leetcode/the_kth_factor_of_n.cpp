// https://leetcode.com/problems/the-kth-factor-of-n

class Solution
{
  public:
    int kthFactor(int n, int k)
    {
        int c = 0;

        for (int i = 1; i <= n; ++i) {
            if (n % i == 0 and --k == 0)
                return i;
        }

        return -1;
    }
};