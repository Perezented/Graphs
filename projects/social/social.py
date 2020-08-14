# 3. Questions

# 1. To create 100 users with an average of 10 friends each, how many times would you need to call `add_friendship()`? Why?
# 100 times, it runs thru i for the range of average times.
# 2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?


import random


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'User({repr(self.name)})'


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # print(random.randint(0, num_users))
        possible = []
        if num_users > avg_friendships:
            print(num_users)
            print(avg_friendships)
            # Add users
            for i in range(num_users):
                self.add_user(i + 1)
        # Create friendships
            for user_id in self.users:
                for friend_id in range(user_id + 1, self.last_id+1):
                    possible.append((user_id, friend_id))
            random.shuffle(possible)
            for i in range(num_users * avg_friendships // 2):
                friendships = possible[i]
                self.add_friendship(friendships[0], friendships[1])

    def get_all_social_paths(self, user_id, visited=None):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        print('#'*30)
        if visited is None:
            visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10000, 2)
    # print(sg.users)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
