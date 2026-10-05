# Canonical Evidence Map — ALL(1).zip

The paths below are provenance paths inside the source archive, not report-section names.

| ID | Archive path | SHA-256 | Role |
|---|---|---|---|
| `ENV-CORE-01` | `00_Environment.../PreDemo/Final_PreDemo_Audit.txt` | `532a2fa06ee0df772444ea14242591d4ee407d0477e0081f68a549bff6a66b38` | Final pre-demo OS/network/tool/SMB state |
| `ENV-CORE-02` | `00_Environment.../PreDemo/Before_Demo_Snapshots.txt` | `4e120518454ea263f7ae8aa1373f0a5e1303c81e27e6f6a6bd5e509149222308` | Final snapshot lineage |
| `ENV-CORE-03` | `00_Environment.../PatchBaseline/MS17-010_Official_Mapping.txt` | `938e4c15fb96c0c39cf02ec473fe5addb646e9d8f06f3aab7021ca0f3c8e8261` | Local patch mapping and UNPATCHED state |
| `ENV-CORE-04` | `00_Environment.../FirewallPrep/Windows_FirewallPrep_Final.txt` | `119fb52ab97bb1c467678ff2f796428809ff61e811c6cf6740ee9bea4aeadfe3` | Scoped Windows Firewall rule state |
| `ENV-CORE-05` | `00_Environment.../Network/VirtualBox_HostOnly_Config.txt` | `33d87da88f5357b1601b69e5a4650433f7c031aa33f38d33369fc2cac86d7bc9` | Baseline Host-Only network configuration |
| `ENV-CORE-06` | `00_Environment.../Baseline/Kali/Kali_Baseline.txt` | `48e0b58fdce20e1e2be5e988e8ecc6a53480c6e81a7711f45057f9a832ebe85e` | Historical early Kali baseline; pre-Nmap only |
| `ENV-CORE-07` | `00_Environment.../Baseline/Windows/Windows_Baseline.txt` | `e90610146178766e7be3a6dbad360c0ce7d11f642ae089409bdb5d98b6ce1a6a` | Windows OS/SMB/service baseline |
| `S1-RAW-01` | `01_Scenario1.../raw/b2_host_discovery.nmap` | `d2219adb0a780a139143ddb3cd65131f8a4a7a1c539a52be6d075f17500a3557` | Scenario 1 subnet discovery raw |
| `S1-RAW-02` | `01_Scenario1.../raw/b3_target_alive.nmap` | `502927b7aad6d735b6c05644ac74a65b4d9bab53830be17a04d5f993e2e2520b` | Scenario 1 target-alive raw |
| `S1-RAW-03` | `01_Scenario1.../raw/b4_smb_ports.nmap` | `f15c7d358c9eac1b1457e4b4e014770fc02a9a554f8098128720de3a08ee22e6` | Scenario 1 TCP 139/445 raw |
| `S1-RAW-04` | `01_Scenario1.../raw/b5_smb_version.nmap` | `13b9ff03c7f4ab9d0cc472fd46e60afd65ca2bfc3b646d823cf21b176508fff4` | Scenario 1 service/version raw |
| `S1-RAW-05` | `01_Scenario1.../raw/b6_smb_nse.nmap` | `a4dc92245ee2ea9688f1362b47f42b177cac350ac6b000f6b08adc01c4911c53` | Scenario 1 SMB NSE raw |
| `S2-RAW-01` | `02_Scenario2.../raw/NSE-SMB-01_ports.nmap` | `17395ddf5206cd1aa71e45737163beacea69d3ded80b19ce9cdd35b84ebb71cb` | Scenario 2 ports raw |
| `S2-RAW-02` | `02_Scenario2.../raw/NSE-SMB-02_protocols.nmap` | `cf9447b8f927bf896a582b8ea5ac8efa86b8cebca29c2b9afd7033a36aa4fa08` | Scenario 2 protocols raw |
| `S2-RAW-03` | `02_Scenario2.../raw/NSE-SMB-03_signing.nmap` | `96a7152bf76805ed8539c3c6c97be2a8f88f6a7edd459229bad706371aa31fa0` | Scenario 2 signing raw |
| `S2-RAW-04` | `02_Scenario2.../raw/NSE-SMB-04_ms17010.nmap` | `181fcaab11b414a6943317964d002db5a6f953e63ef43bec01b165f5ac7a4cd4` | Scenario 2 MS17-010 raw |
| `B-RAW-01` | `03_Remediation_SMBv1.../raw/NSE-SMB-02_protocols.nmap` | `30d8877e83b80ac6bd82daca3a80d3bbc33bb65e974e60d1db4d7699deae8337` | Case B protocol retest raw |
| `B-RAW-02` | `03_Remediation_SMBv1.../raw/NSE-SMB-04_ms17010.nmap` | `85336e92da87a65d81145d95e361b8267c2460f30d3f4d66fa7de66631b236c3` | Case B MS17-010 retest raw |
| `C-RAW-01` | `04_Remediation_pfSense.../raw/NSE-SMB-01_ports.nmap` | `5dd208208d4f281b86897a44ad0f3bc4006b380b72475af0893085b9d453481e` | Case C canonical port retest raw |
| `C-RAW-02` | `04_Remediation_pfSense.../raw/NSE-SMB-04_ms17010.nmap` | `ddd2f63535f7b7485c36de1146fb252b4690f3f2c98b259b22a90217ff488d03` | Case C canonical MS17-010 retest raw |
| `B-LOCAL-01` | `03_Remediation_SMBv1.../SMBv1_Remediation_01_Before.png` | `e19cc9c7209769dd3bdfe530f59c8dee85087119c5147ccfb5bd6ac087498ca3` | Case B local before state |
| `B-ACTION-01` | `03_Remediation_SMBv1.../SMBv1_Remediation_02_Action.png` | `feb3a6ba1fe983177a6b4d190d7b1f880beea2c69af914b9edae2e5986b0467f` | Case B SMBv1 disable action |
| `B-LOCAL-02` | `03_Remediation_SMBv1.../SMBv1_Remediation_03_After_Local.png` | `2f762508ec98da3b6ed75813c32ed5622cbe1c982e6e6e2907086152e9a6a6ad` | Case B local after state |
| `C-TOPO-01` | `04_Remediation_pfSense.../pfSense_04_Bridge.png` | `f955b3d556f20372a9a831da4d4daa441e05dea5fe49a7f05d1cca013fd0a517` | Case C bridge membership |
| `C-TOPO-02` | `04_Remediation_pfSense.../pfSense_05_Bridge_Filtering.png` | `9408c0962dd4a221152b9c6fd927a7d9417cfb54c626a3dd9d50f5e325c985da` | Case C bridge filtering tunables |
| `C-RULE-01` | `04_Remediation_pfSense.../pfSense_06_Baseline_Pass_Rule.png` | `30fd54c59431083b19d8ed3dc2f0e002910382d587a361c84bc17adf3dbf1fa6` | Case C baseline pass rule |
| `C-RULE-02` | `04_Remediation_pfSense.../pfSense_07_Block_Rule_Config.png` | `af694b811ebed2a431746198ff3cb62b4af356db8b17b257966889eca11e3fa1` | Case C block rule details |
| `C-RULE-03` | `04_Remediation_pfSense.../pfSense_08_Rule_Order.png` | `6029ea7c923c297aa9bc65c3c551a17e1d4f569a2c98f78846a39c69e22aeb45` | Case C rule ordering |
| `C-VIS-01` | `04_Remediation_pfSense.../pfSense_CaseC_09_NSE01_Ports_CANONICAL.png` | `de266abb4fa3e8412cfc091975d714bb4bf1168a2e3d7f6cba7d7276f22dfba7` | Case C canonical port screenshot |
| `C-LOG-01` | `04_Remediation_pfSense.../pfSense_10_Block_Log_CANONICAL.png` | `3b8383c54143f8a01eb6201462a6b30877f4b95f27b1a72f54b8b07562a68bc2` | Case C canonical pfSense block log |
| `C-VIS-02` | `04_Remediation_pfSense.../pfSense_CaseC_11_NSE04_MS17010_CANONICAL.png` | `ecd605f0c2e46690988253ec104f9111844e06a600e3e2d1b0a45506ce5cbf12` | Case C canonical MS17-010 screenshot |
