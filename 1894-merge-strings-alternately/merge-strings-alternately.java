class Solution {
    public String mergeAlternately(String word1, String word2) {
        int len = word1.length();
        if (word1.length() > word2.length()){
            len = word2.length();
        }

        String res = "";
        int i = 0;
        while (i < len){
            res += word1.charAt(i);
            res += word2.charAt(i);
            i++;
        }

        res += word1.substring(i, i + word1.length() - len);
        res += word2.substring(i, i + word2.length() - len);
        return res;
    }
}