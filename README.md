gappy Is Simple Module Using requests And Proxyscrape Api To Check and Generate Proxies And Make It Easier To User

functions explain
<h3 align="left">generate_proxies</h3>
<pre><code>
from gappy import Proxy
Proxy.generate_proxies('https')
</code></pre>
**Will Generate Proxies And Return Them As List**
Note: **If You Want It As Text Instead Of List Remove .split('\n') Function**

<h3 align="left">check_proxy</h3>
<pre><code>
from gappy import Proxy
Proxy.check_proxy('190.95.202.210:999')
</code></pre>
**Will Check The Proxy And Return True If Work Or False If Died**

<h3 align="left">generate_check</h3>
<pre><code>
from gappy import Proxy
Proxy.generate_check('https')
</code></pre>
**Will Generate Proxies And Check Them And Return Worked Proxies One By One**

<h3 align="left">help</h3>
<pre><code>
from gappy import Proxy
Proxy.help()
</code></pre>
**Print Simple Info About Module Functions**

<h3 align="left">info</h3>
<pre><code>
from gappy import Proxy
Proxy.info()
</code></pre>
**Print Simple Info About Module Coder (Me:3)**
