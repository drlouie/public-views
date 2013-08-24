////////////////////////////
// mp3player.as for Flash MX
//
// description:
//   actionscript generated mp3 player
//   create a blank 550x150 movie and "#include" this file
//
// Enrico Pancaldi
// sw@throp.net
// 23 Nov 2002
//
// THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND
// USE IT AT YOUR OWN RISK
////////////////////////////

objs = 0;
main_color = 0x0000ff;
//stop button
_root.createEmptyMovieClip("stop_btn", objs++);
with (stop_btn)
{
	_x = 10;
	_y = 70;
	beginFill(main_color, 100);
	moveTo(0,0);
	lineTo(0,12);
	lineTo(12,12);
	lineTo(12,0);
	lineTo(0,0);
	endFill();
}
stop_btn.onRelease = function()
{
	_root.offset = 0;
	clearInterval(_root.sliderhandle);
	_root.slider.pointer._x = 0;
	_root.mySound.stop();
	delete _root.mySound;
	_root.mySound = new Sound();
	if (_root.repeat._currentframe == 1)
		_root.mySound.onSoundComplete = _root.singleLoop;
	else
		_root.mySound.onSoundComplete = _root.multiLoop;
	_root.volume.pointer._x = 100;
	_root.balance.pointer._x = 0;
};
//pause hit area
_root.createEmptyMovieClip("pause_hit_area", objs++);
with (pause_hit_area)
{
	_x = 40;
	_y = 70;
	beginFill(main_color, 100);
	moveTo(0,0);
	lineTo(0,12);
	lineTo(12,12);
	lineTo(12,0);
	lineTo(0,0);
	endFill();
}
pause_hit_area._visible = false;
//pause button
_root.createEmptyMovieClip("pause_btn", objs++);
with (pause_btn)
{
	_x = 40;
	_y = 70;
	beginFill(main_color, 100);
	moveTo(0,0);
	lineTo(0,12);
	lineTo(4,12);
	lineTo(4,0);
	lineTo(0,0);
	moveTo(8,0);
	lineTo(8,12);
	lineTo(12,12);
	lineTo(12,0);
	lineTo(8,0);
	endFill();
}
pause_btn.hitArea = pause_hit_area;
pause_btn.onRelease = function()
{
	_root.offset = _root.mySound.position / 1000;
	clearInterval(_root.sliderhandle);
	_root.mySound.stop();
};
//play button
_root.createEmptyMovieClip("play_btn", objs++);
with (play_btn)
{
	_x = 70;
	_y = 70;
	beginFill(main_color, 100);
	moveTo(0,0);
	lineTo(12,6);
	lineTo(0,12);
	lineTo(0,0);
	endFill();
}
play_btn.onRelease = function()
{
	_root.mySound.loadSound(_root.songName.text, true);
	_root.mySound.start(_root.offset);
	_root.sliderhandle = setInterval(_root.updateSlider, 100);
};
//title text filed
_root.createTextField("title", objs++, 10, 6, 40, 18);
title.text = "TITLE";
title.selectable = false;
title.setTextFormat(new TextFormat("Arial", 12, main_color));
//songname input text field
_root.createTextField("songName", objs++, 10, 26, 530, 18);
//songName.variable = "songname";
songName.type = "input";
songName.border = true;
songName.borderColor = main_color;
songName.text = "NO AUDIO FILE";
songName.setTextFormat(new TextFormat("Arial", 12, main_color));
//repeat switch hit area
_root.createEmptyMovieClip("repeat_hit_area", objs++);
with (repeat_hit_area)
{
	_x = 10;
	_y = 114;
	beginFill(main_color);
	moveTo(0,7);
	curveTo(7,7,7,0);
	curveTo(7,-7,0,-7);
	curveTo(-7,-7,-7,0);
	curveTo(-7,7,0,7);
	endFill();
}
repeat_hit_area._visible = false;
//repeat switch
_root.createEmptyMovieClip("repeat", objs++);
with (repeat)
{
	_x = 10;
	_y = 114;
	createEmptyMovieClip("circle",0);
	with (circle)
	{
		_x = 0;
		_y = 0;
		lineStyle(0, main_color);
		moveTo(0,7);
		curveTo(7,7,7,0);
		curveTo(7,-7,0,-7);
		curveTo(-7,-7,-7,0);
		curveTo(-7,7,0,7);
	}
	createTextField("title", 1, 9, -9, 55, 18);
	title.text = "REPEAT";
	title.selectable = false;
	title.setTextFormat(new TextFormat("Arial", 12, main_color));
}
repeat.hitArea = repeat_hit_area;
repeat.onMouseUp = function()
{
	if (this.hitTest( _root._xmouse, _root._ymouse, false))
	{
		if (_root.mySound.onSoundComplete == _root.singleLoop)
		{
			_root.mySound.onSoundComplete = _root.multiLoop;
			with (_root.repeat.circle)
			{
				beginFill(main_color);
				moveTo(0,5);
				curveTo(5,5,5,0);
				curveTo(5,-5,0,-5);
				curveTo(-5,-5,-5,0);
				curveTo(-5,5,0,5);
				endFill();
			}
		}
		else
		{
			_root.mySound.onSoundComplete = _root.singleLoop;
			with (_root.repeat.circle)
			{
				clear();
				lineStyle(0, main_color);
				moveTo(0,7);
				curveTo(7,7,7,0);
				curveTo(7,-7,0,-7);
				curveTo(-7,-7,-7,0);
				curveTo(-7,7,0,7);
			}
		}
	}
};
_root.createEmptyMovieClip("slider", objs++);
with (slider)
{
	_x = 240;
	_y = 70;
	lineStyle(0, main_color);
	moveTo(0,0);
	lineTo(300,0);
	createEmptyMovieClip("pointer", 0);
	with (pointer)
	{
		_y = -5;
		beginFill(main_color);
		moveTo(0,10);
		curveTo(5,10,5,5);
		curveTo(5,0,0,0);
		curveTo(-5,0,-5,5);
		curveTo(-5,10,0,10);
		endFill();
	}
}
//volume
_root.createEmptyMovieClip("volume", objs++);
with (volume)
{
	_x = 240;
	_y = 114;
	lineStyle(0, main_color);
	moveTo(0,0);
	lineTo(100,0);
	createTextField("title", 1, 3, 3, 103, 18);
	title.text = " -     VOLUME     +";
	title.selectable = false;
	title.setTextFormat(new TextFormat("Arial", 12, main_color));
	createEmptyMovieClip("pointer", 0);
	with (pointer)
	{
		_x = 100;
		_y = -5;
		beginFill(main_color);
		moveTo(0,10);
		curveTo(5,10,5,5);
		curveTo(5,0,0,0);
		curveTo(-5,0,-5,5);
		curveTo(-5,10,0,10);
		endFill();
	}
}
volume.pointer.onPress = function()
{
	this.startDrag(false, 0, -5, 100, -5);
};
volume.pointer.onRelease = function()
{
	this.stopDrag();
	_root.mySound.setVolume(Math.floor(_root.volume.pointer._x));
};
volume.pointer.onReleaseOutside = function()
{
	this.stopDrag();
	_root.mySound.setVolume(Math.floor(_root.volume.pointer._x));
};
//balance
_root.createEmptyMovieClip("balance", objs++);
with (balance)
{
	_x = 480;
	_y = 114;
	lineStyle(0, main_color);
	moveTo(-50,0);
	lineTo(50,0);
	createTextField("title", 1, -47, 3, 103, 18);
	title.text = " l    BALANCE    r";
	title.selectable = false;
	title.setTextFormat(new TextFormat("Arial", 12, main_color));
	createEmptyMovieClip("pointer", 0);
	with (pointer)
	{
		_y = -5;
		beginFill(main_color);
		moveTo(0,10);
		curveTo(5,10,5,5);
		curveTo(5,0,0,0);
		curveTo(-5,0,-5,5);
		curveTo(-5,10,0,10);
		endFill();
	}
}
balance.pointer.onPress = function()
{
	this.startDrag(false, -50, -5, 50, -5);
};
balance.pointer.onRelease = function()
{
	this.stopDrag();
	_root.mySound.setPan(Math.floor(_root.balance.pointer._x*2));
};
balance.pointer.onReleaseOutside = function()
{
	this.stopDrag();
	_root.mySound.setPan(Math.floor(_root.balance.pointer._x*2));
};
//_root
mySound = new Sound();
mySound.onSoundComplete = singleLoop;
offset = 0;
function updateSlider()
{
	_root.slider.pointer._x = (_root.mySound.position/_root.mySound.duration)*_root.slider._width;
}
function singleLoop()
{
	clearInterval(_root.sliderhandle);
	_root.slider.pointer._x = 0;
}
function multiLoop()
{
	_root.offset = 0;
	_root.slider.pointer._x = 0;
	_root.mySound.start(_root.offset);
}

