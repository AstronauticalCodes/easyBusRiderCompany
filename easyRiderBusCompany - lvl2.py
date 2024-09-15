# Write your code here
import json
import re
import string


class EasyRider:
    errorDict = {'bus_id': 0, 'stop_id': 0, 'stop_name': 0, 'next_stop': 0, 'stop_type': 0, 'a_time': 0}
    suffixes = ['Road', 'Avenue', 'Boulevard', 'Street']
    characters = ['S', 'O', 'F']
    formatErrorDict = {'stop_name': 0, 'stop_type': 0, 'a_time': 0}

    def __init__(self):
        self.user = input()[1:-1]
        self.userDict = eval(self.user)
        # self.catchErrors()
        # self.output()
        self.formatErrors()
        self.formatOutput()

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

    def output(self):
        print(f'Type and required field validation: {sum(self.errorDict.values())} errors')
        for error in self.errorDict:
            print(f'{error}: {self.errorDict[error]}')

    def formatOutput(self):
        print(f'Format validation: {sum(self.formatErrorDict.values())} errors')
        for error in self.formatErrorDict:
            print(f'{error}: {self.formatErrorDict[error]}')

EasyRider()


