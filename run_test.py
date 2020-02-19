from pyHorace import horace
from matlab import double as md
import matlab

m = horace.initialize()
m.call('pyhorace_init', nargout=0)

proj = m.call('projaxes', [md([-0.5, 1, 0]), md([0, 0, 1]), 'type', 'rrr'])
w1 = m.call('cut_sqw', ['ei30_10K.sqw', proj, md([0.1, 0.02, 0.5]), md([1.5, 2.5]), md([0.4, 0.5]), md([3, 0.5, 20])])
w2 = m.call2('cut_sqw', w1, [md([0.1, 0.5]), md([3, 0.5, 20])])
# This call fails at the moment for some unknown reason...
hf = m.call2('plot', w1, [])
m.call('pause', [10])