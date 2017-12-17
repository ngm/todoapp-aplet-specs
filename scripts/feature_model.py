import xml.etree.ElementTree as et
import graphviz as gv
import argparse

arg_parser = argparse.ArgumentParser(description='Draw dot file from FeatureIDE model.xml')
arg_parser.add_argument('model_xml_file', help="Location of the model XML file")
arg_parser.add_argument('output_dir', help="Location where the output file should be rendered")
arg_parser.add_argument('--output_filename', default="feature_model", help="Name to use for the output file")

args = arg_parser.parse_args()

def parseFeature(feature, parent, graph):
    feature_name = feature.get("name")
    bgcolor = "white"
    if feature.get("abstract") is not None:
        bgcolor = "#cccccc"
    graph.attr('node', fillcolor=bgcolor, style='filled', shape='box')
    graph.node(feature_name, feature_name)
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

graph.render(filename=args.output_filename)
