#include <iostream>
#include <vector>
#include <set>
using namespace std;

vector<vector<int>> partitions(int n, int maxValue, set<int>& coins) {
    if (maxValue == 0) {
        maxValue = n;
    }

    if (n == 0) {
        vector<vector<int>> baseCase;
        return baseCase;
    }
    
    vector<vector<int>> result;
    
    for (int i = min(n, maxValue); i > 0; i--) {
        if (coins.find(i) != coins.end()) {
            for (vector<int>& partition : partitions(n - i, i, coins)) {
                vector<int> newPartition;
                newPartition.push_back(i);
                for (int elem: partition) newPartition.push_back(elem);
                // newPartition.insert(newPartition.end(), partition.begin(), partition.end());
                result.push_back(newPartition);
            }
        }
    }

    return result;
}

int main() {

    set<int> coins;
    coins.insert(200);
    coins.insert(100);
    coins.insert(50);
    coins.insert(20);
    coins.insert(10);
    coins.insert(5);
    coins.insert(2);
    coins.insert(1);

    int n = 200;
    vector<vector<int>> result = partitions(n,0,coins);
    cout << result.size() << endl;

}