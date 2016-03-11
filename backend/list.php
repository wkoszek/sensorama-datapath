<?php

$dir = "sensorama_data";
$dh  = opendir($dir);

while (false !== ($filename = readdir($dh))) {
	if ($filename == "." || $filename == "..") {
		continue;
	}
	$files[] = $filename;
}

sort($files);
print json_encode($files);

?>
