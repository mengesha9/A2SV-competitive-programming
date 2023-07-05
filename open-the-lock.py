class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        visited = set()

        if '0000' in dead:
            return - 1
        queue = deque([('0000', 0)])

        while queue:
            lock, turns = queue.popleft()

            if lock == target:
                return turns

            
            turns += 1
            for i in range(4):
                digit = int(lock[i])

                for move in [-1, 1]:
                    newdigit = (digit + move) % 10
                    newlock = lock[:i] + str(newdigit) + lock[i + 1:]

                    if newlock not in visited and newlock not in dead :
                        queue.append((newlock, turns))
                        visited.add(newlock)


        return -1