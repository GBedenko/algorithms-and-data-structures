'''Script to calculate the number of creatures in a fictional alien invasion.

   An alien lays X eggs each day (there are no genders in this species) and the eggs
   hatch after Y days. For any value X and Y, how many aliens will there be N days
   after a M aliens invade?'''


def alien_eggs(eggs_laid, days_to_hatch, total_days, starting_aliens):
    """For each day up to the total number of days, outputs the current
       number of aliens and number of eggs laid"""

    eggs_per_day = [0] # List for each day for how many eggs are laid on that day

    aliens_per_day = [0] # List for each day for how many aliens there are on that day

    for day in range(1, total_days + 1):

        # If it is the first day, there is just one alien, and that alien lays x amount of eggs
        if day == 1:
            aliens_per_day.append(starting_aliens)
            eggs_per_day.append(eggs_laid * aliens_per_day[day])

            print("Day " + str(day) + "... Number of eggs laid on this day = " + str(eggs_per_day[day]) + " Number of aliens = " + str(aliens_per_day[day]))

        # Until y days have passed, there is still only as many aliens as the previous day
        elif day < days_to_hatch:
            aliens_per_day.append(aliens_per_day[day-1])
            eggs_per_day.append(eggs_laid * aliens_per_day[day])

            print("Day " + str(day) + "... Number of eggs laid on this day = " + str(eggs_per_day[day]) + " Number of aliens = " + str(aliens_per_day[day]))

        # Else, the number of aliens is the total from the previous day plus the number eggs laid y days ago
        else:
            aliens_per_day.append(aliens_per_day[day-1] + eggs_per_day[day-days_to_hatch])
            eggs_per_day.append(eggs_laid * aliens_per_day[day])

            print("Day " + str(day) + "... Number of eggs laid on this day = " + str(eggs_per_day[day]) + " Number of aliens = " + str(aliens_per_day[day]))


if __name__ == "__main__":

    total_days = 30
    eggs_laid = 3
    days_to_hatch = 5
    starting_aliens = 5

    alien_eggs(eggs_laid, days_to_hatch, total_days, starting_aliens)
