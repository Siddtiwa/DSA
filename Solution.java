package DSA;
class Solution{
    public static void main(String[] args) {
        int[] nums = {2,1,1,1,1};
        int j = 0;
        int n = nums.length;
        int sum = 0;
        int k = 4;
        int len = 0;
        for(int i=0;i<n;i++){
            sum += nums[i];
            if(sum == k)
                len = Math.max(len, i - j + 1);
            if(sum>k){
                while(sum>k){
                    sum -= nums[j];
                    j++;
                }
            }
        }
        System.out.println(len);
    }
}