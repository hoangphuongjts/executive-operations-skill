# Music Studio — additive integration for Hoàng Phương Core v16.0.48

Source live plugin: v16.0.47, release pluginrel_6aee153871ec8191987946639e9200ae.

Adds **four instruction skills** for music composition and validation. Uses canonical cluster 13 `Nội dung & đa phương thức`, with secondary clusters 08 and 16. Does not rename or relocate anything in the original 16-cluster registry; records the additive mapping in `MUSIC_STUDIO_CLUSTER13_DELTA.json`. Preserves full 128 agents, seven original skills, 108 study codes, previous manifests, skills, host bindings and historical records.

Built-in offline sample exporter: produces **MIDI/MusicXML**, not WAV/MP3. The AI music render bridge provides provider prompts and approval gates. Runway tool availability was observed in conversation 2026-11-07 but no credit-using generation was run. Suno/Udio cannot be claimed integrated without a connected host tool.

Offline check:

```
python -m unittest discover -s skills/music-midi-arrangement-vn/tests -v
python skills/music-midi-arrangement-vn/scripts/score_export.py --input skills/music-midi-arrangement-vn/examples/melody.json --midi /tmp/song.mid --musicxml /tmp/song.musicxml
```

Source versions before upgrade: 16.0.47. New skill paths and prompt addition are the only modifications. Any host run requires readback of exact files and approved credit before an external call.
