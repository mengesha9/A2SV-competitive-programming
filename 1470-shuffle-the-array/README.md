<h2><a href="https://leetcode.com/problems/shuffle-the-array/">1470. Shuffle the Array</a></h2><h3>Easy</h3><hr><div><p><font _mstmutation="1" _msthash="4660643" _msttexthash="1649726">Given the array  consisting of  elements in the form .</font><code>nums</code><code>2n</code><code>[x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>,y<sub>1</sub>,y<sub>2</sub>,...,y<sub>n</sub>]</code></p>

<p><font _mstmutation="1" _msthash="4660760" _msttexthash="599950"><em _mstmutation="1">Return the array in the form</em> .</font><code>[x<sub>1</sub>,y<sub>1</sub>,x<sub>2</sub>,y<sub>2</sub>,...,x<sub>n</sub>,y<sub>n</sub>]</code></p>

<p>&nbsp;</p>
<p><strong class="example" _msthash="4660994" _msttexthash="114439">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,5,1,3,4,7], n = 3
<strong>Output:</strong> [2,3,5,4,1,7] 
<strong>Explanation:</strong> Since x<sub>1</sub>=2, x<sub>2</sub>=5, x<sub>3</sub>=1, y<sub>1</sub>=3, y<sub>2</sub>=4, y<sub>3</sub>=7 then the answer is [2,3,5,4,1,7].
</pre>

<p><strong class="example" _msthash="4661228" _msttexthash="114621">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,4,4,3,2,1], n = 4
<strong>Output:</strong> [1,4,2,3,3,2,4,1]
</pre>

<p><strong class="example" _msthash="4661462" _msttexthash="114803">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,2,2], n = 2
<strong>Output:</strong> [1,2,1,2]
</pre>

<p>&nbsp;</p>
<p><strong _msthash="4758767" _msttexthash="199901">Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>nums.length == 2n</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^3</code></li>
</ul></div>