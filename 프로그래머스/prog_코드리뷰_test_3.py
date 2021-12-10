def solution(skill,skill_trees):

    answer = 0

    for tree in skill_trees:

        standard_list = list(skill)

        count = 0

        for i in tree:

            if i in standard_list:

                count +=1

                idx = standard_list.index(i)

                standard_list = standard_list[idx:]

            else:

                continue

        if count >= 2:

            answer += 1

    return answer


skill = "CBD"

skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

# skill_trees = "CBADF"


print(solution(skill,skill_trees))













