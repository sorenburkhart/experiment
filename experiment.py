"""Loads and Displays Experiment data

This program is used to load experiment data into experiment objects.

The objects can render themselves into web format.
"""

__author__ = "Soren Burkhart (soren.burkhart@gmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2010/01/29 13:36:22 $"
__copyright__ = "Copyright (c) 2010 Soren Burkhart"
__license__ = "Python"

#Define exceptions
class ExperimentError(Exception): pass
class FileMissingError(ExperimentError): pass

import csv
import copy

class Loader:
    """Loader creates experiments from a file"""
    def __init__(self, file, var_count):
        if None == file:
            raise FileMissingError, 'File cannot be None'
        self.file = file
        self.var_count = var_count
        
        self.experiments = []
    
    def load(self):
        """load in the experiments from the Experiment file.
            Assumes file is a CSV file.
            Format is independent variables TIME REPLICATE OBSERVED
        """
        reader = csv.reader(self.file)
        # get the header row
        header = reader.next()
        
        input_header = header[:self.var_count]
        time_header = header[self.var_count-1]
        replicate_header = header[self.var_count]
        observation_header = header[self.var_count+2:]
        
        # experiment variable
        e = None
        for row in reader:
            ###print row
            # Loop through experiment data
            if None == e:
                ###print "First time"
                # first time through
                input_values = row[0:self.var_count]
                e = Experiment(input_header, input_values, time_header, replicate_header, observation_header)
            elif e.input_values != row[0:self.var_count]:
                ###print "New experiment"
                # done processing current experiment add to list
                self.experiments.append(e)
                # create new experiment            
                input_values = row[0:self.var_count]
                e = Experiment(input_header, input_values, time_header, replicate_header, observation_header)
            
            ###print "adding row"
            e.add_row_of_data(row)
        
        ###print "added last experiment"
        self.experiments.append(e)

class Replicate:
    """Holds a replicate of data for an experiment observation in time."""
    def __init__(self, replicate_number, data):
        "Initialize the data with the replicate number and the data for the observations"
        self.number = replicate_number
        self.data = []
        for value in data:
            if value == '':
                self.data.append(None)
            else:
                self.data.append(float(value))

class Observation:
    """Holds data for an experiment."""
    def __init__(self, observation_time):
        self.time = observation_time
        self.replicates = []

    def add_replicate_data(self, data):
        self.replicates.append(Replicate(len(self.replicates)+1,data))

class Header:
    """Header class holds all the header values"""
    def __init__(self, input_header, time_header, replicate_header, observation_header):
        self.input_header = input_header
        self.time_header = time_header
        self.replicate_header = replicate_header
        self.observation_header = observation_header
        
class Experiment:
    """Experiment class that holds data from observations"""
    def __init__(self, input_header, input_values, time_header, replicate_header, observation_header):
        self.header = Header(input_header, time_header, replicate_header, observation_header)
        self.input_values = input_values
        
        self.time_col = len(input_header)
        self.replicate_col = self.time_col + 1
        self.data_start = self.replicate_col + 1
        #self.data_end = self.data_start + len(self.data_header)
        
        self.set_description()
        self.observations = []
        
    def set_description(self):
        """Set the description for the experiment"""
        self.description = "Experiment: " + " ".join(["%s %s" % (value, header) for value, header in zip(self.input_values, self.header.input_header)])

    def create_replicate_entry_from(self, row):
        """Creates a replicate entry from row"""
        return row[self.data_start:self.data_end]
        
    def create_data_entry_from(self, row):
        """Creates a data entry from row"""
        return {'time': row[self.time_col],
                'replicates': [self.create_replicate_entry_from(row)]}

    def add_row_of_data(self, row):
        """Adds a row of data.
        
        1. Checks to see if the data is a new time set
        2. If not adds the replicate data to the current time set
        """
        
        observation_time = row[self.time_col]
        
        if len(self.observations) == 0:
            "First data set for this experiment"
            self.observations.append(Observation(observation_time))
        elif self.observations[-1].time != observation_time:
            "New time entry"
            self.observations.append(Observation(observation_time))
        
        # Add replicate data
        self.observations[-1].add_replicate_data(row[self.data_start:])

        