<?php

$user_input = $_GET['input'];

$sanitized_input = preg_replace('/[^0-9+]/', '', $user_input);

$result = my_eval($sanitized_input);

function my_eval($input) {
    if (preg_match('/^\d+\+\d+$/', $input)) {
        eval("\$result = $input;");
        return $result;
    } else {
        return "Invalid input";
    }
}

echo "Result: $result";
?>