#Excercise 2: TV Stations
tvStations = [[], [], [], [], [], [], []];
days = (('Su', 'Sunday'), ('Mo', 'Monday'), ('Tu', 'Tuesday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('Fr', 'Friday'), ('Sa', 'Saturday'));

complete = False;

while not complete:
    addItem = input('Add show? (Y/N) >>> ');
    if(addItem.upper() == 'Y'):
        show = input('Show >>> ');
        showDay = input('Day of the Week (Su, Mo, Tu, We, Th, Fr, Sa) >>> ');
        for day in range(len(days)):
            if showDay == days[day][0]:
                tvStations[day].append(show);
                break;
        else:
            print('The given day is invalid');
    else:
        complete = True;
        break;

for day in range(len(days)):
    print(days[day][1], end = '');
    for show in tvStations[day]:
        print(show.rjust(5), end = '');
    print();

print('*' * 30);
