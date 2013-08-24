var playURL,clickURL,adURL,playOn,timeBetweenAds,codebase,archive,fqCap;
var u_referrerURL=document.referrer;
var u_iframe=u_F=false;
var Unicast=true;
var u_agt=navigator.userAgent.toLowerCase();
var u_MSIE=(u_agt.indexOf("msie")!=-1);
var u_NTSC=((u_agt.indexOf("mozilla")!=-1) && (u_agt.indexOf("spoofer")==-1) && (u_agt.indexOf("compatible")==-1));
var u_WIN=(u_agt.indexOf("win")!=-1);
var u_MAC=(u_agt.indexOf("mac")!=-1);
var u_ver=_getVer();
var u_jar="ARCHIVE=adcontroller.jar";
var u_TS="TransitionSensor";
var noTS="tsNotReady";
var hiFrameSecurity=false;
if (_writeTag()) {
 if (!u_iframe) u_referrerURL=location.href;
 if (playURL==null) playURL="";
 if (clickURL==null) clickURL="";
 if (fqCap==null) fqCap="";
 if (u_NTSC && u_ver>4.6 && fqCap==1) fqCap=2;
 if (archive=="no") u_jar="";
 if (codebase==null || codebase=="") codebase="http://adcontroller.unicast.com/java/classes/";
 _dw('<APPLET CODE="com.unicast.adcontroller.tools.TransitionSensor" CODEBASE='+codebase+' NAME='+u_TS+' WIDTH=1 HEIGHT=1 ALIGN=baseline '+u_jar+'>');
 _dw('<PARAM NAME=fqCap VALUE='+fqCap+'>');
 _dw('<PARAM NAME=referrer VALUE='+u_referrerURL+'>');
 _dw('<PARAM NAME=amsPlayURL VALUE='+playURL+'>');
 _dw('<PARAM NAME=amsClickURL VALUE='+clickURL+'>');
 if (timeBetweenAds!=null && timeBetweenAds!="") _dw('<PARAM NAME=timeBetweenAds VALUE='+timeBetweenAds+'>');
 if (adURL!=null && adURL!="") _dw('<PARAM NAME=adURL VALUE='+adURL+'>');
 if (playOn!=null && playOn!="") _dw('<PARAM NAME=playOn VALUE='+playOn+'>');
 _dw('</APPLET>');
 _dw('<APPLET CODE="com.unicast.adcontroller.tools.JSProxy" CODEBASE='+codebase+' NAME=JSProxy WIDTH=1 HEIGHT=1 ALIGN=baseline MAYSCRIPT '+u_jar+'>');
 _dw('</APPLET>');
}

function _writeTag() {
 if (!u_WIN && !u_MAC) return false;
 if (!u_NTSC && !u_MSIE) return false;
// if (u_NTSC && u_WIN) return false;
 if (u_MSIE && u_MAC) return false;
 if (u_ver<4) return false;
 if (u_NTSC && (u_ver==4.6 || u_ver==4.05)) return false;
 if (u_MAC && u_NTSC && u_ver<4.5) return false;
 if (u_NTSC && u_ver>=5) return false;
 if (u_MSIE && u_ver>5.5) return false;
 if (!_sniffFlash()) return false;
// if (_hiFrameSecurity()) return false;
 return !_tagDetected();
}
function _getVer() {
 if (u_MSIE) return parseFloat(u_agt.replace(/[\w\W]*\smsie\s/,''));
 else return parseFloat(navigator.appVersion);
}
function _tagDetected() {
 var flag=navigator.Unicast;
 navigator.Unicast=true;
 if ((u_NTSC || (u_MSIE && u_ver>=5.5)) && !flag) window.onunload=new Function("navigator.Unicast=false;");
 if (u_MSIE){ 
  var cnt=0;
  if (u_ver<5){
   for (var i=0;i<parent.frames.length;i++)
    if (parent.frames[i].Unicast) cnt++;
  }
  else{
   var _msie5TD = new Function("for (var i=cnt=0;i<parent.frames.length;i++) {try {if (parent.frames[i].Unicast)cnt++;}catch(e){}} return cnt;");
   cnt=_msie5TD();
  }
  u_iframe=(cnt>=1);
  if (u_iframe && u_ver<5.5) flag=(cnt>1);
 }
 return flag;
}
function _hiFrameSecurity() {
 if (u_MSIE) {
  _dwl('<script language="VBScript">');
  _dwl('On error resume next');
  _dwl('If parent.frames.length<>0 then');
  _dwl('hiFrameSecurity=IsNull(parent.frames(0))');
  _dwl('If Err.Number<>0 then hiFrameSecurity=true');
  _dwl('End If')
  _dwl('</'+'script>');
 }
 return hiFrameSecurity;
}
function _sniffFlash() {
 if (u_MSIE) {
  _dwl('<script language="VBScript">');
  _dwl('On error resume next');
  _dwl('u_F=NOT IsNull(CreateObject("ShockwaveFlash.ShockwaveFlash.3"))');
  _dwl('</'+'script>');
  return (u_F);
 }
 if (u_NTSC) {
  var sf="Shockwave Flash";
  if (navigator.plugins[sf]) {
   var flash=navigator.plugins[sf].description;
   return (parseInt(flash.replace(/[\w\W]*flash/i,'')) >= 3);
  }
 }
}
window.onerror=new Function("return true;");
function _u() {}
function _p(url) {u_i=new Image(); u_i.src=url;}
function _gp() {if (_TS()) return document.applets[u_TS].gp(Object); else return noTS;}
function _gc() {if (_TS()) return document.applets[u_TS].gc(Object); else return noTS;}
function _gt() {if (_TS()  && typeof document.applets[u_TS].gt(Object)!="undefined") return u_TS; else return null;}
// Paras Bug fix -- not used
/*
function _gt() {if (_TS()  && _gts())return u_TS; else return null;}
function _gts() {
 if (u_NTSC || (u_MSIE && u_ver<5))
  return typeof document.applets[u_TS].gt(Object)!="undefined";
 else{
  var _msie5gt = new Function("try {return typeof document.applets[u_TS].gt(Object)!='undefined';}catch(e){return false;}");
  return _msie5gt();
 }
}
*/
function _plugins(Object) {if (_TS()) return document.applets[u_TS].getPlugins(Object); else return noTS;}
function _untilAdReady() {if (_TS()) return document.applets[u_TS].untilAdReady(); else return noTS;}
function _getAdType() {return document.applets[u_TS].adType();}
function _ready() {return document.applets[u_TS].ready();}
function _needPlugs() {return document.applets[u_TS].needPlugs();}
function _notifyTS() {document.applets[u_TS].notifyTS();}
function _TS() {return (typeof document.applets[u_TS]!="undefined");}
function _isHTMLPlayer() {return document.applets[u_TS].isHTMLPlayer();}
function _dw(string) {document.write(string);}
function _dwl(string) {document.writeln(string);}
