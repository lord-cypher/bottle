%rebase("template.tpl")

%import sqlite3

%conn = sqlite3.connect('data.db')
%c = conn.cursor()
%c.execute('SELECT COUNT(*) FROM blog')
%conn.commit()

%count = c.fetchone()[0]

<div>
	<center>
		<h1>Welcome to the blog</h1>
	
	%for x in range(count):
		<a href="blog/post{{x + 1}}">Post {{x + 1}}</a><br>
	%end

	</center>
</div>


%c.close()