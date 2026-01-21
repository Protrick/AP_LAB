from __future__ import annotations

import functools
import time
import sys

@functools.lru_cache(maxsize=None)
def fib(n: int) -> int:
	if n < 0:
		raise ValueError("n must be non-negative")
	if n < 2:
		return n
	return fib(n - 1) + fib(n - 2)

def fib_no_cache(n: int) -> int:
	"""Plain recursive Fibonacci without memoization (for comparison)."""
	if n < 0:
		raise ValueError("n must be non-negative")
	if n < 2:
		return n
	return fib_no_cache(n - 1) + fib_no_cache(n - 2)

def demo(n: int) -> None:
	print(f"Computing fib({n}) with functools.lru_cache...")
	t0 = time.perf_counter()
	result = fib(n)
	t1 = time.perf_counter()
	print(f"Result: {result} (computed in {t1 - t0:.6f}s)")
	print("Cache info:", fib.cache_info())
	if n <= 30:
		print(f"\nComputing fib({n}) without cache (plain recursion)...")
		t0 = time.perf_counter()
		result2 = fib_no_cache(n)
		t1 = time.perf_counter()
		print(f"Result: {result2} (computed in {t1 - t0:.6f}s)")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		try:
			n_val = int(sys.argv[1])
		except ValueError:
			print("Usage: python lru_cache.py [n]")
			sys.exit(1)
	else:
		n_val = 35

	demo(n_val)