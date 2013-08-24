
class AmazonApplication {

	static function calculateRebate(oldPrice:String, newPrice:String, precision:Number):String {
		var oldPStr:String = AmazonApplication.replace(oldPrice, "$", "");
		var newPStr:String = AmazonApplication.replace(newPrice, "$", "");		
		
		oldPStr = AmazonApplication.trim(oldPStr);
		newPStr = AmazonApplication.trim(newPStr);
		
		var oldP:Number  = Number(oldPStr);
		var newP:Number  = Number(newPStr);
		
		if (oldP == newP) {
			return "";
		}
		
		var percent:Number = (1 - (newP/oldP))*100;
		
		// Source code: class "mx.data.formatters.NumberFormatter"
		var stringval = percent.toString();
		var result;
		if (stringval.indexOf(".") >= 0)
		{
			var items = stringval.split(".");
			if (precision > 0)
			{
				var fraction = items[1] + "000000000000000000000000000000000";
				result = items[0] + "." + fraction.substr(0, precision);
			}
			else
			{
				result = items[0];
			}
		}
		else
		{
			result = stringval;
		}
		
		return "-"+result+"%";
	}
	
	static function formatAuthors(str:String):String {
		var result:String = str.toString();
		
		result = AmazonApplication.replace(result, "<Authors>", "");
		result = AmazonApplication.replace(result, "</Authors>", "");
		// if case sensitive 
		result = AmazonApplication.replace(result, "Authors>", "authors>");
		return result;

	}

	static function trim(str:String):String {
		if (str == undefined) return undefined;
 		for (var i = 0; i < str.length && str.charAt(i) == ' '; i++);
		for (var j = str.length - 1; j >= i && str.charAt(j) == ' '; j--);
		return str.substring(i, ++j);
	}
	
 	/*
		WARNING: Bug in flash player 7 (Corrected in Flash Player version 7.0.r19)

		Si la premiere lettre est egale à la derniere lettre
		
		var sString1 = "delete Worked";
		var sSearchString = "delete";
		txtOutput.text = sString1.replace(sSearchString,"");
		The output ouput using a flash 6 player is Worked which is what you'd expect.
		But the output with a flash 7 player is Worke dropping off the last d. 
		
		String.prototype.replace=function(find,replace) {
 			return this.split(find).join( replace);
 		} 
 		
 		AmazonApplication.replace("delete Worked", "delete", "");  -> " Worke"
 
  	*/
	static function replace(str:String, find:String,replace:String):String {
		return str.split(find).join( replace);
 	}
	
}
