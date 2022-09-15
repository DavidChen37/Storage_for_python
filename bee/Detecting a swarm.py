# you need to write a function that detects if any group of size 2 could be considered a swarm. A swarm is established if the bees flew together for at least a given duration:
def swarm_busyb(trajectories, duration):
    if(duration == 0):
        return True
    # extract & store bees trajectories
    bee1 = trajectories[:]
    bee2 = trajectories[:]

    # length to iterate loop
    length = len(bee1)

    # counter variable to count bee coordinates
    counter = 0

    # looping over coordinates
    for j in range(length):
        for i in range(length):
            # make sure condition is not compairing against itself
            if(i != j):
                if bee1[i] == bee2[i]:
                    length2 = len(bee1[i])
                    # compare the next few elements in array for matches
                    for k in range(length2):
                        # increment count if match is found
                        if(bee1[j][k] == bee2[i][k]):
                            counter += 1
                            # return True if counter equals duration
                            if counter == duration:
                                return True
                    counter = 0

    return False


all_trajectories = [[(3, 3), (2, 3), (2, 2), (2, 1), (1, 1)],
                    [(4, 2), (3, 2), (2, 2), (2, 1), (1, 1)],
                    [(3, 1), (3, 2), (2, 2), (2, 1), (1, 1)],
                    [(3, 1), (3, 2), (4, 2), (4, 1), (4, 0)]]

print(swarm_busyb(all_trajectories, 1))
