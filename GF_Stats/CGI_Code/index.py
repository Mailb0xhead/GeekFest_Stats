#!e:/Python36/python.exe
import sys
import datetime
import time
import gf_procs


timeStr = time.strftime("%c") # obtains current time

gf_procs.set_header(6)

htmlHeader = """
"""
style = """
<style>
p {
  text-align: center;
  font-size: 150%;
  font-weight: bold;
  color: red;
  margin-top:0px;
}
</style>
"""

htmlFormat = """
  <center>
  <img src="/generations.jpg" height="80%" align="middle">
  <p id="clock"></p>
  <a href="/hlstats.php?mode=players&game=csgo">See Test Run Player Stats</a>
  </center>

</body>
</html>"""
js = """
  <script>
  // Set the date we're counting down to
  var countDownDate = new Date("Feb 18, 2018 12:00:00").getTime();

  // Update the count down every 1 second
  var x = setInterval(function() {

  // Get todays date and time
  var now = new Date().getTime();

  // Find the distance between now an the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("clock").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";

  // If the count down is finished, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("clock").innerHTML = "The fun has begun!";
  }
}, 1000);
</script> 
"""

print(htmlHeader)
print(style)

print(htmlFormat)

print(js)
