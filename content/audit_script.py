#!/usr/bin/env python3
"""Audit script for Obgyn markdown files - structural checks."""
import os, re, yaml, json, sys
from pathlib import Path

BASE = Path(r"C:\Users\Ahmad taufiq\Pictures\Project_Kuliah\Stase_Obgyn\Operan\Ebook\Materi dari Modul\quartz\content")

def safeprint(text):
    sys.stdout.buffer.write((text + "\n").encode('utf-8', errors='replace'))
    sys.stdout.buffer.flush()

# Collect all .md files
all_files = list(BASE.rglob("*.md"))
safeprint(f"Total .md files: {len(all_files)}")

# Build name->path mapping for wikilink validation
name_map = {}
for f in all_files:
    stem = f.stem
    name_map[stem.lower().replace(" ", "-")] = f
    # Also add aliases from frontmatter
    try:
        content = f.read_text(encoding="utf-8", errors="replace")
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                fm = yaml.safe_load(parts[1])
                if fm and "aliases" in fm:
                    for alias in fm["aliases"]:
                        if isinstance(alias, str):
                            name_map[alias.lower().replace(" ", "-")] = f
    except:
        pass

results = []

def extract_wikilinks(text):
    return re.findall(r'\[\[([^\]]+)\]\]', text)

def has_frontmatter(text):
    return text.startswith("---")

def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1])
    except:
        return None

def find_sections(text):
    return re.findall(r'^## (.+)$', text, re.MULTILINE)

def find_callouts(text):
    return re.findall(r'> \[!(\w+)\].*$', text, re.MULTILINE)

def check_file(fpath):
    rel = fpath.relative_to(BASE)
    text = fpath.read_text(encoding="utf-8", errors="replace")
    issues = []
    
    # 1. Frontmatter
    fm = parse_frontmatter(text)
    if fm is None:
        issues.append("NO VALID YAML FRONTMATTER")
    else:
        required = ["title", "tags", "level_kompetensi", "kategori", "nomor_modul"]
        missing = [r for r in required if r not in fm]
        if missing:
            issues.append(f"MISSING FRONTMATTER KEYS: {missing}")
    
    # 2. Wikilink validation
    wikilinks = extract_wikilinks(text)
    broken_count = 0
    for wl in wikilinks:
        clean = wl.split("|")[0].strip().lower().replace(" ", "-")
        if clean not in name_map:
            possible = (fpath.parent / (clean + ".md"))
            if not possible.exists():
                broken_count += 1
    if broken_count > 0:
        issues.append(f"{broken_count} BROKEN WIKILINK(S)")
    
    # 3. Placeholder checks
    placeholders = re.findall(r'\(akan diisi|TODO|FIXME|placeholder|belum diisi|akan dilengkapi', text, re.IGNORECASE)
    if placeholders:
        issues.append(f"PLACEHOLDER: {'; '.join(set(p.lower() for p in placeholders))}")
    
    # 4. Sections analysis
    sections = find_sections(text)
    
    # 5. Callout analysis
    callouts = find_callouts(text)
    has_redflag = any("warning" in c.lower() for c in callouts)
    
    # 6. Category-specific checks
    rel_str = str(rel)
    is_keterampilan = rel_str.startswith("keterampilan")
    is_penyakit = rel_str.startswith("penyakit")
    
    if is_keterampilan and rel_str != "keterampilan\\keterampilan.md":
        expected_sections = ["Kenapa", "Persiapan", "Langkah", "Interpretasi", "Kesalahan"]
        missing_sec = [s for s in expected_sections if not any(s.lower() in sec.lower() for sec in sections)]
        if missing_sec:
            issues.append(f"MISSING KETERAMPILAN SECTIONS: {missing_sec}")
        # Check "Dipakai Untuk" or "Referensi"
        if not any("dipakai" in s.lower() or "penyakit a" in s.lower() for s in sections):
            if not any("referensi" in s.lower() for s in sections):
                pass # Allow if Referensi is present
        if not any("referensi" in s.lower() for s in sections):
            issues.append("MISSING 'Referensi' SECTION")
    
    if is_penyakit and rel_str != "penyakit\\penyakit.md":
        # Check for core sections
        core_topics = ["Apa Itu", "Gejala", "Pemeriksaan", "Diagnosis", "Tatalaksana"]
        missing_sec = [s for s in core_topics if not any(s.lower() in sec.lower() for sec in sections)]
        if missing_sec:
            issues.append(f"MISSING PENYAKIT SECTIONS: {missing_sec}")
    
    # 7. Check file size
    lines = text.split("\n")
    if len(lines) < 20:
        issues.append(f"TOO SHORT ({len(lines)} lines)")
    
    status = "OK"
    severity = 0
    for iss in issues:
        if "NO VALID" in iss or "BROKEN WIKILINK" in iss:
            severity = max(severity, 3)
        elif "MISSING FRONTMATTER" in iss:
            severity = max(severity, 3)
        elif "PLACEHOLDER" in iss:
            severity = max(severity, 2)
        elif "MISSING" in iss:
            severity = max(severity, 2)
        else:
            severity = max(severity, 1)
    
    if severity >= 3:
        status = "SERIUS"
    elif severity >= 2:
        status = "PERBAIKI"
    elif severity >= 1:
        status = "MINOR"
    
    redflag_detail = "ADA" if has_redflag else "TIDAK ADA"
    
    return {
        "file": str(rel),
        "status": status,
        "issues": issues,
        "wikilinks": len(wikilinks),
        "broken_wikilinks": broken_count,
        "sections": len(sections),
        "redflag": redflag_detail,
        "lines": len(lines)
    }

