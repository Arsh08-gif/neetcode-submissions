from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweet_map = defaultdict(list)
        self.user_followee_map = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweet_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.user_followee_map[userId]
        users.add(userId)

        for uid in users:
            for t in self.user_tweet_map[uid][-10:]:
                heapq.heappush(heap, t)
                if len(heap) > 10:
                    heapq.heappop(heap)
        
        heap = sorted(heap, reverse = True)
        return [t for _,t in heap]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followee_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followee_map[followerId].discard(followeeId)
