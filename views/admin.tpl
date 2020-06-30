%rebase('template.tpl')

<center>

	<p>
		{{content}}
	</p>

	<p>
		<h1>Please enter the secret password.</h1>
	</p>
	<form accept="/admin" method=post>
		<input name="text" type="text" size="100" />
		<br><br>
		<input type="submit" value="Enter">		
	</form>
</center>