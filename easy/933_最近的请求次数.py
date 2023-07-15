from collections import deque


class RecentCounter:
    """
    平均时间复杂度O(1)
    写一个RecentCounter类来计算特定时间范围内最近的请求。

    请你实现 RecentCounter 类：

    RecentCounter() 初始化计数器，请求数为 0 。
    int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
    保证 每次对 ping 的调用都使用比之前更大的 t 值。

    来源：力扣（LeetCode）
    链接：https://leetcode.cn/problems/number-of-recent-calls
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t-3000:
            self.requests.popleft()
        return len(self.requests)


if __name__ == '__main__':
    recentCounter = RecentCounter()
    recentCounter.ping(1)  # requests = [1]，范围是[-2999, 1]，返回1
    recentCounter.ping(100)  # requests = [1, 100]，范围是[-2900, 100]，返回2
    recentCounter.ping(3001)  # requests = [1, 100, 3001]，范围是[1, 3001]，返回3
    recentCounter.ping(3002)  # requests = [1, 100, 3001, 3002]，范围是[2, 3002]，返回3
