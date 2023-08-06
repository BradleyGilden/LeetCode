/*                                 Solution                         */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPalindrome(int x){
    int size = 1;
    int *arr;
    int cp;

    if (x < 0)
        return false;
    for (cp = x; cp / 10 != 0; cp /= 10)
        size++;

    arr = malloc(sizeof(int) * size);

    for(cp = 0; cp < size; cp++)
    {
        arr[cp] = x % 10;
        x /= 10;
    }

    for (cp = 0; cp < size; cp++)
    {
        if (cp > size - 1 - cp)
            break;
        if (arr[cp] != arr[size - 1 - cp])
        {
            free(arr);
            return false;
        }
    }

    free(arr);
    return true;
}

/*                                  Test Solution                         */

int main(void)
{
	printf("%d\n", isPalindrome(101));
	printf("%d\n", isPalindrome(10));
	printf("%d\n", isPalindrome(-101));
	printf("%d\n", isPalindrome(123));
	printf("%d\n", isPalindrome(0));
	return 0;
}
