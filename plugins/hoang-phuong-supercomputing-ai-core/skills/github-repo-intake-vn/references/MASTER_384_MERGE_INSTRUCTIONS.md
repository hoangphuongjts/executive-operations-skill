> Historical checkpoint: this file describes the pre-merge state in the v16.0.36 snapshot. The exact-source merge is now complete in the offline candidate; see MASTER_384_MERGE_RESULT_2026-11-05.md. Do not reconstruct the registry from deltas again.

# Lossless master merge — blocked on exact 384-row registry source

The plugin's existing `skills/hoangphuong-supercomputing-core/references/GITHUB_16x24_CANDIDATES.json` has 384 rows with many individually audited fields. Do not synthesize a fresh master from names or overwrite it with this smaller delta. The three source revisions to merge are:

1. Batch 13 `BATCH_13_REGISTRY_DELTA.json`: rows 45–48; 1 integrated / 3 excluded.
2. Batch 14 `BATCH_14_REGISTRY_DELTA.json`: rows 49–52; 2 integrated / 2 excluded.
3. Earlier pending `PRIOR_PENDING_ROWS_02_04_RESOLVED_2026-11-05.json`: rows 2 and 4; both excluded.

On a future exact source snapshot mount, validate `len(records)==384`, expected repo and cluster/rank at every target row, and existing release; overlay only individual reviewed fields (not wholesale record replacement) while retaining all non-target rows and every original custom key. Specifically replace `latest_commit` by each verified pinned `pinned_commit` where that field is present; preserve `default_branch` and license scopes. Update root counters to verified 16, excluded 36, pending 332 only after host readback. Emit SHA256 of non-target 374 rows before and after, and compare all 384 repo IDs/order. Publish with fresh expected_release_id and readback every file. **Not executed here:** exact source cannot currently be materialized without reconstructing or risking altered records.
