/*
Most Common Word

Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase. */

class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        unordered_map<string, int> m;
        for(auto &c : paragraph)
            c =  isalpha(c)? tolower(c) : ' '; 
        
        istringstream iss(paragraph);
        string curr_word;
        while(iss >> curr_word)
            if ((find(banned.begin(), banned.end(), curr_word)) == banned.end()){
                ++m[curr_word];  
            }
        
        int max = 0;
        string maxWord;

        for (auto &word : m){
            if (word.second > max){
                max = word.second;
                maxWord = word.first;
            }
        }
        
        return maxWord;
    }
};