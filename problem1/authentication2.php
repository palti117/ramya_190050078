<!DOCTYPE html>
<html>
<head>
    <title>YourBrick | Welcome</title>
    <link rel="stylesheet" type="text/css" href="style4.css">
</head>
<body>
    <?php      
    include('connection.php');  
    if(isset($_POST["submit"])){  
        if(!empty($_POST['user']) && !empty($_POST['pass'])) {  
        $user=$_POST['user'];  
        $pass=$_POST['pass'];   
        $query=mysqli_query("SELECT * FROM login WHERE username='".$user."'");  
        $numrows=mysqli_num_rows($query);  
            if($numrows==0){  
                $sql="INSERT INTO login(username,password) VALUES('$user','$pass')";  
              
                $result=mysqli_query($sql);  
                if($result){  
                    echo "Account Successfully Created";  
                }
                else {  
                    echo "Failure!";  
                }    
            }   
        }
    }
?>
</body>
</html>