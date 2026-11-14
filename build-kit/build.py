#!/usr/bin/env python3
"""Build the PrintFlow Studio installer + latest.json.
usage: build.py VERSION "note 1" "note 2" ...   (reads src/extensions, writes out/)"""
import sys, os, re, json, hashlib, subprocess, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
ver = sys.argv[1]; notes = sys.argv[2:] or ["Cải thiện và sửa lỗi."]
assert re.fullmatch(r"\d+\.\d+\.\d+", ver), "version must be X.Y.Z"
short = ".".join(ver.split(".")[:2])
EXT = "src/extensions"; HUB = EXT + "/ProductionHub"
def sub(path, pat, rep, count_min=1, enc="utf-8"):
    s = open(path, encoding=enc).read(); n = len(re.findall(pat, s))
    assert n >= count_min, (path, pat); open(path, "w", encoding=enc).write(re.sub(pat, rep, s))
# 1. stamp the version into PrintFlow Studio
sub(HUB + "/js/version.js", r'PRINTFLOW_VERSION = "[\d.]+"', 'PRINTFLOW_VERSION = "%s"' % ver)
sub(HUB + "/index.html", r"PrintFlow Studio • v[\d.]+</h1>", "PrintFlow Studio • v%s</h1>" % short)
sub(HUB + "/index.html", r"<small>PrintFlow Studio v[\d.]+</small>", "<small>PrintFlow Studio v%s</small>" % short)
sub(HUB + "/CSXS/manifest.xml", r'(ExtensionBundleVersion|Version)="\d+\.\d+\.\d+"', r'\1="%s"' % ver, 2)
# 2. what's new page (UTF-16 LE with BOM for NSIS)
mods = sorted(d for d in os.listdir(EXT) if os.path.isdir(os.path.join(EXT, d)))
os.makedirs("build", exist_ok=True); os.makedirs("out", exist_ok=True)
txt = ["PrintFlow Studio %s — Prepress Automation Suite" % ver, "Designed by Mr. Haii (In Thành Đạt)", "",
       "CÓ GÌ MỚI", *["  • " + n for n in notes], "",
       "CÁC MODULE TRONG BẢN CÀI", "  Layout bìa kỷ yếu · Layout photobook gáy phụ · Sticker Layout Pro",
       "  Layout bìa keo gáy · Đặt ốc cắt xén · Tạo đường cắt 1 dao · Step & Repeat",
       "  Convert JPG · Xếp hình tiết kiệm · Outline phong bì · Summa Methods · Add Mark Summa",
       "  Text & Number (ẩn sẵn, bật trong nút bánh răng)", "",
       "CÀI ĐẶT VÀO", "  %APPDATA%\\Adobe\\CEP\\extensions  (cho tài khoản Windows này)", "",
       "CẬP NHẬT", "  PrintFlow Studio > nút bánh răng > Kiểm tra cập nhật — chỉ kiểm tra khi bạn bấm."]
open("build/whatsnew.txt", "w", encoding="utf-16").write("\r\n".join(txt) + "\r\n")
# 3. NSIS script
names = mods
checks = "\n".join('  StrCmp "${NAME}" "%s" 0 +2\n  StrCpy $R5 1' % n for n in names)
unrem = "\n".join('  RMDir /r "$EXT\\%s"' % n for n in names)
size_kb = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(EXT) for f in fs) // 1024 + 200
v4 = ver + ".0"
nsi = open("installer.nsi.tpl", encoding="utf-8").read()
nsi = nsi.replace("@VERSION@", ver).replace("@VERSION4@", v4).replace("@NAMECHECKS@", checks).replace("@UNREMOVES@", unrem).replace("@SIZEKB@", str(size_kb))
open("build/installer.nsi", "w", encoding="utf-8-sig").write(nsi)
r = subprocess.run(["makensis", "-V3", "-INPUTCHARSET", "UTF8", "-NOCD", "build/installer.nsi"], capture_output=True, text=True)
print(r.stdout[-3000:], r.stderr[-3000:])
assert r.returncode == 0, "makensis failed"
exe = "out/PrintFlowStudio_Setup_%s.exe" % ver
data = open(exe, "rb").read()
info = {"version": ver, "date": datetime.date.today().isoformat(), "notes": notes,
        "url": "https://github.com/hei909/printflow-studio-update/releases/download/v%s/PrintFlowStudio_Setup_%s.exe" % (ver, ver),
        "page": "https://github.com/hei909/printflow-studio-update/releases/tag/v%s" % ver,
        "size": len(data), "sha256": hashlib.sha256(data).hexdigest()}
json.dump(info, open("out/latest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(json.dumps(info, ensure_ascii=False, indent=2))
