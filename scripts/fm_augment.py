from gherkin3.parser import Parser
import xml.etree.ElementTree as et
import graphviz as gv
from os import listdir, path, makedirs
import argparse
import json
import pprint
import hashlib
import pprint

arg_parser = argparse.ArgumentParser(description='Draw dot file from FeatureIDE model.xml')
arg_parser.add_argument('model_xml_file', help="Location of the model XML file")
arg_parser.add_argument('features_dir', help="Location of the feature files")
arg_parser.add_argument('test_results_file', help="Location of the test results")
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

def parseFeature(feature, parent, graph, test_results):
    feature_name = feature.get("name")
    has_failed_test = False
    fill_color = "white"

    for child in feature.getchildren():
        has_failed_test = parseFeature(child, feature, graph, test_results)

    # add gherkin nodes
    if feature_name in tags:
        tags_for_feature = tags[feature_name]
        with graph.subgraph(name="cluster_" + feature_name) as subgraph:
            feature_name_hash = hashlib.sha256(feature_name.encode('utf-8')).hexdigest()
            subgraph_root_name = "cluster_" + feature_name_hash
            subgraph.node(subgraph_root_name, label="", shape="none", width="0", height="0", style="invis")
            graph.edge(feature_name, subgraph_root_name)
            subgraph.attr(rankdir="TB")
            previous = subgraph_root_name
            for piece_name in tags_for_feature:
                piece_hash = hashlib.sha256(piece_name.encode('utf-8')).hexdigest()
                line_color = "#000000"
                if piece_name[3:] in test_results:
                    if test_results[piece_name[3:]] == True:
                        line_color = "#00cc00"
                    elif test_results[piece_name[3:]] == False:
                        line_color = "#ff0000"
                        has_failed_test = True
                subgraph.node(piece_hash, piece_name, color=line_color, fillcolor="white", shape="box")
                subgraph.edge(previous, piece_hash, style="invis", weight="0")
                previous = piece_hash

    # add fmfeature node
    fillcolor = "white"
    line_color = "green"
    if feature.get("abstract") is not None:
        fillcolor = "#cccccc"
    if has_failed_test is True:
        fillcolor = "#ffeeee"
        line_color = "red"
    graph.node(feature_name, feature_name, fillcolor=fillcolor, style='filled', shape='box', color=line_color)
    if parent is not None:
        parent_name = parent.get("name")
        arrowhead = "odot"
        if feature.get("mandatory") is not None:
            arrowhead = "dot"
        graph.edge(parent_name, feature_name, arrowhead=arrowhead)

    return has_failed_test

# Parse tests results
test_results_file = args.test_results_file #"../tests/_output/report.xml"
tree = et.parse(test_results_file)
root = tree.getroot()
acceptance_suite = root.find('testsuite')

test_results = {}
for testcase in acceptance_suite:
    scenario_name = testcase.get("feature")
    passed = True
    if testcase.find("failure") is not None:
        passed = False
    test_results[scenario_name] = passed

# Parse feature model
tree = et.parse(args.model_xml_file)
root = tree.getroot()
features = root.find('struct')
graph = gv.Digraph(format="svg")

for feature in features.getchildren():
    parseFeature(feature, None, graph, test_results)

graph.render(filename=path.join(args.output_dir, args.output_filename))
