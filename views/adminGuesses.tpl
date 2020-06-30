%rebase('template.tpl')

<p>
	Here are the attempts at the admin password:
</p>

%for x in guesses:
	{{x[0]}}<br>
%end