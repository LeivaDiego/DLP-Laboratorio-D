import os
import graphviz

# Configuración de la ruta de Graphviz.
os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin"

# Función para mostrar un nodo del árbol.
def show_node(node, visual_tree):
    if (node is not None):
        label = str(node.value) if ((node.left != None) or (node.right != None) or (node.value.startswith("#"))) else str(chr(int(node.value)))
        visual_tree.node(str(id(node)), label, shape="circle")
        if (node.left != None):
            visual_tree.edge(str(id(node)), str(id(node.left)))
            show_node(node.left, visual_tree)
        if (node.right != None):
            visual_tree.edge(str(id(node)), str(id(node.right)))
            show_node(node.right, visual_tree)

# Función para visualizar un árbol.
def show_expression_tree(root, view=True, name=""):
    visual_tree = graphviz.Digraph(comment="Expression Tree")
    show_node(root, visual_tree)
    visual_tree.render(f"./out/mega_tree{name}", format="png", view=view, cleanup=True)
