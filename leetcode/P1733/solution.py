import collections
from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_sets = [set(j) for j in languages]

        users_to_teach = set()
        for u, v in friendships:
            user1_idx = u - 1
            user2_idx = v - 1

            if lang_sets[user1_idx].isdisjoint(lang_sets[user2_idx]):
                users_to_teach.add(user1_idx)
                users_to_teach.add(user2_idx)

        if len(users_to_teach) == 0:
            return 0

        lang_counts = collections.defaultdict(int)
        for user_idx in users_to_teach:
            for lang in lang_sets[user_idx]:
                lang_counts[lang] += 1

        max_coverage = 0
        if len(lang_counts) != 0:
            max_coverage = max(lang_counts.values())

        return len(users_to_teach) - max_coverage
