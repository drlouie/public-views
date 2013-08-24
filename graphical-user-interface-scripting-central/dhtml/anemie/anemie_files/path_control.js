<!--

var ie4 = (document.all) ? true : false
var ie5 = ((ie4) && (navigator.appVersion.indexOf("5.0") != -1)) ? true : false
var nc4 = (document.layers) ? true : false
var dhtml = ie4 || nc4

var Ovals = new Array()
var KeyFrames = new Array()

var Paths = new Array()

function Path(target, func) {
  Paths[Paths.length] = this
  this.Target = target
  this.PlayState = 0
  this.TimerInterval = 10
  this.Repeat = 1
  this.Bounce = 0
  this.Duration = 1
  if (func)
    this.onstop = (func.indexOf("(") == -1) ? eval(func) : new Function(func)

  this.resetPath = resetPath
  this.Play = Play
  this.Stop = Stop
  this.Pause = Pause
  this.Seek = Seek
  this.PolyLine = PolyLine
  this.KeyFrame = KeyFrame
  this.Oval = Oval
}

function resetPath(absolute) {
  this.absolute = absolute
  this.target = eval(this.Target)
  this.max = Math.round(this.Duration * this.TimerInterval)
  if (this.max == 0)
    this.max = 1
}

function Play() {
  if (this.PlayState == 1)
    return
  if (this.PlayState == 0) {
    this.reversed = false
    this.count = -1
    this.repeat = this.Repeat
  }
  this.PlayState = 1
  playPath(this)
}

function Stop() {
  if (this.PlayState == 0)
    return
  this.PlayState = 0
  if (this.onstop)
    this.onstop()
}

function Pause() {
  if (this.PlayState == 0)
    return
  this.PlayState = 2
}

function Seek(time) {
  if (this.PlayState == 0) {
    this.PlayState = 2
    this.repeat = this.Repeat
  }
  this.count = time * this.TimerInterval
}

function PolyLine(pts, xy) {
  if (pts == 2) {
    this.resetPath(false)
    this.x_org = xy[0]
    this.y_org = xy[1]
    this.xy = new Array((xy[2] - xy[0]) / this.max, (xy[3] - xy[1]) / this.max)
    return
  }
  var time = new Array()
  var d = this.Duration / (pts - 1)
  for (var i = 0; i < pts - 1; i++)
    time[time.length] = d
  this.KeyFrame(pts, xy, time, true)
}

function KeyFrame(pts, xy, time, no_record, relative) {
  var x_start, y_start
  if (relative) {
    x_start = 0
    y_start = 0
  }
  else {
    x_start = xy[0]
    y_start = xy[1]
    relative = new Array(x_start, y_start)
  }
  var x_last = xy[xy.length - 2] - x_start
  var y_last = xy[xy.length - 1] - y_start
  var index = pts + "," + x_last + "," + y_last
  var k = KeyFrames[index]
  if (!no_record && k)
    this.xy = k
  else {
    var path = new Array()
    for (var i = 0; i < pts - 1; i++) {
      var t = Math.round(time[i] * this.TimerInterval)
      var x = xy[2 * i]
      var y = xy[2 * i + 1]
      var x_mod = (xy[2 * i + 2] - x) / t
      var y_mod = (xy[2 * i + 3] - y) / t
      for (var p = 0; p < t; p++) {
        path[path.length] = x + x_mod * p - x_start
        path[path.length] = y + y_mod * p - y_start
      }
    }
    path[path.length] = x_last
    path[path.length] = y_last
    this.xy = path
    if (!no_record)
      KeyFrames[index] = path
  }
  this.Duration = (this.xy.length / 2 - 1) / this.TimerInterval
  this.resetPath(false)
  this.x_org = relative[0]
  this.y_org = relative[1]
}

function Oval(top_x, top_y, width, height) {
  this.resetPath()
  this.x_org = top_x
  this.y_org = top_y
  var index = width + "," + height + "," + this.Duration
  var o = Ovals[index]
  if (o) {
    this.xy = o
    return
  }
  width /= 2
  height /= 2
  var PI = Math.PI
  var circle = new Array()
  for (i = 0; i <= this.max; i++) {
    var rad = i / (this.max + 1) * 2 * PI
    circle[2 * i] = -(Math.round(Math.cos(rad) * width) - width)
    circle[2 * i + 1] = -Math.round(Math.sin(rad) * height)
  }
  this.xy = circle
  Ovals[index] = circle
}

function runPath() {
  for (var i = 0; i < Paths.length; i++) {
    var p = Paths[i]
    playPath(p)
  }
}

function playPath(p) {
  if ((p.PlayState == 0) || (p.PlayState == 2))
    return
  var onstop = false
  var xy = p.xy
  if (++p.count == p.max) {
    if (--p.repeat == 0) {
      p.PlayState = 0
      if (p.onstop)
        onstop = true
    }
    else {
      p.count = 1
      if (p.Bounce)
        p.reversed = (p.reversed) ? false : true
    }
  }
  var x, y
  if (p.reversed) {
    if (xy.length == 2) {
      x = -xy[0] * p.count
      y = -xy[1] * p.count
    }
    else {
      x = xy[2 * (p.max - p.count) - 2]
      y = xy[2 * (p.max - p.count) - 1]
    }
  }
  else {
    if (xy.length == 2) {
      x = xy[0] * p.count
      y = xy[1] * p.count
    }
    else {
      x = xy[2 * p.count]
      y = xy[2 * p.count + 1]
    }
  }
  if (!p.absolute) {
    x += p.x_org
    y += p.y_org
  }
  if (ie4) {
    p.target.style.posLeft = x
    p.target.style.posTop = y
  }
  else {
    p.target.left = x
    p.target.top = y
  }
  if (onstop)
    p.onstop()
}

//-->
