#include <iostream>
#include <string>
#include <unordered_map>

std::unordered_map<int, std::string> words() {
    std::unordered_map<int, std::string> numWords;
    numWords[0] = "";
    numWords[10] = "ten";
    numWords[20] = "twenty";
    numWords[30] = "thirty";
    numWords[40] = "forty";
    numWords[50] = "fifty";
    numWords[60] = "sixty";
    numWords[70] = "seventy";
    numWords[80] = "eighty";
    numWords[90] = "ninety";

    numWords[11] = "eleven";
    numWords[12] = "twelve";
    numWords[13] = "thirteen";
    numWords[14] = "fourteen";
    numWords[15] = "fifteen";
    numWords[16] = "sixteen";
    numWords[17] = "seventeen";
    numWords[18] = "eighteen";
    numWords[19] = "nineteen";

    numWords[100] = "onehundred";
    numWords[200] = "twohundred";
    numWords[300] = "threehundred";
    numWords[400] = "fourhundred";
    numWords[500] = "fivehundred";
    numWords[600] = "sixhundred";
    numWords[700] = "sevenhundred";
    numWords[800] = "eighthundred";
    numWords[900] = "ninehundred";

    numWords[0] = "";
    numWords[1] = "one";
    numWords[2] = "two";
    numWords[3] = "three";
    numWords[4] = "four";
    numWords[5] = "five";
    numWords[6] = "six";
    numWords[7] = "seven";
    numWords[8] = "eight";
    numWords[9] = "nine";
    return numWords;
}

std::vector<int> placeVals(int n) {
    std::vector<int> num;
    int p = 10; 

    while (n > 0) {
        int l = n % p;
        n -= l;
        p *= 10;
        num.push_back(l);
    }

    return num;
}

int main() {
    std::unordered_map<int, std::string> numWords = words();

    int letters = 0;
    std::string numString;

    for (int i = 1; i < 1000; i++) {
        int teen = i % 100;
        int sub = 0;
        
        if (teen > 10 && teen < 20) {
            numString += numWords.at(teen);
            sub = teen;
        }

        std::vector<int> num = placeVals(i - sub);
        for (int n = 0; n < num.size(); n++) {
            if (num[n] >= 100 && teen > 0) numString += "and";
            numString += numWords.at(num[n]);
        }

        letters += numString.length();
        numString = "";
    }
    letters += 11; // onethousand
    std::cout << letters << std::endl;
}