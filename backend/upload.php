<?php
date_default_timezone_set("UTC");

$putdata = fopen("php://input", "r");
$filename = strftime("sensorama_data/%Y%m%d.%H%M%S." . rand());
print $filename . "\n";
$fp = fopen($filename, "w");
while ($data = fread($putdata, 1024)) {
	fwrite($fp, $data);
}
fclose($fp);
fclose($putdata);

?>
