import math

def distribute_rooms(people, rooms):
    total_effort = sum([room[1] for room in rooms])
    total_people = len(people)
    room_per_person = math.floor(total_effort / total_people)
    remaining_rooms = total_effort % total_people
    
    # Sort the rooms based on effort size
    sorted_rooms = sorted(rooms, key=lambda x: x[1], reverse=True)
    
    # Initialize a dictionary to keep track of room distribution
    distribution = {}
    for person in people:
        distribution[person] = []
    
    # Distribute the rooms
    for room in sorted_rooms:
        for i in range(room[1]):
            person = min(distribution, key=lambda x: sum([r[1] for r in distribution[x]]))
            distribution[person].append(room)
    
    # Assign the remaining rooms
    for i in range(remaining_rooms):
        person = min(distribution, key=lambda x: sum([r[1] for r in distribution[x]]))
        distribution[person].append(sorted_rooms[i])
    
    return distribution

# Example usage
people = ['Alice', 'Bob', 'Charlie']
rooms = [('Floor 1 Room 1', 1), ('Floor 1 Room 2', 1), ('Floor 1 Room 3', 2), ('Floor 2 Room 1', 3), ('Floor 2 Room 2', 1), ('Floor 3 Room 1', 2), ('Floor 4 Room 1', 1), ('Floor 4 Room 2', 2), ('Floor 5 Room 1', 1)]

distribution = distribute_rooms(people, rooms)

for person, assigned_rooms in distribution.items():
    print(f"{person}: {[room[0] for room in assigned_rooms]}")
