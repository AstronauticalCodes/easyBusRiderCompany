# Write your code here
import json
import string


class EasyRider:
    errorDict = {'bus_id': 0, 'stop_id': 0, 'stop_name': 0, 'next_stop': 0, 'stop_type': 0, 'a_time': 0}
    suffixes = ['Road', 'Avenue', 'Boulevard', 'Street']
    characters = ['S', 'O', 'F']

    def __init__(self):
        self.user = input()[1:-1]
        self.userDict = eval(self.user)
        self.catchErrors()
        self.output()

    def catchErrors(self):
        for index, dict in enumerate(self.userDict, start=1):
            if not isinstance(dict['bus_id'], int):
                self.errorDict['bus_id'] += 1
            if not isinstance(dict['stop_id'], int) or len(str(dict['stop_id'])) < 1:
                self.errorDict['stop_id'] += 1
            if not isinstance(dict['stop_name'], str) or len(str(dict['stop_name'])) < 1:
                self.errorDict['stop_name'] += 1

            # if not isinstance(dict['stop_name'], str) or len(dict['stop_name']) < 1:
            #     self.errorDict['stop_name'] += 1
            # elif dict['stop_name'].split()[0][0] not in string.ascii_uppercase:
            #     self.errorDict['stop_name'] += 1
            # elif (len(str(dict['stop_name']).split()) > 1 and dict['stop_name'].split()[-1] not in self.suffixes) or (dict['stop_name'].split()[0] not in self.suffixes):
            #     self.errorDict['stop_name'] += 1
            # self.stop_name(dict['stop_name'], index)
            if not isinstance(dict['next_stop'], int):
                self.errorDict['next_stop'] += 1
            if dict['stop_type'] not in self.characters and len(str(dict['stop_type'])) > 0:
                self.errorDict['stop_type'] += 1
            if not isinstance(dict['a_time'], str) or len(str(dict['a_time'])) < 1:
                self.errorDict['a_time'] += 1

    def stop_name(self, stopName, index):
        if len(str(stopName).split()) < 2:
            print('first', (str(stopName).split()), index)
            self.errorDict['stop_name']  += 1
        elif str(stopName).split()[0][0] not in string.ascii_uppercase:
            print('second', str(stopName).split()[0][0], index)
            self.errorDict['stop_name'] += 1
        elif str(stopName).split()[-1] not in self.suffixes:
            print('third', str(stopName).split()[1], index)
            self.errorDict['stop_name'] += 1
        else:
            print(33)

        # if len(str(stopName)) > 1 and not isinstance(stopName, (int, float)):
        #     if len(stopName.split()) > 1:
        #         if stopName.split()[-1] not in self.suffixes:
        #             self.errorDict['stop_name'] += 1
        #     elif len(stopName.split()) == 1 and stopName[0] not in string.ascii_uppercase:
        #         self.errorDict['stop_name'] += 1
        # else:
        #     self.errorDict['stop_name'] += 1

    def output(self):
        print(f'Type and required field validation: {sum(self.errorDict.values())} errors')
        for error in self.errorDict:
            print(f'{error}: {self.errorDict[error]}')

EasyRider()

