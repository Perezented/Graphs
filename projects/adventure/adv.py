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

traversal_path.append(player.current_room.id)


# def moving_rooms(current_room, direction):
#     player.travel(direction)
#     traversal_path.append(current_room.id)
#     if current_room.id not in visited_rooms:
#         visited_rooms.add(current_room.id)
#     print(current_room)


# def visit_all_rooms(current_room):
#     print('#########'*10)
#     print(current_room)
#     print(current_room.get_exits())
#     s = Stack()
#     s.push(current_room.get_exits())
#     while s.size() > 0:
#         v = s.pop()
#         print(v)
#         moving_rooms(player.current_room.id, v[0])


# visit_all_rooms(player.current_room)
print('#' * 40)


s = Stack()


# def visit_all_rooms(players_room):
#     s.push(players_room.get_exits()[0])
#     print(players_room.get_coords())
#     print(f'players_room: {players_room}')
#     v = s.pop()
#     print(v)
#     for adjacent_rooms in players_room.get_exits():
#         print(adjacent_rooms)
#         player.travel(adjacent_rooms)
#         traversal_path.append(player.current_room.id)
#         if player.current_room.id not in visited_rooms:
#             visited_rooms.add(player.current_room.id)
#             visit_all_rooms(player.current_room)

#     player.travel(v[0])

#     if player.current_room.id not in visited_rooms:
#         visited_rooms.add(players_room.id)
#     traversal_path.append(players_room.id)
#     for adjacent_rooms in players_room.get_exits():
#         return visit_all_rooms(adjacent_rooms, s)


# def visit_all_rooms(players_room):
#     print(players_room.get_exits())
#     s.push(players_room.get_exits())
#     v = s.pop()
#     print(v)
#     if player.current_room.id not in visited_rooms:
#         visited_rooms.add(player.current_room.id)
#         for direction in player.current_room.get_exits():
#             player.travel(direction)
#             visit_all_rooms(player.current_room)


# visit_all_rooms(player.current_room)

print(f'traversal_path {traversal_path}')
print(f'visited rooms: {visited_rooms}')

print('#' * 40)
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
