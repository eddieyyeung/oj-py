# Agentic Coding Guidelines for `oj-py`

Welcome, AI coding agent. This repository contains solutions for competitive programming and online judge (OJ) platforms such as LeetCode and Codeforces. This document outlines the standards, commands, and expectations you must adhere to while operating within this workspace.

## 1. Project Overview and Directory Structure

- **Python Version**: `>=3.12`
- **Structure**: The repository is organized by platform and year or category.

```
oj-py/
├── leetcode2026/          # LeetCode problems (preferred new style)
│   └── house_robber/
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

- **`leetcode2026/`**: Each problem directory contains `solution.py` and `test_solution.py`. Imports use the full package path from the project root (e.g., `from leetcode2026.house_robber.solution import Solution`). Tests are run from the **project root**.
- **`leetcode/`**: Each problem directory must have an `__init__.py`. Same full package path imports. Tests are run from the project root.
- **`codeforces/`**: Problems use a file-based I/O pattern, not `unittest`. See Section 5 for details.
- **Multiple solutions for one problem**: Create subdirectories named by algorithm (e.g., `subsets/backtrack_choose_element/`, `subsets/backtrack_include_exclude/`), each with its own `solution.py` and `test_solution.py`.

---

## 2. Build, Lint, and Test Commands

### Testing — single problem (`leetcode2026/`)

Run from the **project root**:

```bash
python -m unittest leetcode2026.house_robber.test_solution -v
```

### Testing — single test method

```bash
python -m unittest leetcode2026.house_robber.test_solution.TestSolution.test_single_element -v
```

### Testing — `leetcode/` (old style)

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
- **Problem directories**: `snake_case` matching the problem slug (e.g., `house_robber`, `binary_tree_paths`).

### 3.5 Error Handling & Edge Cases

- Handle edge cases using control flow (`if not nums: return 0`), not exceptions.
- Avoid broad `try...except` blocks unless parsing malformed I/O strings.
- Guarantee termination for `while` loops and recursive functions (base cases must be explicit).

### 3.6 Algorithmic Patterns

**Nested Helpers**: Define helper functions (`dfs`, `backtrack`, etc.) *inside* the main method to capture outer variables and avoid polluting the class namespace.

```python
def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    ans = []
    path = []
    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        path.append(str(node.val))
        if not node.left and not node.right:
            ans.append("->".join(path))
        dfs(node.left)
        dfs(node.right)
        path.pop()
    dfs(root)
    return ans
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

1. **Split every scenario into its own `test_*` method** — do NOT use a `test_cases` list with a loop. This makes failure messages precise and readable.
2. Initialize the `Solution` object in `setUp(self)` to keep tests DRY.
3. Use `assertEqual` (not `print`) so failures are caught automatically.
4. Use `assertCountEqual` when the return value is an unordered collection (e.g., subsets, permutations, tree paths).
5. Cover: provided examples, empty input, single element, all-identical elements, boundary values, and problem-specific edge cases.

```python
from unittest import TestCase
from leetcode2026.house_robber.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_non_adjacent(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

    def test_longer_sequence(self):
        self.assertEqual(self.solution.rob([2, 7, 9, 3, 1]), 12)

    def test_single_element(self):
        self.assertEqual(self.solution.rob([5]), 5)

    def test_all_zeros(self):
        self.assertEqual(self.solution.rob([0, 0, 0]), 0)

    def test_empty(self):
        self.assertEqual(self.solution.rob([]), 0)
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
3. **Write Tests**: Create or edit `test_solution.py` with per-scenario `test_*` methods (LeetCode) or prepare `input.txt` (Codeforces).
4. **Self-Verify**: Always run the unit test command using the Bash tool. Debug any failures autonomously. Do not report completion until tests pass.
5. **Finalize**: Only announce completion when tests pass. Do not volunteer verbose explanations unless requested.
