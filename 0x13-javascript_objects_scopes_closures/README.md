<h1 class="gap">0x13. JavaScript - Objects, Scopes and Closures</h1>
<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/OJ4pU6uHwfCrAclbZsk_Hg" title="JavaScript object basics" target="_blank">JavaScript object basics</a> </li>
<li><a href="/rltoken/vLr7QS9h4-nGFKVn5vsrvQ" title="Object-oriented JavaScript" target="_blank">Object-oriented JavaScript</a> (<em><strong>read all examples!</strong></em>)</li>
<li><a href="/rltoken/zMWxOmGWEsOCldCKeDswCA" title="Class - ES6" target="_blank">Class - ES6</a> </li>
<li><a href="/rltoken/DTMKogwFYEgUnpLrNvTcfQ" title="super - ES6" target="_blank">super - ES6</a> </li>
<li><a href="/rltoken/fh2JHfNNa-HLnmfSdOo9TA" title="extends - ES6" target="_blank">extends - ES6</a> </li>
<li><a href="/rltoken/lrlwnQMM82RimJJcfLao5w" title="Object prototypes" target="_blank">Object prototypes</a> </li>
<li><a href="/rltoken/vLr7QS9h4-nGFKVn5vsrvQ" title="Inheritance in JavaScript" target="_blank">Inheritance in JavaScript</a> </li>
<li><a href="/rltoken/qDa7F8060Jlhe3DZZitY4A" title="Closures" target="_blank">Closures</a> </li>
<li><a href="/rltoken/ockP7FQKKmTRvfeAHw-XSw" title="this/self" target="_blank">this/self</a> </li>
<li><a href="/rltoken/22mdHf9KeFhRQrLP-e1hPw" title="Modern JS" target="_blank">Modern JS</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/wrvgHnS5IYuzEVUUixnzJQ" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why JavaScript programming is amazing</li>
<li>How to create an object in JavaScript</li>
<li>What <code>this</code> means</li>
<li>What <code>undefined</code> means </li>
<li>Why the variable type and scope is important</li>
<li>What is a closure</li>
<li>What is a prototype</li>
<li>How to inherit an object from another</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant. <a href="/rltoken/LzTXpt_3kwzaaEQFTvq2UQ" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="/rltoken/_6jQeRtew2qeam8OzERXPw" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="/rltoken/D8wEPwvtilCjNqotmoSruw" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<h2>More Info</h2>

<h3>Install Node 14</h3>

<pre><code>$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>

<h3>Install semi-standard</h3>

<p><a href="/rltoken/_6jQeRtew2qeam8OzERXPw" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install semistandard --global
</code></pre>

  </div>
</div>
<h3 class="panel-title">
      0. Rectangle #0
    </h3>
 <p>Write an empty class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class </li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require(&#39;./0-rectangle&#39;);

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Class: Rectangle]
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>0-rectangle.js</code></li>
</ul>
</div>

<h3 class="panel-title">
      1. Rectangle #1
    </h3>
