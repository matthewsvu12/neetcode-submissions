class Solution {
public:
    void reverseString(vector<char>& s) {

        int r = s.size()-1;
        for (int i = 0; i < s.size() / 2; i++) {
            char temp = s[i];
            s[i] = s[r];
            s[r] = temp;
            r--;
        }

        
    }
};