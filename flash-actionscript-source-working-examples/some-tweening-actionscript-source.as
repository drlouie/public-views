function newTween(obj, prop, func, finish, duration, useSeconds)
{
    if (useSeconds == undefined)
    {
        var _l2 = true;
    } // end if
    tweenObj = "tweenObj" + prop;
    obj[tweenObj].stop();
    obj[tweenObj].clearInterval(name);
    obj[tweenObj].onMotionFinished = undefined;
    obj[tweenObj] = new as.transitions.Tween(obj, prop, func, finish, duration, _l2);
} // End of the function
function BuildHome()
{
    _root.createEmptyMovieClip("buildSectionEngine_mc", mainLevel());
    _root.buildSectionEngine_mc.counter = 1;
    _root.buildSectionEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeOut, 70, 0.800000);
            newTween(MAIN.loader_mc.loadTxt_mc, "_xscale", as.transitions.easing.Strong.easeOut, 180, 0.800000);
            newTween(MAIN.loader_mc.loadTxt_mc, "_yscale", as.transitions.easing.Strong.easeOut, 180, 0.800000);
            newTween(MAIN.loader_mc.loadGlow_mc, "_xscale", as.transitions.easing.Strong.easeOut, 180, 0.800000);
            newTween(MAIN.loader_mc.loadGlow_mc, "_yscale", as.transitions.easing.Strong.easeOut, 180, 0.800000);
            newTween(MAIN.loader_mc.type5_mc, "_x", as.transitions.easing.Strong.easeOut, 20, 0.800000);
        }
        else if (this.counter == 7)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 204, 0.300000);
        }
        else if (this.counter == 10)
        {
            newTween(MAIN.loader_mc.loadTxt_mc, "_xscale", as.transitions.easing.Bounce.easeOut, 100, 0.800000);
            newTween(MAIN.loader_mc.loadTxt_mc, "_yscale", as.transitions.easing.Bounce.easeOut, 100, 0.800000);
            newTween(MAIN.loader_mc.loadGlow_mc, "_xscale", as.transitions.easing.Bounce.easeOut, 100, 0.800000);
            newTween(MAIN.loader_mc.loadGlow_mc, "_yscale", as.transitions.easing.Bounce.easeOut, 100, 0.800000);
            newTween(MAIN.loader_mc.type5_mc, "_x", as.transitions.easing.Bounce.easeOut, -22, 0.800000);
            MAIN.loader_mc.type2_mc._visible = true;
            MAIN.loader_mc.type2_mc._xscale = MAIN.loader_mc.type2_mc._yscale = 250;
            MAIN.loader_mc.type2_mc._alpha = 0;
            MAIN.loader_mc.type2_mc.recordValues();
            MAIN.loader_mc.type2_mc._x = -10;
            newTween(MAIN.loader_mc.type2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.500000);
            newTween(MAIN.loader_mc.type2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.loader_mc.type2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.loader_mc.type2_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type2_mc.origX, 0.300000);
        }
        else if (this.counter == 12)
        {
            MAIN.section.attachMovie("home_colorJpg", "colorJPG_mc", mainLevel());
            MAIN.section.attachMovie("home_photoBG_mc", "photoBG_mc", mainLevel(), {_x: 0, _y: 61, _alpha: 0});
            MAIN.section.attachMovie("home_car_mc", "car_mc", mainLevel(), {_x: 268, _y: 317, _xscale: 10, _yscale: 10, _alpha: 0});
            MAIN.loader_mc.type1_mc._visible = true;
        }
        else if (this.counter == 14)
        {
            if (!audioDisabled)
            {
                boomSound.start(0, 1);
            } // end if
        }
        else if (this.counter == 17)
        {
            MAIN.loader_mc.type3_mc._visible = true;
            MAIN.loader_mc.type3_mc._xscale = MAIN.loader_mc.type3_mc._yscale = 300;
            MAIN.loader_mc.type3_mc._alpha = 0;
            newTween(MAIN.loader_mc.type3_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.loader_mc.type3_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.loader_mc.type3_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (this.counter == 21)
        {
            if (!audioDisabled)
            {
                boomSound.start(0, 1);
            } // end if
        }
        else if (this.counter == 26)
        {
            if (!audioDisabled)
            {
                revSound.start(0, 1);
                revSound.setVolume(100);
            } // end if
            newTween(MAIN.section.car_mc, "_y", as.transitions.easing.Strong.easeIn, 217, 0.300000);
            newTween(MAIN.section.car_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
            newTween(MAIN.section.car_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.section.car_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (this.counter == 30)
        {
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeOut, 110, 0.500000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeOut, 110, 0.500000);
            newTween(MAIN.loader_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.loader_mc._x - 10, 0.500000);
            newTween(MAIN.section.photoBG_mc, "_alpha", as.transitions.easing.Regular.easeOut, 100, 1.500000);
            MAIN.section.photoBG_mc.tweenObj_alpha.onMotionFinished = function ()
            {
                MAIN.section.colorJPG_mc._visible = false;
            };
            MAIN.origX = MAIN._x;
            if (!audioDisabled && !audioOn)
            {
                audioOn = true;
                AudioBed.start(0, 999);
                AudioBed.setVolume(0);
            } // end if
            _root.createEmptyMovieClip("audioBedEngine_mc", mainLevel());
            _root.audioBedVolume = 0;
            _root.audioBedEngine_mc.onEnterFrame = function ()
            {
                audioBedVolume = audioBedVolume + 0.500000;
                AudioBed.setVolume(audioBedVolume);
                if (_root.audioBedVolume > 60)
                {
                    this.removeMovieClip();
                } // end if
            };
        }
        else if (this.counter == 34)
        {
            MAIN._xscale = 105;
            MAIN._yscale = 105;
            MAIN._x = MAIN.origX + 2;
            MAIN._y = 5;
            MAIN.section.car_mc._x = MAIN.section.car_mc._x + 2;
            MAIN.section.car_mc._5 = MAIN.section.car_mc._5 - 10;
            NAV_top._y = NAV_top._y - 5;
            MAIN.loader_mc.type1_mc._y = MAIN.loader_mc.type1_mc._y - 10;
            MAIN.loader_mc.type1_mc._x = MAIN.loader_mc.type1_mc._x - 5;
            MAIN.loader_mc.loadTxt_mc._x = MAIN.loader_mc.loadTxt_mc._x - 15;
            MAIN.loader_mc.type2_mc._x = MAIN.loader_mc.type2_mc._x + 5;
            MAIN.loader_mc.type2_mc._y = MAIN.loader_mc.type2_mc._y - 5;
            MAIN.loader_mc.type3_mc._y = MAIN.loader_mc.type3_mc._y + 15;
            MAIN.loader_mc.type3_mc._x = MAIN.loader_mc.type3_mc._x - 5;
            MAIN.loader_mc.type5_mc._x = MAIN.loader_mc.type5_mc._x - 5;
        }
        else if (this.counter == 35)
        {
            MAIN._xscale = 103;
            MAIN._yscale = 103;
            MAIN._x = MAIN.origX;
            MAIN._y = -5;
            MAIN.section.car_mc._x = MAIN.section.car_mc._x - 2;
            MAIN.section.car_mc._5 = MAIN.section.car_mc._5 + 20;
            newTween(NAV_top, "_y", as.transitions.easing.Strong.easeOut, NAV_top._y = NAV_top._y + 5, 1.500000);
        }
        else if (this.counter == 36)
        {
            newTween(MAIN, "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
            newTween(MAIN, "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
            MAIN._y = 0;
            MAIN.section.car_mc._5 = MAIN.section.car_mc._5 - 10;
            newTween(MAIN.loader_mc.loadTxt_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.loadTxt_mc.origX, 0.300000);
            newTween(MAIN.loader_mc.loadTxt_mc, "_y", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.loadTxt_mc.origY, 0.300000);
            newTween(MAIN.loader_mc.type1_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type1_mc.origX, 0.300000);
            newTween(MAIN.loader_mc.type1_mc, "_y", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type1_mc.origY, 0.300000);
            newTween(MAIN.loader_mc.type2_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type2_mc.origX, 0.300000);
            newTween(MAIN.loader_mc.type2_mc, "_y", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type2_mc.origY, 0.300000);
            newTween(MAIN.loader_mc.type3_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type3_mc.origX, 0.300000);
            newTween(MAIN.loader_mc.type3_mc, "_y", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type3_mc.origY, 0.300000);
            newTween(MAIN.loader_mc.type4_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type4_mc.origX, 0.300000);
            newTween(MAIN.loader_mc.type4_mc, "_y", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type4_mc.origY, 0.300000);
            newTween(MAIN.loader_mc.type5_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type5_mc.origX, 0.300000);
            newTween(MAIN.loader_mc.type5_mc, "_y", as.transitions.easing.Strong.easeIn, MAIN.loader_mc.type5_mc.origY, 0.300000);
            MAIN.loader_mc.type4_mc._x = MAIN.loader_mc.type4_mc._x - 5;
            MAIN.loader_mc.type4_mc._y = MAIN.loader_mc.type4_mc._y + 15;
            MAIN.loader_mc.type4_mc._visible = true;
            MAIN.loader_mc.type4_mc._xscale = MAIN.loader_mc.type4_mc._yscale = 300;
            MAIN.loader_mc.type4_mc._alpha = 0;
            newTween(MAIN.loader_mc.type4_mc, "_al pha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.loader_mc.type4_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.loader_mc.type4_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (this.counter == 40)
        {
            MAIN.section.car_mc.removeTween();
            MAIN.loader_mc.removeTween();
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeOut, 100, 1.500000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeOut, 100, 1.500000);
            newTween(MAIN.loader_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.loader_mc._x + 25, 1.500000);
        }
        else if (this.counter == 48)
        {
            MAIN.section.attachMovie("home_trackSnipe_mc", "trackSnipe_mc", mainLevel(), {_x: -3, _y: 444});
            MAIN.section.trackSnipe_mc.counter = 1;
            MAIN.section.trackSnipe_mc.onEnterFrame = function ()
            {
                if (this.counter == 41)
                {
                    MAIN.section.trackSnipe_mc.txt_mc.recordValues();
                } // end if
                this.counter++;
            };
        }
        else if (this.counter == 100)
        {
            _root.globalColor = "A3CB5E";
            _root.barColorShift = new Array(0, 164, 0, 95, 0, 204, 100, 0);
            RemoveHome("overview");
            this.removeMovieClip();
        } // end if
        this.counter++;
    };
} // End of the function
function TrackSnipeTextExpand(side)
{
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 150, 0.600000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 150, 0.600000);
    if (side == "left")
    {
        newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"], "_x", as.transitions.easing.Strong.easeOut, MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"].origX - 18, 0.300000);
    }
    else
    {
        newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"], "_x", as.transitions.easing.Strong.easeOut, MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"].origX + 18, 0.300000);
    } // end if
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "1_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 120, 0.300000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "1_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 120, 0.300000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "2_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 120, 0.300000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "2_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 120, 0.300000);
} // End of the function
function TrackSnipeTextContract(side)
{
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.600000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.600000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"], "_x", as.transitions.easing.Strong.easeOut, MAIN.section.trackSnipe_mc.txt_mc[side + "A_mc"].origX, 0.300000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "1_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "1_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 120, 0.300000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "2_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
    newTween(MAIN.section.trackSnipe_mc.txt_mc[side + "2_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
} // End of the function
function BuildTrackPage(nextSection)
{
    _root.MAIN.section.counter = 1;
    _root.MAIN.section.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 188, 0.300000);
        }
        else if (this.counter == 6)
        {
            MAIN.section.BG_mc._visible = true;
            MAIN.section.BG_mc.colorJPG_mc._visible = true;
            MAIN.section.BG_mc.photoBG_mc._visible = false;
            MAIN.section.BG_mc.type_mc._visible = false;
            MAIN.section.BG_mc.car_mc._visible = false;
            MAIN.section.BG_mc.tag_mc._visible = false;
            MAIN.section.BG_mc.textHeader_mc._visible = false;
            MAIN.section.BG_mc.vehicleShadow_mc._visible = false;
            MAIN.section.BG_mc.colorJPG_mc.play();
        }
        else if (this.counter == 10)
        {
            MAIN.section.BG_mc.type_mc._visible = true;
            MAIN.section.BG_mc.type_mc._xscale = MAIN.section.BG_mc.type_mc._yscale = 300;
            MAIN.section.BG_mc.type_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.type_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.section.BG_mc.type_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.section.BG_mc.type_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (this.counter == 19)
        {
            MAIN.section.BG_mc.car_mc.origX = MAIN.section.BG_mc.car_mc._x;
            MAIN.section.BG_mc.car_mc.origY = MAIN.section.BG_mc.car_mc._y;
            DropCar();
        }
        else if (this.counter == 40)
        {
            MAIN.section.BG_mc.tag_mc._visible = true;
            MAIN.section.BG_mc.tag_mc.stop_mc._visible = false;
            MAIN.section.BG_mc.tag_mc.play_mc._visible = false;
            MAIN.section.BG_mc.tag_mc.text1_mc._visible = true;
            MAIN.section.BG_mc.tag_mc.origX = MAIN.section.BG_mc.tag_mc._x;
            if (nextSection == "offroad")
            {
                this.contentY = 96;
                MAIN.section.BG_mc.tag_mc._x = MAIN.section.BG_mc.tag_mc._x + 40;
                _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, offroad_array, 557, 133, 230, 310, this.contentY, 13, false);
            }
            else if (nextSection == "performance")
            {
                this.contentY = 102;
                MAIN.section.BG_mc.tag_mc._x = MAIN.section.BG_mc.tag_mc._x - 40;
                _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, performance_array, 54, 114, 230, 316, this.contentY, 13, [0, 143, 0, 35, 0, 59, 100, 100]);
            } // end if
            newTween(MAIN.section.BG_mc.tag_mc, "_x", as.transitions.easing.Back.easeOut, MAIN.section.BG_mc.tag_mc.origX, 0.200000);
        }
        else if (this.counter == 52)
        {
            _root.MAIN.section.BG_mc.textHeader_mc._visible = true;
            MAIN.section.BG_mc.textHeader_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.textHeader_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.300000);
            if (nextSection == "offroad")
            {
                ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 316, offroad_array, headerFormat);
            }
            else
            {
                ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 316, performance_array, headerFormat);
            } // end if
        }
        else if (this.counter == 57)
        {
            MAIN.section.BG_mc.strokeMask_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.stroke_mc.text1_mc._alpha = 0;
            MAIN.section.BG_mc.stroke_mc.text2_mc._alpha = 0;
            MAIN.section.BG_mc.stroke_mc.text3_mc._alpha = 0;
            MAIN.section.BG_mc.stroke_mc.arrow1_mc._alpha = 0;
            MAIN.section.BG_mc.stroke_mc.arrow2_mc._alpha = 0;
            MAIN.section.BG_mc.stroke_mc.arrow3_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.stroke_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.200000);
            MAIN.section.BG_mc.stroke_mc.arrow1_mc._xscale = MAIN.section.BG_mc.stroke_mc.arrow1_mc._yscale = 30;
            newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_xscale", as.transitions.easing.Back.easeOut, 100, 1);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_yscale", as.transitions.easing.Back.easeOut, 100, 1);
        }
        else if (this.counter == 61)
        {
            newTween(MAIN.section.BG_mc.stroke_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.400000);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.400000);
            MAIN.section.BG_mc.stroke_mc.arrow2_mc._xscale = MAIN.section.BG_mc.stroke_mc.arrow2_mc._yscale = 30;
            newTween(MAIN.section.BG_mc.stroke_mc.arrow2_mc, "_xscale", as.transitions.easing.Back.easeOut, 100, 1);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow2_mc, "_yscale", as.transitions.easing.Back.easeOut, 100, 1);
        }
        else if (this.counter == 65)
        {
            MAIN.section.BG_mc.strokeMask2_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.stroke2_mc.text1_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.stroke2_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            MAIN.section.BG_mc.stroke2_mc.button1_mc.onRelease = function ()
            {
                if (nextSection == "offroad")
                {
                    _root.globalColor = "eaa818";
                    _root.barColorShift = new Array(0, 234, 0, 24, 0, 168, 100, 0);
                    RemoveHome("performance");
                }
                else
                {
                    _root.globalColor = "A3CB5E";
                    _root.barColorShift = new Array(0, 164, 0, 95, 0, 204, 100, 0);
                    RemoveHome("offroad");
                } // end if
            };
            newTween(MAIN.section.BG_mc.stroke_mc.text3_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.400000);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow3_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.400000);
            MAIN.section.BG_mc.stroke_mc.arrow3_mc._xscale = MAIN.section.BG_mc.stroke_mc.arrow3_mc._yscale = 30;
            newTween(MAIN.section.BG_mc.stroke_mc.arrow3_mc, "_xscale", as.transitions.easing.Back.easeOut, 100, 1);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow3_mc, "_yscale", as.transitions.easing.Back.easeOut, 100, 1);
            for (z = 1; z <= 3; z++)
            {
                MAIN.section.BG_mc.stroke_mc["button" + z + "_mc"].nowZ = z;
                MAIN.section.BG_mc.stroke_mc["button" + z + "_mc"].onRollOver = function ()
                {
                    newTween(MAIN.section.BG_mc.stroke_mc["arrow" + this.nowZ + "_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 115, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc["arrow" + this.nowZ + "_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 115, 0.500000);
                };
                MAIN.section.BG_mc.stroke_mc["button" + z + "_mc"].onRollOut = function ()
                {
                    newTween(MAIN.section.BG_mc.stroke_mc["arrow" + this.nowZ + "_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc["arrow" + this.nowZ + "_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.500000);
                };
                MAIN.section.BG_mc.stroke_mc["button" + z + "_mc"].onRelease = function ()
                {
                    newTween(MAIN.section.BG_mc.stroke_mc["arrow" + this.nowZ + "_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc["arrow" + this.nowZ + "_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.500000);
                    MAIN.section.BG_mc.stroke_mc.button1_mc.enabled = true;
                    MAIN.section.BG_mc.stroke_mc.button2_mc.enabled = true;
                    MAIN.section.BG_mc.stroke_mc.button3_mc.enabled = true;
                    newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc.arrow2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc.arrow3_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc["arrow" + this.nowZ + "_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc.text3_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.500000);
                    newTween(MAIN.section.BG_mc.stroke_mc["text" + this.nowZ + "_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.500000);
                    MAIN.section.BG_mc.stroke_mc["button" + this.nowZ + "_mc"].enabled = false;
                    if (this.nowZ == 1)
                    {
                        if (MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc != undefined)
                        {
                            removeVideo();
                        } // end if
                        if (nextSection == "offroad")
                        {
                            ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 316, offroad_array, headerFormat);
                        }
                        else
                        {
                            ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 316, performance_array, headerFormat);
                        } // end if
                    }
                    else if (this.nowZ == 2)
                    {
                        if (MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc != undefined)
                        {
                            removeVideo();
                        } // end if
                        if (nextSection == "offroad")
                        {
                            ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 240, offroad_vehicles_array, listFormat);
                            Parade("gallery_offroad_array", 555, 400);
                        }
                        else
                        {
                            ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 250, performance_vehicles_array, listFormat);
                            Parade("gallery_performance_array", 55, 385);
                        } // end if
                    }
                    else if (this.nowZ == 3)
                    {
                        RemoveCar();
                        VidPlayer(nextSection);
                    } // end if
                };
            } // end of for
            MAIN.section.BG_mc.stroke_mc.button1_mc.enabled = false;
            CreateTagline(nextSection);
        }
        else if (this.counter == 66)
        {
            delete this["onEnterFrame"];
        } // end if
        this.counter++;
    };
} // End of the function
function Parade(arrayName, x, y)
{
    MAIN.section.BG_mc.attachMovie("box_mc", "paradeMask_mc", mainLevel(), {_x: x, _y: y - 150, _height: 250, _width: 230, _alpha: 30});
    MAIN.section.createEmptyMovieClip("paradeEngine_mc", mainLevel());
    MAIN.section.paradeEngine_mc.counter = 0;
    MAIN.section.BG_mc.parade_mc.removeMovieClip();
    MAIN.section.BG_mc.createEmptyMovieClip("parade_mc", mainLevel());
    MAIN.section.BG_mc.parade_mc._x = x;
    MAIN.section.BG_mc.parade_mc._y = y;
    MAIN.section.BG_mc.parade_mc.setMask(MAIN.section.BG_mc.paradeMask_mc);
    firstCar = 0;
    MAIN.section.paradeEngine_mc.onEnterFrame = function ()
    {
        if (MAIN.section.BG_mc.parade_mc["veh" + this.counter + "_mc"] == undefined)
        {
            if (this.counter < _root[arrayName].length)
            {
                trace("loading = " + _root[arrayName][this.counter][0][1]);
                carPath = MAIN.section.BG_mc.parade_mc.createEmptyMovieClip("veh" + this.counter + "_mc", this.counter);
                carPath.createEmptyMovieClip("container_mc", 2);
                carPath.container_mc.loadMovie("parade/" + _root[arrayName][this.counter][0][1] + ".png", 1);
                carPath._visible = false;
            }
            else
            {
                trace("FINISHED. Loaded a total of " + this.counter);
                Procession(arrayName);
                this.removeMovieClip();
            } // end if
        }
        else
        {
            trace(carPath.container_mc.getBytesTotal());
            if (carPath.container_mc.getBytesLoaded() >= carPath.container_mc.getBytesTotal() && carPath.container_mc.getBytesTotal() > 15)
            {
                carPath._x = carPath._x + (MAIN.section.BG_mc.parade_mc["veh" + (this.counter - 1) + "_mc"]._x + MAIN.section.BG_mc.parade_mc["veh" + (this.counter - 1) + "_mc"].container_mc._width + 4);
                carPath._visible = true;
                carPath.attachMovie("box_mc", "carMask_mc", mainLevel(), {_y: -50, _width: 150, _height: 50, _alpha: 50});
                carPath.container_mc.setMask(carPath.carMask_mc);
                carPath.container_mc._alpha = 10;
                _root.colorApply(carPath, [0, 255, 0, 255, 0, 255, 100, 100]);
                newTween(carPath.container_mc, "_y", as.transitions.easing.Back.easeOut, -carPath.container_mc._height, 0.600000);
                newTween(carPath.container_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
                _root.colorShift(carPath, [100, 0, 100, 0, 100, 0, 100, 0], 7);
                carPath.attachMovie("paradeLabel_mc", "label_mc", 1, {_x: carPath.container_mc._width / 2, _y: -18});
                carPath.label_mc.labelTxt_mc.text_txt.text = _root[arrayName][this.counter][0][2].toUpperCase();
                carPath.label_mc.labelTxt_mc._visible = false;
                carPath.container_mc.onRollOver = function ()
                {
                    _root.colorApply(this, [0, 255, 0, 255, 0, 255, 100, 100]);
                    _root.colorShift(this, [100, 0, 100, 0, 100, 0, 100, 0], 7);
                    newTween(this._parent.label_mc, "_y", as.transitions.easing.Bounce.easeOut, -5, 0.300000);
                    this._parent.label_mc.labelTxt_mc._visible = true;
                    _root.touching = true;
                };
                carPath.container_mc.onRollOut = function ()
                {
                    newTween(this._parent.label_mc, "_y", as.transitions.easing.Strong.easeOut, -18, 0.300000);
                    this._parent.label_mc.labelTxt_mc._visible = false;
                };
                this.counter++;
                
            } // end if
        } // end if
    };
} // End of the function
function Procession(arrayName)
{
    MAIN.section.createEmptyMovieClip("procession_mc", mainLevel());
    MAIN.section.procession_mc.counter = 1;
    MAIN.section.procession_mc.speed = 0;
    MAIN.section.procession_mc.createEmptyMovieClip("speedUp_mc", mainLevel());
    MAIN.section.procession_mc.speedUp_mc.onEnterFrame = function ()
    {
        MAIN.section.procession_mc.speed = MAIN.section.procession_mc.speed + 0.200000;
        if (MAIN.section.procession_mc.speed > 2)
        {
            this.removeMovieClip();
        } // end if
    };
    for (car = 0; car < _root[arrayName].length; car++)
    {
        MAIN.section.BG_mc.parade_mc["veh" + car + "_mc"].carMask_mc.removeMovieClip();
        MAIN.section.BG_mc.parade_mc["veh" + car + "_mc"].onEnterFrame = function ()
        {
            this._x = this._x + MAIN.section.procession_mc.speed;
        };
    } // end of for
    MAIN.section.procession_mc.onEnterFrame = function ()
    {
        if (MAIN.section.BG_mc.parade_mc["veh" + firstCar + "_mc"]._x > 0)
        {
            lastCar = firstCar - 1;
            if (lastCar < 0)
            {
                lastCar = _root[arrayName].length - 1;
            } // end if
            MAIN.section.BG_mc.parade_mc["veh" + lastCar + "_mc"]._x = -(MAIN.section.BG_mc.parade_mc["veh" + lastCar + "_mc"]._width + 3);
            firstCar = lastCar;
        } // end if
    };
} // End of the function
function ResizeCopyBox(path, newHeight, newContent, format, sectionVar)
{
    MAIN.section.BG_mc.parade_mc.removeMovieClip();
    MAIN.section.BG_mc.paradeMask_mc.removeMovieClip();
    MAIN.section.createEmptyMovieClip("resizeCopyBoxEngine_mc", mainLevel());
    MAIN.section.resizeCopyBoxEngine_mc.counter = 1;
    MAIN.section.resizeCopyBoxEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(path.textBoxMask, "_height", as.transitions.easing.Strong.easeOut, 1, 0.300000);
            newTween(path.copyBoxBG_mc, "_height", as.transitions.easing.Strong.easeOut, newHeight, 0.700000);
            newTween(path.shadow_mc.edgeL_mc, "_y", as.transitions.easing.Strong.easeOut, newHeight - 6, 0.700000);
            newTween(path.shadow_mc.edgeL_mc, "_height", as.transitions.easing.Strong.easeOut, newHeight - 6, 0.700000);
            newTween(path.shadow_mc.edgeR_mc, "_height", as.transitions.easing.Strong.easeOut, newHeight - 6, 0.700000);
            newTween(path.shadow_mc.edgeB_mc, "_y", as.transitions.easing.Strong.easeOut, newHeight, 0.700000);
            newTween(path.shadow_mc.cornerBL_mc, "_y", as.transitions.easing.Strong.easeOut, newHeight, 0.700000);
            newTween(path.shadow_mc.cornerBR_mc, "_y", as.transitions.easing.Strong.easeOut, newHeight, 0.700000);
        }
        else if (this.counter == 8)
        {
            path.container_mc._y = 0;
            path.container_mc.daBox_txt.htmlText = newContent;
            path.textBoxMask.removeTween();
            if (sectionVar == undefined)
            {
                path.textBoxMask._height = newHeight - 104 - 16;
                path.container_mc.daBox_txt.setTextFormat(format);
                ScrollbarEvaluate(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 120);
            }
            else
            {
                path.textBoxMask._height = newHeight - 136 - 26;
                path.container_mc.daBox_txt.setTextFormat(format);
                ScrollbarEvaluate(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 217);
            } // end if
        } // end if
        this.counter++;
    };
} // End of the function
function DropCar()
{
    MAIN.section.BG_mc.createEmptyMovieClip("carDropper_mc", mainLevel());
    MAIN.section.BG_mc.carDropper_mc.counter = 5;
    MAIN.section.BG_mc.carDropper_mc.onEnterFrame = function ()
    {
        if (this.counter == 5)
        {
            if (audioOn)
            {
                boomSound2.setVolume(100);
                boomSound2.start(0, 1);
            } // end if
        }
        else if (this.counter == 19)
        {
            MAIN.section.BG_mc.car_mc._x = MAIN.section.BG_mc.car_mc.origX;
            MAIN.section.BG_mc.car_mc._y = MAIN.section.BG_mc.car_mc.origY;
            MAIN.section.BG_mc.car_mc._xscale = MAIN.section.BG_mc.car_mc._yscale = 100;
            MAIN.section.BG_mc.car_mc._visible = true;
            MAIN.section.BG_mc.car_mc._y = -300;
            newTween(MAIN.section.BG_mc.car_mc, "_y", as.transitions.easing.None.easeIn, MAIN.section.BG_mc.car_mc.origY, 0.100000);
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.section.BG_mc.vehicleShadow_mc._visible = true;
            MAIN.section.BG_mc.vehicleShadow_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.vehicleShadow_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.500000);
        }
        else if (this.counter == 22)
        {
            MAIN.loader_mc.removeMovieClip();
            MAIN._xscale = 105;
            MAIN._yscale = 105;
            MAIN._x = MAIN.origX + 2;
            MAIN._y = 5;
            MAIN.section.BG_mc.car_mc._x = MAIN.section.BG_mc.car_mc._x + 2;
            MAIN.section.BG_mc.car_mc._5 = MAIN.section.BG_mc.car_mc._5 - 10;
            NAV_top._y = NAV_top._y - 5;
            newTween(MAIN.section.BG_mc.type_mc, "_xscale", as.transitions.easing.Strong.easeOut, 110, 0.500000);
            newTween(MAIN.section.BG_mc.type_mc, "_yscale", as.transitions.easing.Strong.easeOut, 110, 0.500000);
            newTween(MAIN.section.BG_mc.type_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.type_mc._y - 20, 0.500000);
        }
        else if (this.counter == 23)
        {
            MAIN._xscale = 103;
            MAIN._yscale = 103;
            MAIN._x = MAIN.origX;
            MAIN._y = -5;
            MAIN.section.BG_mc.car_mc._x = MAIN.section.BG_mc.car_mc._x - 2;
            MAIN.section.BG_mc.car_mc._5 = MAIN.section.BG_mc.car_mc._5 + 20;
            newTween(NAV_top, "_y", as.transitions.easing.Strong.easeOut, NAV_top._y = NAV_top._y + 5, 1.500000);
        }
        else if (this.counter == 24)
        {
            newTween(MAIN, "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
            newTween(MAIN, "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
            MAIN.section.BG_mc.photoBG_mc._alpha = 0;
            MAIN.section.BG_mc.photoBG_mc._visible = true;
            newTween(MAIN.section.BG_mc.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.800000);
            MAIN._y = 0;
        }
        else if (this.counter == 34)
        {
            MAIN.section.BG_mc.type_mc.removeTween();
            newTween(MAIN.section.BG_mc.type_mc, "_xscale", as.transitions.easing.Strong.easeOut, 100, 1.500000);
            newTween(MAIN.section.BG_mc.type_mc, "_yscale", as.transitions.easing.Strong.easeOut, 100, 1.500000);
            newTween(MAIN.section.BG_mc.type_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.type_mc._y + 20, 1.500000);
            MAIN.section.BG_mc.car_mc._5 = MAIN.section.BG_mc.car_mc._5 - 10;
        } // end if
        this.counter++;
    };
} // End of the function
function CreateCopyBox(path, content, x, y, w, h, contentY, margin, scrollBarArray)
{
    if (path.copyBoxEngine_mc == undefined)
    {
        path.createEmptyMovieClip("copyBoxEngine_mc", mainLevel());
        engine = path.copyBoxEngine_mc;
    }
    else
    {
        path.createEmptyMovieClip("copyBoxEngine2_mc", mainLevel());
        engine = path.copyBoxEngine2_mc;
    } // end if
    engine.counter = 1;
    engine.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            if (path.copyBox_mc == undefined)
            {
                path.createEmptyMovieClip("copyBox_mc", mainLevel());
                path = path.copyBox_mc;
            }
            else if (path.copyBox2_mc == undefined)
            {
                path.createEmptyMovieClip("copyBox2_mc", mainLevel());
                path = path.copyBox2_mc;
            } // end if
            path._x = x;
            path._y = y + contentY;
            path.attachMovie("copyBox_mc", "copyBoxBG_mc", mainLevel(), {_y: -contentY, _alpha: 50, _xscale: w * 10, _yscale: h * 10});
        }
        else if (this.counter == 12)
        {
            path.createEmptyMovieClip("shadow_mc", mainLevel());
            path.shadow_mc._y = -contentY;
            path.shadow_mc.attachMovie("copyBox_edge_mc", "edgeL_mc", mainLevel(), {_x: 0, _y: h - 3, _rotation: 180, _height: h - 6});
            path.shadow_mc.attachMovie("copyBox_edge_mc", "edgeR_mc", mainLevel(), {_x: w, _y: 3, _height: h - 6});
            path.shadow_mc.attachMovie("copyBox_edge_mc", "edgeT_mc", mainLevel(), {_x: 3, _y: 0, _rotation: -90, _height: w - 6});
            path.shadow_mc.attachMovie("copyBox_edge_mc", "edgeB_mc", mainLevel(), {_x: w - 3, _y: h, _rotation: 90, _height: w - 6});
            path.shadow_mc.attachMovie("copyBox_corner_mc", "cornerTL_mc", mainLevel(), {_x: 0, _y: 0, _rotation: -90});
            path.shadow_mc.attachMovie("copyBox_corner_mc", "cornerTR_mc", mainLevel(), {_x: w, _y: 0, _rotation: 0});
            path.shadow_mc.attachMovie("copyBox_corner_mc", "cornerBL_mc", mainLevel(), {_x: 0, _y: h, _rotation: 180});
            path.shadow_mc.attachMovie("copyBox_corner_mc", "cornerBR_mc", mainLevel(), {_x: w, _y: h, _rotation: 90});
            path.shadow_mc._alpha = 0;
            newTween(path.shadow_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.300000);
        }
        else if (this.counter == 14)
        {
            if (content == undefined)
            {
                delete this["onEnterFrame"];
            }
            else
            {
                CreateTextBox("container_mc", content, path, headerFormat, margin, 0, w - margin * 2, 1, true, true, true);
                path.attachMovie("box_mc", "textBoxMask", mainLevel(), {_alpha: 50, _x: 0, _width: w, _height: h - contentY - margin * 2});
                path.container_mc.setMask(path.textBoxMask);
                path.container_mc._visible = false;
            } // end if
        }
        else if (this.counter == 15)
        {
            path.totalScrollHeight = h - contentY - margin;
            path.attachMovie("scrollbar_bg", "scrollbar_bg", mainLevel(), {_x: w, _y: -24, _alpha: 70, _height: path.totalScrollHeight + 24});
            path.scrollbar_bg.origHeight = path.scrollbar_bg._height;
            if (scrollBarArray != false)
            {
                colorApply(path.scrollbar_bg, scrollBarArray);
            } // end if
            path.attachMovie("box_mc", "scrollbarBg_mask_mc", mainLevel(), {_x: w, _y: -24, _width: path.scrollbar_bg._width, _height: path.totalScrollHeight + 24});
            path.scrollbar_bg.setMask(path.scrollbarBg_mask_mc);
            path.scrollbar_bg.origX = path.scrollbar_bg._x;
            path.scrollbar_bg._x = path.scrollbar_bg._x - path.scrollbar_bg._width;
            newTween(path.scrollbar_bg, "_x", as.transitions.easing.Strong.easeOut, path.scrollbar_bg.origX, 0.400000);
            path.attachMovie("box_mc", "scrollbar_mc", mainLevel(), {_x: w + 5, _height: path.totalScrollHeight - 25, _width: 8});
            path.scrollbar_mc.changeColor("FFFFFF");
            path.attachMovie("arrowBut_mc", "topArrow_mc", mainLevel(), {_x: path.scrollbar_mc._x + path.scrollbar_mc._width / 2, _y: -9, _rotation: -90});
            path.attachMovie("arrowBut_mc", "botArrow_mc", mainLevel(), {_x: path.scrollbar_mc._x + path.scrollbar_mc._width / 2, _y: path.totalScrollHeight - 16, _rotation: 90});
            path.botArrow_mc.origY = path.botArrow_mc._y;
            ScrollbarEvaluate(path, path.totalScrollHeight - 25);
        }
        else if (this.counter == 35)
        {
            path.container_mc._visible = true;
        } // end if
        this.counter++;
    };
} // End of the function
function BuildEQ()
{
    NAV_bot.copyright_mc.createEmptyMovieClip("eq_mc", mainLevel());
    NAV_bot.copyright_mc.eq_mc._x = -215;
    NAV_bot.copyright_mc.eq_mc._y = 15;
    audioOn = false;
    audioDisabled = false;
    for (x = 1; x < 8; x++)
    {
        NAV_bot.copyright_mc.eq_mc.attachMovie("box_mc", "eq" + x + "_mc", x, {_width: 3, _height: 1, _rotation: 180});
        NAV_bot.copyright_mc.eq_mc["eq" + x + "_mc"].changeColor("808080");
        NAV_bot.copyright_mc.eq_mc["eq" + x + "_mc"]._x = 4 * x + 1 * x;
        NAV_bot.copyright_mc.eq_mc["eq" + x + "_mc"].counter = 1;
        NAV_bot.copyright_mc.eq_mc["eq" + x + "_mc"].onEnterFrame = function ()
        {
            if (this.counter == 1)
            {
                this.x = random(10) + 5;
            }
            else if (this.counter == this.x)
            {
                this.y = random(8) + 5;
                this._height = this.y;
                newTween(this, "_height", Normal.easeIn, 1, 0.500000);
                this.counter = 0;
            } // end if
            if (audioOn)
            {
                this.counter++;
            } // end if
        };
    } // end of for
    NAV_bot.copyright_mc.eq_mc.attachMovie("audioOff_mc", "audioOff_mc", mainLevel(), {_alpha: 0});
    NAV_bot.copyright_mc.attachMovie("box_mc", "eqButton_mc", mainLevel(), {_x: -220, _y: 0, _width: 45, _height: 15, _alpha: 0});
    NAV_bot.copyright_mc.content_mc.origX = NAV_bot.copyright_mc.content_mc._x;
    NAV_bot.copyright_mc.mask_mc.origX = NAV_bot.copyright_mc.mask_mc._x;
    NAV_bot.copyright_mc.mask_mc.origWidth = NAV_bot.copyright_mc.mask_mc._width;
    NAV_bot.copyright_mc.eqButton_mc.onRollOver = function ()
    {
        newTween(NAV_bot.copyright_mc.content_mc, "_x", as.transitions.easing.Strong.easeOut, NAV_bot.copyright_mc.content_mc.origX + 65, 0.500000);
        newTween(NAV_bot.copyright_mc.eqButton_mc, "_width", as.transitions.easing.Strong.easeOut, 145, 0.500000);
        newTween(NAV_bot.copyright_mc.eqButton_mc, "_y", as.transitions.easing.Strong.easeOut, -10, 0.500000);
        newTween(NAV_bot.copyright_mc.eqButton_mc, "_height", as.transitions.easing.Strong.easeOut, 30, 0.500000);
        newTween(NAV_bot.copyright_mc.mask_mc, "_width", as.transitions.easing.Strong.easeOut, 425, 0.500000);
        newTween(NAV_bot.copyright_mc.mask_mc, "_x", as.transitions.easing.Strong.easeOut, NAV_bot.copyright_mc.mask_mc.origX + 65, 0.500000);
    };
    NAV_bot.copyright_mc.eqButton_mc.onRollOut = function ()
    {
        newTween(NAV_bot.copyright_mc.content_mc, "_x", as.transitions.easing.Strong.easeOut, NAV_bot.copyright_mc.content_mc.origX, 0.500000);
        newTween(NAV_bot.copyright_mc.eqButton_mc, "_width", as.transitions.easing.Strong.easeOut, 45, 0.500000);
        newTween(NAV_bot.copyright_mc.eqButton_mc, "_y", as.transitions.easing.Strong.easeOut, 0, 0.500000);
        newTween(NAV_bot.copyright_mc.eqButton_mc, "_height", as.transitions.easing.Strong.easeOut, 15, 0.500000);
        newTween(NAV_bot.copyright_mc.mask_mc, "_width", as.transitions.easing.Strong.easeOut, 365, 0.500000);
        newTween(NAV_bot.copyright_mc.mask_mc, "_x", as.transitions.easing.Strong.easeOut, NAV_bot.copyright_mc.mask_mc.origX, 0.500000);
        NAV_bot.copyright_mc.mask_mc.removeTween();
    };
    audioEnabled = true;
    NAV_bot.copyright_mc.eqButton_mc.onRelease = function ()
    {
        if (audioOn)
        {
            audioEnabled = false;
            StopAudioBed();
        }
        else
        {
            audioEnabled = true;
            StartAudioBed();
        } // end if
        newTween(NAV_bot.copyright_mc.content_mc.audioText_mc, "_y", as.transitions.easing.Strong.easeIn, -13, 0.300000);
        NAV_bot.copyright_mc.content_mc.audioText_mc.tweenObj_y.onMotionFinished = function ()
        {
            NAV_bot.copyright_mc.content_mc.audioText_mc.gotoAndStop(audioGotoFrame);
            NAV_bot.copyright_mc.content_mc.audioText_mc._y = 13;
            newTween(NAV_bot.copyright_mc.content_mc.audioText_mc, "_y", as.transitions.easing.Strong.easeOut, 0, 0.300000);
        };
    };
} // End of the function
function StopAudioBed()
{
    AudioBed.stop();
    audioGotoFrame = 2;
    audioOn = false;
    audioDisabled = true;
    NAV_bot.copyright_mc.eq_mc.audioOff_mc._y = -15;
    newTween(NAV_bot.copyright_mc.eq_mc.audioOff_mc, "_y", as.transitions.easing.Strong.easeIn, 0, 0.600000);
    newTween(NAV_bot.copyright_mc.eq_mc.audioOff_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.600000);
} // End of the function
function StartAudioBed()
{
    AudioBed.start(0, 999);
    audioGotoFrame = 1;
    audioOn = true;
    audioDisabled = false;
    newTween(NAV_bot.copyright_mc.eq_mc.audioOff_mc, "_alpha", Normal.easeOut, 0, 0.500000);
} // End of the function
function MainEngine()
{
    revSound = new Sound(this);
    revSound.attachSound("rev2");
    boomSound = new Sound(this);
    boomSound.attachSound("boom2");
    boomSound.setVolume(60);
    boomSound2 = new Sound(this);
    boomSound2.attachSound("boom3");
    rolloverSound = new Sound(this);
    rolloverSound.attachSound("rollover");
    loadBegin = new Sound(this);
    loadBegin.attachSound("load_begin");
    loadLoop = new Sound(this);
    loadLoop.attachSound("load_loop");
    _root.createEmptyMovieClip("subRollOver_mc", mainLevel());
    subRollOver = new Sound(subRollOver_mc);
    loadLoop.attachSound("load_loop");
    subRollOver = new Sound(this);
    subRollOver.attachSound("subNav");
    _root.createEmptyMovieClip("loadedSound_mc", mainLevel());
    loadedSound = new Sound(loadedSound_mc);
    loadedSound.attachSound("loaded2");
    _root.createEmptyMovieClip("audioBed_mc", mainLevel());
    AudioBed = new Sound(audioBed_mc);
    AudioBed.attachSound("theDrive_01");
    boomSound2.setVolume(60);
    _root.createEmptyMovieClip("mainEngine_mc", mainLevel());
    _root.mainEngine_mc.counter = 1;
    _root.mainEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            NAV_bot.attachMovie("copyright_mc", "copyright_mc", mainLevel(), {_x: 375});
            if (Stage.height <= 680)
            {
                NAV_bot.copyright_mc._y = 645;
            }
            else
            {
                NAV_bot.copyright_mc._y = Stage.height - 35;
            } // end if
            BuildEQ();
            BuildHome();
            MAIN.attachMovie("bot_shape_mc", "bot_shape_mc", mainLevel());
        }
        else if (this.counter == 2)
        {
            NAV_top.attachMovie("top_shape_mc", "top_shape_mc", mainLevel(), {_visible: false});
            NAV_top.attachMovie("top_shape_glow_mc", "glow_mc", mainLevel(), {_x: 248, _alpha: 0});
            newTween(NAV_top.glow_mc, "_alpha", as.transitions.easing.Regular.easeOut, 100, 0.300000);
            NAV_top.glow_mc.tweenObj_alpha.onMotionFinished = function ()
            {
                NAV_top.top_shape_mc._visible = true;
                NAV_top.top_shape_jpg_mc.removeMovieClip();
                NAV_top.glow_mc.removeMovieClip();
            };
            NAV_top.attachMovie("logoGlow_mc", "logoGlow_mc", mainLevel(), {_x: 257, _y: -3});
            NAV_top.logoGlow_mc._visible = false;
            NAV_top.logoGlow_mc._alpha = 0;
            NAV_top.attachMovie("logo_mc", "logo_mc", mainLevel(), {_x: 263, _y: 40});
            NAV_top.logo_mc.onRollOver = function ()
            {
                NAV_top.logoGlow_mc._visible = true;
                NAV_top.logoGlow_mc._alpha = 60;
                newTween(NAV_top.logoGlow_mc, "_alpha", as.transitions.easing.Strong.easeOut, 0, 3);
            };
            NAV_top.logo_mc.onRelease = function ()
            {
                _root.globalColor = "f77b13";
                RemoveHome("home");
            };
            newTween(NAV_top.logo_mc, "_y", as.transitions.easing.Strong.easeOut, -2, 0.500000);
            colorApply(NAV_top.logo_mc, [0, 255, 0, 255, 0, 255, 100, 100]);
            colorShift(NAV_top.logo_mc, [100, 0, 100, 0, 100, 0, 100, 0], 5);
        }
        else if (_root.counter == 14)
        {
        }
        else if (_root.counter == 120)
        {
        }
        else if (_root.counter == 185)
        {
            CreateNav();
        }
        else if (_root.counter == 195)
        {
            trace("say OVERVIEW");
            CreateTagline("overview");
            _root.removeMovieClip();
        } // end if
        _root.counter++;
    };
} // End of the function
function CreateNav()
{
    _root.createEmptyMovieClip("createNavEngine_mc", mainLevel());
    createNavEngine_mc.counter = 1;
    createNavEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            NavBounce();
            for (x = 1; x < 5; x++)
            {
                NAV_top["navB" + x + "_mc"].btn_mc.nowX = x;
                NAV_top["navB" + x + "_mc"].recordValues();
                NAV_top["navB" + x + "_mc"].btn_mc.onRollOver = function ()
                {
                    if (audioOn)
                    {
                        rolloverSound.start(0, 1);
                    } // end if
                    NAV_top["navB" + this.nowX + "_mc"].changeColor(_root.globalColor);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word1_mc, "_x", as.transitions.easing.Strong.easeIn, NAV_top["navB" + this.nowX + "_mc"].word1_mc.origX - 3, 0.150000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word2_mc, "_x", as.transitions.easing.Strong.easeIn, NAV_top["navB" + this.nowX + "_mc"].word2_mc.origX + 3, 0.150000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word1_mc, "_xscale", as.transitions.easing.Strong.easeIn, 130, 0.150000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word1_mc, "_yscale", as.transitions.easing.Strong.easeIn, 130, 0.150000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 130, 0.150000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 130, 0.150000);
                    NAV_top["navB" + this.nowX + "_mc"].word2_mc.tweenObj_xscale.nowX = this.nowX;
                    NAV_top["navB" + this.nowX + "_mc"].word2_mc.tweenObj_xscale.onMotionFinished = function ()
                    {
                        newTween(NAV_top["navB" + this.nowX + "_mc"].word1_mc, "_xscale", as.transitions.easing.Strong.easeOut, 110, 2);
                        newTween(NAV_top["navB" + this.nowX + "_mc"].word1_mc, "_yscale", as.transitions.easing.Strong.easeOut, 110, 2);
                        newTween(NAV_top["navB" + this.nowX + "_mc"].word2_mc, "_xscale", as.transitions.easing.Strong.easeOut, 110, 2);
                        newTween(NAV_top["navB" + this.nowX + "_mc"].word2_mc, "_yscale", as.transitions.easing.Strong.easeOut, 110, 2);
                    };
                };
                NAV_top["navB" + x + "_mc"].btn_mc.onRollOut = NAV_top["navB" + x + "_mc"].btn_mc.onDragOut = function ()
                {
                    NAV_top["navB" + this.nowX + "_mc"].changeColor("ffffff");
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word1_mc, "_x", as.transitions.easing.Strong.easeOut, NAV_top["navB" + this.nowX + "_mc"].word1_mc.origX, 0.300000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word2_mc, "_x", as.transitions.easing.Strong.easeOut, NAV_top["navB" + this.nowX + "_mc"].word2_mc.origX, 0.300000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word1_mc, "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word1_mc, "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word2_mc, "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                    newTween(NAV_top["navB" + this.nowX + "_mc"].word2_mc, "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                };
                NAV_top["navB" + x + "_mc"].btn_mc.onRelease = function ()
                {
                    if (this.nowX == 1)
                    {
                        _root.globalColor = "A3CB5E";
                        _root.barColorShift = new Array(0, 164, 0, 95, 0, 204, 100, 0);
                        RemoveHome("overview");
                    } // end if
                    if (this.nowX == 2)
                    {
                        _root.globalColor = "f77b13";
                        _root.barColorShift = new Array(0, 37, 0, 97, 0, 34, 100, 0);
                        RemoveHome("tracks");
                    } // end if
                    if (this.nowX == 3)
                    {
                        _root.globalColor = "db5fb0";
                        _root.barColorShift = new Array(0, 54, 0, 89, 0, 41, 100, 0);
                        RemoveHome("gallery");
                    } // end if
                    if (this.nowX == 4)
                    {
                        _root.globalColor = "db5fb0";
                        _root.barColorShift = new Array(0, 54, 0, 89, 0, 41, 100, 0);
                        RemoveHome("tix");
                    } // end if
                };
            } // end of for
            NAV_top.navB1_mc.word2_mc.changeColor("FFFFFF");
        }
        else if (this.counter == 6)
        {
            trace("MAKING TAGLINE");
            MAIN.attachMovie("tagline_mc", "tagline_mc", mainLevel(), {_y: 551, _alpha: 0});
            NAV_bot.attachMovie("navB5_mc", "navB5_mc", mainLevel(), {_x: 80, _y: 608, _alpha: 0, _xscale: 10, _yscale: 10});
            NAV_bot.attachMovie("navB6_mc", "navB6_mc", mainLevel(), {_x: 236, _y: 610, _alpha: 0, _xscale: 10, _yscale: 10});
            NAV_bot.attachMovie("navB7_mc", "navB7_mc", mainLevel(), {_x: 454, _y: 609, _alpha: 0, _xscale: 10, _yscale: 10});
            NAV_bot.attachMovie("navB8_mc", "navB8_mc", mainLevel(), {_x: 593, _y: 609, _alpha: 0, _xscale: 10, _yscale: 10});
            _root.createEmptyMovieClip("botNavEngine_mc", mainLevel());
            _root.botNavEngine_mc.counter = 5;
            _root.botNavEngine_mc.onEnterFrame = function ()
            {
                if (this.counter < 9)
                {
                    NAV_bot["navB" + this.counter + "_mc"].nowX = this.counter;
                    newTween(NAV_bot["navB" + this.counter + "_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 100, 1);
                    newTween(NAV_bot["navB" + this.counter + "_mc"], "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                    newTween(NAV_bot["navB" + this.counter + "_mc"], "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                    NAV_bot["navB" + this.counter + "_mc"].onRollOver = function ()
                    {
                        if (audioOn)
                        {
                            subRollOver.start(0, 1);
                        } // end if
                        this.changeColor(_root.globalColor);
                        newTween(this.arrow_mc, "_xscale", as.transitions.easing.Strong.easeOut, 150, 0.600000);
                        newTween(this.arrow_mc, "_yscale", as.transitions.easing.Strong.easeOut, 150, 0.600000);
                    };
                    NAV_bot["navB" + this.counter + "_mc"].onRollOut = NAV_bot["navB" + this.counter + "_mc"].onDragOut = function ()
                    {
                        this.changeColor("ffffff");
                        newTween(this.arrow_mc, "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.600000);
                        newTween(this.arrow_mc, "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.600000);
                    };
                    NAV_bot["navB" + this.counter + "_mc"].onRelease = function ()
                    {
                        if (this.nowX == 5)
                        {
                            _root.globalColor = "f77b13";
                            _root.barColorShift = new Array(0, 37, 0, 97, 0, 34, 100, 0);
                            RemoveHome("maps");
                        } // end if
                        if (this.nowX == 6)
                        {
                            _root.globalColor = "f77b13";
                            _root.barColorShift = new Array(0, 37, 0, 97, 0, 34, 100, 0);
                            RemoveHome("faq");
                        } // end if
                        if (this.nowX == 7)
                        {
                            _root.globalColor = "f77b13";
                            _root.barColorShift = new Array(0, 37, 0, 97, 0, 34, 100, 0);
                            RemoveHome("hours");
                        } // end if
                        if (this.nowX == 8)
                        {
                            _root.globalColor = "f77b13";
                            _root.barColorShift = new Array(0, 37, 0, 97, 0, 34, 100, 0);
                            RemoveHome("partners");
                        } // end if
                    };
                }
                else
                {
                    this.removeMovieClip();
                } // end if
                this.counter = this.counter + 0.500000;
            };
            this.removeMovieClip();
        } // end if
        this.counter++;
    };
} // End of the function
function RemoveHome(nextSection)
{
    _root.createEmptyMovieClip("removeHomeEngine_mc", mainLevel());
    _root.removeHomeEngine_mc.counter = 1;
    _root.removeHomeEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            MAIN.tagline_mc.disclaimer_mc._alpha = 0;
            newTween(MAIN.tagline_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.tagline_mc._x + 40, 0.600000);
            newTween(MAIN.tagline_mc, "_alpha", as.transitions.easing.None.easeIn, 0, 0.500000);
            delete _root.MAIN.section["onEnterFrame"];
            delete _root.buildSectionEngine_mc["onEnterFrame"];
            delete _root.MAIN.section.imageRotatorEngine_mc["onEnterFrame"];
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.loader_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                _root.MAIN.loader_mc._visible = false;
            };
            MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.removeMovieClip();
            newTween(MAIN.section.BG_mc.copyBoxHolder_mc.videoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 0, 0.500000);
            _root.MAIN.section.BG_mc.tagMask_mc.gotoAndPlay("out");
            newTween(MAIN.section.BG_mc.b1_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.section.BG_mc.b1_mc._x - 3, 0.500000);
            newTween(MAIN.section.BG_mc.b1_mc, "_y", as.transitions.easing.Strong.easeIn, MAIN.section.BG_mc.b1_mc._y - 25, 0.500000);
            newTween(MAIN.section.BG_mc.b2_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.section.BG_mc.b2_mc._x - 3, 0.500000);
            newTween(MAIN.section.BG_mc.b2_mc, "_y", as.transitions.easing.Strong.easeIn, MAIN.section.BG_mc.b2_mc._y - 25, 0.500000);
            MAIN.section.BG_mc.b1_mc.tweenObj_x.onMotionFinished = function ()
            {
                MAIN.section.BG_mc.b1_mc._visible = false;
            };
            if (MAIN.section.BG_mc.carList_mc != undefined)
            {
                MAIN.section.BG_mc.carList_mc.listEngine_mc.removeMovieClip();
                MAIN.section.createEmptyMovieClip("listEngine_mc", mainLevel());
                MAIN.section.listEngine_mc.counter = 0;
                MAIN.section.listEngine_mc.onEnterFrame = function ()
                {
                    MAIN.section.BG_mc.carList_mc["item" + this.counter + "_mc"]._visible = true;
                    newTween(MAIN.section.BG_mc.carList_mc["item" + this.counter + "_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 0, 0.500000);
                    if (this.counter > 15)
                    {
                        this.removeMovieClip();
                    } // end if
                    this.counter++;
                };
            } // end if
            _root.MAIN.section.BG_mc.imageHolder_mc._visible = false;
            newTween(MAIN.section.BG_mc.sign_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.500000);
            newTween(MAIN.section.BG_mc.sign_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.500000);
            colorShift(MAIN.section.BG_mc.sign_mc, [0, 255, 0, 255, 0, 255, 50, 100], 3);
            MAIN.section.trackSnipe_mc.gotoAndPlay("out");
            MAIN.section.underline_mc.gotoAndPlay("out");
            newTween(MAIN.section.BG_mc.shadow_mc, "_alpha", as.transitions.easing.Strong.easeIn, 0, 0.300000);
            newTween(_root.MAIN.section.copyBox_mc.textBoxMask, "_height", as.transitions.easing.None.easeIn, 1, 0.300000);
            newTween(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.textBoxMask, "_height", as.transitions.easing.None.easeIn, 1, 0.300000);
            MAIN.section.colorJPG_mc._visible = true;
            newTween(MAIN.section.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeIn, 0, 0.300000);
            MAIN.section.photoBG_mc.tweenObj_alpha.onMotionFinished = function ()
            {
                MAIN.section.photoBG_mc.removeMovieClip();
                MAIN.section.colorJPG_mc.gotoAndPlay("out");
            };
            if (MAIN.section.BG_mc.colorJPG_mc != undefined)
            {
                newTween(MAIN.section.BG_mc.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeIn, 0, 0.300000);
            } // end if
            MAIN.section.BG_mc.photoBG_mc.tweenObj_alpha.onMotionFinished = function ()
            {
                MAIN.section.photoBG_mc.removeMovieClip();
                MAIN.section.BG_mc.colorJPG_mc.gotoAndPlay("out");
            };
            colorApply(MAIN.section.BG_mc.holder_mc.image1_mc, [100, 0, 100, 0, 100, 0, 100, 0]);
            colorShift(MAIN.section.BG_mc.holder_mc.image1_mc, [0, 255, 0, 255, 0, 255, 100, 100], 3);
            MAIN.section.BG_mc.trackChooser_mc.gotoAndPlay("out");
            newTween(MAIN.section.BG_mc.textLeft_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.section.BG_mc.textLeft_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.section.BG_mc.textLeft_mc, "_alpha", as.transitions.easing.Strong.easeIn, 0, 0.200000);
            MAIN.section.BG_mc.textRight_mc._visible = true;
            MAIN.section.BG_mc.textRight_mc._alpha = 0;
            MAIN.section.BG_mc.textRight_mc._xscale = MAIN.section.BG_mc.textRight_mc._yscale = 300;
            newTween(MAIN.section.BG_mc.textRight_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.section.BG_mc.textRight_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.section.BG_mc.textRight_mc, "_alpha", as.transitions.easing.Strong.easeIn, 0, 0.300000);
            newTween(MAIN.section.BG_mc.map_mc, "_alpha", as.transitions.easing.Strong.easeIn, 0, 0.300000);
        }
        else if (this.counter == 7)
        {
            newTween(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 0, 0.400000);
            MAIN.section.BG_mc.photoBG_mc.gotoAndPlay("out");
            _root.MAIN.section.BG_mc.textLeft_mc._visible = false;
            _root.MAIN.section.BG_mc.textRight_mc._visible = false;
            _root.MAIN.section.BG_mc.holder_mc._visible = false;
            _root.MAIN.section.BG_mc.imageMask_mc._visible = true;
            _root.MAIN.section.BG_mc.imageMask_mc.mask_mc.gotoAndPlay("out");
            newTween(_root.MAIN.section.textHeader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(_root.MAIN.section.textHeader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(_root.MAIN.section.textHeader_mc, "_alpha", as.transitions.easing.Strong.easeIn, 0, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc, "_alpha", as.transitions.easing.Strong.easeIn, 0, 0.300000);
        }
        else if (this.counter == 14)
        {
            LoadSection(nextSection);
        }
        else if (this.counter == 18)
        {
            MAIN.section.trackSnipe_mc.removeMovieClip();
            this.removeMovieClip();
        } // end if
        this.counter++;
    };
} // End of the function
function CreateTagline(nextSection)
{
    MAIN.tagline_mc.disclaimer_mc._alpha = 0;
    if (nextSection == "offroad")
    {
        MAIN.tagline_mc._x = 40;
        newTween(MAIN.tagline_mc, "_x", as.transitions.easing.Strong.easeOut, 80, 1);
    }
    else if (nextSection == "hours")
    {
        MAIN.tagline_mc._x = 20;
        newTween(MAIN.tagline_mc, "_x", as.transitions.easing.Strong.easeOut, 60, 1);
    }
    else
    {
        MAIN.tagline_mc._x = 360;
        newTween(MAIN.tagline_mc, "_x", as.transitions.easing.Strong.easeOut, 400, 1);
    } // end if
    trace(MAIN.tagline_mc);
    newTween(MAIN.tagline_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 1.500000);
    MAIN.tagline_mc.tweenObj_alpha.onMotionFinished = function ()
    {
        newTween(MAIN.tagline_mc.disclaimer_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.600000);
    };
} // End of the function
function LoadSection(nextSection)
{
    _root.createEmptyMovieClip("loadSectionEngine_mc", mainLevel());
    _root.loadSectionEngine_mc.counter = 1;
    _root.loadSectionEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            MAIN.section.removeMovieClip();
            MAIN.createEmptyMovieClip("section", mainLevel());
            MAIN.section.createEmptyMovieClip("BG_mc", mainLevel());
            if (nextSection == "home")
            {
                _root.globalColor = "f77b13";
                _root.barColorShift = new Array(0, 36, 0, 95, 0, 32, 100, 0);
                BuildHome();
            }
            else
            {
                MAIN.section.BG_mc.loadMovie("sections/" + nextSection + ".swf", 1);
            } // end if
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeOut, 150, 0.800000);
            colorShift(MAIN.stripe_mc.bar_mc, _root.barColorShift, 3);
            MAIN.loader_mc.removeMovieClip();
            if (nextSection == "home")
            {
                MAIN.attachMovie("homeType_mc", "loader_mc", mainLevel(), {_x: 153, _y: 370});
                MAIN.loader_mc.recordValues();
                MAIN.loader_mc.type1_mc._visible = MAIN.loader_mc.type2_mc._visible = MAIN.loader_mc.type3_mc._visible = MAIN.loader_mc.type4_mc._visible = false;
                MAIN.loader_mc.loadGlow_mc.setMask(MAIN.loader_mc.loadTxt_mc);
            }
            else
            {
                MAIN.attachMovie("loader_mc", "loader_mc", mainLevel(), {_x: 153, _y: 400});
            } // end if
            if (nextSection == "tix" || nextSection == "faq" || nextSection == "maps" || nextSection == "hours" || nextSection == "gallery" || nextSection == "tracks" || nextSection == "partners")
            {
                MAIN.loader_mc.loadTxt_mc.changeColor("fc7c09");
                MAIN.loader_mc.percent_mc.changeColor("fc7c09");
            } // end if
            if (nextSection == "offroad")
            {
                MAIN.loader_mc._x = 153;
            } // end if
            if (nextSection == "performance")
            {
                MAIN.loader_mc._x = 533;
            } // end if
            if (nextSection == "overview")
            {
                MAIN.loader_mc._x = 153;
            } // end if
            if (nextSection == "tix")
            {
                MAIN.loader_mc._x = 533;
            } // end if
            if (nextSection == "faq")
            {
                MAIN.loader_mc._x = 153;
            } // end if
            if (nextSection == "hours")
            {
                MAIN.loader_mc._x = 533;
            } // end if
            if (nextSection == "tracks")
            {
                MAIN.loader_mc._x = 153;
            } // end if
            if (nextSection == "gallery")
            {
                MAIN.loader_mc._x = 153;
            } // end if
            MAIN.loader_mc.recordValues();
            MAIN.loader_mc._xscale = MAIN.loader_mc._yscale = MAIN.loader_mc._alpha = 10;
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.100000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.100000);
            newTween(MAIN.loader_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.300000);
            MAIN.loader_mc.loadTxt_mc.text_txt.htmlText = "<B><I>0</B></I>";
            MAIN.loader_mc.loadTxt_mc._x = MAIN.loader_mc.loadTxt_mc._x + 37;
            MAIN.loader_mc.loadTxt_mc._y = MAIN.loader_mc.loadTxt_mc._y - 4;
            if (nextSection == "home")
            {
                this.counter = 2;
                MAIN.loader_mc.loadTxt_mc.text_txt.htmlText = "<B><I>100</B></I>";
                MAIN.loader_mc.loadTxt_mc._x = MAIN.loader_mc.loadTxt_mc.origX;
                MAIN.loader_mc.loadTxt_mc._y = MAIN.loader_mc.loadTxt_mc.origY;
            } // end if
            if (audioOn)
            {
                loadBegin.start(0, 1);
                loadBegin.onSoundComplete = function ()
                {
                    loadLoop.start(0, 100);
                };
            } // end if
        }
        else if (this.counter == 2)
        {
            if (_root.MAIN.section.BG_mc.getBytesLoaded() >= _root.MAIN.section.BG_mc.getBytesTotal() && _root.MAIN.section.BG_mc.getBytesTotal() > 10)
            {
                MAIN.loader_mc.loadTxt_mc._x = MAIN.loader_mc.loadTxt_mc.origX;
                MAIN.loader_mc.loadTxt_mc._y = MAIN.loader_mc.loadTxt_mc.origY;
                MAIN.loader_mc.loadTxt_mc.text_txt.htmlText = "<B><I>100</B></I>";
                MAIN.loader_mc.loadDash_mc.needle1_mc._rotation = 154;
                MAIN.loader_mc.loadDash_mc.needle2_mc._rotation = 250;
            }
            else
            {
                percent = Math.floor(_root.MAIN.section.BG_mc.getBytesLoaded() / _root.MAIN.section.BG_mc.getBytesTotal() * 100);
                percent = isNaN(percent) ? (0) : (percent);
                MAIN.loader_mc.loadTxt_mc.text_txt.htmlText = "<B><I>" + percent + "</B></I>";
                MAIN.loader_mc.loadDash_mc.needle1_mc._rotation = -11;
                MAIN.loader_mc.loadDash_mc.needle2_mc._rotation = 25;
                MAIN.loader_mc.loadDash_mc.needle1_mc._rotation = -11 + 165 * (percent / 100);
                MAIN.loader_mc.loadDash_mc.needle2_mc._rotation = 25 + 225 * (percent / 100);
                MAIN.loader_mc.loadDash_mc._x = MAIN.loader_mc.loadDash_mc.origX + (random(30) / 10 - 1.500000);
                MAIN.loader_mc.loadDash_mc._y = MAIN.loader_mc.loadDash_mc.origY + (random(30) / 10 - 1.500000);
                this.counter--;
            } // end if
        }
        else if (this.counter == 3)
        {
            loadBegin.stop();
            loadLoop.stop();
            loadBegin.onSoundComplete = function ()
            {
            };
            if (audioOn)
            {
                loadedSound.setVolume(100);
                loadedSound.start(0, 1);
            } // end if
            if (nextSection == "performance" || nextSection == "offroad")
            {
                MAIN.section.createEmptyMovieClip("audioFadeEngine_mc", mainLevel());
                MAIN.section.audioFadeEngine_mc.fadeAmount = 100;
                MAIN.section.audioFadeEngine_mc.onEnterFrame = function ()
                {
                    this.fadeAmount = this.fadeAmount - 2;
                    if (this.fadeAmount <= 0)
                    {
                        loadedSound.stop();
                        this.removeMovieClip();
                    }
                    else
                    {
                        loadedSound.setVolume(this.fadeAmount);
                    } // end if
                };
            } // end if
            MAIN.section.BG_mc._x = -51;
            MAIN.section.BG_mc._y = 54;
            MAIN.section.BG_mc.gotoAndStop(2);
            MAIN.section.BG_mc._visible = false;
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeOut, 70, 0.800000);
            newTween(MAIN.loader_mc.loadTxt_mc, "_xscale", as.transitions.easing.Strong.easeOut, 180, 0.800000);
            newTween(MAIN.loader_mc.loadTxt_mc, "_yscale", as.transitions.easing.Strong.easeOut, 180, 0.800000);
            newTween(MAIN.loader_mc.percent_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.loader_mc.percent_mc.origX + 60, 0.800000);
            newTween(MAIN.loader_mc.text1_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.loader_mc.text1_mc.origY - 40, 0.800000);
            newTween(MAIN.loader_mc.loadDash_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.loader_mc.loadDash_mc.origY - 30, 0.800000);
            newTween(MAIN.loader_mc.loadDash_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.loader_mc.loadDash_mc.origX + 40, 0.800000);
        }
        else if (this.counter == 13)
        {
            newTween(MAIN.loader_mc.loadTxt_mc, "_xscale", as.transitions.easing.Bounce.easeOut, 100, 0.800000);
            newTween(MAIN.loader_mc.loadTxt_mc, "_yscale", as.transitions.easing.Bounce.easeOut, 100, 0.800000);
            newTween(MAIN.loader_mc.percent_mc, "_x", as.transitions.easing.Bounce.easeOut, MAIN.loader_mc.percent_mc.origX, 0.800000);
            newTween(MAIN.loader_mc.text1_mc, "_y", as.transitions.easing.Bounce.easeOut, MAIN.loader_mc.text1_mc.origY, 0.800000);
            newTween(MAIN.loader_mc.loadDash_mc, "_y", as.transitions.easing.Bounce.easeOut, MAIN.loader_mc.loadDash_mc.origY, 0.800000);
            newTween(MAIN.loader_mc.loadDash_mc, "_x", as.transitions.easing.Bounce.easeOut, MAIN.loader_mc.loadDash_mc.origX, 0.800000);
            if (nextSection == "offroad")
            {
                BuildTrackPage(nextSection);
            } // end if
            if (nextSection == "performance")
            {
                BuildTrackPage(nextSection);
            } // end if
            if (nextSection == "overview")
            {
                BuildOverview();
            } // end if
            if (nextSection == "tix")
            {
                BuildTix();
            } // end if
            if (nextSection == "faq")
            {
                BuildFaq();
            } // end if
            if (nextSection == "maps")
            {
                BuildMaps();
            } // end if
            if (nextSection == "hours")
            {
                BuildHours();
            } // end if
            if (nextSection == "tracks")
            {
                BuildTracks();
            } // end if
            if (nextSection == "gallery")
            {
                BuildGallery();
            } // end if
            if (nextSection == "partners")
            {
                BuildPartners();
            } // end if
            this.removeMovieClip();
        } // end if
        this.counter++;
    };
} // End of the function
function BuildOverview()
{
    _root.MAIN.section.counter = 1;
    _root.MAIN.section.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 293, 0.300000);
            MAIN.section.BG_mc._visible = true;
            MAIN.section.BG_mc.holder_mc._visible = false;
            MAIN.section.BG_mc.shadow_mc._visible = false;
            MAIN.section.BG_mc.photoBG_mc._visible = false;
            MAIN.section.BG_mc.textHeader_mc._visible = false;
            MAIN.section.BG_mc.hottest_mc._visible = false;
            MAIN.section.BG_mc.tag_mc._visible = false;
            MAIN.section.BG_mc.textHeader2_mc._visible = false;
            MAIN.section.BG_mc.stroke_mc.promo_mc._visible = false;
            MAIN.section.BG_mc.stroke_mc.back_mc._visible = false;
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.loader_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                _root.MAIN.loader_mc.removeMovieClip();
            };
        }
        else if (_root.counter == 10)
        {
            MAIN.section.BG_mc.photoBG_mc._visible = true;
            MAIN.section.BG_mc.photoBG_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.800000);
            overview_array[0][0][0] = overview_array[0][0][0].replace("&apos;", "\'");
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, overview_array, 79, 67, 332, 381, 134, 13, false);
        }
        else if (_root.counter == 11)
        {
            colorApply(_root.MAIN.section.copyBox_mc, [0, 255, 0, 255, 0, 255, 100, 100]);
        }
        else if (_root.counter == 17)
        {
            colorShift(_root.MAIN.section.copyBox_mc, [100, 0, 100, 0, 100, 0, 100, 0], 3);
            _root.MAIN.section.BG_mc.textHeader_mc._visible = true;
            _root.MAIN.section.BG_mc.textHeader_mc.text1_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (_root.counter == 22)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 300;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
            _root.MAIN.section.BG_mc.textHeader_mc.text3_mc.origY = _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._y;
            _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._y = _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._y - 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text3_mc, "_y", as.transitions.easing.Strong.easeIn, _root.MAIN.section.BG_mc.textHeader_mc.text3_mc.origY, 0.200000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text3_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.100000);
            MAIN.section.BG_mc.strokeMask_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.stroke_mc.text1_mc._alpha = MAIN.section.BG_mc.stroke_mc.text2_mc._alpha = MAIN.section.BG_mc.stroke_mc.text3_mc._alpha = 0;
            MAIN.section.BG_mc.stroke_mc.arrow1_mc._alpha = MAIN.section.BG_mc.stroke_mc.arrow2_mc._alpha = MAIN.section.BG_mc.stroke_mc.arrow3_mc._alpha = 0;
        }
        else if (_root.counter == 25)
        {
            ImageRotator();
        }
        else if (_root.counter == 36)
        {
            MAIN.section.BG_mc.stroke_mc.promo_mc._visible = true;
            MAIN.section.BG_mc.stroke_mc.promo_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.stroke_mc.promo_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            newTween(MAIN.section.BG_mc.stroke_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.200000);
            MAIN.section.BG_mc.stroke_mc.arrow1_mc._xscale = MAIN.section.BG_mc.stroke_mc.arrow1_mc._yscale = 30;
            newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_xscale", as.transitions.easing.Back.easeOut, 100, 1);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_yscale", as.transitions.easing.Back.easeOut, 100, 1);
        }
        else if (_root.counter == 40)
        {
            newTween(MAIN.section.BG_mc.stroke_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            MAIN.section.BG_mc.stroke_mc.arrow2_mc._xscale = MAIN.section.BG_mc.stroke_mc.arrow2_mc._yscale = 30;
            newTween(MAIN.section.BG_mc.stroke_mc.arrow2_mc, "_xscale", as.transitions.easing.Back.easeOut, 100, 1);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow2_mc, "_yscale", as.transitions.easing.Back.easeOut, 100, 1);
        }
        else if (_root.counter == 44)
        {
            newTween(MAIN.section.BG_mc.stroke_mc.text3_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow3_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            MAIN.section.BG_mc.stroke_mc.arrow3_mc._xscale = MAIN.section.BG_mc.stroke_mc.arrow3_mc._yscale = 30;
            newTween(MAIN.section.BG_mc.stroke_mc.arrow3_mc, "_xscale", as.transitions.easing.Back.easeOut, 100, 1);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow3_mc, "_yscale", as.transitions.easing.Back.easeOut, 100, 1);
            MAIN.section.BG_mc.stroke_mc.emailButton_mc.onRelease = function ()
            {
                getURL("mailTo:info@thedrivevegas.com");
            };
        }
        else if (_root.counter == 50)
        {
            MAIN.section.BG_mc.hottest_mc._visible = true;
            MAIN.section.BG_mc.hottest_mc._xscale = MAIN.section.BG_mc.hottest_mc._yscale = 10;
            MAIN.section.BG_mc.hottest_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.hottest_mc, "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.500000);
            newTween(MAIN.section.BG_mc.hottest_mc, "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.500000);
            newTween(MAIN.section.BG_mc.hottest_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.300000);
        }
        else if (_root.counter == 55)
        {
            MAIN.section.BG_mc.stroke_mc.text1_mc._alpha = 100;
            MAIN.section.BG_mc.stroke_mc.text2_mc._alpha = 50;
            MAIN.section.BG_mc.stroke_mc.text3_mc._alpha = 50;
            MAIN.section.BG_mc.stroke_mc.arrow1_mc._alpha = 100;
            MAIN.section.BG_mc.stroke_mc.arrow2_mc._alpha = 50;
            MAIN.section.BG_mc.stroke_mc.arrow3_mc._alpha = 50;
            MAIN.section.BG_mc.stroke_mc.button1_mc.enabled = false;
            MAIN.section.BG_mc.stroke_mc.button1_mc.onRelease = function ()
            {
                MAIN.section.BG_mc.tag_mc._visible = false;
                MAIN.section.BG_mc.textHeader_mc._visible = true;
                MAIN.section.BG_mc.textHeader2_mc._visible = false;
                removeVideo("noDrop");
                MAIN.section.BG_mc.holder_mc._visible = true;
                MAIN.section.BG_mc.shadow_mc._visible = true;
                MAIN.section.BG_mc.imageTag_mc._visible = true;
                MAIN.section.BG_mc.tagText_mc._visible = true;
                MAIN.section.BG_mc.tagArrow_mc._visible = true;
                MAIN.section.BG_mc.stroke_mc.text1_mc._alpha = 100;
                MAIN.section.BG_mc.stroke_mc.text2_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.text3_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.arrow1_mc._alpha = 100;
                MAIN.section.BG_mc.stroke_mc.arrow2_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.arrow3_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.button1_mc.enabled = false;
                MAIN.section.BG_mc.stroke_mc.button2_mc.enabled = true;
                MAIN.section.BG_mc.stroke_mc.button3_mc.enabled = true;
                MAIN.section.BG_mc.stroke_mc.back_mc._visible = false;
                MAIN.section.BG_mc.stroke_mc.promo_mc._visible = true;
                MAIN.section.BG_mc.stroke_mc.promo_mc._alpha = 0;
                newTween(MAIN.section.BG_mc.stroke_mc.promo_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.500000);
                ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 381, overview_array, headerFormat, "~~ overview ~~");
            };
            MAIN.section.BG_mc.stroke_mc.button2_mc.onRelease = function ()
            {
                MAIN.section.BG_mc.textHeader_mc._visible = true;
                MAIN.section.BG_mc.textHeader2_mc._visible = false;
                MAIN.section.BG_mc.holder_mc._visible = false;
                MAIN.section.BG_mc.shadow_mc._visible = false;
                MAIN.section.BG_mc.imageTag_mc._visible = false;
                MAIN.section.BG_mc.tagText_mc._visible = false;
                MAIN.section.BG_mc.tagArrow_mc._visible = false;
                MAIN.section.BG_mc.stroke_mc.button1_mc.enabled = true;
                MAIN.section.BG_mc.stroke_mc.button2_mc.enabled = false;
                MAIN.section.BG_mc.stroke_mc.button3_mc.enabled = true;
                MAIN.section.BG_mc.stroke_mc.text1_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.text2_mc._alpha = 100;
                MAIN.section.BG_mc.stroke_mc.text3_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.arrow1_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.arrow2_mc._alpha = 100;
                MAIN.section.BG_mc.stroke_mc.arrow3_mc._alpha = 50;
                RemoveCar();
                VidPlayer("overview", "overviewVideo.swf");
            };
            MAIN.section.BG_mc.stroke_mc.button3_mc.onRelease = function ()
            {
                removeVideo("noDrop");
                MAIN.section.BG_mc.tag_mc._visible = false;
                MAIN.section.BG_mc.holder_mc._visible = true;
                MAIN.section.BG_mc.shadow_mc._visible = true;
                MAIN.section.BG_mc.imageTag_mc._visible = true;
                MAIN.section.BG_mc.tagText_mc._visible = true;
                MAIN.section.BG_mc.tagArrow_mc._visible = true;
                MAIN.section.BG_mc.stroke_mc.button1_mc.enabled = true;
                MAIN.section.BG_mc.stroke_mc.button2_mc.enabled = true;
                MAIN.section.BG_mc.stroke_mc.button3_mc.enabled = false;
                MAIN.section.BG_mc.stroke_mc.text1_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.text2_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.text3_mc._alpha = 100;
                MAIN.section.BG_mc.stroke_mc.arrow1_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.arrow2_mc._alpha = 50;
                MAIN.section.BG_mc.stroke_mc.arrow3_mc._alpha = 100;
                MAIN.section.BG_mc.textHeader_mc._visible = false;
                MAIN.section.BG_mc.textHeader2_mc._visible = true;
                MAIN.section.BG_mc.stroke_mc.promo_mc._visible = false;
                MAIN.section.BG_mc.stroke_mc.back_mc._visible = true;
                MAIN.section.BG_mc.stroke_mc.back_mc._alpha = 0;
                newTween(MAIN.section.BG_mc.stroke_mc.back_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.500000);
                ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 366, promo_array, headerFormat, "~~ overview ~~");
            };
            CreateTagline("overview");
            delete _root["onEnterFrame"];
        } // end if
        _root.counter++;
    };
} // End of the function
function BuildTracks()
{
    _root.MAIN.section.counter = 1;
    _root.MAIN.section.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 194, 0.300000);
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.loader_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                _root.MAIN.loader_mc.removeMovieClip();
            };
        }
        else if (_root.counter == 8)
        {
            tracks_array[0][0][0] = tracks_array[0][0][0].replace("&apos;", "\'");
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, tracks_array, 261, 93, 332, 298, 126, 22, [0, 45, 0, 72, 0, 35, 100, 100]);
        }
        else if (_root.counter == 10)
        {
            colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 50, 100]);
            MAIN.section.BG_mc._visible = true;
            MAIN.section.BG_mc.trackChooser_mc._visible = false;
            MAIN.section.BG_mc.textLeft_mc._visible = false;
            MAIN.section.BG_mc.textRight_mc._visible = false;
            MAIN.section.BG_mc.photoBG_mc._visible = true;
            MAIN.section.BG_mc.photoBG_mc._alpha = 0;
            MAIN.section.BG_mc.textHeader_mc.text1_mc._alpha = 0;
            MAIN.section.BG_mc.textHeader_mc.text2_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.800000);
            MAIN.section.BG_mc.trackChooser_mc._visible = true;
            MAIN.section.BG_mc.trackChooser_mc.gotoAndPlay(2);
        }
        else if (_root.counter == 17)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (_root.counter == 20)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 300;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
        }
        else if (_root.counter == 25)
        {
            MAIN.section.BG_mc.textLeft_mc._visible = true;
            MAIN.section.BG_mc.textLeft_mc._alpha = 0;
            MAIN.section.BG_mc.textLeft_mc._xscale = MAIN.section.BG_mc.textLeft_mc._yscale = 300;
            newTween(MAIN.section.BG_mc.textLeft_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.section.BG_mc.textLeft_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.section.BG_mc.textLeft_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
            MAIN.section.BG_mc.textRight_mc._visible = true;
            MAIN.section.BG_mc.textRight_mc._alpha = 0;
            MAIN.section.BG_mc.textRight_mc._xscale = MAIN.section.BG_mc.textRight_mc._yscale = 300;
            newTween(MAIN.section.BG_mc.textRight_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.section.BG_mc.textRight_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.section.BG_mc.textRight_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
        }
        else if (_root.counter == 29)
        {
            if (audioOn)
            {
                boomSound.start(0, 1);
            } // end if
        }
        else if (_root.counter == 35)
        {
            MAIN.section.BG_mc.butRight_mc.onRollOver = function ()
            {
                newTween(MAIN.section.BG_mc.textRight_mc, "_xscale", as.transitions.easing.Strong.easeOut, 120, 0.300000);
                newTween(MAIN.section.BG_mc.textRight_mc, "_yscale", as.transitions.easing.Strong.easeOut, 120, 0.300000);
                colorShift(MAIN.section.BG_mc.textRight_mc, [0, 234, 0, 24, 0, 168, 100, 0], 3);
            };
            MAIN.section.BG_mc.butRight_mc.onRollOut = function ()
            {
                newTween(MAIN.section.BG_mc.textRight_mc, "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                newTween(MAIN.section.BG_mc.textRight_mc, "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                colorShift(MAIN.section.BG_mc.textRight_mc, [100, 0, 100, 0, 100, 0, 100, 0], 3);
            };
            MAIN.section.BG_mc.butLeft_mc.onRollOver = function ()
            {
                newTween(MAIN.section.BG_mc.textLeft_mc, "_xscale", as.transitions.easing.Strong.easeOut, 120, 0.300000);
                newTween(MAIN.section.BG_mc.textLeft_mc, "_yscale", as.transitions.easing.Strong.easeOut, 120, 0.300000);
                colorShift(MAIN.section.BG_mc.textLeft_mc, [0, 164, 0, 95, 0, 204, 100, 0], 3);
            };
            MAIN.section.BG_mc.butLeft_mc.onRollOut = function ()
            {
                newTween(MAIN.section.BG_mc.textLeft_mc, "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                newTween(MAIN.section.BG_mc.textLeft_mc, "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.300000);
                colorShift(MAIN.section.BG_mc.textLeft_mc, [100, 0, 100, 0, 100, 0, 100, 0], 3);
            };
            MAIN.section.BG_mc.butLeft_mc.onRelease = function ()
            {
                this.enabled = false;
                MAIN.section.BG_mc.butLeft_mc.onRollOut = MAIN.section.BG_mc.butLeft_mc.onRollOver = MAIN.section.BG_mc.butLeft_mc.onDragOut = MAIN.section.BG_mc.butLeft_mc.onRelease = undefined;
                MAIN.section.BG_mc.butRight_mc.onRollOut = MAIN.section.BG_mc.butRight_mc.onRollOver = MAIN.section.BG_mc.butRight_mc.onDragOut = MAIN.section.BG_mc.butRight_mc.onRelease = undefined;
                _root.globalColor = "A3CB5E";
                _root.barColorShift = new Array(0, 164, 0, 95, 0, 204, 100, 0);
                RemoveHome("offroad");
            };
            MAIN.section.BG_mc.butRight_mc.onRelease = function ()
            {
                MAIN.section.BG_mc.butLeft_mc.onRollOut = MAIN.section.BG_mc.butLeft_mc.onRollOver = MAIN.section.BG_mc.butLeft_mc.onDragOut = MAIN.section.BG_mc.butLeft_mc.onRelease = undefined;
                MAIN.section.BG_mc.butRight_mc.onRollOut = MAIN.section.BG_mc.butRight_mc.onRollOver = MAIN.section.BG_mc.butRight_mc.onDragOut = MAIN.section.BG_mc.butRight_mc.onRelease = undefined;
                this.enabled = false;
                _root.globalColor = "eaa818";
                _root.barColorShift = new Array(0, 234, 0, 24, 0, 168, 100, 0);
                RemoveHome("performance");
            };
            CreateTagline("tracks");
            ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 316, tracks_array, headerFormat);
            delete this["onEnterFrame"];
        } // end if
        this.counter++;
    };
} // End of the function
function BuildHours()
{
    _root.MAIN.section.counter = 1;
    _root.MAIN.section.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 194, 0.300000);
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.loader_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                _root.MAIN.loader_mc.removeMovieClip();
            };
        }
        else if (_root.counter == 4)
        {
            hours_array[0][0][0] = hours_array[0][0][0].replace("&apos;", "\'");
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, hours_array, 437, 93, 331, 381, 138, 22, [0, 45, 0, 72, 0, 35, 100, 100]);
        }
        else if (_root.counter == 10)
        {
            ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 381, hours_array, headerFormat);
            colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 50, 100]);
            MAIN.section.BG_mc._visible = true;
            MAIN.section.BG_mc.photoBG_mc._visible = true;
            MAIN.section.BG_mc.holder_mc._visible = false;
            MAIN.section.BG_mc.shadow_mc._visible = false;
            MAIN.section.BG_mc.textHeader_mc._visible = false;
            MAIN.section.BG_mc.photoBG_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.800000);
        }
        else if (_root.counter == 14)
        {
            _root.MAIN.section.BG_mc.textHeader_mc._visible = true;
            _root.MAIN.section.BG_mc.textHeader_mc.text1_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.keys_mc._alpha = 0;
        }
        else if (_root.counter == 17)
        {
            colorShift(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, [100, 0, 100, 0, 100, 0, 100, 0], 3);
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (_root.counter == 22)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 300;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
            _root.MAIN.section.BG_mc.textHeader_mc.text3_mc.origY = _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._y;
            _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._y = _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._y - 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text3_mc, "_y", as.transitions.easing.Strong.easeIn, _root.MAIN.section.BG_mc.textHeader_mc.text3_mc.origY, 0.200000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text3_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.100000);
        }
        else if (_root.counter == 25)
        {
            ImageRotator();
        }
        else if (_root.counter == 28)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.keys_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.keys_mc._yscale = 300;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.keys_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.keys_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.keys_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
        }
        else if (_root.counter == 35)
        {
        }
        else if (_root.counter == 38)
        {
            MAIN.section.BG_mc.textHeader_mc.splatter_mc.gotoAndPlay(2);
        }
        else if (_root.counter == 40)
        {
            MAIN.section.BG_mc.strokeMask_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.stroke_mc.text1_mc._alpha = 0;
            MAIN.section.BG_mc.stroke_mc.text2_mc._alpha = 0;
            MAIN.section.BG_mc.stroke_mc.arrow1_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.stroke_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.200000);
            MAIN.section.BG_mc.stroke_mc.arrow1_mc._xscale = MAIN.section.BG_mc.stroke_mc.arrow1_mc._yscale = 30;
            newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_xscale", as.transitions.easing.Back.easeOut, 100, 1);
            newTween(MAIN.section.BG_mc.stroke_mc.arrow1_mc, "_yscale", as.transitions.easing.Back.easeOut, 100, 1);
            MAIN.section.BG_mc.stroke_mc.button1_mc.currentText = "hours";
            MAIN.section.BG_mc.stroke_mc.button1_mc.onRelease = function ()
            {
                if (this.currentText == "hours")
                {
                    this.currentText = "special";
                    ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 350, special_array, headerFormat);
                    newTween(MAIN.section.BG_mc.stroke_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 0, 0.300000);
                    newTween(MAIN.section.BG_mc.stroke_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 1);
                    MAIN.section.BG_mc.holder_mc._visible = false;
                    MAIN.section.BG_mc.tagText_mc._visible = false;
                    MAIN.section.BG_mc.tag_mc._visible = false;
                    MAIN.section.BG_mc.special_mc.gotoAndPlay(2);
                }
                else if (this.currentText == "special")
                {
                    this.currentText = "hours";
                    ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 381, hours_array, headerFormat);
                    newTween(MAIN.section.BG_mc.stroke_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 0, 0.300000);
                    newTween(MAIN.section.BG_mc.stroke_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 1);
                    MAIN.section.BG_mc.holder_mc._visible = true;
                    MAIN.section.BG_mc.tagText_mc._visible = true;
                    MAIN.section.BG_mc.tag_mc._visible = true;
                    MAIN.section.BG_mc.special_mc.gotoAndStop(1);
                } // end if
            };
        }
        else if (this.counter == 50)
        {
            _root.MAIN.section.BG_mc.imageMask_mc._visible = false;
            CreateTagline("hours");
            delete this["onEnterFrame"];
        } // end if
        this.counter++;
    };
} // End of the function
function BuildPartners()
{
    _root.MAIN.section.counter = 1;
    _root.MAIN.section.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 194, 0.300000);
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.loader_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                _root.MAIN.loader_mc.removeMovieClip();
            };
        }
        else if (_root.counter == 4)
        {
            hours_array[0][0][0] = hours_array[0][0][0].replace("&apos;", "\'");
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, hours_array, 437, 93, 331, 381, 138, 22, [0, 45, 0, 72, 0, 35, 100, 100]);
        }
        else if (_root.counter == 10)
        {
            colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 50, 100]);
            MAIN.section.BG_mc._visible = true;
            MAIN.section.BG_mc.photoBG_mc._visible = true;
            MAIN.section.BG_mc.holder_mc._visible = false;
            MAIN.section.BG_mc.shadow_mc._visible = false;
            MAIN.section.BG_mc.textHeader_mc._visible = false;
            MAIN.section.BG_mc.underline_mc._visible = true;
            MAIN.section.BG_mc.contentBG_mc._visible = false;
            MAIN.section.BG_mc.textMask_mc._height = 1;
            for (zz = 1; zz < 6; zz++)
            {
                MAIN.section.BG_mc["logo" + zz + "_mc"]._alpha = 0;
                MAIN.section.BG_mc["icon" + zz + "_mc"]._visible = false;
                MAIN.section.BG_mc["icon" + zz + "_sh_mc"]._alpha = 0;
                MAIN.section.BG_mc["iconBG" + zz + "_mc"]._visible = false;
            } // end of for
            MAIN.section.BG_mc.photoBG_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.800000);
        }
        else if (_root.counter == 14)
        {
            _root.MAIN.section.BG_mc.textHeader_mc._visible = true;
            _root.MAIN.section.BG_mc.textHeader_mc.text1_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._alpha = 0;
        }
        else if (_root.counter == 17)
        {
            colorShift(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, [100, 0, 100, 0, 100, 0, 100, 0], 3);
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (_root.counter == 22)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 300;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
            MAIN.section.BG_mc.underline_mc._visible = true;
            MAIN.section.BG_mc.underline_mc.gotoAndPlay(2);
        }
        else if (_root.counter == 30)
        {
            MAIN.section.BG_mc.contentBG_mc._visible = true;
            MAIN.section.BG_mc.contentBG_mask_mc.gotoAndPlay(2);
        }
        else if (_root.counter == 38)
        {
            MAIN.section.BG_mc.iconBG1_mc._visible = true;
            MAIN.section.BG_mc.thumb1_mask_mc.gotoAndPlay(2);
        }
        else if (_root.counter == 42)
        {
            MAIN.section.BG_mc.iconBG2_mc._visible = true;
            MAIN.section.BG_mc.thumb2_mask_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.icon1_mc._visible = true;
            MAIN.section.BG_mc.icon1_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.icon1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 2);
        }
        else if (_root.counter == 46)
        {
            MAIN.section.BG_mc.iconBG3_mc._visible = true;
            MAIN.section.BG_mc.thumb3_mask_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.icon2_mc._visible = true;
            MAIN.section.BG_mc.icon2_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.icon2_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 2);
        }
        else if (_root.counter == 50)
        {
            MAIN.section.BG_mc.iconBG4_mc._visible = true;
            MAIN.section.BG_mc.thumb4_mask_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.icon3_mc._visible = true;
            MAIN.section.BG_mc.icon3_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.icon3_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 2);
        }
        else if (_root.counter == 54)
        {
            MAIN.section.BG_mc.iconBG5_mc._visible = true;
            MAIN.section.BG_mc.thumb5_mask_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.icon4_mc._visible = true;
            MAIN.section.BG_mc.icon4_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.icon4_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 2);
        }
        else if (_root.counter == 56)
        {
            MAIN.section.BG_mc.icon5_mc._visible = true;
            MAIN.section.BG_mc.icon5_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.icon5_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 2);
            for (zz = 1; zz < 6; zz++)
            {
                MAIN.section.BG_mc["b" + zz + "_mc"].nowZZ = zz;
                MAIN.section.BG_mc["b" + zz + "_mc"].onRollOver = function ()
                {
                    newTween(MAIN.section.BG_mc["icon" + this.nowZZ + "_sh_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 40, 1);
                };
                MAIN.section.BG_mc["b" + zz + "_mc"].onRollOut = function ()
                {
                    newTween(MAIN.section.BG_mc["icon" + this.nowZZ + "_sh_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 0, 1);
                };
                MAIN.section.BG_mc["b" + zz + "_mc"].onRelease = function ()
                {
                    MAIN.section.partnerLoopEngine_mc.removeMovieClip();
                    MAIN.section.BG_mc.textMask_mc._height = 1;
                    MAIN.section.BG_mc.text_mc.text_txt.htmlText = _root["partner" + this.nowZZ + "_text"];
                    MAIN.section.BG_mc.logo1_mc._visible = false;
                    MAIN.section.BG_mc.logo2_mc._visible = false;
                    MAIN.section.BG_mc.logo3_mc._visible = false;
                    MAIN.section.BG_mc.logo4_mc._visible = false;
                    MAIN.section.BG_mc.logo5_mc._visible = false;
                    MAIN.section.BG_mc["logo" + this.nowZZ + "_mc"]._visible = true;
                    MAIN.section.BG_mc["logo" + this.nowZZ + "_mc"]._alpha = 0;
                    newTween(MAIN.section.BG_mc["logo" + this.nowZZ + "_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 100, 1.500000);
                    newTween(MAIN.section.BG_mc.textMask_mc, "_height", as.transitions.easing.Strong.easeOut, 180, 2);
                    MAIN.section.BG_mc.text_mc.moreInfo_mc.nowZZ = this.nowZZ;
                    MAIN.section.BG_mc.text_mc.moreInfo_mc.onRelease = function ()
                    {
                        trace(_root["partner" + this.nowZZ + "_url"]);
                        getURL(_root["partner" + this.nowZZ + "_url"], "_blank");
                    };
                };
            } // end of for
        }
        else if (this.counter == 60)
        {
            partner1_text = "Experience the in-vehicle safety and security system that helps keep you protected and connected on the road.  Visit a knowledgeable OnStar product specialist on-site for a live demonstration. Visit onstar.com or call 1-888-4-ONSTAR (1-888-466-7827) for system limitations and details.";
            partner2_text = "With a wide variety of programming, XM has something to excite any driver. Whether you want to be entertained or informed, to laugh, think, or sing, XM has the perfect channel for you - coast-to-coast, and in digital-quality sound. Visit the XM Listening Kiosk today!";
            partner3_text = "Visit the GMAC display to learn affordable and convenient ways to finance the home you\'ve been hoping for and apply for credit pre-approval. You can also learn everything you need to know about vehicle financing, banking and insurance services available through the GMAC Family of companies.";
            partner4_text = "Visit the GM Flexible Earnings Card booth and find out how you can earn vehicle rewards or cash back on every credit card purchase. Low APR. No Annual Fee. Apply today!";
            partner5_text = "Visit the GM Accessories display to see a sample of the wide variety of accessories available for each GM brand. Accessories sold through GM Dealerships are designed to GM standards and covered by GM\'s Bumper-to-Bumper New Vehicle Limited Warranty.";
            partner1_url = "http://www.onstar.com/us_english/jsp/index.jsp";
            partner2_url = "http://www.gm.xmradio.com/";
            partner3_url = "http://www.gmacfs.com/";
            partner4_url = "http://www.gmcard.com/GMCard/index.jsp";
            partner5_url = "http://www.gmaccessorieszone.com";
            MAIN.section.BG_mc.text_mc.text_txt.htmlText = partner1_text;
            newTween(MAIN.section.BG_mc.textMask_mc, "_height", as.transitions.easing.Strong.easeOut, 180, 2);
            newTween(MAIN.section.BG_mc.logo1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 1.500000);
            MAIN.section.BG_mc.text_mc.moreInfo_mc.onRelease = function ()
            {
                getURL(_root.partner1_url, "_blank");
            };
            MAIN.section.createEmptyMovieClip("partnerLoopEngine_mc", mainLevel());
            MAIN.section.partnerLoopEngine_mc.counter = 1;
            MAIN.section.partnerLoopEngine_mc.partner = 1;
            MAIN.section.partnerLoopEngine_mc.onEnterFrame = function ()
            {
                if (this.counter == 175)
                {
                    newTween(MAIN.section.BG_mc.textMask_mc, "_height", as.transitions.easing.Strong.easeOut, 1, 2);
                    newTween(MAIN.section.BG_mc["logo" + this.partner + "_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 0, 1.500000);
                }
                else if (this.counter == 200)
                {
                    this.partner++;
                    if (this.partner > 4)
                    {
                        this.partner = 1;
                    } // end if
                    MAIN.section.BG_mc.textMask_mc._height = 1;
                    MAIN.section.BG_mc.text_mc.text_txt.htmlText = _root["partner" + this.partner + "_text"];
                    MAIN.section.BG_mc.logo1_mc._visible = false;
                    MAIN.section.BG_mc.logo2_mc._visible = false;
                    MAIN.section.BG_mc.logo3_mc._visible = false;
                    MAIN.section.BG_mc.logo4_mc._visible = false;
                    MAIN.section.BG_mc["logo" + this.partner + "_mc"]._visible = true;
                    MAIN.section.BG_mc["logo" + this.partner + "_mc"]._alpha = 0;
                    newTween(MAIN.section.BG_mc["logo" + this.partner + "_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 100, 1.500000);
                    newTween(MAIN.section.BG_mc.textMask_mc, "_height", as.transitions.easing.Strong.easeOut, 180, 2);
                    MAIN.section.BG_mc.text_mc.moreInfo_mc.partner = this.partner;
                    MAIN.section.BG_mc.text_mc.moreInfo_mc.onRelease = function ()
                    {
                        trace(_root["partner" + this.partner + "_url"]);
                        getURL(_root["partner" + this.partner + "_url"], "_blank");
                    };
                    this.counter = 1;
                } // end if
                this.counter++;
            };
        }
        else if (this.counter == 64)
        {
            CreateTagline("partners");
            delete this["onEnterFrame"];
        } // end if
        this.counter++;
    };
} // End of the function
function removeVideo(noDrop)
{
    MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.removeMovieClip();
    MAIN.section.BG_mc.copyBoxHolder_mc.videoBG_mc.removeMovieClip();
    MAIN.section.BG_mc.copyBoxHolder_mc.copyBox2_mc.removeMovieClip();
    MAIN.section.BG_mc.tag_mc.play_mc.onRollOver = MAIN.section.BG_mc.tag_mc.play_mc.onRollOut = MAIN.section.BG_mc.tag_mc.play_mc.onRelease = undefined;
    MAIN.section.BG_mc.tag_mc.stop_mc.onRollOver = MAIN.section.BG_mc.tag_mc.stop_mc.onRollOut = MAIN.section.BG_mc.tag_mc.stop_mc.onRelease = undefined;
    MAIN.section.BG_mc.tag_mc.play_mc._visible = MAIN.section.BG_mc.tag_mc.stop_mc._visible = false;
    MAIN.section.BG_mc.tag_mc.text1_mc._visible = true;
    MAIN.section.BG_mc.tag_mc.text1_mc._alpha = 100;
    if (noDrop == undefined)
    {
        DropCar();
    } // end if
} // End of the function
function RemoveCar()
{
    MAIN.section.BG_mc.vehicleShadow_mc._visible = false;
    newTween(MAIN.section.BG_mc.car_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
    newTween(MAIN.section.BG_mc.car_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
    newTween(MAIN.section.BG_mc.car_mc, "_x", as.transitions.easing.Strong.easeIn, MAIN.section.BG_mc.car_mc._x + MAIN.section.BG_mc.car_mc._width / 2, 0.300000);
    newTween(MAIN.section.BG_mc.car_mc, "_y", as.transitions.easing.Strong.easeIn, MAIN.section.BG_mc.car_mc._y + MAIN.section.BG_mc.car_mc._height / 2, 0.300000);
    MAIN.section.BG_mc.car_mc.tweenObj_xscale.onMotionFinished = function ()
    {
        MAIN.section.BG_mc.car_mc._visible = false;
    };
} // End of the function
function ImageRotator()
{
    _root.MAIN.section.createEmptyMovieClip("imageRotatorEngine_mc", mainLevel());
    _root.MAIN.section.imageRotatorEngine_mc.counter = -15;
    _root.MAIN.section.imageRotatorEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == -15)
        {
            if (imageViewer_array.length == 0)
            {
                this.removeMovieClip();
            }
            else
            {
                _root.MAIN.section.BG_mc.imageMask_mc.gotoAndPlay(2);
            } // end if
        }
        else if (this.counter == -4)
        {
            MAIN.section.BG_mc.shadow_mc._visible = true;
            MAIN.section.BG_mc.shadow_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.shadow_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.500000);
        }
        else if (this.counter == 0)
        {
            MAIN.section.BG_mc.holder_mc._visible = true;
            imageNo = random(imageViewer_array.length);
        }
        else if (this.counter == 1)
        {
            MAIN.section.BG_mc.holder_mc.createEmptyMovieClip("image" + imageNo + "_mc", imageNo);
            MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"].createEmptyMovieClip("container_mc", 1);
            MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"].container_mc.loadMovie("eventPhotography/image" + imageNo + ".jpg", 1);
            MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"]._visible = false;
        }
        else if (this.counter == 2)
        {
            if (MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"].container_mc.getBytesLoaded() >= MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"].container_mc.getBytesTotal() && MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"].container_mc.getBytesTotal() > 15)
            {
            }
            else
            {
                this.counter--;
            } // end if
        }
        else if (this.counter == 3)
        {
            MAIN.section.BG_mc.holder_mc["image" + lastNO + "_mc"].removeMovieClip();
            colorApply(MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"], [0, 255, 0, 255, 0, 255, 100, 100]);
            colorShift(MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"], [100, 0, 100, 0, 100, 0, 100, 0], 7);
            MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"]._x = MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"]._x + 100;
            newTween(MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"], "_x", as.transitions.easing.Strong.easeOut, 0, 3);
            MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"]._visible = true;
            _root.MAIN.section.BG_mc.imageMask_mc._visible = false;
            nameTag = imageViewer_array[imageNo][0][0];
            lastNO = imageNo;
            imageNo++;
            if (imageNo >= imageViewer_array.length)
            {
                imageNo = 0;
            } // end if
            MAIN.section.BG_mc.holder_mc.createEmptyMovieClip("image" + imageNo + "_mc", imageNo);
            MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"].createEmptyMovieClip("container_mc", 1);
            MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"].container_mc.loadMovie("eventPhotography/image" + imageNo + ".jpg", 1);
            MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"]._visible = false;
        }
        else if (this.counter == 5)
        {
            _root.MAIN.section.BG_mc.tagText_mc.daTag_mc.removeMovieClip();
            CreateTextBox("daTag_mc", nameTag.toUpperCase(), _root.MAIN.section.BG_mc.tagText_mc, tagFormat, 0, 0, 1, 1, false, true, false, true);
        }
        else if (this.counter == 6)
        {
            _root.MAIN.section.BG_mc.tagMask_mc.gotoAndPlay(2);
            _root.MAIN.section.BG_mc.tagText_mc.daTag_mc._x = _root.MAIN.section.BG_mc.tagText_mc.daTag_mc._x - _root.MAIN.section.BG_mc.tagText_mc.daTag_mc._width;
            _root.MAIN.section.BG_mc.tagArrow_mc._x = MAIN.section.BG_mc.tagText_mc._x - _root.MAIN.section.BG_mc.tagText_mc.daTag_mc._width - 7;
            _root.MAIN.section.BG_mc.imageTag_mc.tagLeft_mc._x = -_root.MAIN.section.BG_mc.tagText_mc.daTag_mc._width + 50;
            _root.MAIN.section.BG_mc.imageTag_mc.tagFiller_mc._x = _root.MAIN.section.BG_mc.imageTag_mc.tagLeft_mc._x + _root.MAIN.section.BG_mc.imageTag_mc.tagLeft_mc._width;
            tagFiller_width = _root.MAIN.section.BG_mc.imageTag_mc.tagRight_mc._x - _root.MAIN.section.BG_mc.imageTag_mc.tagLeft_mc._x - _root.MAIN.section.BG_mc.imageTag_mc.tagLeft_mc._width;
            if (tagFiller_width < 1)
            {
                tagFiller_width = 1;
            } // end if
            _root.MAIN.section.BG_mc.imageTag_mc.tagFiller_mc._width = tagFiller_width;
        }
        else if (this.counter == 89)
        {
            if (MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"].container_mc.getBytesLoaded() >= MAIN.section.BG_mc.holder_mc["image" + imageNo + "_mc"].container_mc.getBytesTotal())
            {
                _root.MAIN.section.BG_mc.tagMask_mc.gotoAndPlay("out");
            }
            else
            {
                this.counter--;
            } // end if
        }
        else if (this.counter == 99)
        {
            this.counter = 2;
        } // end if
        this.counter++;
    };
} // End of the function
function BuildMaps()
{
    _root.MAIN.section.counter = 1;
    _root.MAIN.section.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 194, 0.300000);
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.loader_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                _root.MAIN.loader_mc.removeMovieClip();
            };
        }
        else if (_root.counter == 4)
        {
            maps_array[0][0][0] = hours_array[0][0][0].replace("&apos;", "\'");
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, maps_array, 94, 196, 383, 285, 34, 24, [0, 45, 0, 72, 0, 35, 100, 100]);
        }
        else if (_root.counter == 10)
        {
            colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 50, 100]);
            MAIN.section.BG_mc._visible = true;
            MAIN.section.BG_mc.photoBG_mc._visible = true;
            MAIN.section.BG_mc.map_mc._visible = false;
            MAIN.section.BG_mc.photoBG_mc._alpha = 0;
            MAIN.section.BG_mc.textHeader_mc.text1_mc._alpha = 0;
            MAIN.section.BG_mc.textHeader_mc.text2_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.800000);
        }
        else if (_root.counter == 15)
        {
            MAIN.section.attachMovie("faq_underline_mc", "underline_mc", mainLevel(), {_x: -5, _y: 186});
            MAIN.section.underline_mc.gotoAndPlay(2);
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, undefined, 542, 244, 244, 237, 34, 24, [0, 45, 0, 72, 0, 35, 100, 100]);
            MAIN.section.BG_mc.textHeader_mc._visible = true;
            _root.MAIN.section.BG_mc.textHeader_mc.text1_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (_root.counter == 20)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 300;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
            colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox2_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 50, 100]);
            _root.MAIN.section.textHeader_mc.text2_mc._xscale = _root.MAIN.section.textHeader_mc.text2_mc._yscale = 300;
            MAIN.section.BG_mc.underline_mc._visible = true;
            MAIN.section.BG_mc.underline_mc.gotoAndPlay(2);
        }
        else if (_root.counter == 25)
        {
            MAIN.section.BG_mc.map_mc._visible = true;
            MAIN.section.BG_mc.map_mc._alpha = 0;
            newTween(_root.MAIN.section.BG_mc.map_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 1);
            _root.MAIN.section.BG_mc.map_mc.star_mc._alpha = _root.MAIN.section.BG_mc.map_mc.blast_mc._alpha = _root.MAIN.section.BG_mc.map_mc.box_mc._alpha = 0;
            _root.MAIN.section.BG_mc.map_mc.box_mc.changeColor("f77b13");
            newTween(_root.MAIN.section.BG_mc.map_mc.box_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.200000);
        }
        else if (_root.counter == 30)
        {
            newTween(_root.MAIN.section.BG_mc.map_mc.blast_mc, "_alpha", as.transitions.easing.Strong.easeOut, 50, 0.800000);
            _root.MAIN.section.BG_mc.map_mc.blast_mc.onEnterFrame = function ()
            {
                this._rotation = this._rotation + 2;
            };
            newTween(_root.MAIN.section.BG_mc.map_mc.star_mc, "_alpha", as.transitions.easing.Strong.easeOut, 80, 0.800000);
            _root.MAIN.section.BG_mc.map_mc.star_mc._xscale = _root.MAIN.section.BG_mc.map_mc.star_mc._yscale = 10;
            newTween(_root.MAIN.section.BG_mc.map_mc.star_mc, "_xscale", as.transitions.easing.Back.easeOut, 100, 0.900000);
            newTween(_root.MAIN.section.BG_mc.map_mc.star_mc, "_yscale", as.transitions.easing.Back.easeOut, 100, 0.900000);
        }
        else if (this.counter == 37)
        {
            newTween(_root.MAIN.section.BG_mc.map_mc.star_mc, "_xscale", as.transitions.easing.Strong.easeInOut, 115, 0.900000);
            newTween(_root.MAIN.section.BG_mc.map_mc.star_mc, "_yscale", as.transitions.easing.Strong.easeInOut, 115, 0.900000);
            _root.MAIN.section.BG_mc.map_mc.star_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                this.yoyo();
            };
            _root.MAIN.section.BG_mc.map_mc.star_mc.tweenObj_yscale.onMotionFinished = function ()
            {
                this.yoyo();
            };
            CreateTagline("maps");
            delete this["onEnterFrame"];
        } // end if
        this.counter++;
    };
} // End of the function
function BuildFaq()
{
    _root.MAIN.section.counter = 1;
    _root.MAIN.section.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 194, 0.300000);
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.loader_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                _root.MAIN.loader_mc.removeMovieClip();
            };
        }
        else if (_root.counter == 4)
        {
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, "", 94, 230, 623, 242, 34, 24, [0, 45, 0, 72, 0, 35, 100, 100]);
        }
        else if (_root.counter == 10)
        {
            colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 50, 100]);
            MAIN.section.BG_mc._visible = true;
            MAIN.section.BG_mc.photoBG_mc._visible = true;
            MAIN.section.BG_mc.textHeader_mc._visible = false;
            MAIN.section.BG_mc.photoBG_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.800000);
        }
        else if (_root.counter == 15)
        {
            MAIN.section.BG_mc.underline_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.textHeader_mc._visible = true;
            _root.MAIN.section.BG_mc.textHeader_mc.text1_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (_root.counter == 20)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 300;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
            MAIN.section.BG_mc.underline_mc._visible = true;
            _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc.daBox_txt._visible = false;
            _root.MAIN.section.createEmptyMovieClip("faqEngine_mc", mainLevel());
            _root.MAIN.section.faqEngine_mc.counter = 1;
            _root.MAIN.section.faqEngine_mc.onEnterFrame = function ()
            {
                if (this.counter == 1)
                {
                    trace("loop. (" + _root.faq_array.length + ")");
                    for (no = 0; no < _root.faq_array.length; no++)
                    {
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc.attachMovie("faq_itemHeader_mc", "itemHeader" + no + "_mc", mainLevel());
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].text_mc.text_txt.text = _root.faq_array[no][0][0].toUpperCase();
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"]._x = 48;
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"]._y = 23 * no;
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].origY = _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"]._y;
                        CreateTextBox("answer_mc", _root.faq_array[no][0][1], _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"], headerFormat, 21, 20, 520, 1, true, true, true);
                        if (no != 0)
                        {
                            _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].attachMovie("box_mc", "underline_mc", mainLevel(), {_x: 0, _y: 0, _width: 500, _height: 1});
                        } // end if
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].underline_mc.changeColor("cdcdd2");
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].attachMovie("box_mc", "mask_mc", mainLevel(), {_x: 0, _y: 0, _width: 550, _height: 23, _alpha: 30});
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].answer_mc.setMask(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].mask_mc);
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].attachMovie("arrow_mc", "arrow_mc", mainLevel(), {_x: -9, _y: 12, _xscale: 90, _yscale: 90});
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].arrow_mc.changeColor("575757");
                        manualContainerHeight = _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"]._y + 23;
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].box_mc.open = false;
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].box_mc.onRollOver = function ()
                        {
                            this._parent.text_mc.changeColor("262463");
                        };
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].box_mc.onRollOut = _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].box_mc.onDragOut = function ()
                        {
                            this._parent.text_mc.changeColor("454243");
                        };
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].box_mc.nowNo = no;
                        _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no + "_mc"].box_mc.onRelease = function ()
                        {
                            this._parent.text_mc.changeColor("454243");
                            if (this.open == false)
                            {
                                this.open = true;
                                newTween(this._parent.arrow_mc, "_rotation", as.transitions.easing.None.easeOut, 90, 0.200000);
                                newTween(this._parent.mask_mc, "_height", as.transitions.easing.Strong.easeOut, this._parent._height, 0.300000);
                                for (no2 = this.nowNo + 1; no2 < _root.faq_array.length; no2++)
                                {
                                    newTween(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no2 + "_mc"], "_y", as.transitions.easing.Strong.easeOut, _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no2 + "_mc"]._y + (_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + this.nowNo + "_mc"]._height - 23 + 6), 0.300000);
                                } // end of for
                                manualContainerHeight = manualContainerHeight + (_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + this.nowNo + "_mc"]._height - 23 + 6);
                                _root.ScrollbarEvaluate(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 159, manualContainerHeight);
                            }
                            else if (this.open == true)
                            {
                                this.open = false;
                                newTween(this._parent.arrow_mc, "_rotation", as.transitions.easing.None.easeOut, 0, 0.200000);
                                newTween(this._parent.mask_mc, "_height", as.transitions.easing.Strong.easeOut, 23, 0.300000);
                                for (no2 = this.nowNo + 1; no2 < _root.faq_array.length; no2++)
                                {
                                    newTween(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no2 + "_mc"], "_y", as.transitions.easing.Strong.easeOut, _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + no2 + "_mc"]._y - (_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + this.nowNo + "_mc"]._height - 23 + 6), 0.300000);
                                } // end of for
                                manualContainerHeight = manualContainerHeight - (_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.container_mc["itemHeader" + this.nowNo + "_mc"]._height - 23 + 6);
                                _root.ScrollbarEvaluate(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 159, manualContainerHeight);
                            } // end if
                        };
                    } // end of for
                }
                else if (this.counter == 2)
                {
                    _root.ScrollbarEvaluate(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 159, manualContainerHeight);
                }
                else if (this.counter == 10)
                {
                } // end if
                this.counter++;
            };
            CreateTagline("faq");
            delete this["onEnterFrame"];
        } // end if
        this.counter++;
    };
} // End of the function
function BuildGallery()
{
    _root.MAIN.section.counter = 1;
    _root.MAIN.section.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 257, 0.300000);
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.loader_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                _root.MAIN.loader_mc.removeMovieClip();
            };
        }
        else if (_root.counter == 5)
        {
            MAIN.section.BG_mc._visible = true;
            MAIN.section.BG_mc.photoBG_mc._visible = true;
            MAIN.section.BG_mc.sign_mc._visible = false;
            MAIN.section.BG_mc.tag_mc._visible = false;
            MAIN.section.BG_mc.textHeader_mc._visible = false;
            MAIN.section.BG_mc.shadow_mc._visible = false;
            MAIN.section.BG_mc.b1_mc._visible = false;
            MAIN.section.BG_mc.b2_mc._visible = false;
            MAIN.section.BG_mc.introType_mc._visible = false;
            MAIN.section.BG_mc.next_mc.prevTxt_mc._visible = false;
            MAIN.section.BG_mc.prev_mc.nextTxt_mc._visible = false;
            MAIN.section.BG_mc.next_mc._visible = false;
            MAIN.section.BG_mc.prev_mc._visible = false;
            MAIN.section.BG_mc.no_mc._visible = false;
            MAIN.section.BG_mc.photoBG_mc.play();
        }
        else if (_root.counter == 15)
        {
            MAIN.section.BG_mc.underline_mc.gotoAndPlay(2);
        }
        else if (_root.counter == 18)
        {
            MAIN.section.BG_mc.textHeader_mc._visible = true;
            _root.MAIN.section.BG_mc.textHeader_mc.text1_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (_root.counter == 22)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 300;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
        }
        else if (_root.counter == 33)
        {
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, undefined, 366, 188, 420, 262, 0, 0, undefined);
        }
        else if (_root.counter == 38)
        {
            colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 30, 100]);
            MAIN.section.BG_mc.shadow_mc._visible = true;
            MAIN.section.BG_mc.shadow_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.shadow_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.300000);
        }
        else if (_root.counter == 41)
        {
            MAIN.section.BG_mc.introType_mc._visible = true;
            MAIN.section.BG_mc.introType_mc._alpha = 0;
            MAIN.section.BG_mc.introType_mc.origY = MAIN.section.BG_mc.introType_mc._y;
            MAIN.section.BG_mc.introType_mc._y = MAIN.section.BG_mc.introType_mc._y + 20;
            newTween(MAIN.section.BG_mc.introType_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.300000);
            newTween(MAIN.section.BG_mc.introType_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.introType_mc.origY, 1);
        }
        else if (_root.counter == 46)
        {
            MAIN.section.BG_mc.b1_mc._visible = true;
            MAIN.section.BG_mc.b1_mc.recordValues();
            MAIN.section.BG_mc.b1_mc._x = MAIN.section.BG_mc.b1_mc._x - 6;
            MAIN.section.BG_mc.b1_mc._y = MAIN.section.BG_mc.b1_mc._y - 35;
            newTween(MAIN.section.BG_mc.b1_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b1_mc.origX, 0.500000);
            newTween(MAIN.section.BG_mc.b1_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b1_mc.origY, 0.500000);
        }
        else if (_root.counter == 50)
        {
            MAIN.section.BG_mc.b2_mc.recordValues();
            MAIN.section.BG_mc.b2_mc._visible = true;
            MAIN.section.BG_mc.b2_mc._x = MAIN.section.BG_mc.b2_mc._x - 6;
            MAIN.section.BG_mc.b2_mc._y = MAIN.section.BG_mc.b2_mc._y - 35;
            newTween(MAIN.section.BG_mc.b2_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b2_mc.origX, 0.500000);
            newTween(MAIN.section.BG_mc.b2_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b2_mc.origY, 0.500000);
        }
        else if (_root.counter == 60)
        {
            MAIN.section.BG_mc.b1_mc.xGoal = MAIN.section.BG_mc.b1_mc.origX + 1;
            MAIN.section.BG_mc.b1_mc.yGoal = MAIN.section.BG_mc.b1_mc.origY + 5;
            MAIN.section.BG_mc.b2_mc.xGoal = MAIN.section.BG_mc.b2_mc.origX + 1;
            MAIN.section.BG_mc.b2_mc.yGoal = MAIN.section.BG_mc.b2_mc.origY + 5;
            MAIN.section.BG_mc.b1_mc.onRollOver = function ()
            {
                newTween(MAIN.section.BG_mc.b1_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b1_mc.xGoal, 0.500000);
                newTween(MAIN.section.BG_mc.b1_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b1_mc.yGoal, 0.500000);
            };
            MAIN.section.BG_mc.b1_mc.onRollOut = MAIN.section.BG_mc.b1_mc.onDragOut = function ()
            {
                newTween(MAIN.section.BG_mc.b1_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b1_mc.origX, 0.500000);
                newTween(MAIN.section.BG_mc.b1_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b1_mc.origY, 0.500000);
            };
            MAIN.section.BG_mc.b1_mc.onRelease = function ()
            {
                newTween(MAIN.section.BG_mc.b1_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b1_mc.origX, 0.500000);
                newTween(MAIN.section.BG_mc.b1_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b1_mc.origY, 0.500000);
                this.enabled = false;
                MAIN.section.BG_mc.b2_mc.enabled = true;
                this.text_mc.changeColor("ffac3b");
                MAIN.section.BG_mc.b2_mc.text_mc.changeColor("ffffff");
                BuildCarList("performance");
            };
            MAIN.section.BG_mc.b2_mc.onRollOver = function ()
            {
                newTween(MAIN.section.BG_mc.b2_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b2_mc.xGoal, 0.500000);
                newTween(MAIN.section.BG_mc.b2_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b2_mc.yGoal, 0.500000);
            };
            MAIN.section.BG_mc.b2_mc.onRollOut = MAIN.section.BG_mc.b2_mc.onDragOut = function ()
            {
                newTween(MAIN.section.BG_mc.b2_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b2_mc.origX, 0.500000);
                newTween(MAIN.section.BG_mc.b2_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b2_mc.origY, 0.500000);
            };
            MAIN.section.BG_mc.b2_mc.onRelease = function ()
            {
                newTween(MAIN.section.BG_mc.b2_mc, "_x", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b2_mc.origX, 0.500000);
                newTween(MAIN.section.BG_mc.b2_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.b2_mc.origY, 0.500000);
                this.enabled = false;
                MAIN.section.BG_mc.b1_mc.enabled = true;
                this.text_mc.changeColor("ffac3b");
                MAIN.section.BG_mc.b1_mc.text_mc.changeColor("ffffff");
                BuildCarList("offroad");
            };
            CreateTagline("gallery");
            BuildCarList("performance");
        }
        else if (this.counter == 70)
        {
            if (!MAIN.section.BG_mc.next_mc._visible)
            {
                MAIN.section.BG_mc.next_mc._visible = true;
                MAIN.section.BG_mc.prev_mc._visible = true;
                MAIN.section.BG_mc.next_mc.origY = MAIN.section.BG_mc.next_mc._y;
                MAIN.section.BG_mc.prev_mc.origY = MAIN.section.BG_mc.prev_mc._y;
                MAIN.section.BG_mc.next_mc.overY = MAIN.section.BG_mc.next_mc._y + 5;
                MAIN.section.BG_mc.prev_mc.overY = MAIN.section.BG_mc.prev_mc._y + 5;
                MAIN.section.BG_mc.next_mc._y = MAIN.section.BG_mc.next_mc._y - 15;
                MAIN.section.BG_mc.prev_mc._y = MAIN.section.BG_mc.prev_mc._y - 15;
                newTween(MAIN.section.BG_mc.next_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.next_mc.origY, 0.300000);
                newTween(MAIN.section.BG_mc.prev_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.prev_mc.origY, 0.300000);
                MAIN.section.BG_mc.next_mc.onRollOver = function ()
                {
                    newTween(MAIN.section.BG_mc.next_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.next_mc.overY, 0.300000);
                };
                MAIN.section.BG_mc.next_mc.onRollOut = MAIN.section.BG_mc.next_mc.onDragOut = function ()
                {
                    newTween(MAIN.section.BG_mc.next_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.next_mc.origY, 0.300000);
                };
                MAIN.section.BG_mc.next_mc.onRelease = function ()
                {
                    currentImage++;
                    if (currentImage >= _root["gallery_" + _root.nowList + "_array"][carGalleryNo].length)
                    {
                        currentImage = 1;
                        carGalleryNo++;
                        if (carGalleryNo >= _root["gallery_" + _root.nowList + "_array"].length)
                        {
                            carGalleryNo = 0;
                        } // end if
                        nextPath = path["item" + carGalleryNo + "_mc"].box_mc;
                        nextPath._parent.tink_mc.removeMovieClip();
                        nextPath._parent.gradient_mc._visible = true;
                        nextPath.enabled = false;
                        nextPath._width = 100;
                        newTween(nextPath, "_width", as.transitions.easing.Strong.easeOut, 270, 0.500000);
                        nextPath._parent.text_mc.changeColor("3b295f");
                        selectedItem_mc = path["item" + selectedItem + "_mc"];
                        selectedItem_mc.box_mc._x = selectedItem_mc.box_mc._x - 1;
                        newTween(selectedItem_mc.box_mc, "_width", as.transitions.easing.Strong.easeOut, 1, 0.200000);
                        selectedItem_mc.text_mc.changeColor("ffffff");
                        selectedItem_mc.box_mc.tweenObj_width.selectedItem_mc = selectedItem_mc;
                        selectedItem_mc.box_mc.tweenObj_width.onMotionFinished = function ()
                        {
                            nextPath.selectedItem_mc.box_mc._x = nextPath.selectedItem_mc.box_mc._x + 1;
                            nextPath.selectedItem_mc.box_mc._width = 264;
                            nextPath.selectedItem_mc.gradient_mc._visible = false;
                            nextPath.selectedItem_mc.box_mc.enabled = true;
                        };
                        selectedItem = carGalleryNo;
                    } // end if
                    trace("vars: _root.nowList = " + _root.nowList + " ------ carGalleryNo = " + carGalleryNo + " ----------- last var = " + _root["gallery_" + _root.nowList + "_array"][_root.carGalleryNo][currentImage]);
                    LoadGalleryImage(_root.nowList, carGalleryNo, _root["gallery_" + _root.nowList + "_array"][_root.carGalleryNo][currentImage]);
                };
                MAIN.section.BG_mc.prev_mc.onRollOver = function ()
                {
                    newTween(MAIN.section.BG_mc.prev_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.prev_mc.overY, 0.300000);
                };
                MAIN.section.BG_mc.prev_mc.onRollOut = MAIN.section.BG_mc.prev_mc.onDragOut = function ()
                {
                    newTween(MAIN.section.BG_mc.prev_mc, "_y", as.transitions.easing.Strong.easeOut, MAIN.section.BG_mc.prev_mc.origY, 0.300000);
                };
                MAIN.section.BG_mc.prev_mc.nowX = _root.nowX;
                MAIN.section.BG_mc.prev_mc.onRelease = function ()
                {
                    currentImage--;
                    if (currentImage == 0)
                    {
                        carGalleryNo--;
                        if (carGalleryNo == -1)
                        {
                            carGalleryNo = _root["gallery_" + _root.nowList + "_array"].length - 1;
                            trace("RESET. New carGalleryNo = " + carGalleryNo);
                        } // end if
                        currentImage = _root["gallery_" + _root.nowList + "_array"][carGalleryNo].length - 1;
                        nextPath = path["item" + carGalleryNo + "_mc"].box_mc;
                        nextPath._parent.tink_mc.removeMovieClip();
                        nextPath._parent.gradient_mc._visible = true;
                        nextPath.enabled = false;
                        nextPath._width = 100;
                        newTween(nextPath, "_width", as.transitions.easing.Strong.easeOut, 270, 0.500000);
                        nextPath._parent.text_mc.changeColor("3b295f");
                        selectedItem_mc = path["item" + selectedItem + "_mc"];
                        selectedItem_mc.box_mc._x = selectedItem_mc.box_mc._x - 1;
                        newTween(selectedItem_mc.box_mc, "_width", as.transitions.easing.Strong.easeOut, 1, 0.200000);
                        selectedItem_mc.text_mc.changeColor("ffffff");
                        selectedItem_mc.box_mc.tweenObj_width.selectedItem_mc = selectedItem_mc;
                        selectedItem_mc.box_mc.tweenObj_width.onMotionFinished = function ()
                        {
                            nextPath.selectedItem_mc.box_mc._x = nextPath.selectedItem_mc.box_mc._x + 1;
                            nextPath.selectedItem_mc.box_mc._width = 264;
                            nextPath.selectedItem_mc.gradient_mc._visible = false;
                            nextPath.selectedItem_mc.box_mc.enabled = true;
                        };
                        selectedItem = carGalleryNo;
                    } // end if
                    LoadGalleryImage(_root.nowList, carGalleryNo, _root["gallery_" + _root.nowList + "_array"][_root.carGalleryNo][currentImage]);
                };
            } // end if
            delete _root["onEnterFrame"];
        } // end if
        _root.counter++;
    };
} // End of the function
function LinkMaps()
{
    _root.globalColor = "f77b13";
    _root.barColorShift = new Array(0, 37, 0, 97, 0, 34, 100, 0);
    RemoveHome("maps");
} // End of the function
function LoadGalleryImage(list, nowX, daImage)
{
    newTween(MAIN.section.BG_mc.no_mc, "_alpha", as.transitions.easing.Strong.easeOut, 0, 0.400000);
    MAIN.section.BG_mc.no_mc.tweenObj_alpha.onMotionFinished = function ()
    {
        MAIN.section.BG_mc.no_mc.text_txt.text = currentImage + "  of  " + (_root["gallery_" + list + "_array"][nowX].length - 1);
        MAIN.section.BG_mc.no_mc._visible = true;
        newTween(MAIN.section.BG_mc.no_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
    };
    imagePath.container_mc.removeMovieClip();
    imagePath.createEmptyMovieClip("container_mc", 1);
    trace("loading Image: " + _root["gallery_" + list + "_array"][nowX][1][0]);
    imagePath.container_mc.loadMovie(daImage, 1);
    imagePath._visible = false;
    imagePath.createEmptyMovieClip("imageEngine_mc", 2);
    imagePath.imageEngine_mc.counter = 1;
    imagePath.imageEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == 10)
        {
            if (imagePath.container_mc.getBytesLoaded() >= imagePath.container_mc.getBytesTotal())
            {
                imagePath._visible = true;
                colorApply(imagePath, [0, 255, 0, 255, 0, 255, 100, 100]);
                colorShift(imagePath, [100, 0, 100, 0, 100, 0, 100, 0], 6);
                this.removeMovieClip();
            } // end if
        } // end if
        this.counter++;
    };
} // End of the function
function BuildTix()
{
    _root.MAIN.section.counter = 1;
    _root.MAIN.section.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
            newTween(MAIN.stripe_mc.bar_mc, "_height", as.transitions.easing.Strong.easeIn, 277, 0.300000);
            newTween(MAIN.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            newTween(MAIN.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.300000);
            MAIN.loader_mc.tweenObj_xscale.onMotionFinished = function ()
            {
                _root.MAIN.loader_mc.removeMovieClip();
            };
        }
        else if (_root.counter == 4)
        {
            MAIN.section.BG_mc._visible = true;
            MAIN.section.BG_mc.colorJPG_mc._visible = true;
            MAIN.section.BG_mc.photoBG_mc._visible = false;
            MAIN.section.BG_mc.sign_mc._visible = false;
            MAIN.section.BG_mc.tag_mc._visible = false;
            MAIN.section.BG_mc.textHeader_mc._visible = false;
            MAIN.section.BG_mc.colorJPG_mc.play();
        }
        else if (_root.counter == 15)
        {
            MAIN.section.BG_mc.photoBG_mc._alpha = 0;
            MAIN.section.BG_mc.photoBG_mc._visible = true;
            newTween(MAIN.section.BG_mc.photoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.800000);
        }
        else if (_root.counter == 19)
        {
            tix_array[0][0][0] = tix_array[0][0][0].replace("&apos;", "\'");
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, tix_array, 79, 104, 302, 349, 126, 15, [0, 45, 0, 72, 0, 35, 100, 100]);
        }
        else if (_root.counter == 25)
        {
            colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 50, 100]);
            MAIN.section.BG_mc.sign_mc._visible = true;
            MAIN.section.BG_mc.type_mc._xscale = MAIN.section.BG_mc.type_mc._xscale = 10;
            newTween(MAIN.section.BG_mc.type_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(MAIN.section.BG_mc.type_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            MAIN.section.BG_mc.sign_mc._xscale = MAIN.section.BG_mc.sign_mc._yscale = 30;
            newTween(MAIN.section.BG_mc.sign_mc, "_xscale", as.transitions.easing.Strong.easeOut, 100, 0.500000);
            newTween(MAIN.section.BG_mc.sign_mc, "_yscale", as.transitions.easing.Strong.easeOut, 100, 0.500000);
            colorApply(MAIN.section.BG_mc.sign_mc, [0, 255, 0, 255, 0, 255, 50, 100]);
            colorShift(MAIN.section.BG_mc.sign_mc, [100, 0, 100, 0, 100, 0, 100, 0], 3);
        }
        else if (_root.counter == 33)
        {
            MAIN.section.BG_mc.textHeader_mc._visible = true;
            _root.MAIN.section.BG_mc.textHeader_mc.text1_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._alpha = 0;
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.300000);
        }
        else if (_root.counter == 38)
        {
            _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._xscale = _root.MAIN.section.BG_mc.textHeader_mc.text2_mc._yscale = 300;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_xscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_yscale", as.transitions.easing.Strong.easeIn, 100, 0.300000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text2_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.200000);
            _root.MAIN.section.BG_mc.textHeader_mc.text3_mc.origY = _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._y;
            _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._y = _root.MAIN.section.BG_mc.textHeader_mc.text3_mc._y - 10;
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text3_mc, "_y", as.transitions.easing.Strong.easeIn, _root.MAIN.section.BG_mc.textHeader_mc.text3_mc.origY, 0.200000);
            newTween(_root.MAIN.section.BG_mc.textHeader_mc.text3_mc, "_alpha", as.transitions.easing.Strong.easeIn, 100, 0.100000);
        }
        else if (_root.counter == 46)
        {
            _root.MAIN.section.BG_mc.tag_mc._visible = true;
            _root.MAIN.section.BG_mc.tag_mc.origY = _root.MAIN.section.BG_mc.tag_mc._y;
            _root.MAIN.section.BG_mc.attachMovie("box_mc", "tagMask_mc", mainLevel(), {_x: 171, _y: 442, _width: _root.MAIN.section.BG_mc.tag_mc._width, _height: _root.MAIN.section.BG_mc.tag_mc._height});
            _root.MAIN.section.BG_mc.tag_mc.setMask(_root.MAIN.section.BG_mc.tagMask_mc);
            _root.MAIN.section.BG_mc.tag_mc._y = _root.MAIN.section.BG_mc.tag_mc._y + 20;
            newTween(_root.MAIN.section.BG_mc.tag_mc, "_y", as.transitions.easing.Strong.easeOut, _root.MAIN.section.BG_mc.tag_mc.origY + 4, 0.300000);
            _root.MAIN.section.BG_mc.tag_mc.onRollOver = function ()
            {
                _root.MAIN.section.BG_mc.tag_mc.removeTween();
                newTween(_root.MAIN.section.BG_mc.tag_mc, "_y", as.transitions.easing.Strong.easeOut, _root.MAIN.section.BG_mc.tag_mc.origY, 0.300000);
            };
            _root.MAIN.section.BG_mc.tag_mc.onRollOut = _root.MAIN.section.BG_mc.tag_mc.onDragOut = function ()
            {
                _root.MAIN.section.BG_mc.tag_mc.removeTween();
                newTween(_root.MAIN.section.BG_mc.tag_mc, "_y", as.transitions.easing.Strong.easeOut, _root.MAIN.section.BG_mc.tag_mc.origY + 4, 0.300000);
            };
            _root.MAIN.section.BG_mc.tag_mc.onRelease = function ()
            {
                this.getURL("http://www.vegas.com/attractions/on_the_strip/gm_thedrive.html", "_blank");
            };
            CreateTagline("tix");
            delete this["onEnterFrame"];
        } // end if
        this.counter++;
    };
} // End of the function
function NavBounce()
{
    NAV_top.attachMovie("navB1_mc", "navB1_mc", mainLevel(), {_x: 24, _y: 38, _visible: false});
    NAV_top.attachMovie("navB2_mc", "navB2_mc", mainLevel(), {_x: 157, _y: 39, _visible: false});
    NAV_top.attachMovie("navB3_mc", "navB3_mc", mainLevel(), {_x: 499, _y: 40, _visible: false});
    NAV_top.attachMovie("navB4_mc", "navB4_mc", mainLevel(), {_x: 644, _y: 40, _visible: false});
    for (y = 1; y < 5; y++)
    {
        NAV_top["navB" + y + "_mc"].word1_mc._y = NAV_top["navB" + y + "_mc"].word1_mc._y + 10;
        NAV_top["navB" + y + "_mc"].word2_mc._y = NAV_top["navB" + y + "_mc"].word2_mc._y + 10;
    } // end of for
    _root.createEmptyMovieClip("navBounceEngine_mc", mainLevel());
    _root.BounceCounter = 1;
    navBounceEngine_mc.onEnterFrame = function ()
    {
        if (_root.BounceCounter < 5)
        {
            NAV_top["navB" + _root.BounceCounter + "_mc"].word1_mc._alpha = NAV_top["navB" + _root.BounceCounter + "_mc"].word2_mc._alpha = 0;
            NAV_top["navB" + _root.BounceCounter + "_mc"]._visible = true;
            NAV_top["navB" + _root.BounceCounter + "_mc"].counter = 1;
            NAV_top["navB" + _root.BounceCounter + "_mc"].BounceCounter = _root.BounceCounter;
            NAV_top["navB" + _root.BounceCounter + "_mc"].onEnterFrame = function ()
            {
                if (this.counter < 3)
                {
                    newTween(this["word" + this.counter + "_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
                    newTween(this["word" + this.counter + "_mc"], "_y", as.transitions.easing.Strong.easeOut, 15, 0.400000);
                }
                else
                {
                    delete this["onEnterFrame"];
                } // end if
                this.counter = this.counter + 0.500000;
            };
        }
        else
        {
            this.removeMovieClip();
        } // end if
        _root.BounceCounter = _root.BounceCounter + 0.500000;
    };
} // End of the function
MovieClip.prototype.removeTween = function ()
{
    while (this != null)
    {
        var _l2 = this;
        if (this[_l2]._type == "tween")
        {
            this[_l2].stop();
            this[_l2].clearInterval(_l2);
            this[_l2].onMotionFinished = undefined;
            delete this[_l2];
        } // end if
    } // end while
};
CreateTextBox = function (daName, daContent, path, daFormat, x, y, width, height, wordWrap_var, autoSize_var, multiline_var, embed_var)
{
    path.createEmptyMovieClip(daName, _root.mainLevel());
    path[daName].createTextField("daBox_txt", 1, x, y, width, height);
    path[daName].daBox_txt.type = "dynamic";
    path[daName].daBox_txt.multiline = multiline_var;
    path[daName].daBox_txt.wordWrap = wordWrap_var;
    path[daName].daBox_txt.condenseWhite = true;
    path[daName].daBox_txt.autoSize = autoSize_var;
    path[daName].daBox_txt.embedFonts = embed_var;
    path[daName].daBox_txt.html = true;
    path[daName].daBox_txt.selectable = false;
    path[daName].daBox_txt.htmlText = daContent;
    path[daName].daBox_txt.setTextFormat(daFormat);
};
CreateTextBox = function (daName, daContent, path, daFormat, x, y, width, height, wordWrap_var, autoSize_var, multiline_var, embed_var)
{
    path.createEmptyMovieClip(daName, _root.mainLevel());
    path[daName].createTextField("daBox_txt", 1, x, y, width, height);
    path[daName].daBox_txt.type = "dynamic";
    path[daName].daBox_txt.multiline = multiline_var;
    path[daName].daBox_txt.wordWrap = wordWrap_var;
    path[daName].daBox_txt.condenseWhite = true;
    path[daName].daBox_txt.autoSize = autoSize_var;
    path[daName].daBox_txt.embedFonts = embed_var;
    path[daName].daBox_txt.html = true;
    path[daName].daBox_txt.selectable = false;
    path[daName].daBox_txt.htmlText = daContent;
    path[daName].daBox_txt.setTextFormat(daFormat);
};
ScrollbarEvaluate = function (path, scrollHeight, manualContainerHeight)
{
    path.scrollX = path.scrollbar_mc._x;
    delete path.container_mc["onEnterFrame"];
    path.scrollBarCurrentHeight = path.scrollbar_mc._height;
    path.scrollbar_mc._height = scrollHeight;
    if (manualContainerHeight != undefined)
    {
        contentHeight = manualContainerHeight;
    }
    else
    {
        contentHeight = path.container_mc._height;
    } // end if
    path.contentOffset = contentHeight - path.textBoxMask._height;
    if (path.contentOffset <= 0)
    {
        path.scrollbar_mc._visible = false;
        path.scrollbar_bg._visible = false;
        path.botArrow_mc._visible = path.topArrow_mc._visible = false;
    }
    else
    {
        path.scrollbar_mc._visible = true;
        path.scrollbar_bg._visible = true;
        if (path.textBoxMask._height < 150)
        {
            path.scrollbar_bg._height = path.textBoxMask._height + 35;
            path.botArrow_mc._y = path.scrollbar_bg._y + path.scrollbar_bg._height - 13;
        }
        else
        {
            trace(path.scrollbar_bg._yscale + " = path.scrollbar_bg");
            trace(path.botArrow_mc._y + " = path.botArrow_mc");
            trace(path.botArrow_mc.origY + " = path.botArrow_mc.origY");
            path.scrollbar_bg._height = path.scrollbar_bg.origHeight;
            path.botArrow_mc._y = path.botArrow_mc.origY;
        } // end if
        path.botArrow_mc._visible = path.topArrow_mc._visible = true;
        MAIN.content_mc.section_mc.scrollbar_mc._visible = true;
        MAIN.content_mc.section_mc.scrollbar_mc._alpha = 0;
        newTween(MAIN.content_mc.section_mc.scrollbar_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.300000);
        path.scrollbarOldHeight = path.scrollbar_mc._yscale;
        path.scrollbar_mc._yscale = path.textBoxMask._height / contentHeight * path.scrollbar_mc._yscale;
        path.scrollbarOffset = scrollHeight - path.scrollbar_mc._height;
        path.scrollbarNewHeight = path.scrollbar_mc._height;
        path.scrollbar_mc._yscale = path.scrollbarOldHeight;
        path.scrollbar_mc.createEmptyMovieClip("yscaler", mainLevel());
        path.scrollbar_mc.createEmptyMovieClip("yshifter", mainLevel());
        path.scrollbar_mc._height = path.scrollBarCurrentHeight;
        path.scrollbar_mc._height = path.scrollbarNewHeight;
        path.scrollbar_mc._visible = true;
        path.scrollbar_bg._visible = true;
        path.scrollrate = path.contentOffset / path.scrollbarOffset * -1;
        if (path.container_mc._y < path.textBoxMask._height - contentHeight)
        {
            path.container_mc._y = path.textBoxMask._height - contentHeight;
        } // end if
        path.scrollbar_mc._y = path.container_mc._y / path.scrollrate;
        path.scrollbar_mc.onPress = function ()
        {
            path.scrollbar_mc.startDrag(0, path.scrollX, scrollHeight - path.scrollbarNewHeight, path.scrollX);
            path.scrollbar_mc.onEnterFrame = function ()
            {
                path.container_mc._y = Math.ceil(path.scrollbar_mc._y) * path.scrollrate;
            };
            updateAfterEvent();
        };
        path.botArrow_mc.onPress = function ()
        {
            ScrollBy(-10);
        };
        path.topArrow_mc.onPress = function ()
        {
            ScrollBy(10);
        };
        ScrollBy = function (amount, kill)
        {
            path.createEmptyMovieClip("scrollByEngine_mc", mainLevel());
            path.scrollByEngine_mc.counter = 1;
            path.scrollByEngine_mc.onEnterFrame = function ()
            {
                if (this.counter == 1 || this.counter > 5)
                {
                    if (path.container_mc._y > path.textBoxMask._height - contentHeight || path.container_mc._y < 0)
                    {
                        path.container_mc._y = path.container_mc._y + amount;
                        if (kill)
                        {
                            delete this["onEnterFrame"];
                        } // end if
                        if (path.container_mc._y < path.textBoxMask._height - contentHeight)
                        {
                            path.container_mc._y = path.textBoxMask._height - contentHeight;
                            delete this["onEnterFrame"];
                        }
                        else if (path.container_mc._y > 0)
                        {
                            path.container_mc._y = 0;
                            delete this["onEnterFrame"];
                        } // end if
                        path.scrollbar_mc._y = path.container_mc._y / path.scrollrate;
                    } // end if
                } // end if
                this.counter++;
            };
        };
        path.botArrow_mc.onRelease = path.topArrow_mc.onRelease = path.topArrow_mc.onReleaseOutside = path.botArrow_mc.onReleaseOutside = function ()
        {
            delete path.scrollByEngine_mc["onEnterFrame"];
        };
        path.scrollbar_mc.onRelease = path.scrollbar_mc.onReleaseOutside = function ()
        {
            path.scrollbar_mc.stopDrag();
            delete path.scrollbar_mc["onEnterFrame"];
        };
        var _l2 = new Object();
        _l2.onMouseWheel = function (delta)
        {
            if (delta > 0)
            {
                var _l1 = 10;
            }
            else
            {
                _l1 = -10;
            } // end if
            ScrollBy(_l1, true);
        };
        Mouse.addListener(_l2);
    } // end if
};
_root.globalColor = "f77b13";
headerFormat = new TextFormat();
headerFormat.font = "Verdana";
0;
headerFormat.size = 11;
headerFormat.leading = 4;
headerFormat.color = 3355443;
listFormat = new TextFormat();
listFormat.font = "Verdana";
listFormat.size = 11;
listFormat.leading = 2;
listFormat.color = 3355443;
tagFormat = new TextFormat();
tagFormat.font = "GarageGothic";
tagFormat.bold = true;
tagFormat.size = 24;
tagFormat.leading = 0;
tagFormat.color = 16777215;
VidPlayer = function (nextSection, swfName)
{
    MAIN.section.loadMovieEngine_mc.removeMovieClip();
    MAIN.section.createEmptyMovieClip("loadMovieEngine_mc", mainLevel());
    MAIN.section.loadMovieEngine_mc.counter = 1;
    MAIN.section.loadMovieEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == 1)
        {
        }
        else if (this.counter == 5)
        {
            if (nextSection == "offroad")
            {
                _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, undefined, 110, 133, 410, 307, 0, 0, undefined);
            }
            else if (nextSection == "overview")
            {
                _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, undefined, 433, 176, 361, 272, 0, 0, undefined);
            }
            else if (nextSection == "performance")
            {
                _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, undefined, 331, 121, 406, 308, 0, 0, undefined);
            } // end if
        }
        else if (this.counter == 15)
        {
            if (nextSection == "offroad")
            {
                MAIN.section.BG_mc.copyBoxHolder_mc.attachMovie("box_mc", "videoBG_mc", mainLevel(), {_x: 118, _y: 149, _width: 392, _height: 286, _alpha: 0});
                MAIN.section.BG_mc.copyBoxHolder_mc.createEmptyMovieClip("videoHolder_mc", mainLevel());
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc._x = 118;
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc._y = 141;
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.createEmptyMovieClip("container_mc", 1);
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.loadMovie("video/offroad.swf", 1);
                MAIN.section.BG_mc.copyBoxHolder_mc.attachMovie("offroad_loader_mc", "loader_mc", mainLevel(), {_x: 145, _y: 170, _xscale: 30, _yscale: 30, _alpha: 0});
                MAIN.section.BG_mc.tag_mc._visible = true;
            }
            else if (nextSection == "overview")
            {
                MAIN.section.BG_mc.copyBoxHolder_mc.attachMovie("box_mc", "videoBG_mc", mainLevel(), {_x: 437, _y: 180, _width: 352, _height: 264, _alpha: 0});
                MAIN.section.BG_mc.copyBoxHolder_mc.createEmptyMovieClip("videoHolder_mc", mainLevel());
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc._x = 437;
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc._y = 180;
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.createEmptyMovieClip("container_mc", 1);
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.loadMovie("video/overviewVideo.swf", 1);
                MAIN.section.BG_mc.copyBoxHolder_mc.attachMovie("offroad_loader_mc", "loader_mc", mainLevel(), {_x: 480, _y: 225, _xscale: 30, _yscale: 30, _alpha: 0});
                MAIN.section.BG_mc.tag_mc._visible = true;
                MAIN.section.BG_mc.tag_mc._alpha = 100;
                MAIN.section.BG_mc.tag_mc._y = 401;
                newTween(MAIN.section.BG_mc.tag_mc, "_y", as.transitions.easing.Strong.easeOut, 446, 0.500000);
            }
            else if (nextSection == "performance")
            {
                MAIN.section.BG_mc.copyBoxHolder_mc.attachMovie("box_mc", "videoBG_mc", mainLevel(), {_x: 338, _y: 129, _width: 392, _height: 294, _alpha: 0});
                MAIN.section.BG_mc.copyBoxHolder_mc.createEmptyMovieClip("videoHolder_mc", mainLevel());
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc._x = 338;
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc._y = 129;
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.createEmptyMovieClip("container_mc", 1);
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.loadMovie("video/performance.swf", 1);
                MAIN.section.BG_mc.copyBoxHolder_mc.attachMovie("offroad_loader_mc", "loader_mc", mainLevel(), {_x: 365, _y: 173, _xscale: 30, _yscale: 30, _alpha: 0});
            } // end if
            MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.copyBoxHolder_mc.videoBG_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.500000);
            newTween(MAIN.section.BG_mc.copyBoxHolder_mc.loader_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 1);
            MAIN.section.BG_mc.copyBoxHolder_mc.loader_mc.loadTxt_mc.text_txt.text = "0";
            newTween(MAIN.section.BG_mc.tag_mc.text1_mc, "_alpha", as.transitions.easing.Strong.easeOut, 0, 0.200000);
            MAIN.section.BG_mc.tag_mc.stop_mc._visible = MAIN.section.BG_mc.tag_mc.play_mc._visible = true;
            MAIN.section.BG_mc.tag_mc.stop_mc._alpha = MAIN.section.BG_mc.tag_mc.play_mc._alpha = 0;
            newTween(MAIN.section.BG_mc.tag_mc.play_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.400000);
            newTween(MAIN.section.BG_mc.tag_mc.stop_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.400000);
        }
        else if (this.counter == 16)
        {
            if (MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.getBytesLoaded() >= MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.getBytesTotal())
            {
                MAIN.section.BG_mc.copyBoxHolder_mc.loader_mc.loadTxt_mc.text_txt.htmlText = "<B><I>100</B></I>";
                newTween(MAIN.section.BG_mc.copyBoxHolder_mc.loader_mc, "_xscale", as.transitions.easing.Strong.easeIn, 10, 0.200000);
                newTween(MAIN.section.BG_mc.copyBoxHolder_mc.loader_mc, "_yscale", as.transitions.easing.Strong.easeIn, 10, 0.200000);
                MAIN.section.BG_mc.copyBoxHolder_mc.loader_mc.tweenObj_xscale.onMotionFinished = function ()
                {
                    MAIN.section.BG_mc.copyBoxHolder_mc.loader_mc.removeMovieClip();
                };
            }
            else
            {
                percent = Math.floor(MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.getBytesLoaded() / MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.getBytesTotal() * 100);
                MAIN.section.BG_mc.copyBoxHolder_mc.loader_mc.loadTxt_mc.text_txt.htmlText = "<B><I>" + percent + "</B></I>";
                this.counter--;
            } // end if
        }
        else if (this.counter == 20)
        {
            StopAudioBed();
            newTween(MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.300000);
            MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.gotoAndPlay(2);
            MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.onEnterFrame = function ()
            {
                if (MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc._currentframe >= MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc._totalframes)
                {
                    MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.gotoAndStop(1);
                    MAIN.section.BG_mc.tag_mc.stop_mc.enabled = false;
                    MAIN.section.BG_mc.tag_mc.play_mc.enabled = true;
                    if (audioEnabled)
                    {
                        StartAudioBed();
                    } // end if
                    if (nextSection == "overview")
                    {
                        MAIN.section.BG_mc.tag_mc._visible = false;
                        MAIN.section.BG_mc.textHeader_mc._visible = true;
                        MAIN.section.BG_mc.textHeader2_mc._visible = false;
                        removeVideo("noDrop");
                        MAIN.section.BG_mc.holder_mc._visible = true;
                        MAIN.section.BG_mc.shadow_mc._visible = true;
                        MAIN.section.BG_mc.imageTag_mc._visible = true;
                        MAIN.section.BG_mc.tagText_mc._visible = true;
                        MAIN.section.BG_mc.tagArrow_mc._visible = true;
                        MAIN.section.BG_mc.stroke_mc.text1_mc._alpha = 100;
                        MAIN.section.BG_mc.stroke_mc.text2_mc._alpha = 50;
                        MAIN.section.BG_mc.stroke_mc.text3_mc._alpha = 50;
                        MAIN.section.BG_mc.stroke_mc.arrow1_mc._alpha = 100;
                        MAIN.section.BG_mc.stroke_mc.arrow2_mc._alpha = 50;
                        MAIN.section.BG_mc.stroke_mc.arrow3_mc._alpha = 50;
                        MAIN.section.BG_mc.stroke_mc.button1_mc.enabled = false;
                        MAIN.section.BG_mc.stroke_mc.button2_mc.enabled = true;
                        MAIN.section.BG_mc.stroke_mc.button3_mc.enabled = true;
                        MAIN.section.BG_mc.stroke_mc.back_mc._visible = false;
                        MAIN.section.BG_mc.stroke_mc.promo_mc._visible = true;
                        MAIN.section.BG_mc.stroke_mc.promo_mc._alpha = 0;
                        newTween(MAIN.section.BG_mc.stroke_mc.promo_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.500000);
                        ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 381, overview_array, headerFormat, "~~ overview ~~");
                    }
                    else if (nextSection == "offroad")
                    {
                        removeVideo();
                        ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 316, offroad_array, headerFormat);
                    }
                    else if (nextSection == "performance")
                    {
                        removeVideo();
                        ResizeCopyBox(MAIN.section.BG_mc.copyBoxHolder_mc.copyBox_mc, 316, performance_array, headerFormat);
                    } // end if
                    delete this["onEnterFrame"];
                } // end if
            };
            newTween(MAIN.section.BG_mc.tag_mc.stop_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
            MAIN.section.BG_mc.tag_mc.stop_mc.onRollOver = MAIN.section.BG_mc.tag_mc.play_mc.onRollOver = function ()
            {
                if (nextSection == "offroad")
                {
                    this.changeColor("a4cc5f");
                }
                else
                {
                    this.changeColor("eaa818");
                } // end if
            };
            MAIN.section.BG_mc.tag_mc.stop_mc.onRollOut = MAIN.section.BG_mc.tag_mc.play_mc.onRollOut = function ()
            {
                this.changeColor("ffffff");
            };
            MAIN.section.BG_mc.tag_mc.play_mc.onRelease = function ()
            {
                StopAudioBed();
                newTween(MAIN.section.BG_mc.tag_mc.play_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.400000);
                newTween(MAIN.section.BG_mc.tag_mc.stop_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
                this.changeColor("ffffff");
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.gotoAndPlay(2);
                this.enabled = false;
                MAIN.section.BG_mc.tag_mc.stop_mc.enabled = true;
            };
            MAIN.section.BG_mc.tag_mc.stop_mc.onRelease = function ()
            {
                if (audioEnabled)
                {
                    StartAudioBed();
                } // end if
                newTween(MAIN.section.BG_mc.tag_mc.play_mc, "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.400000);
                newTween(MAIN.section.BG_mc.tag_mc.stop_mc, "_alpha", as.transitions.easing.Strong.easeOut, 40, 0.400000);
                this.changeColor("ffffff");
                MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc.container_mc.gotoAndStop(1);
                this.enabled = false;
                MAIN.section.BG_mc.tag_mc.play_mc.enabled = true;
                delete MAIN.section.BG_mc.copyBoxHolder_mc.videoHolder_mc["onEnterFrame"];
            };
        } // end if
        this.counter++;
    };
};
BuildCarList = function (list)
{
    _root.nowList = list;
    _root.MAIN.section.BG_mc.imageHolder_mc.image_mc.container_mc.removeMovieClip();
    MAIN.section.BG_mc.introType_mc._visible = false;
    MAIN.section.listEngine_mc.removeMovieClip();
    MAIN.section.BG_mc.carList_mc.removeMovieClip();
    MAIN.section.BG_mc.createEmptyMovieClip("carList_mc", mainLevel());
    path = MAIN.section.BG_mc.carList_mc;
    path._x = 79;
    path._y = 220;
    path.attachMovie("box_mc", "underline_mc", mainLevel(), {_width: 264, _height: 1});
    path.underline_mc.changeColor("635581");
    for (x = 0; x < _root["gallery_" + list + "_array"].length; x++)
    {
        path.attachMovie("gallery_item_mc", "item" + x + "_mc", mainLevel(), {_y: x * 19, _alpha: 0});
        path["item" + x + "_mc"].box_mc.nowX = x;
        path["item" + x + "_mc"].text_mc.text_txt.text = _root["gallery_" + list + "_array"][x][0][0].toUpperCase();
        path["item" + x + "_mc"].gradient_mc._visible = false;
        path["item" + x + "_mc"].box_mc.onRollOver = function ()
        {
            this._parent.attachMovie("box_mc", "tink_mc", mainLevel(), {_y: 17, _width: 1, _height: 16, _rotation: 180});
            newTween(this._parent.tink_mc, "_width", as.transitions.easing.Strong.easeOut, 3, 0.400000);
        };
        path["item" + x + "_mc"].box_mc.onRollOut = path["item" + x + "_mc"].box_mc.onDragOut = function ()
        {
            this._parent.tink_mc.removeMovieClip();
        };
        _root.selectedItem = -1;
        path["item" + x + "_mc"].box_mc.onRelease = function ()
        {
            currentImage = 1;
            this._parent.tink_mc.removeMovieClip();
            this._parent.gradient_mc._visible = true;
            this.enabled = false;
            this._width = 100;
            newTween(this, "_width", as.transitions.easing.Strong.easeOut, 270, 0.500000);
            this._parent.text_mc.changeColor("3b295f");
            selectedItem_mc = path["item" + selectedItem + "_mc"];
            selectedItem_mc.box_mc._x = selectedItem_mc.box_mc._x - 1;
            newTween(selectedItem_mc.box_mc, "_width", as.transitions.easing.Strong.easeOut, 1, 0.200000);
            selectedItem_mc.text_mc.changeColor("ffffff");
            selectedItem_mc.box_mc.tweenObj_width.selectedItem_mc = selectedItem_mc;
            selectedItem_mc.box_mc.tweenObj_width.onMotionFinished = function ()
            {
                this.selectedItem_mc.box_mc._x = this.selectedItem_mc.box_mc._x + 1;
                this.selectedItem_mc.box_mc._width = 264;
                this.selectedItem_mc.gradient_mc._visible = false;
                this.selectedItem_mc.box_mc.enabled = true;
            };
            selectedItem = this.nowX;
            _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox2_mc.removeMovieClip();
            _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, undefined, 373, 195, 406, 248, 0, 0, undefined);
            _root.MAIN.section.BG_mc.copyBoxHolder_mc.createEmptyMovieClip("brightEngine_mc", mainLevel());
            _root.MAIN.section.BG_mc.copyBoxHolder_mc.brightEngine_mc.counter = 1;
            _root.MAIN.section.BG_mc.copyBoxHolder_mc.brightEngine_mc.onEnterFrame = function ()
            {
                if (this.counter == 3)
                {
                    colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox2_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 100, 100]);
                    this.removeMovieClip();
                } // end if
                this.counter++;
            };
            imagePath = _root.MAIN.section.BG_mc.imageHolder_mc.createEmptyMovieClip("image_mc", 9999999);
            imagePath._x = 373;
            imagePath._y = 195;
            _root.carGalleryNo = this.nowX;
            LoadGalleryImage(list, this.nowX, _root["gallery_" + list + "_array"][this.nowX][1]);
        };
        path["item" + x + "_mc"]._alpha = 0;
        path["item" + x + "_mc"]._visible = false;
    } // end of for
    path.createEmptyMovieClip("listEngine_mc", mainLevel());
    path.listEngine_mc.counter = 0;
    path.listEngine_mc.onEnterFrame = function ()
    {
        path["item" + this.counter + "_mc"]._visible = true;
        newTween(path["item" + this.counter + "_mc"], "_alpha", as.transitions.easing.Strong.easeOut, 100, 0.800000);
        if (this.counter > _root["gallery_" + list + "_array"].length)
        {
            this.removeMovieClip();
        } // end if
        this.counter++;
    };
    currentImage = 1;
    firstPath = MAIN.section.BG_mc.carList_mc.item0_mc.box_mc;
    firstPath._parent.tink_mc.removeMovieClip();
    firstPath._parent.gradient_mc._visible = true;
    firstPath.enabled = false;
    firstPath._width = 100;
    newTween(firstPath, "_width", as.transitions.easing.Strong.easeOut, 270, 0.500000);
    firstPath._parent.text_mc.changeColor("3b295f");
    selectedItem_mc = path["item" + selectedItem + "_mc"];
    selectedItem_mc.box_mc._x = selectedItem_mc.box_mc._x - 1;
    newTween(selectedItem_mc.box_mc, "_width", as.transitions.easing.Strong.easeOut, 1, 0.200000);
    selectedItem_mc.text_mc.changeColor("ffffff");
    selectedItem_mc.box_mc.tweenObj_width.selectedItem_mc = selectedItem_mc;
    selectedItem_mc.box_mc.tweenObj_width.onMotionFinished = function ()
    {
        firstPath.selectedItem_mc.box_mc._x = firstPath.selectedItem_mc.box_mc._x + 1;
        firstPath.selectedItem_mc.box_mc._width = 264;
        firstPath.selectedItem_mc.gradient_mc._visible = false;
        firstPath.selectedItem_mc.box_mc.enabled = true;
    };
    selectedItem = 0;
    _root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox2_mc.removeMovieClip();
    _root.CreateCopyBox(_root.MAIN.section.BG_mc.copyBoxHolder_mc, undefined, 373, 195, 406, 248, 0, 0, undefined);
    _root.MAIN.section.BG_mc.copyBoxHolder_mc.createEmptyMovieClip("brightEngine_mc", mainLevel());
    _root.MAIN.section.BG_mc.copyBoxHolder_mc.brightEngine_mc.counter = 1;
    _root.MAIN.section.BG_mc.copyBoxHolder_mc.brightEngine_mc.onEnterFrame = function ()
    {
        if (this.counter == 3)
        {
            colorApply(_root.MAIN.section.BG_mc.copyBoxHolder_mc.copyBox2_mc.copyBoxBG_mc, [0, 255, 0, 255, 0, 255, 100, 100]);
            this.removeMovieClip();
        } // end if
        this.counter++;
    };
    imagePath = _root.MAIN.section.BG_mc.imageHolder_mc.createEmptyMovieClip("image_mc", 9999999);
    imagePath._x = 373;
    imagePath._y = 195;
    _root.carGalleryNo = 0;
    if (list == "performance")
    {
        LoadGalleryImage(list, 0, "galleryImages/chevyCorvetteCoup1.jpg");
    }
    else if (list == "offroad")
    {
        LoadGalleryImage(list, 0, "galleryImages/chevyAvalance_e851.jpg");
    } // end if
};
MainEngine();
stop();
