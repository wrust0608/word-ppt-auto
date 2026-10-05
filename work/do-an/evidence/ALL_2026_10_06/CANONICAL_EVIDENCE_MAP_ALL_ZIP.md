# Canonical Evidence Map — ALL(1).zip

Status: `AUDITED_R2`

All archive paths are exact paths inside the source ZIP. No ellipses are used. Full inventory of all 174 files is in `FULL_ARCHIVE_MANIFEST_ALL_2026_10_06.csv`.

## Environment and baseline

| ID | Exact archive path | SHA-256 | Grade | Role / boundary |
|---|---|---|---|---|
| `ENV-CORE-01` | `ALL/00_Environment_Hình và các bằng chứng xây dựng môi trường/PreDemo/Final_PreDemo_Audit.txt` | `532a2fa06ee0df772444ea14242591d4ee407d0477e0081f68a549bff6a66b38` | PRIMARY_LOCAL_STATE | Final pre-demo OS/network/tool/SMB state; snapshot line is pre-snapshot chronology |
| `ENV-CORE-02` | `ALL/00_Environment_Hình và các bằng chứng xây dựng môi trường/PreDemo/Before_Demo_Snapshots.txt` | `4e120518454ea263f7ae8aa1373f0a5e1303c81e27e6f6a6bd5e509149222308` | PRIMARY_LOCAL_STATE | Final snapshot verification after pre-demo audit |
| `ENV-CORE-03` | `ALL/00_Environment_Hình và các bằng chứng xây dựng môi trường/PatchBaseline/MS17-010_Official_Mapping.txt` | `938e4c15fb96c0c39cf02ec473fe5addb646e9d8f06f3aab7021ca0f3c8e8261` | PRIMARY_LOCAL_STATE | Local patch mapping/state; academic claim still cites Microsoft source ledger |
| `ENV-CORE-04` | `ALL/00_Environment_Hình và các bằng chứng xây dựng môi trường/FirewallPrep/Windows_FirewallPrep_Final.txt` | `119fb52ab97bb1c467678ff2f796428809ff61e811c6cf6740ee9bea4aeadfe3` | PRIMARY_LOCAL_STATE | Windows Firewall lab rule/listener audit |
| `ENV-CORE-05` | `ALL/00_Environment_Hình và các bằng chứng xây dựng môi trường/Network/VirtualBox_HostOnly_Config.txt` | `33d87da88f5357b1601b69e5a4650433f7c031aa33f38d33369fc2cac86d7bc9` | PRIMARY_LOCAL_STATE | Host-Only baseline and VM NIC configuration |
| `ENV-HIST-01` | `ALL/00_Environment_Hình và các bằng chứng xây dựng môi trường/Baseline/Kali/Kali_Baseline.txt` | `48e0b58fdce20e1e2be5e988e8ecc6a53480c6e81a7711f45057f9a832ebe85e` | HISTORICAL_EARLY_STATE | Early pre-Nmap Kali state; not final tool baseline |
| `ENV-SUP-01` | `ALL/00_Environment_Hình và các bằng chứng xây dựng môi trường/Baseline/Windows/Windows_Baseline.txt` | `e90610146178766e7be3a6dbad360c0ce7d11f642ae089409bdb5d98b6ce1a6a` | SUPPORTING_BASELINE | Early Windows baseline; final local records have precedence |

## Scenario 1

Each `.nmap` row below has matching `.xml` and `.gnmap` siblings. Their complete hashes are in the full archive manifest.

| ID | Exact archive path | SHA-256 | Grade | Role |
|---|---|---|---|---|
| `S1-RAW-01` | `ALL/01_Scenario1_Hình và các bằng chứng kịch bản 1/raw/b2_host_discovery.nmap` | `d2219adb0a780a139143ddb3cd65131f8a4a7a1c539a52be6d075f17500a3557` | PRIMARY_RAW | Subnet discovery |
| `S1-RAW-02` | `ALL/01_Scenario1_Hình và các bằng chứng kịch bản 1/raw/b3_target_alive.nmap` | `502927b7aad6d735b6c05644ac74a65b4d9bab53830be17a04d5f993e2e2520b` | PRIMARY_RAW | Target alive |
| `S1-RAW-03` | `ALL/01_Scenario1_Hình và các bằng chứng kịch bản 1/raw/b4_smb_ports.nmap` | `f15c7d358c9eac1b1457e4b4e014770fc02a9a554f8098128720de3a08ee22e6` | PRIMARY_RAW | TCP 139/445 state |
| `S1-RAW-04` | `ALL/01_Scenario1_Hình và các bằng chứng kịch bản 1/raw/b5_smb_version.nmap` | `13b9ff03c7f4ab9d0cc472fd46e60afd65ca2bfc3b646d823cf21b176508fff4` | PRIMARY_RAW | Service/version fingerprint |
| `S1-RAW-05` | `ALL/01_Scenario1_Hình và các bằng chứng kịch bản 1/raw/b6_smb_nse.nmap` | `a4dc92245ee2ea9688f1362b47f42b177cac350ac6b000f6b08adc01c4911c53` | PRIMARY_RAW | Protocol/signing/capability output |
| `S1-META-01` | `ALL/01_Scenario1_Hình và các bằng chứng kịch bản 1/Scenario1_Run_Manifest.txt` | `3f8f92f0efca82bd4e1a93b9539c210f1adad1cf0e62a3b6d1e6d3b8716983ef` | SECONDARY_META | Operator commands/run metadata; subordinate to raw for Nmap output |

