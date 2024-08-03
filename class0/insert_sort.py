# 后一个比前一个小就换位置，直到换到最小或者index=0
# 如果写range（1,len(arr))下面的while条件不能写i-1！=0，
# 写了i=1时就没办法跑进去了,但是可以写i>0就对了
# 从0开始还是从1开始条件都是一样的😂

def insert_sort(arr):
    for i in range(len(arr)):
        while arr[i-1]>arr[i] and i>0:
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
        
    return arr


import unittest

class TestInsertSort(unittest.TestCase):
    def test_normal_cases(self):
        self.assertEqual(insert_sort([5, 3, 8, 4, 2]), [2, 3, 4, 5, 8])
        self.assertEqual(insert_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # Already sorted
        self.assertEqual(insert_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  # Reverse order

    def test_edge_cases(self):
        self.assertEqual(insert_sort([]), [])  # Empty list
        self.assertEqual(insert_sort([1]), [1])  # Single element list

    def test_with_duplicates(self):
        self.assertEqual(insert_sort([3, 3, 2, 1, 2]), [1, 2, 2, 3, 3])
        self.assertEqual(insert_sort([1, 2, 2, 1, 1]), [1, 1, 1, 2, 2])

    def test_large_list(self):
        large_list = list(range(1000, 0, -1))
        sorted_large_list = list(range(1, 1001))
        self.assertEqual(insert_sort(large_list), sorted_large_list)

    def test_longer_examples(self):
        longer_list = [i for i in range(10000, 0, -1)]
        sorted_longer_list = [i for i in range(1, 10001)]
        self.assertEqual(insert_sort(longer_list), sorted_longer_list)
        
        large_random_list = [99, 23, 4, 1, 8, 7, 0, 98, 45, 67, 56, 89, 12, 34, 76, 43, 21, 88, 9, 11]
        self.assertEqual(insert_sort(large_random_list), sorted(large_random_list))

if __name__ == '__main__':
    unittest.main()

    #for i in range(len(arr)):

        #while arr[i-1]>arr[i] and i!=0:
            #arr[i-1],arr[i]=arr[i],arr[i-1]
            #i -= 1