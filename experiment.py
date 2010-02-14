"""Loads and Displays Experiment data

This program is used to load experiment data into experiment objects.

The objects can render themselves into web format.
"""

__author__ = "Soren Burkhart (soren.burkhart@gmail.com)"
__version__ = "$Revision: 0.23 $"
__date__ = "$Date: 2010/01/29 13:36:22 $"
__copyright__ = "Copyright (c) 2010 Soren Burkhart"
__license__ = "Python"

#Define exceptions
class ExperimentError(Exception): pass
class FileMissingError(ExperimentError): pass

import csv

class Loader:
    """Loader creates experiments from a file"""
    def __init__(self, file, input_count):
        if None == file:
            raise FileMissingError, 'File cannot be None'
        self.file = file
        self.input_count = input_count
        
        self.experiments = []
    
    def load(self):
        """load in the experiments from the Experiment file.
            Assumes file is a CSV file.
            Format is independent variables TIME REPLICATE OBSERVED
        """
        reader = csv.reader(self.file)
        # get the header row
        header = reader.next()
        
        input_header = header[:self.input_count]
        time_header = header[self.input_count]
        replicate_header = header[self.input_count+1]
        observation_header = header[self.input_count+2:]
        
        # experiment variable
        e = None
        for row in reader:
            # Loop through experiment data
            if None == e:
                # first time through
                input_values = row[0:self.input_count]
                e = Experiment(input_header, input_values, time_header, replicate_header, observation_header)
            elif e.input_values != row[0:self.input_count]:
                # done processing current experiment add to list
                self.experiments.append(e)
                # create new experiment            
                input_values = row[0:self.input_count]
                e = Experiment(input_header, input_values, time_header, replicate_header, observation_header)

            e.add_row_of_data(row)
        
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
        "Adds a row of replicate data"
        self.replicates.append(Replicate(len(self.replicates)+1,data))
    
    def means(self):
        "returns the means of the replicate data.  If there are missing data points returns None"
        m = []
        
        # create an empty array with zero value
        for i in xrange(len(self.replicates[0].data)):
            m.append(0.0)
            
        # Add up all the values
        # Insert None for blank entries
        for replicate in self.replicates:
            for (counter,value) in enumerate(replicate.data):
                #print "counter = %d value = %s m[%d]= %s (m[counter] == None) or (value == None) = %s" %(counter,value,counter,m[counter],(m[counter] == None) or (value == None))
                if (m[counter] == None) or (value == None):
                    m[counter] = None
                else:
                    m[counter] += value
        
        # Divide by the number of replicates to get the mean
        for (counter,replicate_sum) in enumerate(m):
            if replicate_sum != None:
                m[counter] = replicate_sum/float(len(self.replicates))
        
        return m
        
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
        
        self.set_description()
        self.observations = []
        
    def set_description(self):
        """Set the description for the experiment"""
        self.description = "Experiment: " + " ".join(["%s %s" % (value, header) for value, header in zip(self.input_values, self.header.input_header)])

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

        