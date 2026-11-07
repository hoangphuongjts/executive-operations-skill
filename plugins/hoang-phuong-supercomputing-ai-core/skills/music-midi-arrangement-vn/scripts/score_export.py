#!/usr/bin/env python3
"""Export a simple monophonic melody to SMF MIDI and MusicXML. stdlib only, offline.
No interpretation of lyrics, no external calls, no MIDI device playback.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import struct
import xml.etree.ElementTree as ET

ALLOWED_BEATS = {0.25: '16th', 0.5: 'eighth', 1.0: 'quarter', 2.0: 'half', 4.0: 'whole'}
PITCH_NAMES = ('C', 'C', 'D', 'D', 'E', 'F', 'F', 'G', 'G', 'A', 'A', 'B')
ALTER = (0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0)


def validate(spec):
    if not isinstance(spec, dict):
        raise ValueError('Song specification must be a JSON object')
    bpm = spec.get('bpm')
    if type(bpm) is not int or not 40 <= bpm <= 240:
        raise ValueError('bpm must be an integer between 40 and 240')
    if spec.get('time_signature', [4, 4]) != [4, 4]:
        raise ValueError('only 4/4 time signature is supported')
    program = spec.get('program', 0)
    if type(program) is not int or not 0 <= program <= 127:
        raise ValueError('program must be an integer MIDI instrument 0..127')
    notes = spec.get('notes')
    if not isinstance(notes, list) or not 1 <= len(notes) <= 512:
        raise ValueError('notes length must be 1..512')
    for i, n in enumerate(notes):
        if not isinstance(n, dict) or type(n.get('pitch')) is not int or not 0 <= n['pitch'] <= 127:
            raise ValueError(f'note {i}: pitch must be integer 0..127')
        if type(n.get('beats')) not in (int, float) or float(n['beats']) not in ALLOWED_BEATS:
            raise ValueError(f'note {i}: beats must be one of {sorted(ALLOWED_BEATS)}')
    return bpm, program, notes


def vlq(number):
    if number < 0:
        raise ValueError('negative delta')
    data = [number & 127]
    number >>= 7
    while number:
        data.insert(0, 128 | (number & 127))
        number >>= 7
    return bytes(data)


def midi_bytes(spec):
    bpm, program, notes = validate(spec)
    ticks_per_quarter = 480
    tempo = round(60_000_000 / bpm)
    track = bytearray()
    track.extend(b'\x00\xff\x51\x03' + tempo.to_bytes(3, 'big'))
    track.extend(b'\x00\xff\x58\x04\x04\x02\x18\x08')
    track.extend(b'\x00\xc0' + bytes([program]))
    for note in notes:
        track.extend(b'\x00\x90' + bytes([note['pitch'], 85]))
        track.extend(vlq(round(note['beats'] * ticks_per_quarter)) + b'\x80' + bytes([note['pitch'], 0]))
    track.extend(b'\x00\xff\x2f\x00')
    return b'MThd' + struct.pack('>IHHH', 6, 0, 1, ticks_per_quarter) + b'MTrk' + struct.pack('>I', len(track)) + track


def musicxml_bytes(spec):
    bpm, program, notes = validate(spec)
    score = ET.Element('score-partwise', version='4.0')
    ET.SubElement(ET.SubElement(score, 'work'), 'work-title').text = str(spec.get('title', 'Untitled'))[:100]
    ET.SubElement(score, 'movement-title').text = str(spec.get('title', 'Untitled'))[:100]
    part_list = ET.SubElement(score, 'part-list')
    score_part = ET.SubElement(part_list, 'score-part', id='P1')
    ET.SubElement(score_part, 'part-name').text = 'Melody'
    part = ET.SubElement(score, 'part', id='P1')
    position = 0.0
    measure_num = 0
    measure = None
    for note in notes:
        beats = float(note['beats'])
        if measure is None or position >= 4:
            measure_num += 1
            measure = ET.SubElement(part, 'measure', number=str(measure_num))
            position = 0.0
            if measure_num == 1:
                attributes = ET.SubElement(measure, 'attributes')
                ET.SubElement(attributes, 'divisions').text = '4'
                ET.SubElement(ET.SubElement(attributes, 'key'), 'fifths').text = '0'
                time = ET.SubElement(attributes, 'time')
                ET.SubElement(time, 'beats').text = '4'
                ET.SubElement(time, 'beat-type').text = '4'
                clef = ET.SubElement(attributes, 'clef')
                ET.SubElement(clef, 'sign').text = 'G'
                ET.SubElement(clef, 'line').text = '2'
                direction = ET.SubElement(measure, 'direction', placement='above')
                sound = ET.SubElement(direction, 'sound', tempo=str(bpm))
        if position + beats > 4:
            raise ValueError('a note crosses a 4/4 measure boundary; split it in the input')
        n = ET.SubElement(measure, 'note')
        pitch = ET.SubElement(n, 'pitch')
        number = note['pitch']
        ET.SubElement(pitch, 'step').text = PITCH_NAMES[number % 12]
        if ALTER[number % 12]:
            ET.SubElement(pitch, 'alter').text = '1'
        ET.SubElement(pitch, 'octave').text = str(number // 12 - 1)
        ET.SubElement(n, 'duration').text = str(round(beats * 4))
        ET.SubElement(n, 'type').text = ALLOWED_BEATS[beats]
        position += beats
    return ET.tostring(score, encoding='utf-8', xml_declaration=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input', required=True)
    ap.add_argument('--midi')
    ap.add_argument('--musicxml')
    args = ap.parse_args()
    if not args.midi and not args.musicxml:
        ap.error('Provide --midi, --musicxml or both')
    spec = json.loads(Path(args.input).read_text(encoding='utf-8'))
    validate(spec)
    # Build BOTH exports before writing either to reduce partial side effects.
    mid = midi_bytes(spec) if args.midi else None
    xml = musicxml_bytes(spec) if args.musicxml else None
    if mid is not None:
        Path(args.midi).write_bytes(mid)
    if xml is not None:
        Path(args.musicxml).write_bytes(xml)
    print(json.dumps({'midi':args.midi, 'musicxml':args.musicxml, 'notes':len(spec['notes'])}, ensure_ascii=False))

if __name__ == '__main__':
    main()
