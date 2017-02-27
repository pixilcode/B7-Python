from show import Show

#Excercise 2 Improvment: TV Stations
tvStations = [[], [], [], [], [], [], []];
days = (('Su', 'Sunday'), ('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('Fr', 'Friday'), ('Sa', 'Saturday'));

complete = False;

while not complete:
    addItem = input('Add show? (Y/N) >>> ');
    if(addItem.upper() == 'Y'):
        show = input('Show >>> ');
        showDay = input('Day of the Week (Su, Mo, Tu, We, Th, Fr, Sa) >>> ');
        startTime = input('Start Time >>> ');
        endTime = input('End Time >>> ');
        for day in range(len(days)):
            if showDay == days[day][0]:
                tvStations[day].append(Show(show, showDay, startTime, endTime));
                break;
        else:
            print('The given day is invalid');
    else:
        complete = True;
        break;

for day in range(len(days)):
    print(days[day][1]);
    for show in tvStations[day]:
        print('Show: ' + show.name + '\tStart Time: ' + show.startTime + '\tEnd Time: ' + show.endTime);
    print();

print('*' * 30);
