<!DOCTYPE html>
	<html>
	<head>
		<title></title>
		<link rel="stylesheet" type="text/css" href="/static/css/minar.css">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
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
						<u>LISTINN MINN</u>
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
		<h1>LISTINN MINN</h1><br>
			Notandi: <b>{{nafn}}</b>
			<br><br>
			<br><br>
			<table>
				<tbody>
				    % for i in data:
                        <tr>
                            <td>{{i[1]}}</td>
                        </tr>
                    % end
				</tbody>
			</table>
			<br><br>
		</article>
	</body>
</html>