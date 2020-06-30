%rebase('template.tpl')

<div>
	<p>Please provide a username and password for your account</p>
    <form action="/signup" method="post">
        Username: <input name="username" type="text"/>
        Password: <input name="password" type="password"/>
        <input value="Sign up" type="submit"/>
    </form>
</div>