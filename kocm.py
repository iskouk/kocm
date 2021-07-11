import pandas as pd
import rdfpandas
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, SKOS, DCTERMS

df = pd.read_csv('kocm.csv', index_col = '@id', keep_default_na = True)
namespace_manager = NamespaceManager(Graph())
namespace_manager.bind('skos', SKOS, override = True)
namespace_manager.bind('dcterms', DCTERMS, override = True)
namespace_manager.bind('kocm', Namespace('https://iskouk.org/kocm/'), override = True)
namespace_manager.bind('pav', Namespace('http://purl.org/pav/'), override = True)
g = rdfpandas.to_graph(df, namespace_manager)
ttl = g.serialize(format = 'turtle')
with open('kocm.ttl', 'wb') as file:
   file.write(ttl)