# Process all files
for f in sorted(all_files):
    res = check_file(f)
    results.append(res)
    line = f"[{res['status']:>7}] {res['file']} -- {', '.join(res['issues']) if res['issues'] else 'OK'}"
    safeprint(line)

# Summary
safeprint("")
safeprint("="*80)
safeprint("SUMMARY")
safeprint("="*80)
safeprint(f"Total files: {len(results)}")
ok_count = sum(1 for r in results if r['status'] == 'OK')
minor_count = sum(1 for r in results if r['status'] == 'MINOR')
perbaiki_count = sum(1 for r in results if r['status'] == 'PERBAIKI')
serius_count = sum(1 for r in results if r['status'] == 'SERIUS')
safeprint(f"OK: {ok_count} | MINOR: {minor_count} | PERBAIKI: {perbaiki_count} | SERIUS: {serius_count}")

safeprint("")
safeprint("--- FILES WITH BROKEN WIKILINKS ---")
for r in results:
    if r['broken_wikilinks'] > 0:
        safeprint(f"  {r['file']} ({r['broken_wikilinks']} broken)")

safeprint("")
safeprint("--- FILES WITH PLACEHOLDERS ---")
for r in results:
    if any("PLACEHOLDER" in i for i in r['issues']):
        safeprint(f"  {r['file']}")

safeprint("")
safeprint("--- FILES MISSING RED FLAG CALL-OUTS ---")
for r in results:
    if r['redflag'] == 'TIDAK ADA' and r['lines'] > 30:
        safeprint(f"  {r['file']}")

safeprint("")
safeprint("--- SERIUS FILES ---")
for r in results:
    if r['status'] == 'SERIUS':
        for i in r['issues']:
            safeprint(f"  {r['file']}: {i}")

safeprint("")
safeprint("--- FILES WITH MISSING SECTIONS ---")
for r in results:
    if any("MISSING" in i and "FRONTMATTER" not in i for i in r['issues']):
        issues_str = "; ".join(i for i in r['issues'] if "MISSING" in i)
        safeprint(f"  {r['file']}: {issues_str}")

safeprint("")
safeprint("--- FILES WITH FRONTMATTER ISSUES ---")
for r in results:
    if any("FRONTMATTER" in i for i in r['issues']):
        safeprint(f"  {r['file']}: {'; '.join(i for i in r['issues'] if 'FRONTMATTER' in i)}")

# Save detailed results
with open(BASE / "audit_report.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
safeprint("")
safeprint("Detailed report saved to audit_report.json")
