###.2

def solution(participants,completions):

    dict = {}

    for participant in participants:

        dict[participant] = dict.get(participant,0) +1

    for completion in completions:

        dict[completion] = dict.get(completion,0) -1

    return sorted(dict.items(),key=lambda x: -x[1])[0][0]


participants = ["mislav", "stanko", "mislav", "ana"]

comopletions = ["stanko", "ana", "mislav"]

print(solution(participants,comopletions))

# O(N)




































###.1

# def solution(participants,completions):
#
#     for completion in completions:
#
#         if completion in participants:
#
#             participants.remove(completion)
#
#     return participants[0]
#
#
# participants = ["marina", "josipa", "nikola", "vinko", "filipa"]
#
# completions = ["josipa", "filipa", "marina", "nikola"]
#
# print(solution(participants,completions))


# O(N^2)