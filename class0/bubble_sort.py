# index 两两比较，谁大谁往后交换，最后一个就是最大的，然后再交换，确定倒数第二大的
# 从后往前确定，每次交换的越来越短
# 每次都从第一个开始比较，交换

def bubble_sort(arr):
    for n in range(len(arr)-1):
        for i in range(len(arr)-n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i],arr[i+1]
    return arr

import unittest

class TestBubbleSort(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(bubble_sort([5, 3, 8, 4, 2]), [2, 3, 4, 5, 8])
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Already sorted
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  # Reverse order

    def test_edge_cases(self):
        self.assertEqual(bubble_sort([]), [])  # Empty list
        self.assertEqual(bubble_sort([1]), [1])  # Single element list

    def test_with_duplicates(self):
        self.assertEqual(bubble_sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])
        self.assertEqual(bubble_sort([1, 2, 2, 1, 1]), [1, 1, 1, 2, 2])

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        sorted_large_list = list(range(1, 1001))
        self.assertEqual(bubble_sort(large_list), sorted_large_list)

    def test_longer_examples(self):
        longer_list = [i for i in range(10000, 0, -1)]
        sorted_longer_list = [i for i in range(1, 10001)]
        self.assertEqual(bubble_sort(longer_list), sorted_longer_list)
        
        large_random_list = [99, 23, 4, 1, 8, 7, 0, 98, 45, 67, 56, 89, 12, 34, 76, 43, 21, 88, 9, 11]
        self.assertEqual(bubble_sort(large_random_list), sorted(large_random_list))

if __name__ == '__main__':
    unittest.main()

    #for n in range(len(arr)-1):
    # 第一次是在0～N-1之间进行比较（下面有个i和i+1比，所以先只考虑这个）
    # 第二次在0～N-2之间，N就是长度，所以要len-1
        #for i in range(len(arr)-n-1):
            # 这里需要和后一个数比较，有个+1，所以上面要再-1
           # if arr[i]>arr[i+1]:
            #    arr[i],arr[i+1] =arr[i+1],arr[i]