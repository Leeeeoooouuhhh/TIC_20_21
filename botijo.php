<?php
//Aquí el código
$token = "1664353563:AAFrBvhGSWgqFtJDj4dn3qsIspRR0v6hlPc";
$website = "https://api.telegram.org/bot".$token;
$input = file_get_contents("php://input");
$update = json_decode($input, TRUE);

$chatId = $update["message"]["chat"]["id"];
$message = $update["message"]["text"];
switch($message){
	case "Hola":
		$response = "Que tal?";
		break
	case "/start":
		$response = "Buenas taldes, soy el bot";
		break
	case "/info":
		$response = "¿Eres bobo o que te pasa?";
		break
	default:
		$response= "Bueno no lo sé";
		break
}
function sendMessage($chatId, $response) {
	$url = $GLOBALS["website"]."/sendMessage?chatId=".$GLOBALS["chatId"]."&parse_mode=HTML&text=".urlencode($response);
	file_get_contents($url);

}
?>
