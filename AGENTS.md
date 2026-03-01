# Agentic Coding Guidelines for `oj-py`

Welcome, AI coding agent. This repository contains solutions for competitive programming and online judge (OJ) platforms such as LeetCode and Codeforces. This document outlines the standards, commands, and expectations you must adhere to while operating within this workspace.

## 1. Project Overview and Directory Structure

- **Python Version**: `>=3.12`
- **Structure**: The repository is organized by platform and year or category (e.g., `leetcode2026/`, `codeforces/`, `example/`).
- **Problem Folders**: Each algorithmic problem has its own dedicated directory.
  - Implementation: `solution.py` (Contains the `Solution` class).
  - Tests: `test_solution.py` (Contains the `TestSolution` class).

---

## 2. Build, Lint, and Test Commands

### Testing
We use Python's built-in `unittest` framework. Never assume `pytest` is installed unless specified. 

**Running a single test file (Recommended for iterative development):**
To run tests for a specific problem, change into that problem's directory and run the test module.
```bash
cd leetcode2026/house-robber
python -m unittest test_solution -v
```

**Running all tests project-wide:**
```bash
python -m unittest discover -s . -p "test_*.py" -v
```

### Linting & Formatting
The project uses `ruff` for fast linting and code formatting (indicated by `.ruff_cache`).

**Check for linting errors:**
```bash
ruff check .
```

**Auto-format the codebase:**
```bash
ruff format .
```

### Dependency Management
The project uses `uv` (indicated by `pyproject.toml` and `uv.lock`) or `pipenv` (indicated by `Pipfile`).
- To install/sync dependencies, you can use `uv sync` or standard `pip install -r requirements.txt`.

---

## 3. Code Style Guidelines

### 3.1 Imports
- Group standard libraries first, then third-party, then local modules.
- Prefer explicit typing imports (e.g., `from typing import List, Optional, Tuple`) as this matches LeetCode templates, even in Python 3.12.
- Only import what you need. Remove unused imports.

### 3.2 Formatting and Syntax
- Follow PEP 8 (4 spaces for indentation).
- Use structural pattern matching (`match / case`) if it simplifies complex conditionals.
- Maximize the use of standard library features suited for algorithms (`collections.deque`, `collections.defaultdict`, `heapq`, `math`, `bisect`).

### 3.3 Types and Type Hints
- **Strictly type all functions.** All method arguments and return types must be fully annotated.
- Example:
  ```python
  def maxProfit(self, prices: List[int]) -> int:
      ...
  ```

### 3.4 Naming Conventions
- **Classes**: `PascalCase` (e.g., `Solution`, `TestSolution`).
- **Functions/Methods**: `snake_case` (e.g., `rob`, `test_rob`, `binary_search`). Note: LeetCode method names may sometimes be `camelCase`; maintain the signature exactly as provided by the platform.
- **Variables**: Use concise but descriptive `snake_case` (e.g., `max_profit`, `nums`, `left`, `right`, `expected`).
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MOD = 10**9 + 7`).

### 3.5 Error Handling & Edge Cases
- For algorithmic problems, handle edge cases (e.g., empty arrays, single elements, negative inputs) gracefully using control flow (`if not nums: return 0`) rather than raising exceptions.
- Avoid broad `try...except` blocks unless specifically parsing malformed I/O strings.
- Guarantee termination for loops (`while`) and recursive calls (base cases).

### 3.6 Algorithmic Patterns
- **Nested Helpers**: Define helper functions (like `dfs` or `backtrack`) *inside* the main method. This avoids polluting the class namespace and allows the helper to capture the outer method's variables, eliminating the need to pass large arrays or state repeatedly.
  ```python
  def findPaths(self, root: Optional[TreeNode]) -> List[str]:
      res = []
      def dfs(node, path):
          if not node: return
          # ... logic ...
      dfs(root, [])
      return res
  ```
- **Memoization**: Always prefer `from functools import cache` (or `lru_cache(None)`) on inner recursive helper functions instead of building manual dictionary caches, as it is cleaner and faster.

---

## 4. Test Writing Guidelines

When generating or updating `test_solution.py`:
1. Use a **table-driven testing** approach within a single test method where possible. Iterate over an array of `(input, expected)` tuples.
2. Ensure you initialize the `Solution` object in the `setUp(self)` method to keep tests DRY.
3. Test a robust set of scenarios:
   - Provided examples.
   - Happy paths.
   - Boundaries (e.g., empty inputs, 1-element arrays, all identical elements, all zeros).
   - Worst-case complexities (e.g., strictly decreasing arrays, max values).

**Example:**
```python
from unittest import TestCase
from solution import Solution

class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_logic(self):
        test_cases = [
            ([1, 2, 3, 1], 4),
            ([2, 7, 9, 3, 1], 12),
            ([0, 0, 0], 0),
            ([], 0),
        ]
        for nums, expected in test_cases:
            self.assertEqual(self.solution.rob(nums), expected)
```

---

## 5. Agent Workflow Expectations

When you receive an instruction to implement a solution:
1. **Acknowledge and Plan**: Analyze the problem and state the algorithm (e.g., "I will use top-down DP with memoization").
2. **Implement**: Create or edit `solution.py` matching the style guidelines above.
3. **Write Tests**: Create or edit `test_solution.py` ensuring comprehensive coverage.
4. **Self-Verify**: Always run the unit test command using `bash`. Use the output to debug any failures autonomously. Do not tell the user you are done until tests pass.
5. **Finalize**: Only announce completion when tests pass successfully. Do not volunteer verbose explanations of the code unless requested.