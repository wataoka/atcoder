int a[100];
int n, k;

bool dfs(int i, int sum) {
    if (i == n) return sum == k;
    if (dfs(i+1, sum)) return true;
    return false;
}
