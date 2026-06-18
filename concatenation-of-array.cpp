class Solution {

public:
    vector<int> getConcatenation(vector<int>& nums) {    
        //ideas 
        //1.create two arrays
        std::vector<int> TotalArray(nums.size()*2);

        //2.iterate over the nums
        for(int i=0;i<nums.size();i++){
            //3.asignar el valor de nums[i]  a las dos posiciones de total Array
            TotalArray[i] = nums[i];
            TotalArray[i+nums.size()] = nums[i]; //pegar la segunda copia del arreglo exactamente donde termina la primera.
        }

        return TotalArray;

    }

};
