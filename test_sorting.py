import unittest
from Sorting.BUBBLESORT import bubble_sort
from Sorting.selectionsort import selection_sort
from Sorting.insertion_sort import insertion_sort
from Sorting.Merge_sort import merge_sort
from Sorting.quick_sort import quick_sort


class TestSortingAlgorithms(unittest.TestCase):
    """Test all sorting algorithms with various test cases"""
    
    # ==================== BUBBLE SORT TESTS ====================
    def test_bubble_sort_basic(self):
        """Test bubble sort with basic unsorted array"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bubble_sort(arr), expected)
    
    def test_bubble_sort_empty(self):
        """Test bubble sort with empty array"""
        self.assertEqual(bubble_sort([]), [])
    
    def test_bubble_sort_single(self):
        """Test bubble sort with single element"""
        self.assertEqual(bubble_sort([5]), [5])
    
    def test_bubble_sort_already_sorted(self):
        """Test bubble sort with already sorted array"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])
    
    def test_bubble_sort_reverse(self):
        """Test bubble sort with reverse sorted array"""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])
    
    def test_bubble_sort_duplicates(self):
        """Test bubble sort with duplicate elements"""
        arr = [3, 1, 3, 1, 2, 2]
        self.assertEqual(bubble_sort(arr), [1, 1, 2, 2, 3, 3])
    
    def test_bubble_sort_negative(self):
        """Test bubble sort with negative numbers"""
        arr = [-5, 2, -1, 0, 3]
        self.assertEqual(bubble_sort(arr), [-5, -1, 0, 2, 3])
    
    # ==================== SELECTION SORT TESTS ====================
    def test_selection_sort_basic(self):
        """Test selection sort with basic unsorted array"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(selection_sort(arr), expected)
    
    def test_selection_sort_empty(self):
        """Test selection sort with empty array"""
        self.assertEqual(selection_sort([]), [])
    
    def test_selection_sort_single(self):
        """Test selection sort with single element"""
        self.assertEqual(selection_sort([5]), [5])
    
    def test_selection_sort_already_sorted(self):
        """Test selection sort with already sorted array"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(arr), [1, 2, 3, 4, 5])
    
    def test_selection_sort_duplicates(self):
        """Test selection sort with duplicate elements"""
        arr = [3, 1, 3, 1, 2, 2]
        self.assertEqual(selection_sort(arr), [1, 1, 2, 2, 3, 3])
    
    # ==================== INSERTION SORT TESTS ====================
    def test_insertion_sort_basic(self):
        """Test insertion sort with basic unsorted array"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(insertion_sort(arr), expected)
    
    def test_insertion_sort_empty(self):
        """Test insertion sort with empty array"""
        self.assertEqual(insertion_sort([]), [])
    
    def test_insertion_sort_single(self):
        """Test insertion sort with single element"""
        self.assertEqual(insertion_sort([5]), [5])
    
    def test_insertion_sort_already_sorted(self):
        """Test insertion sort with already sorted array"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(arr), [1, 2, 3, 4, 5])
    
    def test_insertion_sort_reverse(self):
        """Test insertion sort with reverse sorted array"""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(insertion_sort(arr), [1, 2, 3, 4, 5])
    
    def test_insertion_sort_negative(self):
        """Test insertion sort with negative numbers"""
        arr = [-5, 2, -1, 0, 3]
        self.assertEqual(insertion_sort(arr), [-5, -1, 0, 2, 3])
    
    # ==================== MERGE SORT TESTS ====================
    def test_merge_sort_basic(self):
        """Test merge sort with basic unsorted array"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(merge_sort(arr), expected)
    
    def test_merge_sort_empty(self):
        """Test merge sort with empty array"""
        self.assertEqual(merge_sort([]), [])
    
    def test_merge_sort_single(self):
        """Test merge sort with single element"""
        self.assertEqual(merge_sort([5]), [5])
    
    def test_merge_sort_two_elements(self):
        """Test merge sort with two elements"""
        self.assertEqual(merge_sort([2, 1]), [1, 2])
    
    def test_merge_sort_duplicates(self):
        """Test merge sort with duplicate elements"""
        arr = [3, 1, 3, 1, 2, 2]
        self.assertEqual(merge_sort(arr), [1, 1, 2, 2, 3, 3])
    
    def test_merge_sort_negative(self):
        """Test merge sort with negative numbers"""
        arr = [-5, 2, -1, 0, 3]
        self.assertEqual(merge_sort(arr), [-5, -1, 0, 2, 3])
    
    # ==================== QUICK SORT TESTS ====================
    def test_quick_sort_basic(self):
        """Test quick sort with basic unsorted array"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(quick_sort(arr), expected)
    
    def test_quick_sort_empty(self):
        """Test quick sort with empty array"""
        self.assertEqual(quick_sort([]), [])
    
    def test_quick_sort_single(self):
        """Test quick sort with single element"""
        self.assertEqual(quick_sort([5]), [5])
    
    def test_quick_sort_two_elements(self):
        """Test quick sort with two elements"""
        self.assertEqual(quick_sort([2, 1]), [1, 2])
    
    def test_quick_sort_already_sorted(self):
        """Test quick sort with already sorted array"""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(quick_sort(arr), [1, 2, 3, 4, 5])
    
    def test_quick_sort_reverse(self):
        """Test quick sort with reverse sorted array"""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(quick_sort(arr), [1, 2, 3, 4, 5])
    
    def test_quick_sort_duplicates(self):
        """Test quick sort with duplicate elements"""
        arr = [3, 1, 3, 1, 2, 2]
        self.assertEqual(quick_sort(arr), [1, 1, 2, 2, 3, 3])
    
    def test_quick_sort_negative(self):
        """Test quick sort with negative numbers"""
        arr = [-5, 2, -1, 0, 3]
        self.assertEqual(quick_sort(arr), [-5, -1, 0, 2, 3])
    
    # ==================== COMPARISON TESTS ====================
    def test_all_sorts_same_result(self):
        """Test that all sorting algorithms produce the same result"""
        arr = [64, 34, 25, 12, 22, 11, 90]
        
        result_bubble = bubble_sort(arr)
        result_selection = selection_sort(arr)
        result_insertion = insertion_sort(arr)
        result_merge = merge_sort(arr)
        result_quick = quick_sort(arr)
        
        self.assertEqual(result_bubble, result_selection)
        self.assertEqual(result_bubble, result_insertion)
        self.assertEqual(result_bubble, result_merge)
        self.assertEqual(result_bubble, result_quick)


if __name__ == '__main__':
    unittest.main()
