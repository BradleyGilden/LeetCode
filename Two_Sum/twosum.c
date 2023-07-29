#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 * steps: 1) declare return size 2, since we are only going to store 2 int's in the array
 *        2) allocate dynamic memory to array 'arr' of size 2 * 4 bytes
 *        3) take first element and iterate the addition through every element in front
 *        4) if element1 + element2 = target, assign them in that order
 *        5) return address of first element of the array
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i = 0, j = 0;

    *returnSize = 2;

    int *arr = malloc(*returnSize * sizeof(int)); 

    for (i = 0; i < numsSize - 1; i++)
    {
        for (j = i + 1; j < numsSize; j++)
        {
            if (nums[i] + nums[j] == target)
            {
                arr[0] = i;
                arr[1] = j;
            }
        }

    }

    return (arr);
}

/**
 * main - Entry point
 * Return: 0 Always
 */
int main(void)
{
    int test[] = {2, 7, 11, 15};
    int numSize = (int)(sizeof(test) / sizeof(test[0]));
    int target = 9;
    int returnSize = 2;
    int *arr = twoSum(test, numSize, target, &returnSize);

    printf("[%d, %d]\n", arr[0], arr[1]);

    free(arr);
    return (0);
}
