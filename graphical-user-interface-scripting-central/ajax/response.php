<?php
  header('Content-type: text/xml');
  
  $rating = $_POST['rating'];
  
  function record_rating($rating) {
    // Add data to database here
    return 1;
  }
?>
<xmlresponse>
    <rating><?= $rating ?></rating>
    <result><?= record_rating($rating) ?></result>
</xmlresponse>