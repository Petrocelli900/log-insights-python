import io
import json
import unittest
from contextlib import redirect_stdout
from tempfile import NamedTemporaryFile
from log_insights import summarize,main

class LogTests(unittest.TestCase):
    def event(self,**updates):
        event={'status':200,'duration_ms':10,'path':'/users?token=secret'}; event.update(updates)
        return json.dumps(event)
    def test_statistics(self):
        result=summarize([self.event(),self.event(status=503,duration_ms=50)])
        self.assertEqual(result['error_rate'],0.5); self.assertEqual(result['p95_ms'],50)
        self.assertEqual(result['routes'],{'/users':2}); self.assertNotIn('secret',str(result))
    def test_nearest_rank(self):
        self.assertEqual(summarize(self.event(duration_ms=i) for i in range(1,101))['p95_ms'],95)
    def test_invalid(self):
        events=['bad','[]','{}',self.event(status=True),self.event(duration_ms=-1),self.event(duration_ms=float('nan')),self.event(path='//host/x')]
        self.assertEqual(summarize(events)['invalid_lines'],7)
    def test_empty(self):
        report=summarize(['\n']); self.assertEqual(report['requests'],0); self.assertIsNone(report['p95_ms'])
    def test_cli(self):
        with NamedTemporaryFile(mode='w+',encoding='utf-8') as file:
            file.write(self.event()+'\n'); file.flush()
            out=io.StringIO()
            with redirect_stdout(out): self.assertEqual(main([file.name]),0)
            self.assertEqual(json.loads(out.getvalue())['requests'],1)
