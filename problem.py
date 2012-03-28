"""Sphinx extension for adding problem directive.
"""

from sphinx.util.compat import Directive
from docutils import nodes
import sys


class problem(nodes.Element):
    pass


class example(nodes.Element):
    pass


class ProblemDirective(Directive):
    has_content = True
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True    
    option_spec = {}

    def run(self):
        node = self._create_node()
        node.document = self.state.document
        node.line = self.lineno

        inodes, messages = self.state.inline_text(self.arguments[0],
                                                  self.lineno)
        node.extend(inodes)
        
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node] + messages
        
    def _create_node(self):
        return problem()
        

class ExampleDirective(ProblemDirective):
    def _create_node(self):
        return example()


def process_problem_nodes(app, doctree, docname):
    def process(nodecls, label):
        index = 1
        for node in doctree.traverse(nodecls):
            out = [nodes.strong(None, "%s %d: " % (label, index))] + node.children
            p = nodes.paragraph()
            p.document = node.document
            p.line = node.line
            p.children = out
            node.replace_self(p)
            index += 1
    process(problem, "Problem")
    process(example, "Example")


def setup(app):
    app.add_node(problem)
    app.add_directive('problem', ProblemDirective)
    app.add_node(example)
    app.add_directive('example', ExampleDirective)
    app.connect('doctree-resolved', process_problem_nodes)
