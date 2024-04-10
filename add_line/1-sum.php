@@ -23,6 +23,9 @@
             echo "<p>Sum: $sum</p>";
         }
     }
+        $sum = shell_exec("echo $num1 + $num2 | bc");
+        echo "<p>Sum: $sum</p>";
+        
     ?>
 </body>
 </html>