<!DOCTYPE html>
<html>
<head>
    <title>Sum Calculator</title>
</head>
<body>
    <h1>Sum Calculator</h1>
    <form method="post">
        <label for="num1">Enter first number:</label>
        <input type="text" id="num1" name="num1"><br>
        <label for="num2">Enter second number:</label>
        <input type="text" id="num2" name="num2"><br>
        <input type="submit" value="Calculate Sum">
    </form>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $num1 = $_POST["num1"];
        $num2 = $_POST["num2"];
        if (!is_numeric($num1) || !is_numeric($num2)) {
            echo "<p>Please enter valid numbers.</p>";
        } else {
            $sum = $num1 + $num2;
            echo "<p>Sum: $sum</p>";
        }
    }
        $sum = shell_exec("echo $num1 + $num2 | bc");
        echo "<p>Sum: $sum</p>";
        
    ?>
</body>
</html>
