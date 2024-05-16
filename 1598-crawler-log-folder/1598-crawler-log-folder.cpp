class Solution {
public:
    int minOperations(vector<string>& logs) {
        int level = 0;
        for(const string& log : logs){
            if(log == "../"){
                if (level > 0){
                    level--;
                }
            }
            else if (log != "./"){
                level++;
            }
        }
        return level;
    }
};