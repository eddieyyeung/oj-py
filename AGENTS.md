# Agentic Coding Guidelines for `oj-py`

Welcome, AI coding agent. This repository contains solutions for competitive programming and online judge (OJ) platforms such as LeetCode and Codeforces. This document outlines the standards, commands, and expectations you must adhere to while operating within this workspace.

## 1. Project Overview and Directory Structure

- **Python Version**: `>=3.12`
- **Structure**: The repository is organized by platform and year or category.

```
oj-py/
├── leetcode2026/          # LeetCode problems (new style, directory-local imports)
│   └── house-robber/
│       ├── solution.py
│       └── test_solution.py
├── leetcode/              # LeetCode problems (old style, root-relative imports)
│   └── P3000/
│       ├── __init__.py
│       ├── solution.py
│       └── test_solution.py
└── codeforces/            # Codeforces problems (I/O-based, not unittest)
    └── P774A/
        ├── __init__.py
        ├── solution.py
        ├── solution_test.py
        ├── input.txt
        └── output.txt
```

- **`leetcode2026/`**: Each problem directory contains `solution.py` and `test_solution.py`. Imports are local (e.g., `from solution import Solution`). Tests are run from within the problem directory.
- **`leetcode/`**: Each problem directory must have an `__init__.py`. Imports use the full package path (e.g., `from leetcode.P3000.solution import Solution`). Tests are run from the project root.
- **`codeforces/`**: Problems use a file-based I/O pattern, not `unittest`. See Section 5 for details.

---

## 2. Build, Lint, and Test Commands

### Testing — `leetcode2026/` (preferred new style)

Run from **within** the problem directory:

```bash
cd leetcode2026/house-robber
python -m unittest test_solution -v
```

### Testing — `leetcode/` (old style, root-relative)

Run from the **project root**:

```bash
python -m unittest leetcode.P3000.test_solution -v
```

### Testing — all tests project-wide

```bash
python -m unittest discover -s . -p "test_*.py" -v
```

### Testing — Codeforces problems

Codeforces problems are not unittest-based. Edit `input.txt` with the test input, then run from the project root:

```bash
python codeforces/P774A/solution_test.py
```

Check `output.txt` for results.

### Linting & Formatting

The project uses `ruff` for linting and formatting.

```bash
ruff check .       # check for linting errors
ruff format .      # auto-format the codebase
```

### Dependency Management

```bash
uv sync            # install/sync dependencies (preferred)
```

---

## 3. Code Style Guidelines

### 3.1 Imports

- Group standard libraries first, then third-party, then local modules.
- Prefer explicit typing imports (e.g., `from typing import List, Optional, Tuple`) to match LeetCode templates, even in Python 3.12.
- Only import what you need. Remove unused imports.
- Module-level constants (e.g., lookup tables) belong at the top of `solution.py`, after imports and before the class definition.

### 3.2 Formatting and Syntax

- Follow PEP 8 (4 spaces for indentation).
- Use structural pattern matching (`match / case`) if it simplifies complex conditionals.
- Maximize the use of standard library features suited for algorithms: `collections.deque`, `collections.defaultdict`, `heapq`, `math`, `bisect`, `itertools`.

### 3.3 Types and Type Hints

- **Strictly type all functions.** All method arguments and return types must be fully annotated.
- Example:
  ```python
  def maxProfit(self, prices: List[int]) -> int:
      ...
  ```
- For Codeforces `Args` dataclasses, annotate class-level fields directly (no `__init__` needed).

### 3.4 Naming Conventions

