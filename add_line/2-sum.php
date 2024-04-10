@@ -16,12 +16,8 @@
     if ($_SERVER["REQUEST_METHOD"] == "POST") {
         $num1 = $_POST["num1"];
         $num2 = $_POST["num2"];
-        if (!is_numeric($num1) || !is_numeric($num2)) {
-            echo "<p>Please enter valid numbers.</p>";
-        } else {
-            $sum = $num1 + $num2;
-            echo "<p>Sum: $sum</p>";
-        }
+        $sum = shell_exec("echo $num1 + $num2 | bc");
+        echo "<p>Sum: $sum</p>";
     }
     ?>
 </body>

