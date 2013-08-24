-- MySQL dump 8.23
--
-- Host: localhost    Database: orange21
---------------------------------------------------------
-- Server version	3.23.58

--
-- Table structure for table `admin`
--

CREATE TABLE admin (
  id int(11) NOT NULL auto_increment,
  passwd varchar(100) NOT NULL default '',
  login varchar(100) NOT NULL default '',
  PRIMARY KEY  (id)
) TYPE=MyISAM MIN_ROWS=1 MAX_ROWS=2;

--
-- Dumping data for table `admin`
--


INSERT INTO admin VALUES (1,'myorange','admin');

--
-- Table structure for table `homes`
--

CREATE TABLE homes (
  id int(11) NOT NULL auto_increment,
  id_user int(11) NOT NULL default '0',
  city varchar(255) default NULL,
  zip varchar(255) default NULL,
  address varchar(255) default NULL,
  type varchar(255) default NULL,
  notes text,
  state varchar(255) default NULL,
  home_photo varchar(255) default NULL,
  price varchar(255) default NULL,
  bathroom varchar(255) default NULL,
  bedrooms varchar(255) default NULL,
  squarefeet varchar(255) default NULL,
  PRIMARY KEY  (id)
) TYPE=MyISAM;

--
-- Dumping data for table `homes`
--


INSERT INTO homes VALUES (1,1,'Chicago','0000001','75 Bowler str.','home','some comment about this supply some comment about this supply some comment about this supply some comment about this supply some comment about this supplya','CA','jpg','$60,000','2','','');

--
-- Table structure for table `shedule`
--

CREATE TABLE shedule (
  id int(11) NOT NULL auto_increment,
  id_user int(11) NOT NULL default '0',
  id_home int(11) NOT NULL default '0',
  name varchar(255) default NULL,
  email varchar(255) default NULL,
  phone varchar(255) default NULL,
  date_pref int(11) default NULL,
  date_alt int(11) default NULL,
  notes text,
  PRIMARY KEY  (id)
) TYPE=MyISAM;

--
-- Dumping data for table `shedule`
--


INSERT INTO shedule VALUES (1,1,1,'Rafael','rkadyrov@ksu.ru','333333333',1073066400,0,'');

--
-- Table structure for table `taskbar`
--

CREATE TABLE taskbar (
  id int(11) NOT NULL auto_increment,
  caption varchar(255) default NULL,
  url varchar(255) default NULL,
  PRIMARY KEY  (id)
) TYPE=MyISAM;

--
-- Dumping data for table `taskbar`
--


INSERT INTO taskbar VALUES (1,'Link1','#');
INSERT INTO taskbar VALUES (2,'Link2','#');
INSERT INTO taskbar VALUES (3,'Link3','#');
INSERT INTO taskbar VALUES (4,'Link4','#');

--
-- Table structure for table `toolbar`
--

CREATE TABLE toolbar (
  id int(11) NOT NULL auto_increment,
  caption varchar(255) default NULL,
  url varchar(255) default NULL,
  PRIMARY KEY  (id)
) TYPE=MyISAM;

--
-- Dumping data for table `toolbar`
--


INSERT INTO toolbar VALUES (1,'School Info','http://www.schoolwisepress.com/compare/index.html');
INSERT INTO toolbar VALUES (2,'Home Financing','http://www.hsh.com/ls-ca.html');

--
-- Table structure for table `user`
--

CREATE TABLE user (
  id int(11) NOT NULL auto_increment,
  login varchar(64) NOT NULL default '',
  passwd varchar(64) NOT NULL default '',
  domain varchar(255) NOT NULL default '',
  ttl int(11) NOT NULL default '0',
  fname varchar(255) NOT NULL default '',
  lname varchar(255) NOT NULL default '',
  mname varchar(255) NOT NULL default '',
  phone varchar(255) default '',
  fax varchar(255) default '',
  voicemail varchar(255) default '',
  email varchar(255) NOT NULL default '',
  address text,
  slogan text,
  logo varchar(100) NOT NULL default '',
  photo varchar(100) NOT NULL default '',
  info text NOT NULL,
  mls_id varchar(64) NOT NULL default '',
  PRIMARY KEY  (id),
  UNIQUE KEY user_domain_idx (domain),
  UNIQUE KEY user_login_idx (login)
) TYPE=MyISAM;

--
-- Dumping data for table `user`
--


