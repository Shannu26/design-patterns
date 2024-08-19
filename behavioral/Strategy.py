from abc import ABC, abstractmethod

# Strategy Interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Concrete Strategies
class BubbleSort(SortingStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        print("Sorted using Bubble Sort")
        return data

class MergeSort(SortingStrategy):
    def sort(self, data):
        self._merge_sort(data, 0, len(data) - 1)
        print("Sorted using Merge Sort")
        return data

    def _merge_sort(self, data, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(data, left, mid)
            self._merge_sort(data, mid + 1, right)
            self._merge(data, left, mid, right)

    def _merge(self, data, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        L = data[left:mid + 1]
        R = data[mid + 1:right + 1]

        i = j = 0
        k = left
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            data[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            data[k] = R[j]
            j += 1
            k += 1

class QuickSort(SortingStrategy):
    def sort(self, data):
        self._quick_sort(data, 0, len(data) - 1)
        print("Sorted using Quick Sort")
        return data

    def _quick_sort(self, data, low, high):
        if low < high:
            pi = self._partition(data, low, high)
            self._quick_sort(data, low, pi - 1)
            self._quick_sort(data, pi + 1, high)

    def _partition(self, data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

# Context Class
class SortContext:
    def __init__(self, strategy: SortingStrategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.sort(data)

# Client Code
if __name__ == "__main__":
    data = [34, 7, 23, 32, 5, 62]

    # Using Bubble Sort
    context = SortContext(BubbleSort())
    sorted_data = context.execute_strategy(data.copy())
    print(sorted_data)

    # Using Merge Sort
    context.set_strategy(MergeSort())
    sorted_data = context.execute_strategy(data.copy())
    print(sorted_data)

    # Using Quick Sort
    context.set_strategy(QuickSort())
    sorted_data = context.execute_strategy(data.copy())
    print(sorted_data)