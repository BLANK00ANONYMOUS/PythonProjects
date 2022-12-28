class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> pq;
        for (int pile: piles) pq.push(pile);

        for (int i = 0; i < k; ++i) {
            int temp = pq.top();
            pq.pop();
            int rem = temp / 2;
            temp -= rem;
            pq.push(temp);
        }
        int res = 0;
        while (!pq.empty()) {
            res += pq.top();
            pq.pop();
        }
        return res;
    }
};