# Write your code here
import json
import re
import string


class EasyRider:
    errorDict = {'bus_id': 0, 'stop_id': 0, 'stop_name': 0, 'next_stop': 0, 'stop_type': 0, 'a_time': 0}
    suffixes = ['Road', 'Avenue', 'Boulevard', 'Street']
    characters = ['S', 'O', 'F']
    formatErrorDict = {'stop_name': 0, 'stop_type': 0, 'a_time': 0}
    busRouteStops = {}
    transferStopDict = {}
    buslines = {}
    finishStops = set()
    startStops = set()
    startTransferFinsish = set()
    onDemandStops = set()

    def __init__(self):
        self.user = input()[1:-1]
        self.userDict = eval(self.user)
        # self.catchErrors()
        # self.output()
        # self.formatErrors()
        # self.formatOutput()
        # self.busStops()
        # self.busStopsOutput()
        # self.stops()
        # self.checkStartFinish()
        # self.stopsOutput()
        # self.timeCheck()
        self.transferStartFinish()
        self.checkOnDemand()

    def catchErrors(self):
        for index, dict in enumerate(self.userDict, start=1):
            if not isinstance(dict['bus_id'], int):
                self.errorDict['bus_id'] += 1
            if not isinstance(dict['stop_id'], int) or len(str(dict['stop_id'])) < 1:
                self.errorDict['stop_id'] += 1
            if not isinstance(dict['stop_name'], str) or len(str(dict['stop_name'])) < 1:
                self.errorDict['stop_name'] += 1
            if not isinstance(dict['next_stop'], int):
                self.errorDict['next_stop'] += 1
            if dict['stop_type'] not in self.characters and len(str(dict['stop_type'])) > 0:
                self.errorDict['stop_type'] += 1
            if not isinstance(dict['a_time'], str) or len(str(dict['a_time'])) < 1:
                self.errorDict['a_time'] += 1

    def formatErrors(self):
        for dict in self.userDict:
            self.stopName(dict['stop_name'])
            self.stopType(dict['stop_type'])
            self.aTime(dict['a_time'])

    def output(self):
            print(f'Type and required field validation: {sum(self.errorDict.values())} errors')
            for error in self.errorDict:
                print(f'{error}: {self.errorDict[error]}')

    def stopName(self, stop_name):
        pattern = re.compile(r'[A-Z][\w ]+ (Road|Avenue|Boulevard|Street)$')

        match = re.match(pattern, str(stop_name))
        if not match:
            self.formatErrorDict['stop_name'] += 1

    def stopType(self, stop_type):
        if stop_type not in self.characters and len(stop_type) > 0:
            self.formatErrorDict['stop_type'] += 1

    def aTime(self, a_time):
        pattern = re.compile(r'[012][\d]:[012345][\d]')
        match = re.sub(pattern, '', a_time)

        if len(match) > 1:
            self.formatErrorDict['a_time'] += 1

    def formatOutput(self):
        print(f'Format validation: {sum(self.formatErrorDict.values())} errors')
        for error in self.formatErrorDict:
            print(f'{error}: {self.formatErrorDict[error]}')

    def busStops(self):
        for dict in self.userDict:
            if dict['bus_id'] not in self.busRouteStops:
                self.busRouteStops[dict['bus_id']] = 0
            self.busRouteStops[dict['bus_id']] += 1

    def busStopsOutput(self):
        print(f'Line names and number of stops:')
        for route in self.busRouteStops:
            print(f'bus_id: {route}, stops: {self.busRouteStops[route]}')

    def stops(self):
        for dict in self.userDict:
            if dict['stop_name'] not in self.transferStopDict:
                self.transferStopDict[dict['stop_name']] = 0
            self.transferStopDict[dict['stop_name']] += 1
            if dict['bus_id'] not in self.buslines:
                self.buslines[dict['bus_id']] = []
            self.buslines[dict['bus_id']].append(dict['stop_type'])
            if dict['stop_type'] == 'F':
                self.finishStops.add(dict['stop_name'])
            elif dict['stop_type'] == 'S':
                self.startStops.add(dict['stop_name'])

    def checkStartFinish(self):
        for busLine in self.buslines:
            lst = self.buslines[busLine]
            if lst.count('S') != 1 or lst.count('F') != 1:
                print(f'There is no start or end stop for the line: {busLine}')
                exit()

    def stopsOutput(self):
        sortedTransfer = [x for x in self.transferStopDict if self.transferStopDict[x] > 1]
        print(f'Start stops: {len(self.startStops)} {sorted(x for x in self.startStops)}')
        print(f'Transfer stops: {len(sortedTransfer)} {sorted(sortedTransfer)}')
        print(f'Finish stops: {len(self.finishStops)} {sorted(x for x in self.finishStops)}')

    def timeCheck(self):
        print('Arrival time test:')
        ids = []
        prevTime = [0, 0, 0]
        error = 0
        for index, dict in enumerate(self.userDict):
            hour, mins, id = int(dict['a_time'][:2]), int(dict['a_time'][-2:]), dict['bus_id']
            # print(prevTime)
            if id != prevTime[2]:
                prevTime = [0, 0, 0]

            if hour <= prevTime[0] and mins < prevTime[1] and id not in ids:
                print(f'bus_id line {dict["bus_id"]}:  wrong time on station {dict["stop_name"]}')
                error += 1
                ids.append(id)

            # else:
            prevTime = [hour, mins, id]

        if error == 0:
            print('OK')

    def transferStartFinish(self):
        for dict in self.userDict:
            stopName = dict['stop_name']
            if dict['stop_type'] in ['S', 'F', '']:
                self.startTransferFinsish.add(stopName)
            elif dict['stop_type'] == 'O':
                self.onDemandStops.add(stopName)

    def checkOnDemand(self):
        print('On demand stops test:')
        intersection = self.startTransferFinsish & self.onDemandStops
        if len(intersection) > 0:
            print(f'Wrong stop type: {sorted(x for x in intersection)}')
        else:
            print('OK')

EasyRider()


