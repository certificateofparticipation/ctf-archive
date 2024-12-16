#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> dp;

int knap(vector<int>& nums, int n, int W) {
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= W; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            } else if (nums[i - 1] > j) {
                dp[i][j] = dp[i - 1][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], nums[i - 1] + dp[i - 1][j - nums[i - 1]]);
            }
        }
    }
    return dp[n][W];
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;

        vector<int> cals(n);
        int sum = 0;

        for (int i = 0; i < n; i++) {
            cin >> cals[i];
            sum += cals[i];
        }

        dp.assign(n + 1, vector<int>(sum / 2 + 1, 0));

        int lamb = knap(cals, n, sum / 2);
        int wolf = sum - lamb;

        cout << lamb << " " << wolf << endl;
    }

    return 0;
}