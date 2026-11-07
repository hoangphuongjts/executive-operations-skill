import importlib.util
import sys
import unittest
from pathlib import Path
import xml.etree.ElementTree as ET

FILE = Path(__file__).resolve().parents[1] / 'scripts' / 'score_export.py'
spec = importlib.util.spec_from_file_location('score_export', FILE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class ExportTests(unittest.TestCase):
    def setUp(self):
        self.music = {'title':'Tự sáng tác','bpm':96,'time_signature':[4,4],
                      'notes':[{'pitch':60,'beats':1},{'pitch':64,'beats':1},
                               {'pitch':67,'beats':2},{'pitch':69,'beats':4}]}
    def test_midi_structure(self):
        b = module.midi_bytes(self.music)
        self.assertEqual(b[:4], b'MThd')
        self.assertEqual(b[14:18], b'MTrk')
        self.assertTrue(b.endswith(bytes([0,255,47,0])))
    def test_musicxml_structure(self):
        x = ET.fromstring(module.musicxml_bytes(self.music))
        self.assertEqual(x.attrib['version'], '4.0')
        self.assertEqual(len(x.findall('.//note')),4)
    def test_reject_invalid_bpm(self):
        self.music['bpm'] = -1
        with self.assertRaises(ValueError): module.midi_bytes(self.music)
    def test_reject_cross_bar(self):
        self.music['notes'] = [{'pitch':60,'beats':2},{'pitch':64,'beats':4}]
        with self.assertRaises(ValueError): module.musicxml_bytes(self.music)
    def test_reject_invalid_pitch(self):
        self.music['notes'][0]['pitch'] = 400
        with self.assertRaises(ValueError): module.musicxml_bytes(self.music)

if __name__ == '__main__': unittest.main()
