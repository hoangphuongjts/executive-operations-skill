import json, pathlib, sys, tempfile, unittest
SCRIPTS=pathlib.Path(__file__).parent
sys.path.insert(0,str(SCRIPTS))
import unified_library as hub

class HubCatalogTests(unittest.TestCase):
    def setUp(self):
        self.data=hub.load()
    def test_mount_returns_safe_source_refs(self):
        output=hub.mount(self.data,'xây kênh video',4)
        self.assertTrue(output['source_plugins_unmodified'])
        self.assertTrue(output['no_credential_or_code_transfer'])
        self.assertTrue(output['host_tool_call_requires_current_permission'])
        self.assertTrue(all(uri.startswith('skills://plugins/') for uri in output['read_skill_uris_on_demand']))
    def test_connection_status_is_snapshot_only(self):
        got=hub.connection_status(self.data,'vidIQ')
        self.assertEqual(got['status'],'read_verified_at_snapshot_only')
        self.assertEqual(got['live_connection_now'],'unknown')
    def test_unchecked_connector_not_credited(self):
        got=hub.connection_status(self.data,'Gmail')
        self.assertEqual(got['status'],'tool_interface_visible_at_snapshot_only')
    def test_no_unlicensed_code_copied(self):
        self.assertTrue(all(s['source_preserved'] for s in self.data['skill_sources']))
        self.assertTrue(all(s['integration_mode']=='read_original_skill_on_demand_via_host' for s in self.data['skill_sources']))
    def test_validate(self):self.assertEqual(hub.validate(self.data)['status'],'pass')
    def test_external_skills_172(self):self.assertEqual(len(self.data['skill_sources']),172)
    def test_external_families_22(self):self.assertEqual(len({x['source_plugin'] for x in self.data['skill_sources']}),22)
    def test_owned_plugins_11(self):self.assertEqual(len(self.data['owned_plugins']),11)
    def test_connector_namespaces_19(self):self.assertEqual(len(self.data['connector_namespaces']),19)
    def test_no_duplicate_uris(self):self.assertEqual(len({x['uri'] for x in self.data['skill_sources']}),172)
    def test_no_core_skill_copied(self):self.assertFalse(any('hoang-phuong-supercomputing-ai-core' in x['uri'] for x in self.data['skill_sources']))
    def test_no_skill_source_copy(self):self.assertTrue(all(x['copy_into_core'] is False for x in self.data['skill_sources']))
    def test_no_assumed_connection(self):self.assertTrue(all(x['not_a_connection_confirmation'] for x in self.data['connector_namespaces']))
    def test_personal_plugin_ids(self):self.assertTrue(all(p['plugin_id'].startswith(('plugin_','plugins_')) for p in self.data['owned_plugins']))
    def test_no_duplicate_owned_plugin(self):self.assertFalse(any('hoang-phuong-supercomputing-ai-core'==p['name'] for p in self.data['owned_plugins']))
    def test_search_video(self):self.assertTrue(any('video' in x['slug'] or 'vidiq' in x['source_plugin'] for x in hub.search(self.data,'youtube video',15)))
    def test_search_security(self):self.assertTrue(any('security' in x['slug'] for x in hub.search(self.data,'security',15)))
    def test_vietnamese_channel(self):self.assertTrue(any(x['source_plugin']=='channel-growth-agent-vn' for x in hub.search(self.data,'xây kênh youtube',12)))
    def test_vietnamese_coding(self):self.assertTrue(any(x['source_plugin']=='ai-coding-vietnamese-kit' for x in hub.search(self.data,'kiểm thử phần mềm',12)))
    def test_diversifies_sources(self):
        from collections import Counter
        counts=Counter(x['source_plugin'] for x in hub.search(self.data,'xây kênh youtube video',6))
        self.assertTrue(all(x<=2 for x in counts.values()))
    def test_search_unknown(self):self.assertEqual(hub.search(self.data,'zzzxxyy_not_real',3),[])
    def test_plan_is_nonexecuting(self):self.assertFalse(hub.plan(self.data,'ai content youtube')['external_execution'])
    def test_core_clustering_bounds(self):self.assertLessEqual(len(hub.plan(self.data,'ai content youtube')['suggested_core_clusters']),4)
    def test_empty_query_gives_empty(self):self.assertEqual(hub.search(self.data,'',10),[])
    def test_validate_duplicate_negative(self):
        d=json.loads(json.dumps(self.data));d['skill_sources'][0]=d['skill_sources'][1];self.assertEqual(hub.validate(d)['status'],'fail')
    def test_validate_unauthorized_copy_negative(self):
        d=json.loads(json.dumps(self.data));d['skill_sources'][0]['copy_into_core']=True;self.assertEqual(hub.validate(d)['status'],'fail')
    def test_validate_connection_overclaim_negative(self):
        d=json.loads(json.dumps(self.data));d['connector_namespaces'][0]['not_a_connection_confirmation']=False;self.assertEqual(hub.validate(d)['status'],'fail')
    def test_manifest_release_consistency(self):
        root=SCRIPTS.parents[2]
        a=json.loads((root/'plugin.json').read_text(encoding='utf-8'))
        b=json.loads((root/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        self.assertEqual(a['version'],b['version']);self.assertGreaterEqual(tuple(map(int,a['version'].split('.'))),(14,4,0))
        self.assertEqual(a['name'],b['name'])
    def test_registry_and_profiles_preservation(self):
        root=SCRIPTS.parents[2]
        p=root/'skills/hoangphuong-supercomputing-core/references/AGENTS_128.json'
        if not p.exists():self.skipTest('partial overlay; original tree is preserved by Plugin Creator')
        data=json.loads(p.read_text(encoding='utf-8'))
        self.assertEqual([r['id'] for r in data['roles']],list(range(1,129)))
        for i in (1,25,32,64,128):
            f=root/f'skills/hoangphuong-supercomputing-core/profiles/agent-{i:03}.json'
            self.assertEqual(json.loads(f.read_text(encoding='utf-8'))['id'],i)
if __name__=='__main__':unittest.main()
