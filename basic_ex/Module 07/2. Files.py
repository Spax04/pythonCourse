# You are working as a data scientist for a fictional cybersecurity company. As part of your job, you need to analyze log files generated by various network devices. Each log file contains multiple entries, and each entry follows a specific format:
#
# Timestamp | Source IP | Destination IP | Protocol | Status
#
# Your task is to create a Python class called "LogAnalyzer" that performs the following operations:
#
# 1.	Read the log file and count the total number of entries.
# 2.	Find the percentage of successful connections (entries with a "Status" of "Success") out of the total number of entries.
# 3.	Determine the unique source IP addresses present in the log file.
# 4.	Calculate the average number of entries per source IP address.
# 5.	Write the analysis results to a new file named "log_analysis.txt".

class LogAnalyzer:
    def __init__(self, log_file_path):

	# Your code here


    def analyze_log_file(self):

	# Your code here


# Usage example:
analyzer = LogAnalyzer('log_file.txt')
analyzer.analyze_log_file()