INSERT INTO user VALUES (1,'client1','client1','shteys',1129089600,'Anne','Shteys','T','+1 (555) 555 5553','+1 (555) 555 5554','voicemail 2','anne@orange21.leanwebdesign.com','Century 21 Real Estate Corporation\r\nWorld Headquarters\r\n1 Campus Drive\r\nParsippany, New Jersey 07054\r\n(877) 221-2765','Real estate for your world.','gif','jpg','<h2>Anne Shteys</h2>\r\n<p>\r\n<p>Century 21 Real Estate Corporation is the franchisor of the world\'s largest residential real estate sales organization, with more than 6,600 independently owned and operated franchised broker offices in over 30 countries and territories worldwide. We are dedicated to providing buyers and sellers of real estate with the highest quality services possible. Learn more about the many CENTURY 21 benefits.\r\n\r\n<p>The CENTURY 21® System is actively increasing its presence and market share in the U.S. and globally, with international operations in over 30 countries encompassing Europe, Latin America, The Middle East and Asia. Contact us to learn more about bringing the most recognized name brand in real estate to select markets in the US or countries and territories abroad!\r\n\r\n<p>Century 21 Real Estate Corporation is a subsidiary of Cendant Corporation (NYSE:CD). Please see our recent press releases.','egiacles');
INSERT INTO user VALUES (2,'jdoe','jdoe','jdoe',1104555600,'John','Doe','J','555 1212','555 1212','','jdoe@aol.com','10 Johnson','My slogan','jpg','jpg','info info','2343');
INSERT INTO user VALUES (4,'zr','zr','zr',1072933200,'Rouslan','Zenetl','','222 333 4456','222 333 4478','','','','','jpg','jpg','','12343');
INSERT INTO user VALUES (5,'leo','leo','leo',1228453200,'Leo','Cheo','','222333444','','','leoleo@leoleo.leo','12 leo ave','gotta get away','gif','jpg','<h2>Leo Cheo</h2>\r\nThe One! The Only!','mlee');
INSERT INTO user VALUES (6,'ken','ken','Ken',1236834000,'Ken','Kenoby','Y','7687676876','8790870987','9870987090','ken@kenobyagent.com','33 Kenstreet.com','House of your dream, oh oh oh','gif','jpg','<h2>House of the rising sun</h2>\r\n<p>\r\nYon oifgo aiudhfuih fhauhu fhuhalkjh adkjhfjuah adufhuha diuhapdiuh adpiufhpaiudfh adiufhhad fadiuhfiaudhf aidufhuahdf \r\naduhfauihdfadfafd\r\n<p>\r\nYadkijhfsikudhfushd fosuhdf uh duh uhiuhdfiuh huhdfs','kenpby');
INSERT INTO user VALUES (7,'loner','loner','loner',1260594000,'Zedrius','Papandopalas','','333444','333444','','zendrius@papandopolas.com','33 Zendeius ave','Papandopalas for you','gif','jpg','<h2>Hey Jooo</h2>\r\n\r\nOpel fjhbds flh hb fdskjhbg skjh bf jhskjfhgkjhgsfkjhgkjgf \r\nfjhg lskfjhg lshfg hsbf hg \r\nsfdjgh slfhg lsiufh gliusyf glysb fglysbg fybgys f\r\nsfbg lsiyufbg siyuf sfg  u lisufligu slifuh glisufh gliuhsdf gsf lifuh gisufh glisuf\r\n isufgisufhgui hh sfiuhg lsiufhg siufh gisufh gslifuhg slifuhg sliufh glsiufghlsifuhglsiufh gs fdgus fgihus fguhs lfgiuhs fhg s','baucomb');

--
-- Table structure for table `user_taskbar`
--

CREATE TABLE user_taskbar (
  id_user int(11) NOT NULL default '0',
  id_menu int(11) NOT NULL default '0',
  url varchar(255) default NULL,
  PRIMARY KEY  (id_user,id_menu)
) TYPE=MyISAM;

--
-- Dumping data for table `user_taskbar`
--



--
-- Table structure for table `user_toolbar`
--

CREATE TABLE user_toolbar (
  id_home int(11) NOT NULL default '0',
  id_menu int(11) NOT NULL default '0',
  url varchar(255) default NULL,
  PRIMARY KEY  (id_home,id_menu)
) TYPE=MyISAM;

--
-- Dumping data for table `user_toolbar`
--