## Scenario 2

| ID | Exact archive path | SHA-256 | Grade | Role |
|---|---|---|---|---|
| `S2-RAW-01` | `ALL/02_Scenario2_Hình và các bằng chứng kịch bản 2/raw/NSE-SMB-01_ports.nmap` | `17395ddf5206cd1aa71e45737163beacea69d3ded80b19ce9cdd35b84ebb71cb` | PRIMARY_RAW | Ports |
| `S2-RAW-02` | `ALL/02_Scenario2_Hình và các bằng chứng kịch bản 2/raw/NSE-SMB-02_protocols.nmap` | `cf9447b8f927bf896a582b8ea5ac8efa86b8cebca29c2b9afd7033a36aa4fa08` | PRIMARY_RAW | Protocols |
| `S2-RAW-03` | `ALL/02_Scenario2_Hình và các bằng chứng kịch bản 2/raw/NSE-SMB-03_signing.nmap` | `96a7152bf76805ed8539c3c6c97be2a8f88f6a7edd459229bad706371aa31fa0` | PRIMARY_RAW | Signing |
| `S2-RAW-04` | `ALL/02_Scenario2_Hình và các bằng chứng kịch bản 2/raw/NSE-SMB-04_ms17010.nmap` | `181fcaab11b414a6943317964d002db5a6f953e63ef43bec01b165f5ac7a4cd4` | PRIMARY_RAW | MS17-010 probe; no usable verdict |
| `S2-META-01` | `ALL/02_Scenario2_Hình và các bằng chứng kịch bản 2/Scenario2_Run_Manifest.txt` | `2b18d0d61cfa820526d53f6ff2d593b27b8bddbce971bb5a25b4d0da6e6658bd` | SECONDARY_META | Operator commands/run metadata |

## Case B — disable SMBv1

| ID | Exact archive path | SHA-256 | Grade | Role |
|---|---|---|---|---|
| `B-LOCAL-01` | `ALL/03_Remediation_SMBv1_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi tắt smbv1/SMBv1_Remediation_01_Before.png` | `e19cc9c7209769dd3bdfe530f59c8dee85087119c5147ccfb5bd6ac087498ca3` | PRIMARY_VISUAL | Local before state |
| `B-ACTION-01` | `ALL/03_Remediation_SMBv1_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi tắt smbv1/SMBv1_Remediation_02_Action.png` | `feb3a6ba1fe983177a6b4d190d7b1f880beea2c69af914b9edae2e5986b0467f` | PRIMARY_VISUAL | Disable action |
| `B-LOCAL-02` | `ALL/03_Remediation_SMBv1_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi tắt smbv1/SMBv1_Remediation_03_After_Local.png` | `2f762508ec98da3b6ed75813c32ed5622cbe1c982e6e6e2907086152e9a6a6ad` | PRIMARY_VISUAL | Local after state |
| `B-RAW-01` | `ALL/03_Remediation_SMBv1_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi tắt smbv1/raw/NSE-SMB-02_protocols.nmap` | `30d8877e83b80ac6bd82daca3a80d3bbc33bb65e974e60d1db4d7699deae8337` | PRIMARY_RAW | Protocol retest |
| `B-RAW-02` | `ALL/03_Remediation_SMBv1_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi tắt smbv1/raw/NSE-SMB-04_ms17010.nmap` | `85336e92da87a65d81145d95e361b8267c2460f30d3f4d66fa7de66631b236c3` | PRIMARY_RAW | MS17-010 retest; no usable verdict |
| `B-META-01` | `ALL/03_Remediation_SMBv1_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi tắt smbv1/SMBv1_Remediation_Run_Manifest.txt` | `6a0a60568c545b7bbf457e5199d0e6a3d8e2eebe85817698cf5f8e3d07abc0d0` | SECONDARY_META | Operator command/metadata; causal summary text not promoted |

