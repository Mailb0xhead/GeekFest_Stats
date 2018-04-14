#!e:/Python36/python.exe
import sys
import datetime
import woodstock_web_procs

vStyle = """
<STYLE>
@font-face { font-family: Century; src: url('GOTHIC.ttf'); }
body{
font-family: Century;
background: rgb(51,51,51);
color: #fff;
padding:20px;
}
.pagina{
width:auto;
height:auto;
}
.linha{
width:auto;
padding:5px;
height:auto;
display:table;
align: center;
}
.tile{
height:100px;
width:100px;
float:left;
margin:0 5px 0 0;
padding:2px;
background-image: url("metal_bkg.jpg");
}
.tileLargo{
width:210px;
}
.amarelo{
background:#DAA520;
}
.vermelho{
background:#CD0000;
}
.azul{
background:#4682B4;
}
.verde{
background-color: #2E8B57;
}
#outPopUp {
  position: absolute;
  width: 300px;
  height: 200px;
  z-index: 15;
  top: 50%;
  left: 50%;
  margin: -100px 0 0 -150px;
  background-image: url(metal_bkg.jpg);
}

.flip-container {
	perspective: 100px;
}
	/* flip the pane when hovered */
	.flip-container:hover .flipper, .flip-container.hover .flipper {
		transform: rotateY(180deg);
	}

.flip-container, .front, .back {
	width: 100px;
	height: 100px;
}

/* flip speed goes here */
.flipper {
	transition: 0.6s;
	transform-style: preserve-3d;

	position: relative;
}

/* hide back of pane during swap */
.front, .back {
	backface-visibility: hidden;

	position: absolute;
	top: 0;
	left: 0;
}

/* front pane, placed above back */
.front {
	z-index: 2;
	/* for firefox 31 */
	transform: rotateY(0deg);
}

/* back, initially hidden pane */
.back {
	transform: rotateY(180deg);
}
</STYLE>
"""

vHTML = """
<table><tr>
<td>
<div class="pagina flip-container" ontouchstart"this.classList.toggle('hover');>
<div class="flipper">
<div class="front tile amarelo">This is the front</div>
<div class="back tile azul">this is the back</div>
</div></div></td>
<td>
<div class="pagina flip-container" ontouchstart"this.classList.toggle('hover');>
<div class="flipper">
<div class="front tile amarelo">This is the front</div>
<div class="back tile azul">this is the back</div>
</div></div></td>
<td>
<div class="pagina flip-container" ontouchstart"this.classList.toggle('hover');>
<div class="flipper">
<div class="front tile amarelo">This is the front</div>
<div class="back tile azul">this is the back</div>
</div></div></td>
<tr>
<td>
<div class="pagina flip-container" ontouchstart"this.classList.toggle('hover');>
<div class="flipper">
<div class="front tile amarelo">This is the front</div>
<div class="back tile azul">this is the back</div>
</div></div></td>
<td>
<div class="pagina flip-container" ontouchstart"this.classList.toggle('hover');>
<div class="flipper">
<div class="front tile amarelo">This is the front</div>
<div class="back tile azul">this is the back</div>
</div></div></td>
<td>
<div class="pagina flip-container" ontouchstart"this.classList.toggle('hover');>
<div class="flipper">
<div class="front tile amarelo">This is the front</div>
<div class="back tile azul">this is the back</div>
</div></div></td>
</tr></table>
<div class="pagina flip-container" ontouchstart"this.classList.toggle('hover');>
<div class="linha">
<div class="flipper">
<div class="front tile amarelo"></div>
<div class="back tile azul"></div>
</div>
<div class="tile tileLargo vermelho">
</div> <div class="tile verde">
</div>
<div class="tile tileLargo amarelo">
</div>
</div>
<div class="linha">
<div class="tile tileLargo amarelo">
</div> <div class="tile">
</div> <div class="tile verde" style="background-image: "metal_bkg.jpg;">
</div> <div class="tile vermelho">
</div> <div class="tile tileLargo verde">
</div> </div>
<div class="linha">
<div class="tile amarelo">
</div> <div class="tile verde">
</div> <div class="tile vermelho">
</div> <div class="tile tileLargo verde">
</div> <div class="tile azul">
</div> <div class="tile verde">
</div> </div> </div>
"""



# MAIN PROGRAM
woodstock_web_procs.set_header(1)
print(vStyle)
print(vHTML)
print('<div id="outPopUp">TEST</div>')
print('<BR><BR><div style="overflow-x:auto; font-size: x-large; padding:5px; float: left;">')
print('COMING SOON')
print('</DIV>')
woodstock_web_procs.set_footer()
