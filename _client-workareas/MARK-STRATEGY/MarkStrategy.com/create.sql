#use `homeseek`;

# Host: 127.0.0.1
# Database: homeseek
# Table: 'admin'
# 
#drop table `admin`;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL auto_increment,
  `passwd` varchar(100) NOT NULL default '',
  `login` varchar(100) NOT NULL default '',
  PRIMARY KEY  (`id`)
) TYPE=MyISAM MIN_ROWS=1 MAX_ROWS=2; 
INSERT INTO `admin` (`login`, `passwd`) VALUES ('admin', 'admin');

# Host: 127.0.0.1
# Database: homeseek
# Table: 'user'
# 
#drop table `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL auto_increment,
  `login` varchar(64) NOT NULL default '',
  `passwd` varchar(64) NOT NULL default '',
  `domain` varchar(255) NOT NULL default '',
  `ttl` int(11) NOT NULL default '0',
  `fname` varchar(255) NOT NULL default '',
  `lname` varchar(255) NOT NULL default '',
  `mname` varchar(255) NOT NULL default '',
  `phone` varchar(255) default '',
  `fax` varchar(255) default '',
  `voicemail` varchar(255) default '',
  `email` varchar(255) NOT NULL default '',
  `address` text,
  `slogan` text,
  `logo` varchar(100) NOT NULL default '',
  `photo` varchar(100) NOT NULL default '',
  `info` text NOT NULL,
  `mls_id` varchar(64) NOT NULL default '',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `user_login_idx` (`login`),
  UNIQUE KEY `user_domain_idx` (`domain`)
) TYPE=MyISAM; 
#INSERT INTO `user` VALUES (4, 'rafuck', 'rafuck', 'rafuck', 0, 'Rafael', 'Kadyrov', 'F.', '666666', '999999', '', 'rkadyrov@ksu.ru', 'address', 'we are the champions', 'gif', 'gif', 'some personal information');