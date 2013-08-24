var bar = new NavBar(20);
var menu;

bar.setColors("#000000", "#ffffff", "#808080", "#000000", "#6C6C6C", "#000000", "#9D9E9C", "#ffffff", "#8F94A7");
bar.setFonts("MS Sans Serif, sans-serif", "plain", "bold", "8pt", "MS Sans Serif, sans-serif", "plain", "bold", "8pt");
bar.setSizes(1, 2, 1);

menu = new NavBarMenu(125, 0);
menu.addItem(new NavBarMenuItem("<center>About Us</center>", "/aboutus.html"));
menu.addItem(new NavBarMenuItem("The Start", "/aboutus/"));
menu.addItem(new NavBarMenuItem("Company Motto", "/aboutus/motto.html"));
menu.addItem(new NavBarMenuItem("Our Background", "/aboutus/background.html"));
menu.addItem(new NavBarMenuItem("Why the Name?", "/aboutus/name.html"));
bar.addMenu(menu);

menu = new NavBarMenu(125, 0);
menu.addItem(new NavBarMenuItem("<center>Our Services</center>", "/services.html"));
menu.addItem(new NavBarMenuItem("Web Site Development", "/services/webdev.html"));
menu.addItem(new NavBarMenuItem("Flash Production", "/services/flash.html"));
menu.addItem(new NavBarMenuItem("Marketing", "/services/marketing.html"));
menu.addItem(new NavBarMenuItem("Collateral", "/services/collateral.html"));
menu.addItem(new NavBarMenuItem("Banners", "/services/banners.html"));
bar.addMenu(menu);

menu = new NavBarMenu(125, 0);
menu.addItem(new NavBarMenuItem("<center>Portfolio</center>", "/portfolio.html"));
menu.addItem(new NavBarMenuItem("Websites", "/portfolio/websites.html"));
menu.addItem(new NavBarMenuItem("Flash Samples", "/portfolio/flash.html"));
menu.addItem(new NavBarMenuItem("Banners", "/portfolio/banners.html"));
menu.addItem(new NavBarMenuItem("Collateral", "/portfolio/collateral.html"));
bar.addMenu(menu);

menu = new NavBarMenu(125, 0);
menu.addItem(new NavBarMenuItem("<center>Tools</center>", "/tools.html"));
menu.addItem(new NavBarMenuItem("Interactive Calendar", "/cgi-bin/calendar/"));
menu.addItem(new NavBarMenuItem("Domian Name Search", "/tools/domainlook.html"));
menu.addItem(new NavBarMenuItem("File Upload", "/tools/upload.html"));
menu.addItem(new NavBarMenuItem("Streaming Music", "/tools/music.html"));
bar.addMenu(menu);

menu = new NavBarMenu(125, 0);
menu.addItem(new NavBarMenuItem("<center>Contact Us</center>", "/contactus.html"));
menu.addItem(new NavBarMenuItem("Web Site Development", "/contactus/webdev.html"));
menu.addItem(new NavBarMenuItem("Flash Production", "/contactus/flash.html"));
menu.addItem(new NavBarMenuItem("Networking", "/contactus/networking.html"));
menu.addItem(new NavBarMenuItem("Marketing", "/contactus/marketing.html"));
menu.addItem(new NavBarMenuItem("Collateral", "/contactus/collateral.html"));
menu.addItem(new NavBarMenuItem("Technical Support", "/contactus/techsupport.html"));
bar.addMenu(menu);

menu = new NavBarMenu(125, 0);
menu.addItem(new NavBarMenuItem("<center>Search</center>", "/search.html"));
menu.addItem(new NavBarMenuItem("Our Site", "/search/oursite.html"));
menu.addItem(new NavBarMenuItem("The Internet", "/search/internet.html"));
menu.addItem(new NavBarMenuItem("For Domain Name(s)", "/search/domainlook.html"));
menu.addItem(new NavBarMenuItem("Frequently Asked Questions", "/search/faq.html"));
bar.addMenu(menu);

function init() {

  bar.create();
}