<!DOCTYPE html>
<html>
	<head>
		<title></title>
	</head>
	<link rel="stylesheet" type="text/css" href="/static/css/auka.css">
	<body style="font-family: Arial;">

	    <nav>
			<ul>
				<li><a href="/">Sign In</a></li>
				<li><a href="/signup">Sign Up</a></li>
			</ul>
		</nav>

		<h2>Sign Up</h2>
		<form method="post" action="/signup">
			Notendanafn<br>
			<input type="text" name="SignUp_username" autocomplete="off" placeholder="Sláðu inn nýtt notendanafn" required><p>
			Lykilorð<br>
			<input type="password" maxlength="10" name="SignUp_password" placeholder="Sláðu inn nýtt lykilorð" required><p>
			<input type="submit" value="Sign up">
		</form>
	</body>
</html>
