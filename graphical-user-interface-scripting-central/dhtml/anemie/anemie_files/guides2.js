<!--

// Copyright © 1997-1999 Butz Yung. All rights reserved.
// Do NOT copy or modify any part of the script without permission.
// All comments and notice must be left as is.
// Homepage: http://animetheme.vill.edu/

if (dhtml)
  var width = screen.width - (120 + 167 + 80)
else
  event = null

var Rei = new pilot("Rei", reiTable)
var reiPath = null
var loaded = false

var visible, hidden
if (ie4) {
  visible = "visible"
  hidden = "hidden"
}
else {
  visible = "show"
  hidden = "hide"
}

function start() {
  loaded = true
  status = "Welcome to Anime Theme!"
  if (ie4) {
    reiPath = new Path("rei", "pathStop")
    Rei.target = rei.style
    Rei.msg = Lrei.style
    Rei.img = Irei
    Rei.y += document.body.scrollTop
    rei.style.visibility = visible
  }
  else {
    reiPath = new Path("document.rei", "pathStop")
    Rei.target = document.rei
    Rei.msg = document.Lrei
    Rei.img = document.rei.document.Irei
    document.rei.visibility = visible
    setInterval('runPath2()', 100)
    setTimeout('scrollTo(0,0)', 0)
  }
  wander()
  Rei.hello(Rei.events[0])
  Rei.img.src = guides_img[guide_count][1].src
}

function distance(x, y) {
  return Math.sqrt(Math.pow(Math.abs(Rei.x - x), 2) + Math.pow(Math.abs(Rei.y - y), 2))
}

function move(x, y) {
  var xy = new Array(Rei.x, Rei.y, x, y)
  reiPath.Stop()
  reiPath.Duration = distance(x, y) / 500
  reiPath.Bounce = 0
  reiPath.Repeat = 1
  reiPath.PolyLine(2,xy)
  Rei.x = x
  Rei.y = y
  Rei.running = true
  reiPath.Play()
}

function wander() {
  reiPath.Repeat = -1
  reiPath.Duration = 5
  reiPath.Oval(Rei.x, Rei.y, 50, 20)
  reiPath.Play()
}

function pilot(name, events) {
  this.name = name
  this.x = 50
  this.y = 50
  this.event_count = 0
  this.hide_count = 0
  this.guide_count = 0
  this.events = events
  this.intros = new Array(events[0])
  this.running = false
  this.hello = hello
}

function come(intros, e, link) {
  if (!loaded || Rei.running || (Rei.intros[0] == intros[0]))
    return
  Rei.intros = intros
  if (link) {
    Rei.href = link.href
    Rei.link_target = (link.target) ? link.target : ""
  }
  else
    Rei.href = ""
  Rei.clicked = false
  var x = (ie5) ? e.clientX + document.body.scrollLeft : e.x
  var y = (ie5) ? e.clientY + document.body.scrollTop : e.y
  if (x < 215)
    x = 25
  else if (x > width + 215)
    x = width
  else
    x -= 215
  Rei.guide_count = 0
  Rei.img.src = guides_img[guide_count][0].src
  move(x, y - 50)
}

function hello(msg) {
  if (!msg) {
    var target = (Math.random() > 0.5) ? this.events : this.intros
    msg = target[random(target)]
  }
  if (ie4)
    Lrei_msg.innerText = msg
  else {
    var d = document.Lrei.document.Lrei_msg.document
    d.open()
    d.write('<LAYER style="font-size:14px;font-family:Comic Sans MS; color:black">' + msg + '</LAYER>')
    d.close()
  }
  Rei.msg.top = parseInt(this.target.top) + 120
  Rei.msg.left = parseInt(this.target.left) + 120
  Rei.msg.visibility = visible
  Rei.hide_count = 20
  Rei.event_count = Math.round(Math.random() * 50 + 0.5) + 30
}

function introduce() {
  if (!loaded || !dhtml || Rei.running)
    return
  Rei.img.src = guides_img[guide_count][0].src
  Rei.guide_count = 50
  if (Rei.href) {
    if (Rei.clicked) {
      var target
      if (Rei.link_target.indexOf("top") != -1)
        target = top
      else if (Rei.link_target.indexOf("parent") != -1)
        target = parent
      else
        target = self
      Rei.hello(ok_msg)
      target.location = Rei.href
    }
    else {
      Rei.clicked = true
      Rei.hello(default_msg)
    }
  }
  else
    Rei.hello(Rei.intros[random(Rei.intros)])
}

function random(target) {
  return Math.round(Math.random() * target.length - 0.5)
}

function checkGuide() {
  if (--Rei.hide_count == 0)
    Rei.msg.visibility = hidden
  if (--Rei.event_count == 0)
    Rei.hello()
  if (--Rei.guide_count == 0)
    Rei.img.src = guides_img[guide_count][1].src
}

function runPath2() {
  runPath()
  checkGuide()
}

function pathStop() {
  if (!Rei.running)
    return
  Rei.running = false
  Rei.guide_count = 50
  Rei.hello(Rei.intros[0])
  wander()
}

var guide_count, temp_count, guides, img_loaded, guides_img, load_count

function initLoading(target) {
  guide_count = 0
  guides = target
  guides_img = new Array()
  for (var i = 0; i < guides.length; i++)
    guides_img[i] = new Array()
  for (var i = 0; i < 2; i++) {
    guides_img[0][i] = new Image()
    guides_img[0][i].src = guides[0] + "0" + i + ".gif"
  }
  img_loaded = new Array()
  img_loaded[0] = true
}

function nextGuide() {
  if (!dhtml) {
    status = "This requires MSIE or Netscape 4.0."
    return
  }
  if (!loaded) {
    status = "Please wait until the page is completely loaded."
    return
  }
  temp_count = guide_count + 1
  if (temp_count == guides.length)
    temp_count = 0
  Rei.hello("A new guide is coming. Please wait for a while~!")
  if (img_loaded[temp_count]) {
    setTimeout("prepareGuide()", 1000)
    return
  }
  load_count = 0
  for (var i = 0; i < 2; i++) {
    var img = guides_img[temp_count]
    img[i] = new Image()
    img[i].onload = loadingGuide
    img[i].src = guides[temp_count] + "0" + i + ".gif"
  }
}

function loadingGuide() {
  if (++load_count < 2)
    return
  img_loaded[temp_count] = true
  setTimeout("prepareGuide()", 1000)
}

function prepareGuide() {
  guide_count = temp_count
  Rei.img.src = guides_img[guide_count][1].src
  Rei.hello("Hello~!")
}

var first_error = true

function error(msg, filename, line) {
  if (first_error) {
    if (confirm("An error has occurred in the script on this page.\n\nLine: " + line + "\nError: " + msg + "\n\n" + "Press OK to send me an automatic bug report, or press CANCEL to continue."))
      window.location = "mailto:butz@hkstar.com?body=" + window.location.href + "%0A" + filename + "%0A" + line + "%0A" + msg + "%0A" + navigator.appName + " " + navigator.appVersion
    first_error = false
  }
  return true
}

window.onerror = error

if (dhtml)
  window.onload = start

//-->
