import difflib
nowname="ahbb"
allnamelist=["bhhh","ahbb"]
for i in allnamelist:
    compareini = difflib.SequenceMatcher(None, nowname, i).quick_ratio()
    print(compareini)