""" Drunken sailor simulation """

"""
Drunken sailor needs to get to 100 steps to East nearest shore to get to the home.
Sailors home is 100 steps East and 100 steps to North from where he starts his journey.
Sailor walks his journeys as a random walker, he takes one step the North, East, West or South
with eqaul probability. When he finds the shore, he can walk straight to home.
Simulation calculates time to get to the home, 1 step takes 1 second.
Finally plot path taken with no. steps with start and endpoint marked to the plot.
"""

import matplotlib.pyplot as plt
import random
import logging as logger


def take_step() -> str():
    direction = random.randint(1,4)
    if direction == 1:
        return "up"
    elif direction == 2:
        return "left"
    elif direction == 3:
        return "down"
    elif direction == 4:
        return "right"


def plot_journey(x_data, y_data, time) -> None:
    home_x = [100]
    home_y = [100]
    start_x = [0]
    start_y = [0]
    logger.info("Plotting results for position")
    plt.title(f"Drunken sailor simulation, steps taken {time}")
    plt.xlabel("East/West direction")
    plt.ylabel("North/South direction")
    plt.plot(x_data, y_data, color = "blue", label="Path taken")
    plt.plot(home_x , home_y, color = "red", marker = "o", markersize = 7, markeredgecolor = "black", label="Home")
    plt.plot(start_x , start_y, color = "yellow", marker = "o", markersize = 7, markeredgecolor = "black", label="Start point")
    plt.legend(loc="upper left")
    plt.show()


def plot_time_elapsed(time_data) -> None:
    logger.info("Plotting results for elapsed time")
    plt.hist(time_data, bins = 10)
    plt.show()

def simulation() -> list():
    pos_x = 0
    pos_y = 0
    time = 0
    x_data = []
    y_data = []
    x_data.append(pos_x)
    y_data.append(pos_y)
    while True:
        logger.info("Taking a step")
        direction = take_step()
        if direction == "up":
            pos_y += 1
        elif direction == "right":
            pos_x += 1
        elif direction == "left":
            pos_x -= 1
        elif direction == "down":
            pos_y -= 1

        logger.info(f"Current coordinates are ({pos_x}, {pos_y})")
        time += 1

        # Saving positions to x_data and y_data
        x_data.append(pos_x)
        y_data.append(pos_y)

        #print(f"({pos_x}, {pos_y})")
        if pos_x == 100:
            print(f"Found beach in position ({pos_x}, {pos_y})")
            logger.info(f"Sailor has found beach in time {time}. Current position is ({pos_x}, {pos_y}). ")
            if pos_y > 100:
                distance = pos_y - 100
                for i in range(distance):
                    time += 1
                    pos_y -= 1

                    x_data.append(pos_x)
                    y_data.append(pos_y)
                    logger.info(f"Current coordinates are ({pos_x}, {pos_y})")

                logger.info(f"Final time used for journey: {time}")
                print(f"Final time used for journey: {time}")
                return [x_data, y_data, time]

            elif pos_y < 100:
                distance = 100 - pos_y
                for i in range(distance):
                    time += 1
                    pos_y += 1

                    x_data.append(pos_x)
                    y_data.append(pos_y)
                    logger.info(f"Current coordinates are ({pos_x}, {pos_y})")

                logger.info(f"Final time used for journey: {time}")
                print(f"Final time used for journey: {time}")
                return [x_data, y_data, time]

            else:
                logger.info("Sailor has found straight to home!")
                logger.info(f"Final time used for journey: {time}")
                print(f"Final time used for journey: {time}")
                return [x_data, y_data, time]



def main() -> None:
    time_data = []
    # Assign number of runs for Drunken sailor -simulation
    runs = 1
    for i in range(runs):
        x_data, y_data, time = simulation()
        time_data.append(time)

    #plot_time_elapsed(time_data)
    plot_journey(x_data, y_data, time)





if __name__=="__main__":
    main()
