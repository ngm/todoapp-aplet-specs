# coding=utf-8
from gherkin3.parser import Parser
from os import listdir, path, makedirs
import hashlib
import graphviz as gv
import argparse

arg_parser = argparse.ArgumentParser(description='Parse feature files, print a text file and a graph image.')
arg_parser.add_argument('features_dir', help="Location of the feature files")
arg_parser.add_argument('output_dir', help="Location where the output files should be rendered")
arg_parser.add_argument('--output_filename', default="fm_to_bdd_features_map", help="Name to use for the output files")

args = arg_parser.parse_args()

gherkin_parser = Parser()
tags = {}

for feature_file in listdir(args.features_dir):
    feature_file = open(path.join(args.features_dir, feature_file), "r")
    feature_parsed = gherkin_parser.parse(feature_file.read())

    for tag in feature_parsed['tags']:
        tag_name = tag['name'][1:] # remove @
        if tag_name not in tags:
            tags[tag_name] = []
        tags[tag_name].append("Feature: " + feature_parsed['name'])

    for scenario in feature_parsed['scenarioDefinitions']:
        for tag in scenario['tags']:
            tag_name = tag['name'][1:] # remove @
            if tag_name not in tags:
                tags[tag_name] = []
            tags[tag_name].append("Scenario: " + scenario['name'])


if not path.exists(args.output_dir):
    makedirs(args.output_dir)

output = open(path.join(args.output_dir, args.output_filename + ".txt"), "w")
graph = gv.Graph(format="svg")
graph.body.extend(['rankdir=LR', 'size="5,5"'])

for tag_name, tag in tags.items():
    print(tag_name, file=output)
    tag_hash = hashlib.sha256(tag_name.encode('utf-8')).hexdigest()

    graph.node(tag_hash, tag_name)

    for gherkinpiece_name in tag:
        gherkinpiece_hash = hashlib.sha256(gherkinpiece_name.encode('utf-8')).hexdigest()
        graph.node(gherkinpiece_hash, gherkinpiece_name)
        graph.edge(tag_hash, gherkinpiece_hash)
        print("     {:s}".format(gherkinpiece_name), file=output)

graph.render(filename=path.join(args.output_dir,args.output_filename))
