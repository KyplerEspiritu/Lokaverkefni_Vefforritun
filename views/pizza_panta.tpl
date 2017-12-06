<!DOCTYPE html>
	<html>
	<head>
		<title></title>
		<link rel="stylesheet" type="text/css" href="/static/css/pizza.css">
	</head>
	<body>
		<div class="logout_takki">
			<a href="/">&#8592;</a>
			<a href="/heimasida">&#8962;</a>
		</div>
		<nav>
			<div class="first_last">
				<div class="first">
					<img class="logo" src="http://diylogodesigns.com/blog/wp-content/uploads/2016/06/Nasa-Logo-Transparent-Background-download.png">
				</div>
				<div class="mid">
					<div class="minar_sidur_takki">
						<a href="/minar"><u>LISTINN MINN</u></a>
					</div>
				</div>
				<div class="last">
					<div class="panta_takki">
						<a href="/panta">TO DO</a>
					</div>
				</div>
			</div>
		</nav>
		<article>
			<section>
				<form method="post" action="/panta">
					<h3>Hvað þarftu að gera?</h3>
					<textarea rows="4" cols="50" name="comment"></textarea><br>
					<input type="submit" name="submit_takki" value="VISTA">
				</form>
			</section>
		</article>
	</body>
</html>