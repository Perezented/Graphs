from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())

# room_graph = {
#     0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
#     1: [(3, 6), {'s': 0, 'n': 2}],
#     2: [(3, 7), {'s': 1}],
#     3: [(4, 5), {'w': 0, 'e': 4}],
#     4: [(5, 5), {'w': 3}],
#     5: [(3, 4), {'n': 0, 's': 6}],
#     6: [(3, 3), {'n': 5}],
#     7: [(2, 5), {'w': 8, 'e': 0}],
#     8: [(1, 5), {'e': 7}]
# }

# room_graph = {
#     0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
#     1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}],
#     2: [(3, 7), {'s': 1}],
#     3: [(4, 5), {'w': 0, 'e': 4}],
#     4: [(5, 5), {'w': 3}],
#     5: [(3, 4), {'n': 0, 's': 6}],
#     6: [(3, 3), {'n': 5, 'w': 11}],
#     7: [(2, 5), {'w': 8, 'e': 0}],
#     8: [(1, 5), {'e': 7}],
#     9: [(1, 4), {'n': 8, 's': 10}],
#     10: [(1, 3), {'n': 9, 'e': 11}],
#     11: [(2, 3), {'w': 10, 'e': 6}],
#     12: [(4, 6), {'w': 1, 'e': 13}],
#     13: [(5, 6), {'w': 12, 'n': 14}],
#     14: [(5, 7), {'s': 13}],
#     15: [(2, 6), {'e': 1, 'w': 16}],
#     16: [(1, 6), {'n': 17, 'e': 15}],
#     17: [(1, 7), {'s': 16}]
# }


world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# for i in range(499):
#     traversal_path.append('e')

visited = dict()

inv = {'n': 's', 's': 'n', 'w': 'e',  'e': 'w', }

# setup for dict of rooms


def make_visited(room):
    visited[room.id] = dict()
    for adj_room in room.get_exits():
        visited[room.id][adj_room] = '?'


def join_visited(room1, room2, direction):
    visited[room1.id][direction] = room2.id
    visited[room2.id][inv[direction]] = room1.id


def move_player(direction):
    player.travel(direction)
    traversal_path.append(direction)


def check_room(current_room):
    for adj_room in current_room.get_exits():
        print(adj_room)
        if visited[current_room.id][adj_room] == '?':
            return adj_room


def check_visited(visited_room):
    go_here_next = None
    for adj_room in visited_room:

        # print(adj_room)
        if visited_room[adj_room] == '?':
            go_here_next = adj_room
    return go_here_next


make_visited(player.current_room)
# i = 1
while len(visited) != len(room_graph):

    current_room = player.current_room
    print(f'currentRoom:  {current_room.id} ')
    adj_room = check_room(current_room)
    print(f'We are trying to go to {adj_room} ')
    if adj_room in visited[current_room.id] and visited[current_room.id][adj_room] == '?':
        next_room = current_room.get_room_in_direction(adj_room)
        print(f'NextRoom: {next_room.id} ')
        if next_room.id not in visited:
            make_visited(next_room)
        move_player(adj_room)
        join_visited(current_room, next_room, adj_room)
        i = 0

    else:
        q = Queue()
        q.enqueue([current_room.id])
        this_visted = set()
        while q.size() > 0:
            v = q.dequeue()
            room_id = v[-1]
            go_here_next = check_visited(visited[room_id])
            if go_here_next is None:
                if room_id not in this_visted:
                    this_visted.add(room_id)
                    for adj_room in visited[room_id]:
                        # print(adj_room)
                        new_v = list(v)
                        # print(visited[room_id][adj_room])
                        new_v.append(visited[room_id][adj_room])
                        q.enqueue(new_v)
            else:
                for i in range(0, len(v) - 1):
                    print(v[i], v[i + 1])
                    for exit in visited[v[i]]:
                        print(exit)
                        if visited[v[i]][exit] == v[i + 1]:
                            direction = exit
                    print(visited[v[i]])
                    print(visited[v[i+1]])
                    move_player(direction)

                # print(len(traversal_path))
                break
    # elif adj_room is None:
        # print(adj_room, visited[current_room.id], traversal_path)
        # # q = Queue()
        # # q.enqueue([traversal_path[i]])
        # i += 2
        # this_visit = set()
        # this_set = set()
        # for exits in player.current_room.get_exits():
        #     this_set.add(visited[player.current_room.id][exits])
        # print(f'this_set {this_set} ')
        # while '?' not in this_set:
        #     print(player.current_room.get_exits())

        #     if len(player.current_room.get_exits()) == 1:
        #         print(player.current_room.get_exits())
        #         this_visit.add(player.current_room.get_exits()[0])
        #         player.travel(player.current_room.get_exits()[0])
        #     if len(player.current_room.get_exits()) > 1:
        #         print(player.current_room)
        #         print(player.current_room.get_exits())
        #         print(traversal_path)
        #         player.travel(traversal_path[-i])
        #         traversal_path.append(traversal_path[-i])
        #         i += 1
        #         this_set = set()
        #         for exits in player.current_room.get_exits():
        #             this_set.add(visited[player.current_room.id][exits])

        # while q.size() > 0:
        #     v = q.dequeue()
        #     room_id = v[-1]
        #     go_here_next = v
        #     print(f'go_here_next: {go_here_next} ')
        #     if go_here_next is None:
        #         if room_id not in this_visit:
        #             this_visit.add(room_id)
        #             for adj_room in visited[room_id]:
        #                 # print(adj_room)
        #                 new_v = list(adj_room)
        #                 # print(information[room_id][adj_room])
        #                 new_v.append(visited[room_id][adj_room])
        #                 q.enqueue(new_v)
            # else:

            #     print(f'v: {v} ')
            #     print(f'currentRoom: {player.current_room.id} ')
            #     print(v)
            #     player.travel(inv[traversal_path[-i]])
            #     traversal_path.append(traversal_path[-i])

            #     print(len(traversal_path))
            #     break


print(visited)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
