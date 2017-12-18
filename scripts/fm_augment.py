from gherkin3.parser import Parser
import xml.etree.ElementTree as et
import graphviz as gv
from os import listdir, path, makedirs
import argparse
import json
import pprint
import hashlib

arg_parser = argparse.ArgumentParser(description='Draw dot file from FeatureIDE model.xml')
arg_parser.add_argument('model_xml_file', help="Location of the model XML file")
arg_parser.add_argument('features_dir', help="Location of the feature files")
arg_parser.add_argument('output_dir', help="Location where the output file should be rendered")
arg_parser.add_argument('--output_filename', default="feature_model", help="Name to use for the output file")

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
        tags[tag_name].append("F: " + feature_parsed['name'])

    for scenario in feature_parsed['scenarioDefinitions']:
        for tag in scenario['tags']:
            tag_name = tag['name'][1:] # remove @
            if tag_name not in tags:
                tags[tag_name] = []
            tags[tag_name].append("S: " + scenario['name'])


def parseFeature(feature, parent, graph):
    feature_name = feature.get("name")
    bgcolor = "white"
    if feature.get("abstract") is not None:
        bgcolor = "#cccccc"
    graph.attr('node', fillcolor=bgcolor, style='filled', shape='box')
    graph.node(feature_name, feature_name)
    if feature_name in tags:
        tags_for_feature = tags[feature_name]
        for piece_name in tags_for_feature:
            piece_hash = hashlib.sha256(piece_name.encode('utf-8')).hexdigest()
            graph.node(piece_hash, piece_name)
            graph.edge(feature_name, piece_hash)
    if parent is not None:
        parent_name = parent.get("name")
        arrowhead = "odot"
        if feature.get("mandatory") is not None:
            arrowhead = "dot"
        graph.edge(parent_name, feature_name, arrowhead=arrowhead)
    for child in feature.getchildren():
        parseFeature(child, feature, graph)

tree = et.parse(args.model_xml_file)
root = tree.getroot()
features = root.find('struct')
graph = gv.Digraph(format="svg")

for feature in features.getchildren():
    parseFeature(feature, None, graph)

graph.render(filename=path.join(args.output_dir, args.output_filename))
