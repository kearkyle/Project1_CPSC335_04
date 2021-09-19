# Author: Vong Chen

from operator import itemgetter

def groupSchedule(pers1Schedule, pers1DailyAct, pers2Schedule, pers2DailyAct, duration):
    updatedSchedule1 = updateSchedule(pers1Schedule, pers1DailyAct)
    # print(updatedSchedule1)
    updatedSchedule2 = updateSchedule(pers2Schedule, pers2DailyAct)
    # print(updatedSchedule2)
    mergedSchedule = mergedSchedules(updatedSchedule1, updatedSchedule2)
    # print(mergedSchedule)
    sortedSchedules = sortedAllSchedules(mergedSchedule)
    # print(sortedSchedules)
    print("Available Schedule is: ", matchedAvailabilities(sortedSchedules, duration))


def updateSchedule(Schedule, DailyAct):
    updatedSchedule = Schedule[:]  # make a copy of the schedule
    updatedSchedule.insert(0, ['00:00', DailyAct[0]])  # update unavailable schedules and add early morning hours
    updatedSchedule.append([DailyAct[1], '23:59'])  # update unavailable schedules and add after work hours
    i = 0
    while i < len(updatedSchedule):
        if len(updatedSchedule[i][0]) == 4:
            updatedSchedule[i][0] = "0" + updatedSchedule[i][0]
        if len(updatedSchedule[i][1]) == 4:
            updatedSchedule[i][1] = "0" + updatedSchedule[i][1]
        i += 1
    return updatedSchedule
    # return list(map(lambda s: [convertToMinutes(s[0]), convertToMinutes(s[1])], updatedSchedule))


def mergedSchedules(pers1Schedule, pers2Schedule):
    merged = []
    i, j = 0, 0
    while i < len(pers1Schedule):
        merged.append(pers1Schedule[i])
        i += 1
    while j < len(pers2Schedule):
        merged.append(pers2Schedule[j])
        j += 1
    return merged


def sortedAllSchedules(Schedule):
    # Todo: write a function to  arrange all schedules. New meeting starts AFTER the end of current meeting.
    allSchedules = Schedule[:]
    allSchedules.sort(key=itemgetter(0, 1))
    return allSchedules


def matchedAvailabilities(Schedule, duration):
    # Todo: write a function to match all availabilities
    availabilities = []  # create empty list to store all the available times
    tempSchedule = Schedule[:]  # make a copy of Schedule to avoid changing the original Schedule in memory
    tempTime = tempSchedule[0]  # assigning current Time to be the one at index 0
    i = 0
    while i < len(tempSchedule):  # this while loop will go through the Schedule list
        # and will append the available times to empty list of availabilities when the algorithm is true
        if tempTime[1] == tempSchedule[i][0] and \
                (convertToMinutes(tempSchedule[i][0])
                 - convertToMinutes(tempTime[1])) \
                < int(duration):
            tempTime = tempSchedule[i]
        elif tempTime[1] < tempSchedule[i][0] and \
                (convertToMinutes(tempSchedule[i][0])
                 - convertToMinutes(tempTime[1])) \
                >= int(duration):
            availableTime = [tempTime[1], tempSchedule[i][0]]
            availabilities.append(availableTime)
            tempTime = tempSchedule[i]
        elif tempSchedule[i][0] <= tempTime[1] <= tempSchedule[i][1]:
            tempTime = [tempTime[1], tempSchedule[i][1]]

        i += 1
    return availabilities


def convertToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes


def main():
    sp_chars = ['‘', '’']
    pers1Schedule = input("Enter schedule for person 1:")
    for i in sp_chars:
        pers1Schedule = pers1Schedule.replace(i, "'")  # Replacing the ‘,’ characters into '
    pers1Schedule = eval(pers1Schedule)  # This will convert the string into a list of list
    pers2Schedule = input("Enter schedule for person 2:")
    for i in sp_chars:
        pers2Schedule = pers2Schedule.replace(i, "'")  # Replacing the ‘,’ characters into '
    pers2Schedule = eval(pers2Schedule)  # This will convert the string into a list of list
    pers1DailyAct = input("Enter Daily Availability for pers 1: ")
    for i in sp_chars:
        pers1DailyAct = pers1DailyAct.replace(i, "'")  # Replacing the ‘,’ characters into '
    pers1DailyAct = eval(pers1DailyAct)  # This will convert the string into a list of list
    pers2DailyAct = input("Enter Daily Availability for pers 2: ")
    for i in sp_chars:
        pers2DailyAct = pers2DailyAct.replace(i, "'")  # Replacing the ‘,’ characters into '
    pers2DailyAct = eval(pers2DailyAct)  # This will convert the string into a list of list
    duration = input("Enter duration of the proposed meeting: ")
    groupSchedule(pers1Schedule, pers1DailyAct, pers2Schedule, pers2DailyAct, duration)


if __name__ == "__main__":
    main()
