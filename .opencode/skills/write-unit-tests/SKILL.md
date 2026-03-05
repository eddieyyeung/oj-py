---
name: write-unit-tests
description: 为 oj-py 项目中的题目编写或生成测试相关内容，包括 test_solution.py 文件、测试用例列表、边界条件分析等。当用户提及"测试"、"测试用例"、"test case"、"边界条件"、"补充测试"、"生成 test_solution.py"，或题目目录缺少 test_solution.py 时，使用此 skill。
---

# Write Unit Tests

为 oj-py 项目中的题目目录生成 `test_solution.py`，或补充测试用例、分析边界条件。

## 工作流

1. **读取** `solution.py` — 理解 `Solution` 类的所有方法：名称、参数名称与类型、返回类型、算法意图
2. **分析边界条件** — 根据参数类型和逻辑推断出需要覆盖的测试场景
3. **生成** `test_solution.py` — 严格遵循下方规范，写入文件后报告完成

## 测试文件规范

### 导入与结构

导入路径根据 `solution.py` 的实际位置动态推断：将从项目根目录到 `solution.py` 的文件路径转换为 Python 包路径（路径分隔符 `/` 替换为 `.`，去掉 `.py` 后缀）。

```python
from unittest import TestCase
from <package.path.to>.solution import Solution
```

**推断规则示例：**

| `solution.py` 路径 | 对应导入语句 |
|---|---|
| `leetcode2026/house_robber/solution.py` | `from leetcode2026.house_robber.solution import Solution` |
| `leetcode/P3000/solution.py` | `from leetcode.P3000.solution import Solution` |
| `codeforces/P774A/solution.py` | `from codeforces.P774A.solution import Solution` |

- 类名固定为 `TestSolution(TestCase)`
- 在 `setUp(self)` 中初始化 `self.solution = Solution()`
- 每个测试场景拆分为独立的 `test_*` 方法，命名清晰描述场景（如 `test_empty`、`test_single_node`）

### 测试用例格式

每个测试场景对应一个独立的 `test_*` 方法，直接在方法体内断言，不使用 `test_cases` 列表循环。

```python
def test_two_non_adjacent(self):
    self.assertEqual(self.solution.rob([1, 2, 3, 1]), 4)

def test_single_element(self):
    self.assertEqual(self.solution.rob([5]), 5)

def test_empty(self):
    self.assertEqual(self.solution.rob([]), 0)
```

> 当返回值是无序集合（如全排列、组合、树路径）时，使用 `assertCountEqual` 代替 `assertEqual`。

### 必须覆盖的场景

| 场景 | 示例 |
|------|------|
| 题目提供的样例 | 直接从题干复制 |
| 正常路径（happy path） | 典型输入 |
| 空输入 | `[]`, `""`, `0` |
| 单元素 | `[5]`, `"a"` |
| 全相同元素 | `[3, 3, 3]` |
| 边界值 | 最小值、最大值 |
| 特殊情况 | 全为零、负数、严格递减等（视题目而定） |

## 参考示例

以下是 `leetcode2026/house_robber/` 的完整示例，展示了规范的应用。

### solution.py

```python
from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            rst = max(dfs(i-1), dfs(i-2) + nums[i])
            return rst

        return dfs(len(nums)-1)
```

### test_solution.py（目标输出风格）

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

    def test_two_elements(self):
        self.assertEqual(self.solution.rob([2, 1]), 2)

    def test_all_same(self):
        self.assertEqual(self.solution.rob([3, 3, 3, 3]), 6)

    def test_increasing(self):
        self.assertEqual(self.solution.rob([1, 2, 3, 4, 5]), 9)

    def test_all_zeros(self):
        self.assertEqual(self.solution.rob([0, 0, 0]), 0)

    def test_empty(self):
        self.assertEqual(self.solution.rob([]), 0)
```

## 注意事项

- 不要创建或修改 `__init__.py`
- 不要运行测试命令；生成文件后直接报告完成
- 如果 `solution.py` 包含多个方法（如构造函数类题目），为每个公开方法单独写一个 `test_*` 方法
- 每个测试场景拆分为独立的 `test_*` 方法，而非全部写在同一个方法的 `test_cases` 列表中；这样失败信息更精确，可读性更好
- 保持 PEP 8 格式：4 空格缩进，顶层类/函数之间空两行
