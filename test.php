<?php
//時間は前処理で時間にして渡す
$data=array(25,'男性',175.5,68.2,15,5,450.0,650.0);
$pythonPath=dirname(__FILE__)."/stomach_api/lightGBM_Inference.py";
$cmd="python3 ".$pythonPath." ".implode(" ",$data);
exec($cmd,$out);

$result=$out[0];

echo $result;

?>