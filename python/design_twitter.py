class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        self.count = 0
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.dic.setdefault(userId, {'follower':[], 'followee':[], 'post':[]})
        self.dic[userId]['post'].append((tweetId, self.count))
        self.count += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        self.dic.setdefault(userId, {'follower':[], 'followee':[], 'post':[]})
        res = self.dic[userId]['post'][:]
        for u in self.dic[userId]['follower']:
            res += self.dic[u]['post']
        tmp = []
        for x, y in sorted(res, cmp=lambda x,y:cmp(x[1],y[1])):
            tmp.append(x)
        return tmp[:-11:-1]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return 
        self.dic.setdefault(followerId, {'follower':[], 'followee':[], 'post':[]})
        self.dic.setdefault(followeeId, {'follower':[], 'followee':[], 'post':[]})
        if followerId not in self.dic[followeeId]['followee']:
            self.dic[followeeId]['followee'].append(followerId)
        if followeeId not in self.dic[followerId]['follower']:
            self.dic[followerId]['follower'].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return 
        self.dic.setdefault(followerId, {'follower':[], 'followee':[], 'post':[]})
        self.dic.setdefault(followeeId, {'follower':[], 'followee':[], 'post':[]})
        try:
            self.dic[followeeId]['followee'].remove(followerId)
        except:
            pass
        try:
            self.dic[followerId]['follower'].remove(followeeId)
        except:
            pass

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
