from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # Step 1: Initialize graph and indegree for every unique character
        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for ch in word:
                indegree[ch] = 0

        # Step 2: Build the graph
        for i in range(len(words) - 1):

            word1 = words[i]
            word2 = words[i + 1]

            # Invalid prefix case
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            # Compare until first differing character
            minimum = min(len(word1), len(word2))

            for j in range(minimum):

                if word1[j] != word2[j]:

                    # Avoid duplicate edges
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1

                    # Only first difference matters
                    break

        # Step 3: Push all characters with indegree 0
        queue = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)

        # Step 4: Topological Sort
        answer = []

        while queue:

            current = queue.popleft()
            answer.append(current)

            for neighbor in graph[current]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: Detect cycle
        if len(answer) != len(indegree):
            return ""

        return "".join(answer)