## Case C — pfSense

| ID | Exact archive path | SHA-256 | Grade | Role / boundary |
|---|---|---|---|---|
| `C-IFACE-01` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_03_Interface_Assignment.png` | `ecf111151386022a55bbea657b314009eb3efb08f0a6232ab13f910dce3b6b6d` | PRIMARY_VISUAL | CASE_C_KALI=em2; CASE_C_WINDOWS=em3 |
| `C-BRIDGE-01` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_04_Bridge.png` | `f955b3d556f20372a9a831da4d4daa441e05dea5fe49a7f05d1cca013fd0a517` | PRIMARY_VISUAL | bridge0 membership |
| `C-TUNE-DIRECT-01` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_05_Bridge_Filtering.png` | `9408c0962dd4a221152b9c6fd927a7d9417cfb54c626a3dd9d50f5e325c985da` | PRIMARY_VISUAL | Directly proves pfil_member=1 and pfil_bridge=0; does not visibly prove pfil_onlyip |
| `C-RULE-01` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_06_Baseline_Pass_Rule.png` | `30fd54c59431083b19d8ed3dc2f0e002910382d587a361c84bc17adf3dbf1fa6` | PRIMARY_VISUAL | Baseline pass rule |
| `C-RULE-02` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_07_Block_Rule_Config.png` | `af694b811ebed2a431746198ff3cb62b4af356db8b17b257966889eca11e3fa1` | PRIMARY_VISUAL | Block rule configuration and logging enabled |
| `C-RULE-03` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_08_Rule_Order.png` | `6029ea7c923c297aa9bc65c3c551a17e1d4f569a2c98f78846a39c69e22aeb45` | PRIMARY_VISUAL | Block row above pass row |
| `C-RAW-01` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/raw/NSE-SMB-01_ports.nmap` | `5dd208208d4f281b86897a44ad0f3bc4006b380b72475af0893085b9d453481e` | PRIMARY_RAW | 139/445 filtered/no-response |
| `C-RAW-02` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/raw/NSE-SMB-04_ms17010.nmap` | `ddd2f63535f7b7485c36de1146fb252b4690f3f2c98b259b22a90217ff488d03` | PRIMARY_RAW | 445 filtered; no script verdict |
| `C-VIS-01` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` | `de266abb4fa3e8412cfc091975d714bb4bf1168a2e3d7f6cba7d7276f22dfba7` | PRIMARY_VISUAL | Canonical port screenshot |
| `C-LOG-01` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_10_Block_Log_CANONICAL.png` | `3b8383c54143f8a01eb6201462a6b30877f4b95f27b1a72f54b8b07562a68bc2` | PRIMARY_VISUAL / CONFLICTING | Proves blocked matching SMB SYN traffic; visible rule label conflicts with manifest named-rule attribution |
| `C-VIS-02` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` | `ecd605f0c2e46690988253ec104f9111844e06a600e3e2d1b0a45506ce5cbf12` | PRIMARY_VISUAL | Canonical MS17-010 screenshot |
| `C-META-01` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/pfSense_Remediation_Run_Manifest.txt` | `2b0cf912febf59ed93d2e76e5ac40da056af6dce3d353b4a3737c9ad7b4df54c` | SECONDARY_META | Operator commands, data/management planes, pfil_onlyip=1, version/snapshot; cannot override conflicting log label |
| `C-CLOSURE-01` | `ALL/04_Remediation_pfSense_Hình và các bằng chứng thực thi biện pháp giảm thiểu khi có firewall pfsen hạn chế/RUN4_PAUSE_STATE_REPORT.txt` | `e88212e41f9b36d8d8dacdf695d06dd0b51b32a07f3d22c6b626c9993e228dca` | MIXED_CHRONOLOGY | Only Section 21 final closure may support final chronology; earlier content is troubleshooting/history |

## Conflict lock — C-LOG-01

Direct screenshot:
- blocked action;
- CASE_C_KALI;
- `.56.10 -> .56.20:139/445`;
- TCP SYN;
- visible rule label `CASE C baseline pass Kali to Windows (100000104)`.

Manifest/closure:
- attributes same traffic to `CASE C - Block SMB Kali to Windows (1000000104)`.

Status:
`CONFLICTING_EVIDENCE — RULE_LABEL_ATTRIBUTION_UNRESOLVED`.

Do not claim exact named-rule attribution until separately resolved.
