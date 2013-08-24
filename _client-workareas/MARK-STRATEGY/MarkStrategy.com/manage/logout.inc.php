<?
	if (!defined('INNER')) exit;

	$message = 'You successfully logged out';
	session_destroy();

	include 'login.inc.php';
?>