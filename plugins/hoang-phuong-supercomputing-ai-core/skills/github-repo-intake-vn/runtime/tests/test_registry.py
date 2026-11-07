import unittest
from source.cluster_registry import inventory,REPLACEMENTS
class TestRegistry(unittest.TestCase):
 def test_sixteen_clusters(self):
  x=inventory();self.assertEqual(len(x),16);self.assertEqual([a['cluster_id'] for a in x],list(range(1,17)))
 def test_targets_are_not_falsely_installed(self):
  self.assertEqual(sum(x['upstream_installed'] for x in inventory()),0)
 def test_four_replacements(self):
  self.assertEqual(set(REPLACEMENTS),{3,9,10,16})
