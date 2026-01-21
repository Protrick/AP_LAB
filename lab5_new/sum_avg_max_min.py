def compute_sum(nums):
    """Return the sum of numbers in nums (empty list -> 0)."""
    return sum(nums)

def compute_average(nums):
    if not nums:
        raise ValueError("Cannot compute average of empty list")
    return compute_sum(nums) / len(nums)

def compute_max(nums):
    if not nums:
        raise ValueError("Cannot compute max of empty list")
    return max(nums)

def compute_min(nums):
    if not nums:
        raise ValueError("Cannot compute min of empty list")
    return min(nums)


def analyze(nums):
    if not nums:
        return None

    total = compute_sum(nums)
    return {
        "sum": total,
        "average": compute_average(nums),
        "max": compute_max(nums),
        "min": compute_min(nums),
    }


if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    results = analyze(nums)

    if results:
        print(f"List: {nums}")
        print(f"Sum: {results['sum']}")
        print(f"Average: {results['average']}")
        print(f"Max: {results['max']}")
        print(f"Min: {results['min']}")

    empty_list_results = analyze([])
    if empty_list_results is None:
        print("analyze([]) returned None for empty list")
