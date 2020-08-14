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
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room.id)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room.id)


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)

# traversal_path.append(player.current_room.id)

print('#-' * 30)

inv = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e', }


def find_all_rooms(players_room, information=None):
    s = Stack()
    if information is None:
        information = dict()
    # seting up the information dict to the current room and the n, s, w, e rooms with their room id or '?'
    traversal_path.append(player.current_room.id)
    if player.current_room.id not in information:
        information[players_room.id] = dict()
        for directions in players_room.get_exits():
            if directions not in information[players_room.id]:
                information[players_room.id][directions] = '?'
    for adj_rooms in information[player.current_room.id]:
        print(players_room.id)
        print(player.current_room.id, adj_rooms)
        if information[players_room.id][adj_rooms] == '?':
            player.travel(adj_rooms)
            if player.current_room.id not in information:
                information[player.current_room.id] = dict()
                for directions in player.current_room.get_exits():
                    if directions not in information[player.current_room.id]:
                        information[player.current_room.id][directions] = '?'
            information[players_room.id][adj_rooms] = player.current_room.id
            # information[player.current_room.id][adj_rooms] = player.current_room.id
            find_all_rooms(player.current_room, information)
        #     player.travel(adj_rooms)
        #     information[players_room.id][adj_rooms] = player.current_room.id
        #     # information[player.current_room.id][inv[adj_rooms]
        #     #                                     ] = players_room.id
    print(information)
    # while len(visited_rooms) != len(room_graph):


find_all_rooms(player.current_room)
# print(information)
print(f'traversal_path {traversal_path}')
print(f'visited rooms: {visited_rooms}')

print('#-' * 30)
print('')
print('~~~TESTS~~~')
if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
print(visited_rooms)
print('~~~END OF TESTS~~~')


# while True:

#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#         if player.current_room.id not in visited_rooms:
#             visited_rooms.add(player.current_room.id)
#         traversal_path.append(player.current_room.id)
#         print(f'traversal_path {traversal_path}')
#         print(f'visited rooms: {visited_rooms}')
#         # print('heeeeeeeeeyyyyyyy')

#         # print("possible directions")

#         for d in player.current_room.get_exits():
#             print(d)
#             print(player.current_room.get_room_in_direction(d).id)

#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
