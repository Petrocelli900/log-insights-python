"""Summarize JSON Lines request logs from a file or stdin."""
import argparse
from collections import Counter
import json
import math
import sys
from urllib.parse import urlsplit

def summarize(lines):
    total=invalid=errors=0
    durations=[]; routes=Counter()
    for line in lines:
        if not line.strip(): continue
        try:
            event=json.loads(line)
            if not isinstance(event,dict): raise ValueError("object required")
            status=event['status']; duration=event['duration_ms']; path=event['path']
            if type(status) is not int or not 100<=status<=599: raise ValueError("bad status")
            if type(duration) not in (int,float) or not math.isfinite(duration) or duration<0: raise ValueError("bad duration")
            if not isinstance(path,str) or not path.startswith('/') or path.startswith('//'): raise ValueError("relative path required")
            route=urlsplit(path).path
        except (ValueError,KeyError,TypeError,OverflowError):
            invalid+=1; continue
        total+=1; errors+=status>=500; durations.append(duration); routes[route]+=1
    durations.sort()
    return {'requests':total,'invalid_lines':invalid,'server_errors':errors,
            'error_rate':errors/total if total else 0.0,
            'p95_ms':durations[math.ceil(total*0.95)-1] if total else None,
            'routes':dict(sorted(routes.items()))}

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file',nargs='?',default='-')
    args=parser.parse_args(argv)
    try:
        if args.file=='-': report=summarize(sys.stdin)
        else:
            with open(args.file,encoding='utf-8') as stream: report=summarize(stream)
    except (OSError,UnicodeError) as error:
        print(str(error),file=sys.stderr); return 2
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 1 if report['invalid_lines'] else 0

if __name__=='__main__': sys.exit(main())
