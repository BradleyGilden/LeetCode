from typing import List


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    """
    determines if all rooms can be opened
    """
    keys = set([0])
    used = set()
    roomNo = len(rooms)

    while keys:
        currentroom = keys.pop()
        if currentroom in used:
            continue
        used.add(currentroom)
        keys.update(rooms[currentroom])
        roomNo -= 1

    return roomNo == 0


if __name__ == "__main__":
    rooms = [[1], [2], [3], []]
    print(can_visit_all_rooms(rooms))
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    print(can_visit_all_rooms(rooms))
