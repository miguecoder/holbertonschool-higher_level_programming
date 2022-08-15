<h1 class="gap">0x12. JavaScript - Warm up</h1>
 <h2>Background Context</h2>

<p>JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:</p>

<ul>
<li>Scripting (same as we did with Python)</li>
<li>Web front-end</li>
</ul>

<p>For the moment, and for learning all basic concepts of this language, we will do some scripting.
After, we will make our AirBnB project dynamic by using Javascript and JQuery.</p>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg" alt="" style="" /></p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/OdMLtl6Y9mpQkaoEqJCRSg" title="Writing JavaScript Code" target="_blank">Writing JavaScript Code</a> </li>
<li><a href="/rltoken/iE6zaLw7pybp648IfRmk5Q" title="Variables" target="_blank">Variables</a> </li>
<li><a href="/rltoken/4td1BbZAYn4Dldi6k0CY7A" title="Data Types" target="_blank">Data Types</a> </li>
<li><a href="/rltoken/OdMLtl6Y9mpQkaoEqJCRSg" title="Operators" target="_blank">Operators</a> </li>
<li><a href="/rltoken/ALCoiVRvxmsjdqCUdWC_lg" title="Operator Precedence" target="_blank">Operator Precedence</a> </li>
<li><a href="/rltoken/Nlfhdy6Thyu_WgtBSqoAUw" title="Controlling Program Flow" target="_blank">Controlling Program Flow</a> </li>
<li><a href="/rltoken/Ta66PZ6_16K3q99oELvjkQ" title="Functions" target="_blank">Functions</a> </li>
<li><a href="/rltoken/osu583B5jskDVwmcm50-NQ" title="Objects and Arrays" target="_blank">Objects and Arrays</a> </li>
<li><a href="/rltoken/osu583B5jskDVwmcm50-NQ" title="Intrinsic Objects" target="_blank">Intrinsic Objects</a> </li>
<li><a href="/rltoken/mduSK-WOoRe6WohU1p2zZQ" title="Module patterns" target="_blank">Module patterns</a> </li>
<li><a href="/rltoken/kNWuHjyUvjr74wU2hBqd_A" title="var, let and const" target="_blank">var, let and const</a> </li>
<li><a href="/rltoken/qkp1hdLiI8DJje88bxcL6w" title="JavaScript Tutorial" target="_blank">JavaScript Tutorial</a> </li>
<li><a href="/rltoken/ieSajamJQ-Nv3XzcS_d5lA" title="Modern JS" target="_blank">Modern JS</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/kr1GDINhryJdjBSzQxCv0w" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>Why JavaScript programming is amazing</li>
<li>How to run a JavaScript script</li>
<li>How to create variables and constants</li>
<li>What are differences between <code>var</code>, <code>const</code> and <code>let</code></li>
<li>What are all the data types available in JavaScript</li>
<li>How to use the <code>if</code>, <code>if ... else</code> statements</li>
<li>How to use comments</li>
<li>How to affect values to variables</li>
<li>How to use <code>while</code> and <code>for</code> loops</li>
<li>How to use <code>break</code> and <code>continue</code> statements</li>
<li>What is a function and how do you use functions</li>
<li>What does a function that does not use any <code>return</code> statement return</li>
<li>Scope of variables</li>
<li>What are the arithmetic operators and how to use them</li>
<li>How to manipulate dictionary</li>
<li>How to import a file</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS using <code>node</code> (version 14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant (version 16.x.x). <a href="/rltoken/EK3q1S4Ouo08kTMI42cSig" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="/rltoken/FuXjfOYe18hUXCDoyMxBSg" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="/rltoken/iIDdBVB4HNhPpb_5e5L-Qg" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Install Node 14</h3>

<pre><code>$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>

<h3>Install semi-standard</h3>

<p><a href="/rltoken/FuXjfOYe18hUXCDoyMxBSg" title="Documentation" target="_blank">Documentation</a></p>

<pre><code>$ sudo npm install semistandard --global
</code></pre>

  </div>
</div>

<h3 class="panel-title">
      0. First constant, first print
    </h3>

<p>Write a script that prints &ldquo;JavaScript is amazing&rdquo;:</p>

<ul>
<li>You must create a constant variable called <code>myVar</code> with the value &ldquo;JavaScript is amazing&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>0-javascript_is_amazing.js</code></li>
</ul>
</div>

 <h3 class="panel-title">
      1. 3 languages
    </h3>
<p>Write a script that prints 3 lines:</p>

<ul>
<li>The first line: &ldquo;C is fun&rdquo;</li>
<li>The second line: &ldquo;Python is cool&rdquo;</li>
<li>The third line: &ldquo;JavaScript is amazing&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>1-multi_languages.js</code></li>
</ul>
</div>

<h3 class="panel-title">
      2. Arguments
    </h3>
<p>Write a script that prints a message depending of the number of arguments passed:</p>

<ul>
<li>If no arguments are passed to the script, print &ldquo;No argument&rdquo;</li>
<li>If only one argument is passed to the script, print &ldquo;Argument found&rdquo;</li>
<li>Otherwise, print &ldquo;Arguments found&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<p>Reference: <a href="/rltoken/E5x0rMmgii1g_Da9R7DUag" title="process.argv" target="_blank">process.argv</a></p>

<pre><code>guillaume@ubuntu:~/0x12$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>2-arguments.js</code></li>
</ul>
</div>
<h3 class="panel-title">
      3. Value of my argument
    </h3>

<p>Write a script that prints the first argument passed to it:</p>

<ul>
<li>If no arguments are passed to the script, print &ldquo;No argument&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>length</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
School
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>3-value_argument.js</code></li>
</ul>
</div>
<h3 class="panel-title">
      4. Create a sentence
    </h3>

<p>Write a script that prints two arguments passed to it, in the following format: &ldquo;<first argument> is <second argument>&rdquo;</p>

<ul>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>4-concat.js</code></li>
</ul>
</div>
<h3 class="panel-title">
      5. An Integer
    </h3>
<p>Write a script that prints <code>My number: &lt;first argument converted in integer&gt;</code> if the first argument can be converted to an integer:</p>

<ul>
<li>If the argument can&rsquo;t be converted to an integer, print &ldquo;Not a number&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use <code>try/catch</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js &quot;89&quot;
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>5-to_integer.js</code></li>
</ul>
</div>

<h3 class="panel-title">
      6. Loop to languages
    </h3>
 <p>Write a script that prints 3 lines: (like <code>1-multi_languages.js</code>) but by using an array of string and a loop</p>

<ul>
<li>The first line: &ldquo;C is fun&rdquo;</li>
<li>The second line: &ldquo;Python is cool&rdquo;</li>
<li>The third line: &ldquo;JavaScript is amazing&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You are not allowed to use any <code>if/else</code> statement</li>
<li>You can use only one <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>6-multi_languages_loop.js</code></li>
</ul>
</div>

<h3 class="panel-title">
      7. I love C
    </h3>
<p>Write a script that prints <code>x</code> times &ldquo;C is fun&rdquo;</p>

<ul>
<li>Where <code>x</code> is the first argument of the script</li>
<li>If the first argument can&rsquo;t be converted to an integer, print &ldquo;Missing number of occurrences&rdquo;</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You can use only two <code>console.log</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>



<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>7-multi_c.js</code></li>
</ul>
</div>
<h3 class="panel-title">
      8. Square
    </h3>
 <p>Write a script that prints a square</p>

<ul>
<li>The first argument is the size of the square</li>
<li>If the first argument can&rsquo;t be converted to an integer, print &ldquo;Missing size&rdquo;</li>
<li>You must use the character <code>X</code> to print the square</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
<li>You must use a loop (<code>while</code>, <code>for</code>, etc.)</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js School
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>8-square.js</code></li>
</ul>
</div>

<h3 class="panel-title">
      9. Add
    </h3>
 <p>Write a script that prints the addition of 2 integers</p>

<ul>
<li>The first argument is the first integer</li>
<li>The second argument is the second integer</li>
<li>You have to define a function with this prototype: <code>function add(a, b)</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./9-add.js 
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>9-add.js</code></li>
</ul>
</div>

 <h3 class="panel-title">
      10. Factorial
    </h3>
   <p>Write a script that computes and prints a factorial</p>

<ul>
<li>The first argument is integer (argument can be cast as integer) used for computing the factorial</li>
<li>Factorial of <code>NaN</code> is <code>1</code></li>
<li>You must do it recursively</li>
<li>You must use a function</li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./10-factorial.js 
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>10-factorial.js</code></li>
</ul>
</div>
 <h3 class="panel-title">
      11. Second biggest!
    </h3>
<p>Write a script that searches the second biggest integer in the list of arguments.</p>

<ul>
<li>You can assume all arguments can be converted to integer</li>
<li>If no argument passed, print <code>0</code></li>
<li>If the number of arguments is 1, print <code>0</code></li>
<li>You must use <code>console.log(...)</code> to print all output</li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>11-second_biggest.js</code></li>
</ul>
</div>
 <h3 class="panel-title">
      12. Object
    </h3>
<p>Update this script to replace the value <code>12</code> with <code>89</code>:</p>

<ul>
<li>You are not allowed to use <code>var</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: &#39;object&#39;,
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: &#39;object&#39;, value: 12 }
{ type: &#39;object&#39;, value: 89 }
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>12-object.js</code></li>
</ul>
</div>
<h3 class="panel-title">
      13. Add file
    </h3>
<p>Write a function that returns the addition of 2 integers.</p>

<ul>
<li>The function must be visible from outside</li>
<li>The name of the function must be <code>add</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>

<p><a href="/rltoken/M3uMoMlngAtefSYF1c7PNQ" title="Tip" target="_blank">Tip</a> </p>

<pre><code>guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require(&#39;./13-add&#39;).add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$ 
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

<!-- Github information -->
<div class="list-group-item">
<p><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holbertonschool-higher_level_programming</code></li>
    <li>Directory: <code>0x12-javascript-warm_up</code></li>
    <li>File: <code>13-add.js</code></li>
</ul>
</div>