- **Classes**: `PascalCase` (e.g., `Solution`, `TestSolution`, `Args`).
- **Functions/Methods**: `snake_case` (e.g., `rob`, `test_rob`, `binary_search`). LeetCode method names may be `camelCase`; maintain the signature exactly as given by the platform.
- **Variables**: Concise, descriptive `snake_case` (e.g., `max_profit`, `nums`, `left`, `right`, `expected`).
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MOD = 10**9 + 7`, `MAPPING = [...]`).

### 3.5 Error Handling & Edge Cases

- Handle edge cases using control flow (`if not nums: return 0`), not exceptions.
- Avoid broad `try...except` blocks unless parsing malformed I/O strings.
- Guarantee termination for `while` loops and recursive functions (base cases must be explicit).

### 3.6 Algorithmic Patterns

**Nested Helpers**: Define helper functions (`dfs`, `backtrack`, etc.) *inside* the main method to capture outer variables and avoid polluting the class namespace.

```python
def findPaths(self, root: Optional[TreeNode]) -> List[str]:
    res = []
    def dfs(node: Optional[TreeNode], path: List[str]) -> None:
        if not node:
            return
        # ... logic ...
    dfs(root, [])
    return res
```

**Memoization**: Always prefer `from functools import cache` (or `lru_cache(None)`) on inner recursive helpers instead of manual dict caches.

```python
from functools import cache

def rob(self, nums: List[int]) -> int:
    @cache
    def dfs(i: int) -> int:
        if i < 0:
            return 0
        return max(dfs(i - 1), dfs(i - 2) + nums[i])
    return dfs(len(nums) - 1)
```

---

## 4. Test Writing Guidelines (LeetCode)

When generating or updating `test_solution.py`:

1. Use a **table-driven testing** approach: iterate over a list of `(input, expected)` tuples in a single test method.
2. Initialize the `Solution` object in `setUp(self)` to keep tests DRY.
3. Use `assertEqual` (not just `print`) so failures are caught automatically.
4. Test a robust set of scenarios: provided examples, boundaries (empty input, single element, all identical, all zeros), and worst-case inputs.

```python
from unittest import TestCase
from solution import Solution

class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob(self):
        test_cases = [
            ([1, 2, 3, 1], 4),
            ([2, 7, 9, 3, 1], 12),
            ([5], 5),
            ([0, 0, 0], 0),
            ([], 0),
        ]
        for nums, expected in test_cases:
            self.assertEqual(self.solution.rob(nums), expected)
```

---

## 5. Codeforces Solution Pattern

Codeforces problems use file-based I/O and do not use `unittest`. The structure is:

- **`Args`**: A plain dataclass holding parsed input fields.
- **`Solution.solve(args)`**: A `@staticmethod` containing the algorithm; writes output via `print()`.
- **`Solution.run(input, output)`**: A `@staticmethod` that redirects `sys.stdin`/`sys.stdout`, reads from the `TextIO` stream, populates `Args`, and calls `solve`.
- **`solution_test.py`**: Opens `input.txt` and `output.txt`, calls `Solution.run(input, output)` once per test case.
- **`input.txt` / `output.txt`**: Manual test I/O files.

```python
import sys
from typing import TextIO

class Args:
    n: int
    total: int

class Solution:
    @staticmethod
    def solve(args: Args) -> None:
        # algorithm, output via print()
        ...

    @staticmethod
    def run(input: TextIO, output: TextIO) -> None:
        sys.stdin = input
        sys.stdout = output
        args = Args()
        args.n = int(input.readline())
        # ... parse remaining input into args ...
        Solution.solve(args)

if __name__ == "__main__":
    Solution.run(sys.stdin, sys.stdout)
```

---

## 6. Agent Workflow Expectations

When you receive an instruction to implement a solution:

1. **Acknowledge and Plan**: Analyze the problem and state the algorithm (e.g., "I will use top-down DP with memoization").
2. **Implement**: Create or edit `solution.py` matching the style guidelines above.
3. **Write Tests**: Create or edit `test_solution.py` with comprehensive, assertion-based coverage (LeetCode) or prepare `input.txt` (Codeforces).
4. **Self-Verify**: Always run the unit test command using the Bash tool. Debug any failures autonomously. Do not report completion until tests pass.
5. **Finalize**: Only announce completion when tests pass. Do not volunteer verbose explanations unless requested.