<!-- Task Body -->
<p>Write a class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require(&#39;./1-rectangle&#39;);

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>1-rectangle.js</code></li>
</ul>
</div>
<h3 class="panel-title">
      2. Rectangle #2
    </h3>
 <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require(&#39;./2-rectangle&#39;);

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>2-rectangle.js</code></li>
</ul>
</div>

<h3 class="panel-title">
      3. Rectangle #3
    </h3>
<p>Write a class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments: <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
<li>Create an instance method called <code>print()</code> that prints the rectangle using the character <code>X</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require(&#39;./3-rectangle&#39;);

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>3-rectangle.js</code></li>
</ul>
</div>


<h3 class="panel-title">
      4. Rectangle #4
    </h3>
 <!-- Task Body -->
    <p>Write a class <code>Rectangle</code> that defines a rectangle:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class</li>
<li>The constructor must take 2 arguments: <code>w</code> and <code>h</code></li>
<li>Initialize the instance attribute <code>width</code> with the value of <code>w</code> </li>
<li>Initialize the instance attribute <code>height</code> with the value of <code>h</code> </li>
<li>If <code>w</code> or <code>h</code> is equal to 0 or not a positive integer, create an empty object</li>
<li>Create an instance method called <code>print()</code> that prints the rectangle using the character <code>X</code></li>
<li>Create an instance method called <code>rotate()</code> that exchanges the <code>width</code> and the <code>height</code> of the rectangle</li>
<li>Create an instance method called <code>double()</code> that multiples the <code>width</code> and the <code>height</code> of the rectangle by 2</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require(&#39;./4-rectangle&#39;);

const r1 = new Rectangle(2, 3);
console.log(&#39;Normal:&#39;);
r1.print();

console.log(&#39;Double:&#39;);
r1.double();
r1.print();

console.log(&#39;Rotate:&#39;);
r1.rotate();
r1.print();

guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>4-rectangle.js</code></li>
</ul>
</div>
<h3 class="panel-title">
      5. Square #0
    </h3>
 <p>Write a class <code>Square</code> that defines a square and inherits from <code>Rectangle</code> of <code>4-rectangle.js</code>:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class and <code>extends</code></li>
<li>The constructor must take 1 argument: <code>size</code></li>
<li>The constructor of <code>Rectangle</code> must be called (by using <code>super()</code>)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 5-main.js
#!/usr/bin/node
const Square = require(&#39;./5-square&#39;);

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

guillaume@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>5-square.js</code></li>
</ul>
</div>

<h3 class="panel-title">
      6. Square #1
    </h3>
<p>Write a class <code>Square</code> that defines a square and inherits from <code>Rectangle</code> of <code>4-rectangle.js</code>:</p>

<ul>
<li>You must use the <code>class</code> notation for defining your class and <code>extends</code></li>
<li>Create an instance method called <code>charPrint(c)</code> that prints the rectangle using the character <code>c</code>

<ul>
<li>If <code>c</code> is <code>undefined</code>, use the character <code>X</code></li>
</ul></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 6-main.js
#!/usr/bin/node
const Square = require(&#39;./6-square&#39;);

const s1 = new Square(4);
s1.charPrint();

s1.charPrint(&#39;C&#39;);

guillaume@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>6-square.js</code></li>
</ul>
</div>
<h3 class="panel-title">
      7. Occurrences
    </h3>

<!-- Task Body -->
    <p>Write a function that returns the number of occurrences in a list:</p>

<ul>
<li>Prototype: <code>exports.nbOccurences = function (list, searchElement)</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 7-main.js
#!/usr/bin/node
const nbOccurences = require(&#39;./7-occurrences&#39;).nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences([&quot;S&quot;, 12, &quot;c&quot;, &quot;S&quot;, &quot;School&quot;, 8], &quot;S&quot;));

guillaume@ubuntu:~/0x13$ ./7-main.js
1
4
2
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>7-occurrences.js</code></li>
</ul>
</div>

<h3 class="panel-title">
      8. Esrever
    </h3>
<p>Write a function that returns the reversed version of a list:</p>

<ul>
<li>Prototype: <code>exports.esrever = function (list)</code></li>
<li>You are not allow to use the built-in method <code>reverse</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 8-main.js
#!/usr/bin/node
const esrever = require(&#39;./8-esrever&#39;).esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever([&quot;School&quot;, 89, { id: 12 }, &quot;String&quot;]));

guillaume@ubuntu:~/0x13$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ &#39;String&#39;, { id: 12 }, 89, &#39;School&#39; ]
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>8-esrever.js</code></li>
</ul>
</div>
 <h3 class="panel-title">
      9. Log me
    </h3>
<p>Write a function that prints the number of arguments already printed and the new argument value. (see example below)</p>

<ul>
<li>Prototype: <code>exports.logMe = function (item)</code></li>
<li>Output format: <code>&lt;number arguments already printed&gt;: &lt;current argument value&gt;</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 9-main.js
#!/usr/bin/node
const logMe = require(&#39;./9-logme&#39;).logMe;

logMe(&quot;Hello&quot;);
logMe(&quot;Best&quot;);
logMe(&quot;School&quot;);

guillaume@ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Best
2: School
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>9-logme.js</code></li>
</ul>
</div>
 <h3 class="panel-title">
      10. Number conversion
    </h3>

<p>Write a function that converts a number from base 10 to another base passed as argument:</p>

<ul>
<li>Prototype: <code>exports.converter = function (base)</code></li>
<li>You are not allowed to import any file</li>
<li>You are not allowed to declare any new variable (<code>var</code>, <code>let</code>, etc..)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x13$ cat 10-main.js
#!/usr/bin/node
const converter = require(&#39;./10-converter&#39;).converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

guillaume@ubuntu:~/0x13$ ./10-main.js
2
12
89
2
c
59
guillaume@ubuntu:~/0x13$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x13-javascript_objects_scopes_closures</code></li>
    <li>File: <code>10-converter.js</code></li>
</ul>
</div>
