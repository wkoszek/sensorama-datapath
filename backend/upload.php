<?php

$putdata = fopen("php://input", "r");
$filename = strftime("sensorama_data/%Y%m%d.%H%s" . random());
$fp = fopen($filename, "w");
while ($data = fread($putdata, 1024)) {
	fwrite($fp, $data);
}
fclose($fp);
fclose($putdata);

?>
