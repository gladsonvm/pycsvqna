__author__ = 'gladson'
import json
import csv
import pandas as pd


def extract_stopwords(source):
    with open(source, 'r') as json_file:
        ugly_json = json_file.readlines()
    formatted_json = []
    stopwords = []
    [formatted_json.append(json.loads(x)) for x in ugly_json]
    [stopwords.append(formatted_json[x]['properties']['word']) for x in xrange(len(formatted_json))]


def read_csv(csvfile):
    keywords = []
    answer_map = {}
    answer_list = []
    panda_csv_object = pd.read_csv(csvfile)
    summary = panda_csv_object.summary
    description = panda_csv_object.description
    resolution = panda_csv_object.resolution
    print ('\n Extracting keywords from csv file. Please wait....\n')
    for x in xrange(len(summary)):
        if type(summary[x]) != float:
            intersection = set.intersection(*[set(stopwords), set(summary[x].lower().split(' '))])
            answer_map[resolution[x]] = set(summary[x].lower().split(' '))-intersection
            kwords = list(set(summary[x].lower().split(' '))-intersection)
            keywords.append(kwords)
    print ('\nSuccessfully extracted %d keywords from csv file\n', len(keywords))


